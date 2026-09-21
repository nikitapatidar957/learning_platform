'use client';

import * as React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { CheckCircle2, Circle, ChevronDown, ChevronRight, X, Sparkles } from 'lucide-react';
import { TopicSummary } from '@/lib/types';
import { ProgressBar } from '@/components/ui/Progress';

interface CourseSidebarProps {
  subjectName: string;
  subjectSlug: string;
  topics: TopicSummary[];
  currentLessonSlug: string;
  isOpenMobile?: boolean;
  onCloseMobile?: () => void;
}

export function CourseSidebar({
  subjectName,
  subjectSlug,
  topics,
  currentLessonSlug,
  isOpenMobile,
  onCloseMobile,
}: CourseSidebarProps) {
  const [collapsedTopics, setCollapsedTopics] = React.useState<Record<string, boolean>>({});

  const toggleTopic = (slug: string) => {
    setCollapsedTopics((prev) => ({ ...prev, [slug]: !prev[slug] }));
  };

  // Calculate overall course completion
  const allLessons = topics.flatMap((t) => t.lessons || []);
  const completedLessons = allLessons.filter((l) => l.status === 'completed');
  const progressPct = allLessons.length > 0 ? Math.round((completedLessons.length / allLessons.length) * 100) : 0;

  const content = (
    <div className="flex flex-col h-full bg-card border-r border-border overflow-hidden select-none">
      {/* Sidebar Header */}
      <div className="p-4 border-b border-border bg-muted/30">
        <div className="flex items-center justify-between">
          <Link
            href={`/courses/${subjectSlug}`}
            className="text-xs font-semibold text-primary uppercase tracking-wider hover:underline"
          >
            ← {subjectName}
          </Link>
          {onCloseMobile && (
            <button
              onClick={onCloseMobile}
              className="lg:hidden p-1 rounded-md text-muted-foreground hover:bg-muted"
            >
              <X className="h-4 w-4" />
            </button>
          )}
        </div>

        <div className="mt-3 space-y-1.5">
          <div className="flex items-center justify-between text-xs text-muted-foreground">
            <span>Course Progress</span>
            <span className="font-semibold text-foreground">{progressPct}%</span>
          </div>
          <ProgressBar value={progressPct} className="h-1.5" />
          <p className="text-[11px] text-muted-foreground">
            {completedLessons.length} of {allLessons.length} lessons completed
          </p>
        </div>
      </div>

      {/* Modules and Lessons list */}
      <div className="flex-1 overflow-y-auto p-3 space-y-3">
        {topics.map((topic, index) => {
          const isCollapsed = !!collapsedTopics[topic.slug];
          const lessons = topic.lessons || [];

          return (
            <div key={topic.slug} className="space-y-1">
              <button
                onClick={() => toggleTopic(topic.slug)}
                className="w-full flex items-center justify-between px-2.5 py-1.5 text-xs font-semibold text-foreground/80 hover:text-foreground rounded-md hover:bg-muted/60 transition-colors"
              >
                <span className="flex items-center space-x-1.5 truncate">
                  <span className="text-muted-foreground font-mono">{String(index + 1).padStart(2, '0')}.</span>
                  <span className="truncate">{topic.title}</span>
                </span>
                {isCollapsed ? (
                  <ChevronRight className="h-3.5 w-3.5 text-muted-foreground shrink-0" />
                ) : (
                  <ChevronDown className="h-3.5 w-3.5 text-muted-foreground shrink-0" />
                )}
              </button>

              {!isCollapsed && (
                <div className="pl-4 space-y-0.5 border-l border-border/60 ml-2">
                  {lessons.map((lesson) => {
                    const isActive = lesson.slug === currentLessonSlug;
                    const isCompleted = lesson.status === 'completed';

                    return (
                      <Link
                        key={lesson.slug}
                        href={`/courses/${subjectSlug}/${topic.slug}/${lesson.slug}`}
                        onClick={onCloseMobile}
                        className={`flex items-center space-x-2 px-2.5 py-1.5 rounded-lg text-xs transition-colors group ${
                          isActive
                            ? 'bg-primary/10 text-primary font-semibold border border-primary/20'
                            : 'text-muted-foreground hover:text-foreground hover:bg-muted/40'
                        }`}
                      >
                        {isCompleted ? (
                          <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500 shrink-0" />
                        ) : (
                          <Circle
                            className={`h-3.5 w-3.5 shrink-0 ${
                              isActive ? 'text-primary' : 'text-muted-foreground/60 group-hover:text-muted-foreground'
                            }`}
                          />
                        )}
                        <span className="truncate flex-1">{lesson.title}</span>
                        {lesson.interactiveType && (
                          <Sparkles className="h-3 w-3 text-amber-500 shrink-0 opacity-80" />
                        )}
                      </Link>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );

  return (
    <>
      {/* Desktop Persistent Sidebar */}
      <aside className="hidden lg:block w-72 shrink-0 sticky top-16 h-[calc(100vh-4rem)]">
        {content}
      </aside>

      {/* Mobile Drawer */}
      {isOpenMobile && (
        <div className="fixed inset-0 z-50 lg:hidden">
          <div
            className="fixed inset-0 bg-black/60 backdrop-blur-sm"
            onClick={onCloseMobile}
          />
          <div className="fixed inset-y-0 left-0 w-80 max-w-[85vw] shadow-2xl z-10 animate-fade-in">
            {content}
          </div>
        </div>
      )}
    </>
  );
}
