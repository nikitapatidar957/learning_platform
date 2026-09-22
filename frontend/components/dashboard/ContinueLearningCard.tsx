'use client';

import * as React from 'react';
import Link from 'next/link';
import { PlayCircle, ArrowRight, Sparkles, Compass, Zap, Brain, Database, Bot } from 'lucide-react';
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
  // ============================================================
  // EMPTY STATE: Before learning any lesson (Inspiring Onboarding)
  // ============================================================
  if (
    !currentLesson ||
    !currentLesson.lesson_slug ||
    currentLesson.lesson_slug === 'undefined' ||
    !currentLesson.subject_slug ||
    currentLesson.subject_slug === 'undefined' ||
    !currentLesson.topic_slug ||
    currentLesson.topic_slug === 'undefined' ||
    !currentLesson.lesson_title ||
    currentLesson.lesson_title === 'undefined'
  ) {
    return (
      <div className="relative overflow-hidden rounded-3xl border border-border/80 bg-gradient-to-br from-card via-card to-purple-500/5 p-6 sm:p-8 shadow-xl shadow-purple-500/5 my-6">
        {/* Ambient background glow */}
        <div className="absolute top-0 right-0 w-80 h-80 bg-indigo-500/10 dark:bg-indigo-500/15 rounded-full blur-3xl pointer-events-none -z-10" />

        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
          <div className="space-y-3 max-w-2xl">
            <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full border border-purple-200/80 dark:border-purple-800/40 bg-purple-50/80 dark:bg-purple-950/40 text-xs font-semibold text-purple-700 dark:text-purple-300">
              <Sparkles className="h-3.5 w-3.5 text-purple-600 dark:text-purple-400" />
              <span>Start Your Tech Journey • 100% Free</span>
            </div>

            <h3 className="text-2xl sm:text-3xl font-extrabold text-foreground tracking-tight">
              Ready to build your engineering skills?
            </h3>

            <p className="text-sm text-muted-foreground leading-relaxed">
              You haven&apos;t started a lesson yet. Choose from our 8 curated tracks in DSA, Machine Learning, SQL, and Agentic AI with interactive sandboxes and first-principles notes.
            </p>

            {/* Quick Track Shortcuts */}
            <div className="flex flex-wrap gap-2 pt-1 text-xs">
              <Link
                href="/courses/dsa"
                className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-full bg-muted/60 hover:bg-primary/10 hover:text-primary border border-border/60 transition-colors"
              >
                <Zap className="h-3.5 w-3.5 text-amber-500" />
                <span>DSA Foundations</span>
              </Link>
              <Link
                href="/courses/machine-learning"
                className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-full bg-muted/60 hover:bg-primary/10 hover:text-primary border border-border/60 transition-colors"
              >
                <Brain className="h-3.5 w-3.5 text-indigo-500" />
                <span>Machine Learning</span>
              </Link>
              <Link
                href="/courses/sql"
                className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-full bg-muted/60 hover:bg-primary/10 hover:text-primary border border-border/60 transition-colors"
              >
                <Database className="h-3.5 w-3.5 text-emerald-500" />
                <span>SQL & Databases</span>
              </Link>
              <Link
                href="/courses/agentic-ai"
                className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-full bg-muted/60 hover:bg-primary/10 hover:text-primary border border-border/60 transition-colors"
              >
                <Bot className="h-3.5 w-3.5 text-purple-500" />
                <span>Agentic AI</span>
              </Link>
            </div>
          </div>

          {/* Primary Explore Action Button */}
          <div className="shrink-0 pt-2 lg:pt-0 w-full sm:w-auto">
            <Link href="/courses" className="block w-full sm:w-auto">
              <button className="w-full sm:w-auto px-7 py-3.5 rounded-full bg-[#5046e5] hover:bg-[#4338ca] text-white text-sm font-semibold shadow-lg shadow-indigo-500/25 hover:shadow-indigo-500/40 transition-all hover:scale-[1.02] active:scale-[0.98] flex items-center justify-center space-x-2 cursor-pointer">
                <Compass className="h-4 w-4" />
                <span>Explore All Courses</span>
                <ArrowRight className="h-4 w-4" />
              </button>
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // ============================================================
  // ACTIVE STATE: When the user has an ongoing lesson
  // ============================================================
  const courseUrl = `/courses/${currentLesson.subject_slug}/${currentLesson.topic_slug}/${currentLesson.lesson_slug}`;
  const pct = currentLesson.progress_percentage || 50;

  return (
    <div className="relative overflow-hidden rounded-3xl border border-primary/30 bg-gradient-to-r from-card via-card to-primary/5 p-6 sm:p-8 shadow-xl shadow-primary/5 my-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
        <div className="space-y-2.5">
          <div className="flex items-center space-x-2">
            <span className="text-[10px] font-mono uppercase font-bold tracking-wider px-2.5 py-0.5 rounded-full bg-primary/15 text-primary">
              Continue Learning
            </span>
            <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
              {currentLesson.subject_slug}
            </span>
          </div>

          <h3 className="text-xl sm:text-2xl font-extrabold text-foreground tracking-tight">
            {currentLesson.lesson_title}
          </h3>

          <p className="text-xs text-muted-foreground">
            Topic: <span className="text-foreground/80 font-medium capitalize">{currentLesson.topic_slug.replace(/-/g, ' ')}</span>
          </p>

          <div className="w-full sm:w-72 space-y-1.5 pt-2">
            <div className="flex justify-between text-xs text-muted-foreground">
              <span>Lesson Progress</span>
              <span className="font-semibold text-foreground">{pct}%</span>
            </div>
            <ProgressBar value={pct} className="h-2 rounded-full" />
          </div>
        </div>

        <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 shrink-0">
          <Link href={courseUrl}>
            <Button size="lg" className="w-full sm:w-auto shadow-lg shadow-primary/25 rounded-full px-6">
              <PlayCircle className="h-5 w-5 mr-2" />
              Resume Lesson
            </Button>
          </Link>
          <Link href="/courses">
            <Button size="lg" variant="outline" className="w-full sm:w-auto rounded-full px-5 text-xs">
              All Courses
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}
