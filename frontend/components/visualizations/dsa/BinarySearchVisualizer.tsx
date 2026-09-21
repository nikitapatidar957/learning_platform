'use client';

import * as React from 'react';
import { Play, RotateCcw, ArrowRight, CheckCircle2, XCircle } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface BinarySearchVisualizerProps {
  initialItems?: number[];
}

export function BinarySearchVisualizer({
  initialItems = [3, 8, 14, 21, 35, 47, 56, 68, 72, 85, 94],
}: BinarySearchVisualizerProps) {
  const [items] = React.useState<number[]>(initialItems.sort((a, b) => a - b));
  const [target, setTarget] = React.useState<number>(47);
  const [low, setLow] = React.useState<number>(0);
  const [high, setHigh] = React.useState<number>(items.length - 1);
  const [mid, setMid] = React.useState<number | null>(null);
  const [status, setStatus] = React.useState<'idle' | 'searching' | 'found' | 'not_found'>('idle');
  const [message, setMessage] = React.useState<string>('Select a target and click "Step" or "Auto Play".');
  const [stepCount, setStepCount] = React.useState<number>(0);

  const reset = () => {
    setLow(0);
    setHigh(items.length - 1);
    setMid(null);
    setStatus('idle');
    setStepCount(0);
    setMessage('Search space reset.');
  };

  const handleStep = () => {
    if (status === 'found' || status === 'not_found') {
      reset();
      return;
    }

    if (low > high) {
      setStatus('not_found');
      setMessage(`Target ${target} was not found in the array.`);
      return;
    }

    const currentMid = Math.floor((low + high) / 2);
    setMid(currentMid);
    setStepCount((c) => c + 1);

    if (items[currentMid] === target) {
      setStatus('found');
      setMessage(`Match found! arr[${currentMid}] == ${target} in ${stepCount + 1} steps.`);
    } else if (items[currentMid] < target) {
      setMessage(`arr[${currentMid}] (${items[currentMid]}) < ${target}. Eliminate left half, low = ${currentMid + 1}.`);
      setLow(currentMid + 1);
    } else {
      setMessage(`arr[${currentMid}] (${items[currentMid]}) > ${target}. Eliminate right half, high = ${currentMid - 1}.`);
      setHigh(currentMid - 1);
    }
  };

  const handleAutoPlay = async () => {
    reset();
    let l = 0;
    let h = items.length - 1;
    let steps = 0;

    while (l <= h) {
      const m = Math.floor((l + h) / 2);
      setLow(l);
      setHigh(h);
      setMid(m);
      steps++;
      setStepCount(steps);

      if (items[m] === target) {
        setStatus('found');
        setMessage(`Match found! arr[${m}] == ${target} in ${steps} steps.`);
        return;
      } else if (items[m] < target) {
        setMessage(`arr[${m}] < ${target}. Shift low to ${m + 1}`);
        l = m + 1;
      } else {
        setMessage(`arr[${m}] > ${target}. Shift high to ${m - 1}`);
        h = m - 1;
      }

      await new Promise((r) => setTimeout(r, 900));
    }

    setStatus('not_found');
    setMessage(`Target ${target} not found.`);
  };

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center justify-between pb-4 border-b border-border/60">
        <div>
          <h4 className="text-base font-bold text-foreground">Binary Search Visualizer</h4>
          <p className="text-xs text-muted-foreground">O(log n) logarithmic halving of sorted search spaces</p>
        </div>
        <div className="flex items-center space-x-2">
          <Button variant="outline" size="sm" onClick={reset}>
            <RotateCcw className="h-3.5 w-3.5 mr-1" /> Reset
          </Button>
          <Button size="sm" onClick={handleStep}>
            Step <ArrowRight className="h-3.5 w-3.5 ml-1" />
          </Button>
          <Button size="sm" variant="secondary" onClick={handleAutoPlay}>
            <Play className="h-3.5 w-3.5 mr-1" /> Auto
          </Button>
        </div>
      </div>

      {/* Target selector */}
      <div className="flex items-center space-x-3 mt-4 text-xs">
        <span className="font-semibold text-foreground">Target value:</span>
        <select
          value={target}
          onChange={(e) => {
            setTarget(parseInt(e.target.value, 10));
            reset();
          }}
          className="px-2.5 py-1 rounded border border-border bg-background text-foreground text-xs"
        >
          {items.map((it) => (
            <option key={it} value={it}>
              {it}
            </option>
          ))}
          <option value={999}>999 (Not in array)</option>
        </select>
        <span className="text-muted-foreground">
          Step count: <span className="font-semibold text-foreground">{stepCount}</span>
        </span>
      </div>

      {/* Visual Array Blocks */}
      <div className="py-8 overflow-x-auto">
        <div className="flex items-center justify-center space-x-2 min-w-[500px]">
          {items.map((val, idx) => {
            const isMid = mid === idx;
            const isLow = low === idx;
            const isHigh = high === idx;
            const isEliminated = idx < low || idx > high;
            const isMatched = isMid && status === 'found';

            return (
              <div key={idx} className="flex flex-col items-center">
                {/* Top pointers */}
                <div className="h-5 flex space-x-1 text-[10px] font-mono font-bold mb-1">
                  {isLow && <span className="text-blue-500">L</span>}
                  {isMid && <span className="text-amber-500">M</span>}
                  {isHigh && <span className="text-purple-500">H</span>}
                </div>

                <div
                  className={`w-11 h-14 sm:w-13 sm:h-16 rounded-xl flex items-center justify-center font-mono font-bold text-sm sm:text-base border-2 transition-all duration-300 ${
                    isMatched
                      ? 'bg-emerald-500 text-white border-emerald-400 scale-110 shadow-lg shadow-emerald-500/30'
                      : isMid
                      ? 'bg-amber-500 text-white border-amber-400 scale-105 shadow-md shadow-amber-500/20'
                      : isEliminated
                      ? 'bg-muted/20 text-muted-foreground/40 border-border/40 opacity-40'
                      : 'bg-card text-foreground border-border shadow-sm'
                  }`}
                >
                  {val}
                </div>

                <span className="mt-1.5 text-[10px] font-mono text-muted-foreground">
                  [{idx}]
                </span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Status Bar */}
      <div className="p-3 rounded-lg bg-muted/40 border border-border/50 text-xs font-mono text-center text-foreground flex items-center justify-center space-x-2">
        {status === 'found' && <CheckCircle2 className="h-4 w-4 text-emerald-500 inline" />}
        {status === 'not_found' && <XCircle className="h-4 w-4 text-destructive inline" />}
        <span>{message}</span>
      </div>
    </div>
  );
}
