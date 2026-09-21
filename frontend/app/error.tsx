'use client';

import * as React from 'react';
import Link from 'next/link';
import { AlertCircle, RotateCcw, ArrowLeft } from 'lucide-react';
import { Button } from '@/components/ui/Button';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  React.useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center px-4 space-y-4">
      <div className="p-4 rounded-3xl bg-destructive/10 text-destructive w-fit">
        <AlertCircle className="h-10 w-10" />
      </div>
      <h2 className="text-2xl font-bold text-foreground">Something went wrong</h2>
      <p className="text-xs sm:text-sm text-muted-foreground max-w-sm">
        We couldn&apos;t load this content. Please check your connection or try again.
      </p>
      <div className="pt-2 flex items-center space-x-3">
        <Button variant="outline" onClick={() => reset()}>
          <RotateCcw className="h-4 w-4 mr-2" /> Try Again
        </Button>
        <Link href="/courses">
          <Button variant="primary">
            <ArrowLeft className="h-4 w-4 mr-2" /> All Courses
          </Button>
        </Link>
      </div>
    </div>
  );
}
