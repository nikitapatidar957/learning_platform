'use client';

import * as React from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import { Loader2, AlertCircle, ArrowLeft, Lock, Sparkles, Code2, PlayCircle, CheckCircle2 } from 'lucide-react';
import { useAuth, SignedIn, SignedOut, SignInButton, SignUpButton } from '@clerk/nextjs';
import { fetchLessonBySlug, fetchSubjectBySlug, startLessonProgress } from '@/lib/api';
import { LessonDetail, Subject } from '@/lib/types';
import { CourseSidebar } from '@/components/navigation/CourseSidebar';
import { LessonHeader } from '@/components/lessons/LessonHeader';
import { LessonContent } from '@/components/lessons/LessonContent';
import { LessonNavigation } from '@/components/lessons/LessonNavigation';
import { Button } from '@/components/ui/Button';

export default function LessonPage() {
  const params = useParams();
  const subjectSlug = params.subject as string;
  const topicSlug = params.topic as string;
  const lessonSlug = params.lesson as string;

  const { getToken, isSignedIn, isLoaded: authLoaded } = useAuth();
  const [lesson, setLesson] = React.useState<LessonDetail | null>(null);
  const [subject, setSubject] = React.useState<Subject | null>(null);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);
  const [sidebarOpenMobile, setSidebarOpenMobile] = React.useState(false);

  const loadData = React.useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const token = isSignedIn ? await getToken() : null;
      const [lessonData, subjectData] = await Promise.all([
        fetchLessonBySlug(lessonSlug, token),
        fetchSubjectBySlug(subjectSlug, token),
      ]);
      setLesson(lessonData);
      setSubject(subjectData);

      // Auto-start progress tracking if signed in
      if (isSignedIn && lessonData && lessonData.id) {
        startLessonProgress(lessonData.id, token).catch(() => {});
      }
    } catch (err: any) {
      setError(err.message || 'Failed to load lesson content');
    } finally {
      setLoading(false);
    }
  }, [lessonSlug, subjectSlug, isSignedIn, getToken]);

  React.useEffect(() => {
    if (lessonSlug && subjectSlug && authLoaded) {
      loadData();
    }
  }, [lessonSlug, subjectSlug, authLoaded, loadData]);

  if (!authLoaded || loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[70vh] space-y-3">
        <Loader2 className="h-8 w-8 text-primary animate-spin" />
        <p className="text-xs text-muted-foreground">Loading interactive lesson...</p>
      </div>
    );
  }

  if (error || !lesson || !subject) {
    return (
      <div className="max-w-md mx-auto py-24 px-4 text-center space-y-4">
        <AlertCircle className="h-10 w-10 text-destructive mx-auto" />
        <h2 className="text-xl font-bold text-foreground">Something went wrong</h2>
        <p className="text-xs text-muted-foreground">{error || "We couldn't load this lesson."}</p>
        <div className="pt-2 flex justify-center space-x-3">
          <Link href={`/courses/${subjectSlug}`}>
            <Button variant="outline" size="sm">
              <ArrowLeft className="h-3.5 w-3.5 mr-1" /> Course Overview
            </Button>
          </Link>
          <Button size="sm" onClick={loadData}>
            Try Again
          </Button>
        </div>
      </div>
    );
  }

  const currentTopic = subject.topics?.find((t) => t.slug === topicSlug);

  return (
    <div className="flex min-h-[calc(100vh-4rem)]">
      {/* Dynamic Course Navigation Sidebar */}
      <CourseSidebar
        subjectName={subject.name}
        subjectSlug={subject.slug}
        topics={subject.topics || []}
        currentLessonSlug={lesson.slug}
        isOpenMobile={sidebarOpenMobile}
        onCloseMobile={() => setSidebarOpenMobile(false)}
      />

      {/* Main Lesson Content Canvas */}
      <main className="flex-1 max-w-4xl mx-auto px-4 sm:px-8 py-8 w-full overflow-hidden">
        <LessonHeader
          lessonId={lesson.id}
          lessonTitle={lesson.title}
          lessonSlug={lesson.slug}
          subjectName={subject.name}
          subjectSlug={subject.slug}
          topicTitle={currentTopic?.title || topicSlug}
          topicSlug={topicSlug}
          estimatedTime={lesson.estimatedTime}
          difficulty={lesson.difficulty}
          interactiveType={lesson.interactiveType}
          status={lesson.status}
          onOpenSidebar={() => setSidebarOpenMobile(true)}
          onStatusChange={(newStatus) => {
            setLesson((prev) => (prev ? { ...prev, status: newStatus as any } : null));
          }}
        />

        {/* Content Gating: Full Lesson Content when SignedIn */}
        <SignedIn>
          <div className="mt-6">
            <LessonContent sections={lesson.content?.sections || []} />
          </div>

          {/* Prev / Next Navigation Controls */}
          <LessonNavigation
            subjectSlug={subject.slug}
            previousLesson={lesson.previous_lesson}
            nextLesson={lesson.next_lesson}
          />
        </SignedIn>

        {/* Content Gating: Gate Card when SignedOut */}
        <SignedOut>
          <div className="mt-8 p-8 sm:p-10 rounded-3xl border border-primary/20 bg-gradient-to-br from-card via-card to-primary/5 shadow-xl text-center space-y-6 max-w-2xl mx-auto">
            <div className="h-16 w-16 rounded-2xl bg-primary/10 text-primary flex items-center justify-center mx-auto shadow-inner">
              <Lock className="h-8 w-8 text-primary" />
            </div>

            <div className="space-y-2">
              <h3 className="text-2xl font-extrabold text-foreground tracking-tight">
                Sign in to Unlock Full Lesson Content
              </h3>
              <p className="text-sm text-muted-foreground max-w-lg mx-auto leading-relaxed">
                You are currently exploring the course outline. Sign in or register for a free account to unlock interactive visualizers, code playgrounds, and step-by-step guides.
              </p>
            </div>

            <div className="p-5 rounded-2xl border border-border/80 bg-background/60 text-left max-w-lg mx-auto space-y-2.5 text-xs text-muted-foreground">
              <div className="font-semibold text-foreground flex items-center text-sm">
                <Sparkles className="h-4 w-4 mr-2 text-primary" /> Included with free access:
              </div>
              <ul className="space-y-1.5 pl-1">
                <li className="flex items-center">
                  <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500 mr-2 shrink-0" />
                  Full technical breakdown and theory explanations
                </li>
                <li className="flex items-center">
                  <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500 mr-2 shrink-0" />
                  Live interactive algorithm, ML model & SQL/Mongo visualizers
                </li>
                <li className="flex items-center">
                  <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500 mr-2 shrink-0" />
                  Progress tracking saved to your account and learning dashboard
                </li>
              </ul>
            </div>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
              <SignInButton mode="modal">
                <Button size="lg" className="w-full sm:w-auto shadow-lg shadow-primary/25">
                  Sign In to Access Lesson
                </Button>
              </SignInButton>
              <SignUpButton mode="modal">
                <Button variant="outline" size="lg" className="w-full sm:w-auto">
                  Create Free Account
                </Button>
              </SignUpButton>
              <Link href={`/courses/${subjectSlug}`}>
                <Button variant="ghost" size="lg" className="w-full sm:w-auto">
                  Course Overview
                </Button>
              </Link>
            </div>
          </div>
        </SignedOut>
      </main>
    </div>
  );
}
