'use client';

import * as React from 'react';
import Link from 'next/link';
import { ChevronDown, CheckCircle2, Circle, Clock, PlayCircle, Sparkles } from 'lucide-react';
import { TopicSummary } from '@/lib/types';
import { Badge } from '@/components/ui/Badge';

interface TopicAccordionProps {
  topics: TopicSummary[];
  subjectSlug: string;
}

export function TopicAccordion({ topics, subjectSlug }: TopicAccordionProps) {
  const [expandedTopics, setExpandedTopics] = React.useState<Record<string, boolean>>({
    [topics[0]?.slug || '']: true, // first topic expanded by default
  });

  const toggleTopic = (slug: string) => {
    setExpandedTopics((prev) => ({
      ...prev,
      [slug]: !prev[slug],
    }));
  };

  return (
    <div className="space-y-4">
      {topics.map((topic, index) => {
        const isExpanded = !!expandedTopics[topic.slug];
        const moduleNumber = String(index + 1).padStart(2, '0');
        const lessons = topic.lessons || [];
        const completedCount = lessons.filter((l) => l.status === 'completed').length;
        const isModuleCompleted = lessons.length > 0 && completedCount === lessons.length;

        return (
          <div
            key={topic.id || topic.slug}
            className="border border-border rounded-xl bg-card overflow-hidden shadow-sm transition-all"
          >
            {/* Header / Trigger */}
            <button
              onClick={() => toggleTopic(topic.slug)}
              className="w-full flex items-center justify-between p-5 text-left hover:bg-muted/40 transition-colors"
            >
              <div className="flex items-start space-x-4">
                <span className="font-mono text-sm font-bold text-primary/70 mt-0.5">
                  {moduleNumber}
                </span>
                <div>
                  <div className="flex items-center space-x-3">
                    <h4 className="text-base font-semibold text-foreground">
                      {topic.title}
                    </h4>
                    {isModuleCompleted && (
                      <Badge variant="success" className="text-[10px]">
                        Completed
                      </Badge>
                    )}
                  </div>
                  {topic.description && (
                    <p className="text-xs text-muted-foreground mt-1 max-w-xl">
                      {topic.description}
                    </p>
                  )}
                </div>
              </div>

              <div className="flex items-center space-x-4 shrink-0">
                <span className="text-xs text-muted-foreground hidden sm:inline">
                  {completedCount} / {lessons.length} lessons
                </span>
                <ChevronDown
                  className={`h-5 w-5 text-muted-foreground transition-transform duration-200 ${
                    isExpanded ? 'transform rotate-180 text-primary' : ''
                  }`}
                />
              </div>
            </button>

            {/* Collapsible Content */}
            {isExpanded && (
              <div className="border-t border-border/60 bg-muted/20 px-5 py-3 divide-y divide-border/40">
                {lessons.length === 0 ? (
                  <div className="py-4 text-xs text-muted-foreground italic">
                    No lessons published yet in this module.
                  </div>
                ) : (
                  lessons.map((lesson) => {
                    const isCompleted = lesson.status === 'completed';

                    return (
                      <Link
                        key={lesson.id || lesson.slug}
                        href={`/courses/${subjectSlug}/${topic.slug}/${lesson.slug}`}
                        className="flex items-center justify-between py-3 px-2 rounded-lg hover:bg-card/80 transition-colors group"
                      >
                        <div className="flex items-center space-x-3">
                          {isCompleted ? (
                            <CheckCircle2 className="h-4 w-4 text-emerald-500 shrink-0" />
                          ) : (
                            <Circle className="h-4 w-4 text-muted-foreground group-hover:text-primary shrink-0 transition-colors" />
                          )}
                          <div>
                            <span className="text-sm font-medium text-foreground group-hover:text-primary transition-colors">
                              {lesson.title}
                            </span>
                            {lesson.description && (
                              <p className="text-xs text-muted-foreground line-clamp-1 mt-0.5">
                                {lesson.description}
                              </p>
                            )}
                          </div>
                        </div>

                        <div className="flex items-center space-x-3 shrink-0">
                          {lesson.interactiveType && (
                            <Badge variant="accent" className="hidden sm:flex items-center space-x-1 text-[10px]">
                              <Sparkles className="h-3 w-3" />
                              <span>Interactive</span>
                            </Badge>
                          )}
                          <span className="text-xs text-muted-foreground flex items-center">
                            <Clock className="h-3 w-3 mr-1" />
                            {lesson.estimatedTime}
                          </span>
                          <PlayCircle className="h-4 w-4 text-muted-foreground group-hover:text-primary transition-colors" />
                        </div>
                      </Link>
                    );
                  })
                )}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
