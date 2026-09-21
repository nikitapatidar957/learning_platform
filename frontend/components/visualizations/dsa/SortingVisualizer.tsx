'use client';

import * as React from 'react';
import { Play, Pause, RotateCcw, Shuffle, Sparkles } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface SortingVisualizerProps {
  initialItems?: number[];
}

export function SortingVisualizer({
  initialItems = [45, 18, 82, 35, 94, 23, 67, 12, 54, 76],
}: SortingVisualizerProps) {
  const [items, setItems] = React.useState<number[]>(initialItems);
  const [activeIndices, setActiveIndices] = React.useState<number[]>([]);
  const [sortedIndices, setSortedIndices] = React.useState<number[]>([]);
  const [isSorting, setIsSorting] = React.useState<boolean>(false);
  const [algorithm, setAlgorithm] = React.useState<'bubble' | 'selection'>('bubble');
  const [speed, setSpeed] = React.useState<number>(150);
  const isCancelledRef = React.useRef(false);

  const reset = () => {
    isCancelledRef.current = true;
    setIsSorting(false);
    setActiveIndices([]);
    setSortedIndices([]);
    setItems([...initialItems]);
  };

  const shuffle = () => {
    reset();
    const shuffled = [...items].sort(() => Math.random() - 0.5);
    setItems(shuffled);
  };

  const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

  const runBubbleSort = async () => {
    isCancelledRef.current = false;
    setIsSorting(true);
    const arr = [...items];
    const n = arr.length;
    const sorted: number[] = [];

    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n - i - 1; j++) {
        if (isCancelledRef.current) return;
        setActiveIndices([j, j + 1]);
        await sleep(speed);

        if (arr[j] > arr[j + 1]) {
          const temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
          setItems([...arr]);
          await sleep(speed);
        }
      }
      sorted.push(n - i - 1);
      setSortedIndices([...sorted]);
    }

    setActiveIndices([]);
    setIsSorting(false);
  };

  const runSelectionSort = async () => {
    isCancelledRef.current = false;
    setIsSorting(true);
    const arr = [...items];
    const n = arr.length;
    const sorted: number[] = [];

    for (let i = 0; i < n; i++) {
      let minIdx = i;
      for (let j = i + 1; j < n; j++) {
        if (isCancelledRef.current) return;
        setActiveIndices([minIdx, j]);
        await sleep(speed);

        if (arr[j] < arr[minIdx]) {
          minIdx = j;
        }
      }

      if (minIdx !== i) {
        const temp = arr[i];
        arr[i] = arr[minIdx];
        arr[minIdx] = temp;
        setItems([...arr]);
        await sleep(speed);
      }
      sorted.push(i);
      setSortedIndices([...sorted]);
    }

    setActiveIndices([]);
    setIsSorting(false);
  };

  const startSort = () => {
    if (algorithm === 'bubble') runBubbleSort();
    else runSelectionSort();
  };

  const maxHeight = Math.max(...items, 100);

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-border/60 gap-3">
        <div>
          <h4 className="text-base font-bold text-foreground">Sorting Algorithm Visualizer</h4>
          <p className="text-xs text-muted-foreground">Observe pairwise comparisons and element swaps</p>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <select
            value={algorithm}
            onChange={(e) => setAlgorithm(e.target.value as any)}
            disabled={isSorting}
            className="px-2.5 py-1.5 rounded-lg border border-border bg-background text-xs font-medium"
          >
            <option value="bubble">Bubble Sort — O(n²)</option>
            <option value="selection">Selection Sort — O(n²)</option>
          </select>

          <Button size="sm" variant="outline" onClick={shuffle} disabled={isSorting}>
            <Shuffle className="h-3.5 w-3.5 mr-1" /> Shuffle
          </Button>
          <Button size="sm" variant="outline" onClick={reset}>
            <RotateCcw className="h-3.5 w-3.5 mr-1" /> Reset
          </Button>
          <Button size="sm" onClick={startSort} disabled={isSorting}>
            <Play className="h-3.5 w-3.5 mr-1" /> Start
          </Button>
        </div>
      </div>

      {/* Speed Slider */}
      <div className="flex items-center space-x-3 mt-4 text-xs text-muted-foreground">
        <span>Animation Speed:</span>
        <input
          type="range"
          min="30"
          max="400"
          step="20"
          value={speed}
          onChange={(e) => setSpeed(parseInt(e.target.value, 10))}
          className="w-32 accent-primary"
        />
        <span>{speed}ms</span>
      </div>

      {/* Visual Bars Container */}
      <div className="h-56 flex items-end justify-center space-x-2 sm:space-x-3 pt-6 pb-2 px-4 border-b border-border/40">
        {items.map((val, idx) => {
          const isActive = activeIndices.includes(idx);
          const isSorted = sortedIndices.includes(idx);
          const heightPct = Math.round((val / maxHeight) * 100);

          return (
            <div key={idx} className="flex-1 flex flex-col items-center max-w-[48px] h-full justify-end">
              <span className="text-[10px] font-mono text-muted-foreground mb-1">
                {val}
              </span>
              <div
                className={`w-full rounded-t-lg transition-all duration-150 ${
                  isActive
                    ? 'bg-amber-500 scale-x-105'
                    : isSorted
                    ? 'bg-emerald-500'
                    : 'bg-primary/80 hover:bg-primary'
                }`}
                style={{ height: `${heightPct}%` }}
              />
              <span className="mt-1 text-[9px] font-mono text-muted-foreground">
                {idx}
              </span>
            </div>
          );
        })}
      </div>

      {/* Legend */}
      <div className="flex items-center justify-center space-x-6 text-xs text-muted-foreground mt-4">
        <div className="flex items-center space-x-1.5">
          <span className="w-3 h-3 rounded-full bg-primary/80" />
          <span>Unsorted</span>
        </div>
        <div className="flex items-center space-x-1.5">
          <span className="w-3 h-3 rounded-full bg-amber-500" />
          <span>Active Comparison</span>
        </div>
        <div className="flex items-center space-x-1.5">
          <span className="w-3 h-3 rounded-full bg-emerald-500" />
          <span>Sorted in Place</span>
        </div>
      </div>
    </div>
  );
}
