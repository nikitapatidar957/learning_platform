'use client';

import * as React from 'react';
import { useRouter } from 'next/navigation';
import { Search, X, BookOpen, Layers, FileText, ArrowRight, Loader2 } from 'lucide-react';
import { searchContent } from '@/lib/api';
import { SearchResult } from '@/lib/types';

interface SearchDialogProps {
  isOpen: boolean;
  onClose: () => void;
}

export function SearchDialog({ isOpen, onClose }: SearchDialogProps) {
  const [query, setQuery] = React.useState('');
  const [results, setResults] = React.useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = React.useState(false);
  const router = useRouter();
  const inputRef = React.useRef<HTMLInputElement>(null);

  React.useEffect(() => {
    if (isOpen) {
      setTimeout(() => inputRef.current?.focus(), 50);
    } else {
      setQuery('');
      setResults([]);
    }
  }, [isOpen]);

  React.useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        if (isOpen) onClose();
        else onClose(); // parent can toggle
      }
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  // Debounced search
  React.useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      setIsLoading(false);
      return;
    }

    const timer = setTimeout(async () => {
      setIsLoading(true);
      try {
        const res = await searchContent(query);
        setResults(res);
      } catch (err) {
        console.error('Search error', err);
      } finally {
        setIsLoading(false);
      }
    }, 250);

    return () => clearTimeout(timer);
  }, [query]);

  if (!isOpen) return null;

  const handleSelect = (url: string) => {
    onClose();
    router.push(url);
  };

  const getIcon = (type: string) => {
    switch (type) {
      case 'subject':
        return <BookOpen className="h-4 w-4 text-indigo-500" />;
      case 'topic':
        return <Layers className="h-4 w-4 text-emerald-500" />;
      default:
        return <FileText className="h-4 w-4 text-blue-500" />;
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 px-4 bg-black/60 backdrop-blur-sm animate-fade-in">
      <div
        className="fixed inset-0"
        onClick={onClose}
        aria-hidden="true"
      />
      <div className="relative w-full max-w-2xl bg-card border border-border rounded-xl shadow-2xl overflow-hidden z-10">
        <div className="flex items-center px-4 py-3 border-b border-border bg-muted/40">
          <Search className="h-5 w-5 text-muted-foreground mr-3" />
          <input
            ref={inputRef}
            type="text"
            placeholder="Search DSA, Machine Learning, SQL, LLMs, Lessons..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="flex-1 bg-transparent border-0 outline-none text-foreground placeholder:text-muted-foreground text-base"
          />
          {isLoading ? (
            <Loader2 className="h-4 w-4 text-muted-foreground animate-spin mr-2" />
          ) : null}
          <button
            onClick={onClose}
            className="p-1 rounded-md text-muted-foreground hover:text-foreground hover:bg-muted"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        <div className="max-h-96 overflow-y-auto p-2 divide-y divide-border/40">
          {query.trim() && !isLoading && results.length === 0 && (
            <div className="py-8 text-center text-muted-foreground text-sm">
              No results found for &ldquo;<span className="font-semibold">{query}</span>&rdquo;
            </div>
          )}

          {!query.trim() && (
            <div className="py-6 px-4 text-xs text-muted-foreground">
              Try searching for: <span className="text-primary font-medium">Binary Search</span>, <span className="text-primary font-medium">Linear Regression</span>, <span className="text-primary font-medium">SQL</span>, <span className="text-primary font-medium">RAG</span>, or <span className="text-primary font-medium">Agents</span>.
            </div>
          )}

          {results.map((item) => (
            <div
              key={`${item.type}-${item.id}`}
              onClick={() => handleSelect(item.url)}
              className="flex items-center justify-between p-3 rounded-lg hover:bg-muted/60 cursor-pointer transition-colors group"
            >
              <div className="flex items-center space-x-3 overflow-hidden">
                <div className="p-2 rounded-md bg-muted border border-border">
                  {getIcon(item.type)}
                </div>
                <div>
                  <div className="flex items-center space-x-2">
                    <span className="font-medium text-foreground group-hover:text-primary transition-colors text-sm">
                      {item.title}
                    </span>
                    <span className="text-[10px] uppercase font-semibold tracking-wider px-1.5 py-0.5 rounded bg-muted text-muted-foreground">
                      {item.type}
                    </span>
                  </div>
                  {item.description && (
                    <p className="text-xs text-muted-foreground line-clamp-1 mt-0.5">
                      {item.description}
                    </p>
                  )}
                </div>
              </div>
              <ArrowRight className="h-4 w-4 text-muted-foreground group-hover:text-primary group-hover:translate-x-0.5 transition-all ml-2 shrink-0" />
            </div>
          ))}
        </div>

        <div className="px-4 py-2 bg-muted/40 border-t border-border flex items-center justify-between text-xs text-muted-foreground">
          <span>Navigate with mouse or keyboard</span>
          <kbd className="px-1.5 py-0.5 bg-muted rounded border border-border text-[11px]">ESC to close</kbd>
        </div>
      </div>
    </div>
  );
}
