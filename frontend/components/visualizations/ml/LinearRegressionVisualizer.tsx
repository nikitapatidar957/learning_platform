'use client';

import * as React from 'react';
import { RotateCcw, Sparkles } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface Point {
  x: number;
  y: number;
}

export function LinearRegressionVisualizer() {
  const [points] = React.useState<Point[]>([
    { x: 1, y: 2.2 },
    { x: 2, y: 3.8 },
    { x: 3, y: 5.5 },
    { x: 4, y: 7.2 },
    { x: 5, y: 9.1 },
    { x: 6, y: 11.4 },
    { x: 7, y: 12.8 },
  ]);

  const [slope, setSlope] = React.useState<number>(1.8);
  const [intercept, setIntercept] = React.useState<number>(0.5);

  const reset = () => {
    setSlope(1.8);
    setIntercept(0.5);
  };

  // Calculate MSE: 1/N * sum((y_actual - y_pred)^2)
  const mse = React.useMemo(() => {
    const sumSqError = points.reduce((acc, pt) => {
      const yPred = slope * pt.x + intercept;
      return acc + Math.pow(pt.y - yPred, 2);
    }, 0);
    return (sumSqError / points.length).toFixed(3);
  }, [points, slope, intercept]);

  // SVG coordinate bounds
  const svgWidth = 440;
  const svgHeight = 240;
  const padding = 35;
  const scaleX = (svgWidth - padding * 2) / 8;
  const scaleY = (svgHeight - padding * 2) / 16;

  const toSvgX = (x: number) => padding + x * scaleX;
  const toSvgY = (y: number) => svgHeight - padding - y * scaleY;

  const lineX1 = 0;
  const lineY1 = slope * lineX1 + intercept;
  const lineX2 = 8;
  const lineY2 = slope * lineX2 + intercept;

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center justify-between pb-4 border-b border-border/60">
        <div>
          <h4 className="text-base font-bold text-foreground">Linear Regression: Best-Fit Line</h4>
          <p className="text-xs text-muted-foreground">Adjust slope and intercept to minimize Mean Squared Error (MSE)</p>
        </div>
        <Button size="sm" variant="outline" onClick={reset}>
          <RotateCcw className="h-3.5 w-3.5 mr-1" /> Reset
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 my-4 items-center">
        {/* SVG Plot */}
        <div className="md:col-span-2 bg-muted/20 border border-border rounded-xl p-3 flex justify-center">
          <svg width={svgWidth} height={svgHeight} className="overflow-visible select-none max-w-full">
            {/* Grid & Axes */}
            <line
              x1={padding}
              y1={svgHeight - padding}
              x2={svgWidth - padding}
              y2={svgHeight - padding}
              stroke="currentColor"
              strokeOpacity="0.3"
              strokeWidth="2"
            />
            <line
              x1={padding}
              y1={padding}
              x2={padding}
              y2={svgHeight - padding}
              stroke="currentColor"
              strokeOpacity="0.3"
              strokeWidth="2"
            />

            {/* Regression Line */}
            <line
              x1={toSvgX(lineX1)}
              y1={toSvgY(lineY1)}
              x2={toSvgX(lineX2)}
              y2={toSvgY(lineY2)}
              stroke="hsl(var(--primary))"
              strokeWidth="3"
            />

            {/* Residual error vertical lines */}
            {points.map((pt, i) => {
              const yPred = slope * pt.x + intercept;
              return (
                <line
                  key={`err-${i}`}
                  x1={toSvgX(pt.x)}
                  y1={toSvgY(pt.y)}
                  x2={toSvgX(pt.x)}
                  y2={toSvgY(yPred)}
                  stroke="rgba(239, 68, 68, 0.7)"
                  strokeDasharray="3 3"
                  strokeWidth="1.5"
                />
              );
            })}

            {/* Data Points */}
            {points.map((pt, i) => (
              <circle
                key={`pt-${i}`}
                cx={toSvgX(pt.x)}
                cy={toSvgY(pt.y)}
                r="6"
                fill="hsl(var(--primary))"
                stroke="white"
                strokeWidth="2"
              />
            ))}
          </svg>
        </div>

        {/* Metrics & Controls */}
        <div className="space-y-4">
          <div className="p-4 rounded-xl bg-primary/10 border border-primary/20 space-y-1">
            <span className="text-xs text-muted-foreground font-semibold">Mean Squared Error (MSE)</span>
            <div className="text-2xl font-mono font-bold text-primary">{mse}</div>
            <p className="text-[11px] text-muted-foreground">Lower is better. Optimal fit ~ 0.05</p>
          </div>

          <div className="space-y-2">
            <div className="flex justify-between text-xs font-semibold">
              <span>Slope (m): {slope.toFixed(2)}</span>
            </div>
            <input
              type="range"
              min="0.5"
              max="3.0"
              step="0.05"
              value={slope}
              onChange={(e) => setSlope(parseFloat(e.target.value))}
              className="w-full accent-primary"
            />
          </div>

          <div className="space-y-2">
            <div className="flex justify-between text-xs font-semibold">
              <span>Intercept (b): {intercept.toFixed(2)}</span>
            </div>
            <input
              type="range"
              min="-2.0"
              max="4.0"
              step="0.1"
              value={intercept}
              onChange={(e) => setIntercept(parseFloat(e.target.value))}
              className="w-full accent-primary"
            />
          </div>

          <div className="p-2.5 rounded-lg bg-muted text-[11px] font-mono text-muted-foreground">
            y = {slope.toFixed(2)}x + {intercept.toFixed(2)}
          </div>
        </div>
      </div>
    </div>
  );
}
