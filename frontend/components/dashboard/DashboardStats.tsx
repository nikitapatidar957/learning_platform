'use client';

import * as React from 'react';
import { CheckCircle2, Clock, BookOpen, Flame, Award } from 'lucide-react';
import { OverallProgress } from '@/lib/types';
import { ProgressBar } from '@/components/ui/Progress';

interface DashboardStatsProps {
  progress: OverallProgress;
}

export function DashboardStats({ progress }: DashboardStatsProps) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {/* Overall Completion */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Overall Completion
          </span>
          <div className="p-2 rounded-lg bg-primary/10 text-primary">
            <Award className="h-4 w-4" />
          </div>
        </div>
        <div className="flex items-baseline space-x-2">
          <span className="text-3xl font-extrabold font-mono text-foreground">
            {progress.overall_percentage}%
          </span>
          <span className="text-xs text-muted-foreground">curriculum done</span>
        </div>
        <ProgressBar value={progress.overall_percentage} className="h-2" />
      </div>

      {/* Completed Lessons */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Completed Lessons
          </span>
          <div className="p-2 rounded-lg bg-emerald-500/10 text-emerald-500">
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
          {progress.total_lessons - progress.total_completed} lessons remaining
        </p>
      </div>

      {/* In Progress */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Active Topics
          </span>
          <div className="p-2 rounded-lg bg-amber-500/10 text-amber-500">
            <Clock className="h-4 w-4" />
          </div>
        </div>
        <div className="flex items-baseline space-x-2">
          <span className="text-3xl font-extrabold font-mono text-amber-600 dark:text-amber-400">
            {progress.total_in_progress}
          </span>
          <span className="text-xs text-muted-foreground">in progress</span>
        </div>
        <p className="text-xs text-muted-foreground">Actively ongoing modules</p>
      </div>

      {/* Learning Streak */}
      <div className="p-5 rounded-2xl border border-border bg-card shadow-sm space-y-3">
        <div className="flex items-center justify-between">
          <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
            Study Streak
          </span>
          <div className="p-2 rounded-lg bg-rose-500/10 text-rose-500">
            <Flame className="h-4 w-4" />
          </div>
        </div>
        <div className="flex items-baseline space-x-2">
          <span className="text-3xl font-extrabold font-mono text-rose-500">
            3 Days
          </span>
          <span className="text-xs text-muted-foreground">active streak</span>
        </div>
        <p className="text-xs text-muted-foreground">Keep the momentum going!</p>
      </div>
    </div>
  );
}
