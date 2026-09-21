'use client';

import * as React from 'react';
import Link from 'next/link';
import { ArrowLeft, ArrowRight, BookOpen } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface LessonNavInfo {
  slug: string;
  title: string;
  topicSlug: string;
  subjectSlug?: string;
}

interface LessonNavigationProps {
  subjectSlug: string;
  previousLesson?: LessonNavInfo | null;
  nextLesson?: LessonNavInfo | null;
}

export function LessonNavigation({
  subjectSlug,
  previousLesson,
  nextLesson,
}: LessonNavigationProps) {
  return (
    <div className="mt-12 pt-6 border-t border-border flex flex-col sm:flex-row items-center justify-between gap-4">
      {previousLesson ? (
        <Link
          href={`/courses/${subjectSlug}/${previousLesson.topicSlug}/${previousLesson.slug}`}
          className="w-full sm:w-auto"
        >
          <Button variant="outline" className="w-full sm:w-auto flex items-center justify-start sm:justify-center">
            <ArrowLeft className="h-4 w-4 mr-2 shrink-0" />
            <div className="text-left">
              <span className="text-[10px] text-muted-foreground block uppercase font-mono">Previous</span>
              <span className="text-xs font-semibold truncate max-w-[160px] block">{previousLesson.title}</span>
            </div>
          </Button>
        </Link>
      ) : (
        <Link href={`/courses/${subjectSlug}`} className="w-full sm:w-auto">
          <Button variant="ghost" size="sm" className="w-full sm:w-auto">
            <BookOpen className="h-4 w-4 mr-2" /> Back to Subject
          </Button>
        </Link>
      )}

      {nextLesson && (
        <Link
          href={`/courses/${subjectSlug}/${nextLesson.topicSlug}/${nextLesson.slug}`}
          className="w-full sm:w-auto ml-auto"
        >
          <Button variant="primary" className="w-full sm:w-auto flex items-center justify-end sm:justify-center">
            <div className="text-right">
              <span className="text-[10px] text-primary-foreground/80 block uppercase font-mono">Next</span>
              <span className="text-xs font-semibold truncate max-w-[160px] block">{nextLesson.title}</span>
            </div>
            <ArrowRight className="h-4 w-4 ml-2 shrink-0" />
          </Button>
        </Link>
      )}
    </div>
  );
}
