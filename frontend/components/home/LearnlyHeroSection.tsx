'use client';

import * as React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { useRouter } from 'next/navigation';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Search,
  BookOpen,
  Zap,
  Users,
  Sparkles,
} from 'lucide-react';

export function LearnlyHeroSection() {
  const router = useRouter();
  const [searchQuery, setSearchQuery] = React.useState('');
  const [showExamples, setShowExamples] = React.useState(false);
  const searchRef = React.useRef<HTMLDivElement>(null);

  React.useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (searchRef.current && !searchRef.current.contains(event.target as Node)) {
        setShowExamples(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      setShowExamples(false);
      router.push(`/courses?q=${encodeURIComponent(searchQuery.trim())}`);
    } else {
      setShowExamples(true);
    }
  };

  const quickTags = ['DSA', 'Machine Learning', 'Deep Learning', 'SQL', 'MongoDB', 'LLMs', 'Agentic AI'];

  return (
    <div className="relative overflow-hidden pt-6 pb-6 lg:pt-10 lg:pb-8">
      {/* Ambient soft glow background that blends with the illustration */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-[650px] pointer-events-none -z-10 overflow-hidden">
        <div className="absolute top-10 right-1/4 w-[500px] h-[500px] bg-indigo-200/35 dark:bg-indigo-900/15 rounded-full blur-3xl animate-pulse-glow" />
        <div className="absolute top-20 left-1/4 w-[420px] h-[420px] bg-purple-200/30 dark:bg-purple-900/15 rounded-full blur-3xl" />
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-6 items-center">
          {/* ============================================================ */}
          {/* LEFT COLUMN: Hero Copy + Search + Features with Motion        */}
          {/* ============================================================ */}
          <motion.div 
            initial={{ opacity: 0, x: -25 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
            className="lg:col-span-6 space-y-6 text-center lg:text-left z-10"
          >
            {/* Pill Tag */}
            <motion.div 
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.1, duration: 0.5 }}
              className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full border border-purple-200/90 dark:border-purple-800/40 bg-purple-50/90 dark:bg-purple-950/50 text-xs font-semibold text-purple-700 dark:text-purple-300 shadow-xs"
            >
              <Sparkles className="h-3.5 w-3.5 text-purple-600 dark:text-purple-400" />
              <span>Learn • Practice • Grow</span>
            </motion.div>

            {/* Giant Headline */}
            <motion.h1 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2, duration: 0.7 }}
              className="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-foreground tracking-tight leading-[1.12]"
            >
              Learn Today <br />
              Build{' '}
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 via-indigo-600 to-indigo-500">
                Tomorrow
              </span>
            </motion.h1>

            {/* Subtitle */}
            <motion.p 
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3, duration: 0.6 }}
              className="text-base sm:text-lg text-muted-foreground leading-relaxed max-w-xl mx-auto lg:mx-0"
            >
              A simple learning space with well-structured courses to help you understand, revise, and grow at your own pace.
            </motion.p>

            {/* Interactive Compact Pill Search Bar with Dynamic Suggestions */}
            <motion.div 
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4, duration: 0.6 }}
              className="pt-1 max-w-md mx-auto lg:mx-0 relative"
              ref={searchRef}
            >
              <form 
                onSubmit={handleSearchSubmit} 
                className="relative flex items-center p-1 rounded-full border border-border/90 bg-card shadow-md shadow-purple-500/5 focus-within:border-primary focus-within:ring-2 focus-within:ring-primary/20 transition-all"
              >
                <Search className="h-4 w-4 text-muted-foreground ml-3 mr-2 shrink-0" />
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => {
                    setSearchQuery(e.target.value);
                    if (!showExamples) setShowExamples(true);
                  }}
                  onFocus={() => setShowExamples(true)}
                  placeholder="What do you want to learn?"
                  className="w-full bg-transparent text-xs sm:text-sm text-foreground placeholder:text-muted-foreground/70 focus:outline-none pr-2"
                />
                <motion.button
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                  type="submit"
                  onClick={(e) => {
                    if (!searchQuery.trim() && !showExamples) {
                      e.preventDefault();
                      setShowExamples(true);
                    }
                  }}
                  className="px-4 sm:px-5 py-1.5 sm:py-2 rounded-full bg-[#5046e5] hover:bg-[#4338ca] text-white text-xs font-semibold shadow-md shadow-indigo-500/25 transition-all shrink-0 cursor-pointer"
                >
                  Search
                </motion.button>
              </form>

              {/* Dynamic Search Suggestions Popover - Shown on click/focus */}
              <AnimatePresence>
                {showExamples && (
                  <motion.div
                    initial={{ opacity: 0, y: -6, scale: 0.98 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -6, scale: 0.98 }}
                    transition={{ duration: 0.18 }}
                    className="absolute left-0 right-0 top-full mt-2 p-3 rounded-2xl bg-card/95 backdrop-blur-md border border-border/90 shadow-xl shadow-purple-500/10 z-30 text-left"
                  >
                    <div className="flex items-center justify-between pb-2 mb-2 border-b border-border/60 text-[11px] font-medium text-muted-foreground">
                      <span className="flex items-center gap-1.5">
                        <Sparkles className="h-3 w-3 text-primary" />
                        Popular Examples
                      </span>
                      <span className="text-[10px] text-muted-foreground/70">Click to explore</span>
                    </div>

                    <div className="flex flex-wrap gap-1.5">
                      {quickTags.map((tag) => (
                        <button
                          key={tag}
                          type="button"
                          onMouseDown={(e) => {
                            e.preventDefault();
                            setSearchQuery(tag);
                            setShowExamples(false);
                            router.push(`/courses?q=${encodeURIComponent(tag)}`);
                          }}
                          className="px-2.5 py-1 rounded-full bg-muted/80 hover:bg-primary hover:text-primary-foreground text-[11px] font-medium transition-all cursor-pointer"
                        >
                          {tag}
                        </button>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>

            {/* 3 Feature Highlights - Clean, Airy & De-congested */}
            <motion.div 
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.5, duration: 0.6 }}
              className="pt-6 border-t border-border/60 max-w-xl mx-auto lg:mx-0"
            >
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 text-left">
                <div className="flex items-start space-x-3">
                  <div className="h-8 w-8 rounded-xl bg-purple-100 dark:bg-purple-900/40 text-purple-600 dark:text-purple-300 flex items-center justify-center shrink-0 shadow-xs">
                    <BookOpen className="h-4 w-4" />
                  </div>
                  <div>
                    <h4 className="text-xs sm:text-sm font-bold text-foreground">Curated Courses</h4>
                    <p className="text-[11px] text-muted-foreground mt-0.5">Learn at your pace</p>
                  </div>
                </div>

                <div className="flex items-start space-x-3">
                  <div className="h-8 w-8 rounded-xl bg-indigo-100 dark:bg-indigo-900/40 text-indigo-600 dark:text-indigo-300 flex items-center justify-center shrink-0 shadow-xs">
                    <Zap className="h-4 w-4" />
                  </div>
                  <div>
                    <h4 className="text-xs sm:text-sm font-bold text-foreground">Clear & Simple</h4>
                    <p className="text-[11px] text-muted-foreground mt-0.5">Easy to understand</p>
                  </div>
                </div>

                <div className="flex items-start space-x-3">
                  <div className="h-8 w-8 rounded-xl bg-sky-100 dark:bg-sky-900/40 text-sky-600 dark:text-sky-300 flex items-center justify-center shrink-0 shadow-xs">
                    <Users className="h-4 w-4" />
                  </div>
                  <div>
                    <h4 className="text-xs sm:text-sm font-bold text-foreground">Lifelong Learning</h4>
                    <p className="text-[11px] text-muted-foreground mt-0.5">Keep coming back</p>
                  </div>
                </div>
              </div>
            </motion.div>
          </motion.div>

          {/* ============================================================ */}
          {/* RIGHT COLUMN: Seamless Organic 3D Girl Illustration           */}
          {/* ============================================================ */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.94 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
            className="lg:col-span-6 relative flex justify-center items-center"
          >
            {/* Soft radiant ambient glow behind the character */}
            <div className="absolute inset-0 bg-gradient-to-tr from-purple-300/25 via-indigo-200/30 to-sky-200/25 dark:from-purple-900/20 dark:to-indigo-900/20 rounded-full blur-3xl -z-10 transform scale-95 pointer-events-none" />

            {/* Seamless Character Container with gentle floating motion */}
            <motion.div
              animate={{ y: [-5, 5, -5] }}
              transition={{ duration: 5.5, repeat: Infinity, ease: "easeInOut" }}
              whileHover={{ scale: 1.02, transition: { duration: 0.3 } }}
              className="relative w-full max-w-[640px] lg:max-w-[700px] flex items-center justify-center cursor-pointer select-none"
            >
              {/* Unframed, transparent PNG rendering without box or mask borders */}
              <Image
                src="/images/girl-transparent.png"
                alt="Student studying with Learnly"
                width={1424}
                height={1104}
                priority
                unoptimized
                className="w-full h-auto object-contain drop-shadow-[0_15px_35px_rgba(99,102,241,0.12)] transition-all duration-300 pointer-events-none"
              />
            </motion.div>
          </motion.div>
        </div>

        {/* ============================================================ */}
        {/* DIVIDER: "Knowledge today. A better you tomorrow."           */}
        {/* ============================================================ */}
        <motion.div 
          initial={{ opacity: 0, y: 15 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="flex items-center justify-center space-x-4 pt-14 pb-2"
        >
          <div className="h-[1px] w-14 sm:w-28 bg-border/80" />
          <span className="text-xs sm:text-sm font-medium text-muted-foreground tracking-wide text-center">
            Knowledge today. A better you tomorrow.
          </span>
          <div className="h-[1px] w-14 sm:w-28 bg-border/80" />
        </motion.div>
      </div>
    </div>
  );
}
