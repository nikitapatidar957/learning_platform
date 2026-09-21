'use client';

import * as React from 'react';
import { CheckCircle2, Circle, Loader2 } from 'lucide-react';
import { useAuth } from '@clerk/nextjs';
import { Button } from '@/components/ui/Button';
import { completeLessonProgress } from '@/lib/api';

interface CompleteButtonProps {
  lessonId: string;
  initialStatus?: string;
  onStatusChange?: (newStatus: string) => void;
}

export function CompleteButton({
  lessonId,
  initialStatus = 'not_started',
  onStatusChange,
}: CompleteButtonProps) {
  const { getToken, isSignedIn } = useAuth();
  const [status, setStatus] = React.useState(initialStatus);
  const [isUpdating, setIsUpdating] = React.useState(false);

  React.useEffect(() => {
    setStatus(initialStatus);
  }, [initialStatus]);

  const handleToggle = async () => {
    setIsUpdating(true);
    try {
      const nextStatus = status === 'completed' ? 'in_progress' : 'completed';
      const token = isSignedIn ? await getToken() : null;
      await completeLessonProgress(lessonId, token);
      setStatus(nextStatus);
      if (onStatusChange) onStatusChange(nextStatus);
    } catch (err) {
      console.error('Failed to update progress', err);
    } finally {
      setIsUpdating(false);
    }
  };

  const isCompleted = status === 'completed';

  return (
    <Button
      onClick={handleToggle}
      disabled={isUpdating}
      variant={isCompleted ? 'secondary' : 'primary'}
      className={`relative overflow-hidden transition-all duration-300 font-semibold text-sm ${
        isCompleted
          ? 'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30 hover:bg-emerald-500/25'
          : 'bg-primary text-primary-foreground shadow-md shadow-primary/20'
      }`}
    >
      {isUpdating ? (
        <Loader2 className="h-4 w-4 animate-spin mr-2" />
      ) : isCompleted ? (
        <CheckCircle2 className="h-4 w-4 text-emerald-500 mr-2" />
      ) : (
        <Circle className="h-4 w-4 mr-2" />
      )}
      <span>{isCompleted ? 'Completed ✓' : 'Mark as Complete'}</span>
    </Button>
  );
}
