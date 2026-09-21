'use client';

import * as React from 'react';
import { Info, Lightbulb, AlertTriangle, Sparkles } from 'lucide-react';
import { LessonSection } from '@/lib/types';
import { CodeBlock } from '@/components/code/CodeBlock';
import { VisualizerHost } from '@/components/visualizations/VisualizerHost';

interface LessonContentProps {
  sections: LessonSection[];
}

export function LessonContent({ sections }: LessonContentProps) {
  if (!sections || sections.length === 0) {
    return (
      <div className="py-8 text-center text-muted-foreground text-sm italic">
        Content for this lesson is being updated.
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {sections.map((sec, idx) => {
        switch (sec.type) {
          case 'explanation':
            return (
              <div key={idx} className="space-y-2">
                {sec.title && (
                  <h3 className="text-xl font-bold text-foreground tracking-tight">
                    {sec.title}
                  </h3>
                )}
                {sec.content && (
                  <div className="text-sm sm:text-base text-foreground/85 leading-relaxed space-y-3 whitespace-pre-line">
                    {sec.content}
                  </div>
                )}
              </div>
            );

          case 'code':
            return (
              <div key={idx}>
                {sec.code && (
                  <CodeBlock
                    code={sec.code}
                    language={sec.language || 'python'}
                    title={sec.title}
                  />
                )}
              </div>
            );

          case 'callout': {
            const variant = sec.variant || 'info';
            const icon =
              variant === 'tip' ? (
                <Lightbulb className="h-5 w-5 text-amber-500 shrink-0" />
              ) : variant === 'warning' ? (
                <AlertTriangle className="h-5 w-5 text-red-500 shrink-0" />
              ) : (
                <Info className="h-5 w-5 text-blue-500 shrink-0" />
              );

            const bgColors =
              variant === 'tip'
                ? 'bg-amber-500/10 border-amber-500/30'
                : variant === 'warning'
                ? 'bg-red-500/10 border-red-500/30'
                : 'bg-blue-500/10 border-blue-500/30';

            return (
              <div
                key={idx}
                className={`p-4 rounded-xl border flex items-start space-x-3 my-4 ${bgColors}`}
              >
                {icon}
                <div className="text-xs sm:text-sm text-foreground/90 leading-relaxed">
                  {sec.content}
                </div>
              </div>
            );
          }

          case 'visualization':
            return (
              <div key={idx}>
                <VisualizerHost
                  componentName={sec.component}
                  initialState={sec.initialState}
                />
              </div>
            );

          default:
            return null;
        }
      })}
    </div>
  );
}
