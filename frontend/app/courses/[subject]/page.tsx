'use client';

import * as React from 'react';
import Link from 'next/link';
import { useParams } from 'next/navigation';
import {
  BookOpen,
  Clock,
  ArrowRight,
  PlayCircle,
  Loader2,
  AlertCircle,
  Sparkles,
} from 'lucide-react';
import { fetchSubjectBySlug } from '@/lib/api';
import { Subject } from '@/lib/types';
import { TopicAccordion } from '@/components/courses/TopicAccordion';
import { ProgressBar } from '@/components/ui/Progress';
import { Badge } from '@/components/ui/Badge';
import { Button } from '@/components/ui/Button';

export default function SubjectDetailPage() {
  const params = useParams();
  const subjectSlug = params.subject as string;

  const [subject, setSubject] = React.useState<Subject | null>(null);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);

  const loadSubject = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchSubjectBySlug(subjectSlug);
      setSubject(data);
    } catch (err: any) {
      setError(err.message || 'Failed to load subject details');
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    if (subjectSlug) {
      loadSubject();
    }
  }, [subjectSlug]);

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] space-y-3">
        <Loader2 className="h-8 w-8 text-primary animate-spin" />
        <p className="text-xs text-muted-foreground">Loading curriculum...</p>
      </div>
    );
  }

  if (error || !subject) {
    return (
      <div className="max-w-lg mx-auto py-20 px-4 text-center space-y-4">
        <div className="p-3 rounded-full bg-destructive/10 text-destructive w-fit mx-auto">
          <AlertCircle className="h-8 w-8" />
        </div>
        <h2 className="text-xl font-bold text-foreground">Course Not Found</h2>
        <p className="text-xs text-muted-foreground">{error || 'Could not locate this course.'}</p>
        <div className="pt-2 flex justify-center space-x-3">
          <Link href="/courses">
            <Button variant="outline" size="sm">
              All Courses
            </Button>
          </Link>
          <Button size="sm" onClick={loadSubject}>
            Try Again
          </Button>
        </div>
      </div>
    );
  }

  // Calculate completion percentage from topics and lessons
  const allLessons = (subject.topics || []).flatMap((t) => t.lessons || []);
  const completedCount = allLessons.filter((l) => l.status === 'completed').length;
  const progressPct = allLessons.length > 0 ? Math.round((completedCount / allLessons.length) * 100) : 0;

  // First uncompleted lesson or first lesson
  const firstUncompleted = allLessons.find((l) => l.status !== 'completed') || allLessons[0];
  const firstTopic = subject.topics?.[0];
  const continueUrl = firstUncompleted && firstTopic
    ? `/courses/${subject.slug}/${firstTopic.slug}/${firstUncompleted.slug}`
    : '#';

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      {/* Subject Banner Header */}
      <div className="p-8 rounded-3xl border border-border bg-gradient-to-br from-card via-card to-primary/5 shadow-xl shadow-primary/5 mb-12">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="flex items-center space-x-2">
              <Badge variant="default" className="text-xs">
                {subject.difficulty}
              </Badge>
              <span className="text-xs font-mono text-muted-foreground uppercase">
                {subject.slug}
              </span>
            </div>

            <h1 className="text-3xl sm:text-4xl font-extrabold text-foreground tracking-tight">
              {subject.name}
            </h1>

            <p className="text-sm sm:text-base text-muted-foreground leading-relaxed">
              {subject.description}
            </p>

            <div className="flex items-center space-x-6 pt-2 text-xs text-muted-foreground">
              <span className="flex items-center font-medium">
                <BookOpen className="h-4 w-4 mr-1.5 text-primary" />
                {subject.topics?.length || 0} Modules • {allLessons.length} Lessons
              </span>
              {subject.estimated_hours && (
                <span className="flex items-center font-medium">
                  <Clock className="h-4 w-4 mr-1.5 text-primary" />
                  {subject.estimated_hours}
                </span>
              )}
            </div>
          </div>

          <div className="flex flex-col items-start md:items-end space-y-3">
            {allLessons.length > 0 && (
              <Link href={continueUrl}>
                <Button size="lg" className="shadow-lg shadow-primary/25">
                  <PlayCircle className="h-5 w-5 mr-2" />
                  {progressPct > 0 ? 'Continue Course' : 'Start Course'}
                </Button>
              </Link>
            )}

            <div className="w-full md:w-56 space-y-1.5">
              <div className="flex justify-between text-xs text-muted-foreground">
                <span>Progress</span>
                <span className="font-semibold text-foreground">{progressPct}%</span>
              </div>
              <ProgressBar value={progressPct} className="h-2" />
            </div>
          </div>
        </div>
      </div>

      {/* Curriculum Topic Modules */}
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <h2 className="text-2xl font-bold text-foreground tracking-tight">
            Curriculum Structure
          </h2>
          <span className="text-xs text-muted-foreground">
            {completedCount} of {allLessons.length} lessons completed
          </span>
        </div>

        <TopicAccordion
          topics={subject.topics || []}
          subjectSlug={subject.slug}
        />
      </div>
    </div>
  );
}
