'use client';

import * as React from 'react';
import Link from 'next/link';
import { Clock, BarChart, Sparkles, ChevronRight, Menu } from 'lucide-react';
import { Badge } from '@/components/ui/Badge';
import { SignedIn } from '@clerk/nextjs';
import { CompleteButton } from './CompleteButton';

interface LessonHeaderProps {
  lessonId: string;
  lessonTitle: string;
  lessonSlug: string;
  subjectName: string;
  subjectSlug: string;
  topicTitle: string;
  topicSlug: string;
  estimatedTime?: string;
  difficulty?: string;
  interactiveType?: string | null;
  status?: string;
  onOpenSidebar?: () => void;
  onStatusChange?: (newStatus: string) => void;
}

export function LessonHeader({
  lessonId,
  lessonTitle,
  subjectName,
  subjectSlug,
  topicTitle,
  topicSlug,
  estimatedTime = '15 min',
  difficulty = 'Beginner',
  interactiveType,
  status = 'not_started',
  onOpenSidebar,
  onStatusChange,
}: LessonHeaderProps) {
  return (
    <div className="pb-6 border-b border-border/80 mb-6">
      {/* Breadcrumb + Mobile Menu Button */}
      <div className="flex items-center justify-between text-xs text-muted-foreground mb-4">
        <div className="flex items-center space-x-1.5 flex-wrap">
          <Link href="/courses" className="hover:text-primary transition-colors">
            Courses
          </Link>
          <ChevronRight className="h-3 w-3" />
          <Link href={`/courses/${subjectSlug}`} className="hover:text-primary transition-colors font-medium">
            {subjectName}
          </Link>
          <ChevronRight className="h-3 w-3" />
          <span className="text-foreground/70">{topicTitle}</span>
        </div>

        {onOpenSidebar && (
          <button
            onClick={onOpenSidebar}
            className="lg:hidden flex items-center space-x-1 px-2.5 py-1 rounded-lg border border-border bg-card text-xs text-foreground hover:bg-muted"
          >
            <Menu className="h-3.5 w-3.5" />
            <span>Modules</span>
          </button>
        )}
      </div>

      {/* Main Title and Complete Button */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-foreground tracking-tight">
            {lessonTitle}
          </h1>

          <div className="flex items-center space-x-3 mt-3 flex-wrap gap-y-2">
            <Badge variant="outline" className="text-xs">
              {difficulty}
            </Badge>

            <span className="flex items-center text-xs text-muted-foreground">
              <Clock className="h-3.5 w-3.5 mr-1" />
              {estimatedTime}
            </span>

            {interactiveType && (
              <Badge variant="accent" className="flex items-center space-x-1 text-xs">
                <Sparkles className="h-3 w-3" />
                <span>Interactive Component</span>
              </Badge>
            )}
          </div>
        </div>

        <SignedIn>
          <CompleteButton
            lessonId={lessonId}
            initialStatus={status}
            onStatusChange={onStatusChange}
          />
        </SignedIn>
      </div>
    </div>
  );
}
