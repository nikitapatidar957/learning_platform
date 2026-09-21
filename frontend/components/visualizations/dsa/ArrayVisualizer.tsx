'use client';

import * as React from 'react';
import { Play, RotateCcw, Plus, Trash2, Search, Sparkles } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface ArrayVisualizerProps {
  initialItems?: number[];
}

export function ArrayVisualizer({ initialItems = [10, 25, 38, 42, 67, 89] }: ArrayVisualizerProps) {
  const [items, setItems] = React.useState<number[]>(initialItems);
  const [highlightedIndex, setHighlightedIndex] = React.useState<number | null>(null);
  const [foundIndex, setFoundIndex] = React.useState<number | null>(null);
  const [inputValue, setInputValue] = React.useState<string>('50');
  const [insertIndex, setInsertIndex] = React.useState<string>('2');
  const [searchValue, setSearchValue] = React.useState<string>('42');
  const [message, setMessage] = React.useState<string>('Ready. Select an operation below.');
  const [isSearching, setIsSearching] = React.useState(false);

  const reset = () => {
    setItems(initialItems);
    setHighlightedIndex(null);
    setFoundIndex(null);
    setMessage('Array reset to initial state.');
  };

  const handleAppend = () => {
    const val = parseInt(inputValue, 10);
    if (isNaN(val)) return;
    setItems((prev) => [...prev, val]);
    setHighlightedIndex(items.length);
    setFoundIndex(null);
    setMessage(`Appended ${val} at index ${items.length} in O(1) amortized time.`);
  };

  const handleInsert = () => {
    const val = parseInt(inputValue, 10);
    const idx = parseInt(insertIndex, 10);
    if (isNaN(val) || isNaN(idx)) return;
    const boundedIdx = Math.max(0, Math.min(idx, items.length));
    const next = [...items];
    next.splice(boundedIdx, 0, val);
    setItems(next);
    setHighlightedIndex(boundedIdx);
    setFoundIndex(null);
    setMessage(`Inserted ${val} at index ${boundedIdx}. Elements to the right shifted in O(n) time.`);
  };

  const handleDelete = (index: number) => {
    const deletedVal = items[index];
    const next = items.filter((_, i) => i !== index);
    setItems(next);
    setHighlightedIndex(null);
    setFoundIndex(null);
    setMessage(`Deleted ${deletedVal} from index ${index}. Remaining elements shifted.`);
  };

  const handleSearch = async () => {
    const target = parseInt(searchValue, 10);
    if (isNaN(target)) return;
    setIsSearching(true);
    setFoundIndex(null);
    setMessage(`Searching linearly for ${target}...`);

    for (let i = 0; i < items.length; i++) {
      setHighlightedIndex(i);
      await new Promise((res) => setTimeout(res, 500));
      if (items[i] === target) {
        setFoundIndex(i);
        setMessage(`Found target ${target} at index ${i}!`);
        setIsSearching(false);
        return;
      }
    }

    setHighlightedIndex(null);
    setMessage(`Target ${target} was not found in array.`);
    setIsSearching(false);
  };

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center justify-between pb-4 border-b border-border/60">
        <div className="flex items-center space-x-2">
          <div className="p-2 rounded-lg bg-indigo-500/10 text-indigo-500">
            <Sparkles className="h-5 w-5" />
          </div>
          <div>
            <h4 className="text-base font-bold text-foreground">Interactive Array Visualizer</h4>
            <p className="text-xs text-muted-foreground">Memory indices, insertion shifts, and search operations</p>
          </div>
        </div>
        <Button variant="outline" size="sm" onClick={reset}>
          <RotateCcw className="h-3.5 w-3.5 mr-1" />
          Reset
        </Button>
      </div>

      {/* Array Element Blocks */}
      <div className="py-8 overflow-x-auto">
        <div className="flex items-center justify-center space-x-3 min-w-[340px]">
          {items.map((val, idx) => {
            const isHighlight = highlightedIndex === idx;
            const isFound = foundIndex === idx;

            return (
              <div key={idx} className="flex flex-col items-center group">
                <div
                  className={`w-14 h-16 sm:w-16 sm:h-20 rounded-xl flex items-center justify-center font-mono font-bold text-lg border-2 transition-all duration-300 shadow-sm relative ${
                    isFound
                      ? 'bg-emerald-500 text-white border-emerald-400 scale-105 shadow-emerald-500/30'
                      : isHighlight
                      ? 'bg-primary text-primary-foreground border-primary scale-105 shadow-primary/30'
                      : 'bg-muted/60 text-foreground border-border hover:border-primary/40'
                  }`}
                >
                  {val}
                  <button
                    onClick={() => handleDelete(idx)}
                    className="absolute -top-2 -right-2 p-1 rounded-full bg-destructive text-destructive-foreground opacity-0 group-hover:opacity-100 transition-opacity hover:scale-110 shadow"
                    title={`Delete index ${idx}`}
                  >
                    <Trash2 className="h-3 w-3" />
                  </button>
                </div>
                <span className="mt-2 text-xs font-mono font-semibold text-muted-foreground">
                  [{idx}]
                </span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Status Bar */}
      <div className="p-3 rounded-lg bg-muted/40 border border-border/50 text-xs font-mono text-center text-foreground">
        {message}
      </div>

      {/* Controls Grid */}
      <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4 pt-4 border-t border-border/60">
        {/* Append & Insert */}
        <div className="space-y-2">
          <label className="text-xs font-semibold text-foreground">Insert / Append Element</label>
          <div className="flex space-x-2">
            <input
              type="number"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Value"
              className="w-20 px-3 py-1.5 rounded-lg border border-border bg-background text-sm"
            />
            <input
              type="number"
              value={insertIndex}
              onChange={(e) => setInsertIndex(e.target.value)}
              placeholder="Index"
              className="w-20 px-3 py-1.5 rounded-lg border border-border bg-background text-sm"
            />
            <Button size="sm" variant="secondary" onClick={handleInsert}>
              <Plus className="h-3.5 w-3.5 mr-1" /> Insert
            </Button>
            <Button size="sm" variant="primary" onClick={handleAppend}>
              Append
            </Button>
          </div>
        </div>

        {/* Linear Search */}
        <div className="space-y-2">
          <label className="text-xs font-semibold text-foreground">Search Value in Array</label>
          <div className="flex space-x-2">
            <input
              type="number"
              value={searchValue}
              onChange={(e) => setSearchValue(e.target.value)}
              placeholder="Target value"
              className="flex-1 px-3 py-1.5 rounded-lg border border-border bg-background text-sm"
            />
            <Button size="sm" onClick={handleSearch} disabled={isSearching}>
              <Search className="h-3.5 w-3.5 mr-1" /> Search
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
