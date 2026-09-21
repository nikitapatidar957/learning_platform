import Link from 'next/link';
import { Compass, ArrowLeft } from 'lucide-react';
import { Button } from '@/components/ui/Button';

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] text-center px-4 space-y-4">
      <div className="p-4 rounded-3xl bg-primary/10 text-primary w-fit shadow-inner">
        <Compass className="h-10 w-10" />
      </div>
      <h1 className="text-4xl font-extrabold text-foreground tracking-tight">404</h1>
      <h2 className="text-xl font-bold text-foreground">Page Not Found</h2>
      <p className="text-xs sm:text-sm text-muted-foreground max-w-sm">
        The course, topic, or lesson you were looking for doesn&apos;t exist or has moved.
      </p>
      <div className="pt-2">
        <Link href="/">
          <Button variant="primary">
            <ArrowLeft className="h-4 w-4 mr-2" /> Back to Home
          </Button>
        </Link>
      </div>
    </div>
  );
}
