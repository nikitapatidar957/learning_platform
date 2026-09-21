'use client';

import * as React from 'react';
import { Search, Loader2, AlertCircle, BookOpen } from 'lucide-react';
import { fetchSubjects } from '@/lib/api';
import { Subject } from '@/lib/types';
import { SubjectCard } from '@/components/courses/SubjectCard';
import { Button } from '@/components/ui/Button';

export default function CoursesPage() {
  const [subjects, setSubjects] = React.useState<Subject[]>([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState<string | null>(null);
  const [filterDifficulty, setFilterDifficulty] = React.useState<string>('All');
  const [searchTerm, setSearchTerm] = React.useState<string>('');

  const loadData = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchSubjects();
      setSubjects(data);
    } catch (err: any) {
      setError(err.message || 'Failed to load courses');
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    loadData();
  }, []);

  const difficulties = ['All', 'Beginner', 'Intermediate', 'Advanced'];

  const filteredSubjects = subjects.filter((s) => {
    const matchesDiff =
      filterDifficulty === 'All' ||
      s.difficulty.toLowerCase().includes(filterDifficulty.toLowerCase());
    const matchesSearch =
      s.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      s.description.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesDiff && matchesSearch;
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      {/* Header */}
      <div className="space-y-3 mb-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold text-foreground tracking-tight">
          Explore Courses
        </h1>
        <p className="text-sm sm:text-base text-muted-foreground max-w-2xl leading-relaxed">
          Comprehensive, hands-on learning paths in core computing and modern artificial intelligence.
        </p>
      </div>

      {/* Filter and Search Bar */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pb-8 border-b border-border">
        {/* Difficulty Pills */}
        <div className="flex items-center space-x-2 overflow-x-auto w-full sm:w-auto pb-2 sm:pb-0">
          {difficulties.map((diff) => (
            <button
              key={diff}
              onClick={() => setFilterDifficulty(diff)}
              className={`px-3.5 py-1.5 rounded-full text-xs font-semibold transition-colors ${
                filterDifficulty === diff
                  ? 'bg-primary text-primary-foreground'
                  : 'bg-muted text-muted-foreground hover:text-foreground'
              }`}
            >
              {diff}
            </button>
          ))}
        </div>

        {/* Search Bar */}
        <div className="relative w-full sm:w-72">
          <Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" />
          <input
            type="text"
            placeholder="Filter courses..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-9 pr-4 py-2 rounded-xl border border-border bg-card text-xs sm:text-sm text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary"
          />
        </div>
      </div>

      {/* State Handlers */}
      {loading && (
        <div className="flex flex-col items-center justify-center py-20 space-y-3">
          <Loader2 className="h-8 w-8 text-primary animate-spin" />
          <p className="text-xs text-muted-foreground">Loading curriculum...</p>
        </div>
      )}

      {error && (
        <div className="p-8 rounded-2xl border border-destructive/40 bg-destructive/10 text-center max-w-lg mx-auto space-y-3 my-12">
          <AlertCircle className="h-8 w-8 text-destructive mx-auto" />
          <h4 className="text-sm font-bold text-foreground">Could not load courses</h4>
          <p className="text-xs text-muted-foreground">{error}</p>
          <Button size="sm" variant="outline" onClick={loadData}>
            Try Again
          </Button>
        </div>
      )}

      {!loading && !error && filteredSubjects.length === 0 && (
        <div className="py-20 text-center text-muted-foreground text-sm">
          No courses found matching your filter criteria.
        </div>
      )}

      {/* Courses Grid */}
      {!loading && !error && filteredSubjects.length > 0 && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pt-8">
          {filteredSubjects.map((subject) => (
            <SubjectCard key={subject.id || subject.slug} subject={subject} />
          ))}
        </div>
      )}
    </div>
  );
}
