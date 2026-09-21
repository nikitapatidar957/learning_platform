'use client';

import * as React from 'react';
import { RotateCcw } from 'lucide-react';
import { Button } from '@/components/ui/Button';

export function ConfusionMatrixVisualizer() {
  const [tp, setTp] = React.useState<number>(85);
  const [fp, setFps] = React.useState<number>(15);
  const [fn, setFn] = React.useState<number>(10);
  const [tn, setTn] = React.useState<number>(140);

  const reset = () => {
    setTp(85);
    setFps(15);
    setFn(10);
    setTn(140);
  };

  const total = tp + fp + fn + tn;
  const accuracy = total > 0 ? (((tp + tn) / total) * 100).toFixed(1) : '0';
  const precision = tp + fp > 0 ? ((tp / (tp + fp)) * 100).toFixed(1) : '0';
  const recall = tp + fn > 0 ? ((tp / (tp + fn)) * 100).toFixed(1) : '0';
  const precNum = parseFloat(precision);
  const recNum = parseFloat(recall);
  const f1 = precNum + recNum > 0 ? ((2 * (precNum * recNum)) / (precNum + recNum)).toFixed(1) : '0';

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center justify-between pb-4 border-b border-border/60">
        <div>
          <h4 className="text-base font-bold text-foreground">Interactive Confusion Matrix</h4>
          <p className="text-xs text-muted-foreground">Inspect how TP, FP, FN, and TN shape Precision and Recall</p>
        </div>
        <Button size="sm" variant="outline" onClick={reset}>
          <RotateCcw className="h-3.5 w-3.5 mr-1" /> Reset
        </Button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 my-6 items-center">
        {/* Matrix Grid */}
        <div className="space-y-3">
          <div className="text-center text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-2">
            Predicted Class
          </div>

          <div className="flex">
            <div className="w-8 flex items-center justify-center">
              <span className="text-xs font-semibold text-muted-foreground -rotate-90 uppercase tracking-wider whitespace-nowrap">
                Actual
              </span>
            </div>

            <div className="flex-1 grid grid-cols-2 gap-3">
              {/* TP */}
              <div className="p-4 rounded-xl bg-emerald-500/10 border-2 border-emerald-500/40 text-center">
                <span className="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400 block">
                  True Positive (TP)
                </span>
                <input
                  type="number"
                  min="0"
                  max="500"
                  value={tp}
                  onChange={(e) => setTp(Math.max(0, parseInt(e.target.value, 10) || 0))}
                  className="w-20 text-center text-2xl font-bold font-mono bg-transparent outline-none mt-1"
                />
              </div>

              {/* FP */}
              <div className="p-4 rounded-xl bg-rose-500/10 border-2 border-rose-500/40 text-center">
                <span className="text-[11px] font-semibold text-rose-600 dark:text-rose-400 block">
                  False Positive (FP)
                </span>
                <input
                  type="number"
                  min="0"
                  max="500"
                  value={fp}
                  onChange={(e) => setFps(Math.max(0, parseInt(e.target.value, 10) || 0))}
                  className="w-20 text-center text-2xl font-bold font-mono bg-transparent outline-none mt-1"
                />
              </div>

              {/* FN */}
              <div className="p-4 rounded-xl bg-amber-500/10 border-2 border-amber-500/40 text-center">
                <span className="text-[11px] font-semibold text-amber-600 dark:text-amber-400 block">
                  False Negative (FN)
                </span>
                <input
                  type="number"
                  min="0"
                  max="500"
                  value={fn}
                  onChange={(e) => setFn(Math.max(0, parseInt(e.target.value, 10) || 0))}
                  className="w-20 text-center text-2xl font-bold font-mono bg-transparent outline-none mt-1"
                />
              </div>

              {/* TN */}
              <div className="p-4 rounded-xl bg-blue-500/10 border-2 border-blue-500/40 text-center">
                <span className="text-[11px] font-semibold text-blue-600 dark:text-blue-400 block">
                  True Negative (TN)
                </span>
                <input
                  type="number"
                  min="0"
                  max="500"
                  value={tn}
                  onChange={(e) => setTn(Math.max(0, parseInt(e.target.value, 10) || 0))}
                  className="w-20 text-center text-2xl font-bold font-mono bg-transparent outline-none mt-1"
                />
              </div>
            </div>
          </div>
        </div>

        {/* Calculated Metrics Cards */}
        <div className="grid grid-cols-2 gap-3">
          <div className="p-4 rounded-xl bg-muted/40 border border-border">
            <span className="text-xs text-muted-foreground font-medium">Precision</span>
            <div className="text-2xl font-mono font-bold text-foreground mt-1">{precision}%</div>
            <span className="text-[10px] text-muted-foreground font-mono">TP / (TP + FP)</span>
          </div>

          <div className="p-4 rounded-xl bg-muted/40 border border-border">
            <span className="text-xs text-muted-foreground font-medium">Recall (Sensitivity)</span>
            <div className="text-2xl font-mono font-bold text-foreground mt-1">{recall}%</div>
            <span className="text-[10px] text-muted-foreground font-mono">TP / (TP + FN)</span>
          </div>

          <div className="p-4 rounded-xl bg-primary/10 border border-primary/20">
            <span className="text-xs text-primary font-medium">F1-Score</span>
            <div className="text-2xl font-mono font-bold text-primary mt-1">{f1}%</div>
            <span className="text-[10px] text-muted-foreground font-mono">Harmonic Mean</span>
          </div>

          <div className="p-4 rounded-xl bg-muted/40 border border-border">
            <span className="text-xs text-muted-foreground font-medium">Overall Accuracy</span>
            <div className="text-2xl font-mono font-bold text-foreground mt-1">{accuracy}%</div>
            <span className="text-[10px] text-muted-foreground font-mono">(TP + TN) / Total</span>
          </div>
        </div>
      </div>
    </div>
  );
}
