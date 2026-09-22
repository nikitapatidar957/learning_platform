'use client';

import * as React from 'react';
import { CheckCircle2, Clock, BookOpen, Flame, Award, Sparkles } from 'lucide-react';
import { OverallProgress } from '@/lib/types';
import { ProgressBar } from '@/components/ui/Progress';

interface DashboardStatsProps {
  progress: OverallProgress;
}

export function DashboardStats({ progress }: DashboardStatsProps) {
  const isBeginner = progress.total_completed === 0;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {/* 1. Overall Completion */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3 hover:border-primary/40 transition-colors">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Overall Completion
          </span>
          <div className="p-2 rounded-xl bg-primary/10 text-primary shadow-xs">
            <Award className="h-4 w-4" />
          </div>
        </div>
        <div className="flex items-baseline space-x-2">
          <span className="text-3xl font-extrabold font-mono text-foreground">
            {progress.overall_percentage}%
          </span>
          <span className="text-xs text-muted-foreground">
            {isBeginner ? 'ready to start' : 'curriculum done'}
          </span>
        </div>
        <ProgressBar value={progress.overall_percentage} className="h-2 rounded-full" />
      </div>

      {/* 2. Completed Lessons */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3 hover:border-emerald-500/40 transition-colors">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Completed Lessons
          </span>
          <div className="p-2 rounded-xl bg-emerald-500/10 text-emerald-500 shadow-xs">
            <CheckCircle2 className="h-4 w-4" />
          </div>
        </div>
        <div className="flex items-baseline space-x-2">
          <span className="text-3xl font-extrabold font-mono text-emerald-600 dark:text-emerald-400">
            {progress.total_completed}
          </span>
          <span className="text-xs text-muted-foreground">/ {progress.total_lessons} total</span>
        </div>
        <p className="text-xs text-muted-foreground">
          {isBeginner
            ? `${progress.total_lessons} interactive lessons available`
            : `${progress.total_lessons - progress.total_completed} lessons remaining`}
        </p>
      </div>

      {/* 3. Active Topics */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3 hover:border-amber-500/40 transition-colors">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Active Topics
          </span>
          <div className="p-2 rounded-xl bg-amber-500/10 text-amber-500 shadow-xs">
            <Clock className="h-4 w-4" />
          </div>
        </div>
        <div className="flex items-baseline space-x-2">
          <span className="text-3xl font-extrabold font-mono text-amber-600 dark:text-amber-400">
            {progress.total_in_progress}
          </span>
          <span className="text-xs text-muted-foreground">
            {isBeginner ? 'in progress' : 'in progress'}
          </span>
        </div>
        <p className="text-xs text-muted-foreground">
          {isBeginner ? 'Pick a track below to start' : 'Actively ongoing modules'}
        </p>
      </div>

      {/* 4. Study Streak */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3 hover:border-rose-500/40 transition-colors">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Study Streak
          </span>
          <div className="p-2 rounded-xl bg-rose-500/10 text-rose-500 shadow-xs">
            <Flame className="h-4 w-4" />
          </div>
        </div>
        <div className="flex items-baseline space-x-2">
          <span className="text-3xl font-extrabold font-mono text-rose-500">
            {isBeginner ? 'Day 1' : '3 Days'}
          </span>
          <span className="text-xs text-muted-foreground">
            {isBeginner ? 'ready' : 'active streak'}
          </span>
        </div>
        <p className="text-xs text-muted-foreground">
          {isBeginner ? 'Complete 1st lesson to build streak' : 'Keep the momentum going!'}
        </p>
      </div>
    </div>
  );
}
