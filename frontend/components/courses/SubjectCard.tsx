'use client';

import * as React from 'react';
import Link from 'next/link';
import {
  Binary,
  Brain,
  Cpu,
  Database,
  Layers,
  Sparkles,
  Wand2,
  Bot,
  ArrowRight,
  BookOpen,
  Clock,
} from 'lucide-react';
import { Subject } from '@/lib/types';
import { Badge } from '@/components/ui/Badge';
import { ProgressBar } from '@/components/ui/Progress';

interface SubjectCardProps {
  subject: Subject;
  progressPercentage?: number;
}

export function SubjectCard({ subject, progressPercentage = 0 }: SubjectCardProps) {
  const getSubjectIcon = (iconName: string) => {
    switch (iconName.toLowerCase()) {
      case 'binary':
        return <Binary className="h-6 w-6 text-indigo-500" />;
      case 'brain':
        return <Brain className="h-6 w-6 text-purple-500" />;
      case 'cpu':
        return <Cpu className="h-6 w-6 text-cyan-500" />;
      case 'database':
        return <Database className="h-6 w-6 text-blue-500" />;
      case 'layers':
        return <Layers className="h-6 w-6 text-emerald-500" />;
      case 'sparkles':
        return <Sparkles className="h-6 w-6 text-amber-500" />;
      case 'wand2':
        return <Wand2 className="h-6 w-6 text-pink-500" />;
      case 'bot':
        return <Bot className="h-6 w-6 text-rose-500" />;
      default:
        return <BookOpen className="h-6 w-6 text-primary" />;
    }
  };

  return (
    <Link
      href={`/courses/${subject.slug}`}
      className="group relative flex flex-col justify-between p-6 rounded-2xl border border-border/80 bg-card hover:border-primary/50 hover:shadow-xl hover:shadow-primary/5 transition-all duration-300 hover:-translate-y-1"
    >
      <div>
        <div className="flex items-start justify-between mb-4">
          <div className="p-3 rounded-xl bg-muted/80 border border-border/50 group-hover:scale-110 transition-transform">
            {getSubjectIcon(subject.icon)}
          </div>
          <Badge variant="outline" className="text-[11px]">
            {subject.difficulty}
          </Badge>
        </div>

        <h3 className="text-lg font-bold text-foreground group-hover:text-primary transition-colors tracking-tight">
          {subject.name}
        </h3>

        <p className="mt-2 text-xs sm:text-sm text-muted-foreground line-clamp-2 leading-relaxed">
          {subject.description}
        </p>
      </div>

      <div className="mt-6 pt-4 border-t border-border/60">
        <div className="flex items-center justify-between text-xs text-muted-foreground mb-3">
          <span className="flex items-center">
            <BookOpen className="h-3.5 w-3.5 mr-1 text-muted-foreground" />
            {subject.topic_count} Topics • {subject.lesson_count} Lessons
          </span>
          {subject.estimated_hours && (
            <span className="flex items-center">
              <Clock className="h-3.5 w-3.5 mr-1" />
              {subject.estimated_hours}
            </span>
          )}
        </div>

        {progressPercentage > 0 ? (
          <div className="space-y-1.5 mb-2">
            <div className="flex justify-between text-[11px] text-muted-foreground">
              <span>Progress</span>
              <span className="font-semibold text-primary">{progressPercentage}%</span>
            </div>
            <ProgressBar value={progressPercentage} className="h-1.5" />
          </div>
        ) : null}

        <div className="flex items-center justify-between text-xs font-semibold text-primary pt-1">
          <span>{progressPercentage > 0 ? 'Continue Learning' : 'Explore Curriculum'}</span>
          <ArrowRight className="h-4 w-4 group-hover:translate-x-1 transition-transform" />
        </div>
      </div>
    </Link>
  );
}
