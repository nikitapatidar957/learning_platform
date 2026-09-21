'use client';

import * as React from 'react';
import Link from 'next/link';
import { PlayCircle, ArrowRight, Sparkles, Compass } from 'lucide-react';
import { Button } from '@/components/ui/Button';
import { ProgressBar } from '@/components/ui/Progress';

interface ContinueLearningCardProps {
  currentLesson?: {
    lesson_id: string;
    lesson_slug: string;
    lesson_title: string;
    subject_slug: string;
    topic_slug: string;
    status: string;
    progress_percentage: number;
  } | null;
}

export function ContinueLearningCard({ currentLesson }: ContinueLearningCardProps) {
  if (!currentLesson) {
    return (
      <div className="rounded-2xl border border-dashed border-border/80 bg-muted/20 p-8 text-center my-6 space-y-4">
        <div className="mx-auto w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary">
          <Compass className="h-6 w-6" />
        </div>
        <div className="space-y-1">
          <h3 className="text-lg font-bold text-foreground">Welcome to Your Learning Journey!</h3>
          <p className="text-xs sm:text-sm text-muted-foreground max-w-md mx-auto">
            You haven&apos;t started a lesson yet. Explore our curriculum in DSA, Machine Learning, SQL, or Agentic AI to get started.
          </p>
        </div>
        <Link href="/courses">
          <Button size="md" variant="primary">
            Explore All Courses <ArrowRight className="h-4 w-4 ml-1.5" />
          </Button>
        </Link>
      </div>
    );
  }

  const courseUrl = `/courses/${currentLesson.subject_slug}/${currentLesson.topic_slug}/${currentLesson.lesson_slug}`;
  const pct = currentLesson.progress_percentage || 50;

  return (
    <div className="relative overflow-hidden rounded-2xl border border-primary/30 bg-gradient-to-r from-card via-card to-primary/5 p-6 sm:p-8 shadow-xl shadow-primary/5 my-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
        <div className="space-y-2">
          <div className="flex items-center space-x-2">
            <span className="text-[10px] font-mono uppercase font-bold tracking-wider px-2 py-0.5 rounded bg-primary/15 text-primary">
              Continue Learning
            </span>
            <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
              {currentLesson.subject_slug}
            </span>
          </div>

          <h3 className="text-xl sm:text-2xl font-bold text-foreground tracking-tight">
            {currentLesson.lesson_title}
          </h3>

          <p className="text-xs text-muted-foreground">
            Topic: <span className="text-foreground/80 font-medium">{currentLesson.topic_slug}</span>
          </p>

          <div className="w-full sm:w-72 space-y-1.5 pt-2">
            <div className="flex justify-between text-xs text-muted-foreground">
              <span>Lesson Progress</span>
              <span className="font-semibold text-foreground">{pct}%</span>
            </div>
            <ProgressBar value={pct} className="h-2" />
          </div>
        </div>

        <div className="shrink-0">
          <Link href={courseUrl}>
            <Button size="lg" className="w-full sm:w-auto shadow-lg shadow-primary/25">
              <PlayCircle className="h-5 w-5 mr-2" />
              Resume Lesson
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}
