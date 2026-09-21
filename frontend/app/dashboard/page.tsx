'use client';

import * as React from 'react';
import Link from 'next/link';
import {
  Compass,
  ArrowRight,
  BookOpen,
  Loader2,
  AlertCircle,
  PlayCircle,
  Clock,
  History,
} from 'lucide-react';
import { useUser, useAuth, SignInButton } from '@clerk/nextjs';
import { fetchOverallProgress, fetchSubjects } from '@/lib/api';
import { OverallProgress, Subject } from '@/lib/types';
import { DashboardStats } from '@/components/dashboard/DashboardStats';
import { ContinueLearningCard } from '@/components/dashboard/ContinueLearningCard';
import { SubjectCard } from '@/components/courses/SubjectCard';
import { Button } from '@/components/ui/Button';

export default function DashboardPage() {
  const { user, isLoaded: userLoaded } = useUser();
  const { getToken, isLoaded: authLoaded, isSignedIn } = useAuth();
  const [progress, setProgress] = React.useState<OverallProgress | null>(null);
  const [subjects, setSubjects] = React.useState<Subject[]>([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);

  const loadDashboardData = React.useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const token = isSignedIn ? await getToken() : null;
      const [progData, subjectsData] = await Promise.all([
        fetchOverallProgress(token),
        fetchSubjects(),
      ]);
      setProgress(progData);
      setSubjects(subjectsData);
    } catch (err: any) {
      setError(err.message || 'Failed to load dashboard progress');
    } finally {
      setLoading(false);
    }
  }, [isSignedIn, getToken]);

  React.useEffect(() => {
    if (authLoaded && userLoaded) {
      if (isSignedIn) {
        loadDashboardData();
      } else {
        setLoading(false);
      }
    }
  }, [authLoaded, userLoaded, isSignedIn, loadDashboardData]);

  const userName = user?.firstName || user?.fullName || 'Learner';

  if (!authLoaded || !userLoaded || loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[70vh] space-y-3">
        <Loader2 className="h-8 w-8 text-primary animate-spin" />
        <p className="text-xs text-muted-foreground">Loading your personalized dashboard...</p>
      </div>
    );
  }

  if (!isSignedIn) {
    return (
      <div className="max-w-md mx-auto py-24 px-4 text-center space-y-5">
        <div className="h-14 w-14 rounded-2xl bg-primary/10 text-primary flex items-center justify-center mx-auto shadow-inner">
          <BookOpen className="h-7 w-7 text-primary" />
        </div>
        <h2 className="text-2xl font-bold text-foreground">Sign In to View Dashboard</h2>
        <p className="text-xs text-muted-foreground leading-relaxed">
          Your dashboard tracks your completed lessons, quiz scores, and learning streak across all developer tracks.
        </p>
        <div className="pt-2">
          <SignInButton mode="modal">
            <Button size="lg" className="shadow-lg shadow-primary/20">
              Sign In with Free Account
            </Button>
          </SignInButton>
        </div>
      </div>
    );
  }

  if (error || !progress) {
    return (
      <div className="max-w-md mx-auto py-20 px-4 text-center space-y-4">
        <AlertCircle className="h-10 w-10 text-destructive mx-auto" />
        <h2 className="text-xl font-bold text-foreground">Failed to Load Dashboard</h2>
        <p className="text-xs text-muted-foreground">{error}</p>
        <Button size="sm" onClick={loadDashboardData}>
          Try Again
        </Button>
      </div>
    );
  }

  // Map progress percentages onto subject cards
  const progressMap = new Map<string, number>();
  progress.subjects_progress.forEach((sp) => {
    progressMap.set(sp.subject_slug, sp.percentage);
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10">
      {/* Greeting Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-border">
        <div>
          <h1 className="text-3xl sm:text-4xl font-extrabold text-foreground tracking-tight">
            Welcome back, {userName} 👋
          </h1>
          <p className="text-sm text-muted-foreground mt-1">
            Pick up where you left off or dive into a new technical discipline.
          </p>
        </div>

        <Link href="/courses">
          <Button variant="outline" size="sm">
            <Compass className="h-4 w-4 mr-1.5" /> Browse All Courses
          </Button>
        </Link>
      </div>

      {/* Continue Learning Resume Card */}
      <ContinueLearningCard currentLesson={progress.current_lesson} />

      {/* Progress Metric Statistics */}
      <DashboardStats progress={progress} />

      {/* Recently Viewed Lessons */}
      {progress.recently_viewed && progress.recently_viewed.length > 0 && (
        <div className="space-y-4">
          <div className="flex items-center space-x-2">
            <History className="h-4 w-4 text-primary" />
            <h3 className="text-lg font-bold text-foreground">Recently Viewed</h3>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {progress.recently_viewed.map((item, idx) => (
              <Link
                key={idx}
                href={`/courses/${item.subject_slug}/${item.topic_slug}/${item.lesson_slug}`}
                className="p-4 rounded-xl border border-border bg-card hover:border-primary/40 hover:shadow-md transition-all group"
              >
                <div className="flex items-center justify-between text-[11px] text-muted-foreground mb-1">
                  <span className="uppercase font-mono font-semibold">{item.subject_slug}</span>
                  <span className="font-semibold text-primary">{item.progress_percentage}%</span>
                </div>
                <h4 className="text-sm font-semibold text-foreground group-hover:text-primary transition-colors line-clamp-1">
                  {item.lesson_title}
                </h4>
                <div className="flex items-center justify-between mt-3 text-xs text-primary font-medium">
                  <span>Resume →</span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* Enrolled & Available Subjects */}
      <div className="space-y-6 pt-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-foreground tracking-tight">Your Learning</h2>
            <p className="text-xs text-muted-foreground mt-0.5">Explore active and new subject tracks</p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {subjects.map((subj) => (
            <SubjectCard
              key={subj.id || subj.slug}
              subject={subj}
              progressPercentage={progressMap.get(subj.slug) || 0}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
