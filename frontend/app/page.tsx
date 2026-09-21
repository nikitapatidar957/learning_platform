'use client';

import * as React from 'react';
import Link from 'next/link';
import {
  Sparkles,
  ArrowRight,
  Code,
  Brain,
  Cpu,
  Layers,
  CheckCircle,
  Terminal,
  Zap,
  Globe,
  Loader2,
  AlertCircle,
  GraduationCap,
} from 'lucide-react';
import { SignUpButton } from '@clerk/nextjs';
import { fetchSubjects } from '@/lib/api';
import { Subject } from '@/lib/types';
import { SubjectCard } from '@/components/courses/SubjectCard';
import { Button } from '@/components/ui/Button';
import { motion } from 'framer-motion';
import { LearnlyHeroSection } from '@/components/home/LearnlyHeroSection';
import { InteractiveHomeWindow } from '@/components/home/InteractiveHomeWindow';

export default function HomePage() {
  const [subjects, setSubjects] = React.useState<Subject[]>([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);

  const loadSubjects = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchSubjects();
      setSubjects(data);
    } catch (err: any) {
      setError(err.message || 'Failed to connect to FastAPI backend');
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    loadSubjects();
  }, []);

  return (
    <div className="flex flex-col min-h-screen">
      {/* ============================================================ */}
      {/* SECTION 1: Learnly Hero + Seamless girl.png + Search          */}
      {/* ============================================================ */}
      <LearnlyHeroSection />

      {/* ============================================================ */}
      {/* SECTION 2: Subject Explorer (8 Core Disciplines)              */}
      {/* ============================================================ */}
      <motion.section 
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-60px" }}
        transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
        className="py-16 sm:py-20 bg-muted/20 border-t border-border/80"
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-14 space-y-3">
            <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-primary/10 text-primary text-xs font-semibold">
              <GraduationCap className="h-3.5 w-3.5" />
              <span>Full Curriculum</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-foreground tracking-tight">
              Explore Our Core Learning Tracks
            </h2>
            <p className="text-sm sm:text-base text-muted-foreground leading-relaxed">
              Every course is built from first principles with hands-on interactive components, algorithmic sandboxes, and step-by-step visualizations.
            </p>
          </div>

          {/* Loading State */}
          {loading && (
            <div className="flex flex-col items-center justify-center py-16 space-y-3">
              <Loader2 className="h-8 w-8 text-primary animate-spin" />
              <p className="text-xs text-muted-foreground">Loading curriculum from backend...</p>
            </div>
          )}

          {/* Error State */}
          {error && (
            <div className="p-6 rounded-2xl border border-destructive/40 bg-destructive/10 text-center max-w-lg mx-auto space-y-3 my-8">
              <AlertCircle className="h-8 w-8 text-destructive mx-auto" />
              <h4 className="text-sm font-bold text-foreground">Failed to Load Courses</h4>
              <p className="text-xs text-muted-foreground">{error}</p>
              <Button size="sm" variant="outline" onClick={loadSubjects}>
                Try Again
              </Button>
            </div>
          )}

          {/* Dynamic Subject Cards Grid with Motion */}
          {!loading && !error && (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {subjects.map((subject, index) => (
                <motion.div
                  key={subject.id || subject.slug}
                  initial={{ opacity: 0, y: 25 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.06, duration: 0.5 }}
                  whileHover={{ y: -6, transition: { duration: 0.2 } }}
                >
                  <SubjectCard subject={subject} />
                </motion.div>
              ))}
            </div>
          )}
        </div>
      </motion.section>

      {/* ============================================================ */}
      {/* SECTION 3: Interactive Playground & Studio Window            */}
      {/* ============================================================ */}
      <motion.section 
        id="playground"
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-60px" }}
        transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
        className="py-16 sm:py-20 border-t border-border/80 bg-card/40 relative"
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto mb-8 space-y-3">
            <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 text-xs font-semibold">
              <Sparkles className="h-3.5 w-3.5" />
              <span>Interactive In-Browser Studio</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-foreground tracking-tight">
              Test-Drive Algorithms & Models Live
            </h2>
            <p className="text-sm sm:text-base text-muted-foreground leading-relaxed">
              Step through live sorting, simulate neural hyperplanes, execute SQL & Mongo queries, and orchestrate autonomous AI agents before opening a lesson.
            </p>
          </div>

          <InteractiveHomeWindow />
        </div>
      </motion.section>

      {/* ============================================================ */}
      {/* SECTION 4: Final Call to Action Banner                       */}
      {/* ============================================================ */}
      <section className="py-20 border-t border-border/80 relative overflow-hidden bg-gradient-to-b from-transparent to-primary/5">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6 relative z-10">
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-foreground tracking-tight">
            Your Tech Journey Starts Here.
          </h2>
          <p className="text-base sm:text-lg text-muted-foreground max-w-2xl mx-auto leading-relaxed">
            Learn DSA, ML, SQL, and Agentic AI. Build skills that actually matter.{' '}
            <strong className="font-bold text-foreground">Free to learn.</strong>
          </p>
          <div className="flex flex-wrap items-center justify-center gap-3.5 pt-2">
            <SignUpButton mode="modal">
              <button className="px-8 py-3.5 text-base font-semibold text-white bg-[#5046e5] hover:bg-[#4338ca] rounded-full shadow-xl shadow-indigo-500/25 hover:shadow-indigo-500/40 transition-all hover:scale-[1.02] active:scale-[0.98]">
                Get Started Free →
              </button>
            </SignUpButton>
            <Link href="/courses">
              <Button size="lg" variant="outline" className="rounded-full px-7">
                Browse All Courses
              </Button>
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}

