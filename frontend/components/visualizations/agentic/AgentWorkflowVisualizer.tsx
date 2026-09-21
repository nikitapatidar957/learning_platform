'use client';

import * as React from 'react';
import { Bot, ArrowRight, RotateCcw, CheckCircle2, Play, Wrench } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface AgentStep {
  id: number;
  stage: string;
  thought: string;
  action: string;
  observation: string;
}

const AGENT_TRACE: AgentStep[] = [
  {
    id: 1,
    stage: 'Goal Formulation',
    thought: 'The user asks: "Find the 30-day average price of AAPL stock and determine volatility."',
    action: 'Plan breakdown: 1. Fetch 30-day historical prices, 2. Compute mean, 3. Compute standard deviation.',
    observation: 'Sub-goals created.',
  },
  {
    id: 2,
    stage: 'Tool Selection & Invocation',
    thought: 'I need quantitative historical market data. Available tools: [web_search, stock_api, calculator].',
    action: 'Calling tool: stock_api.get_historical_prices(symbol="AAPL", days=30)',
    observation: 'Tool output: [182.5, 184.2, 181.9, ..., 189.4] (30 price points returned)',
  },
  {
    id: 3,
    stage: 'Reasoning & Calculation',
    thought: 'With 30 data points, calculate mean and standard deviation for volatility.',
    action: 'Calling tool: python_repl("import numpy as np; mean=np.mean(prices); std=np.std(prices); (mean, std)")',
    observation: 'Tool output: Mean = $185.34, Standard Deviation = $3.12 (low-moderate volatility)',
  },
  {
    id: 4,
    stage: 'Final Synthesis',
    thought: 'All sub-goals satisfied. Formulate clear, concise answer with sources.',
    action: 'Generate structured markdown response to user.',
    observation: 'Done. Task completed in 4 execution turns.',
  },
];

export function AgentWorkflowVisualizer() {
  const [currentStepIdx, setCurrentStepIdx] = React.useState<number>(0);

  const nextStep = () => {
    setCurrentStepIdx((prev) => Math.min(prev + 1, AGENT_TRACE.length - 1));
  };

  const reset = () => {
    setCurrentStepIdx(0);
  };

  const current = AGENT_TRACE[currentStepIdx];

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center justify-between pb-4 border-b border-border/60">
        <div className="flex items-center space-x-2">
          <div className="p-2 rounded-lg bg-rose-500/10 text-rose-500">
            <Bot className="h-5 w-5" />
          </div>
          <div>
            <h4 className="text-base font-bold text-foreground">Autonomous Agent Execution Loop</h4>
            <p className="text-xs text-muted-foreground">ReAct Pattern: Thought → Action → Tool Execution → Observation</p>
          </div>
        </div>

        <div className="flex items-center space-x-2">
          <Button size="sm" variant="outline" onClick={reset}>
            <RotateCcw className="h-3.5 w-3.5 mr-1" /> Reset
          </Button>
          <Button size="sm" onClick={nextStep} disabled={currentStepIdx >= AGENT_TRACE.length - 1}>
            Next Step <ArrowRight className="h-3.5 w-3.5 ml-1" />
          </Button>
        </div>
      </div>

      {/* Progress Timeline */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 my-6">
        {AGENT_TRACE.map((step, idx) => {
          const isCurrent = idx === currentStepIdx;
          const isPast = idx < currentStepIdx;

          return (
            <button
              key={step.id}
              onClick={() => setCurrentStepIdx(idx)}
              className={`p-3 rounded-xl border text-left transition-all ${
                isCurrent
                  ? 'bg-rose-500/10 border-rose-500/60 shadow-sm ring-1 ring-rose-500'
                  : isPast
                  ? 'bg-muted/30 border-emerald-500/40 text-muted-foreground'
                  : 'bg-muted/20 border-border opacity-50'
              }`}
            >
              <div className="flex items-center justify-between text-[10px] font-mono mb-1">
                <span>Step {step.id}</span>
                {isPast && <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500" />}
              </div>
              <span className={`text-xs font-bold block truncate ${isCurrent ? 'text-rose-500' : 'text-foreground'}`}>
                {step.stage}
              </span>
            </button>
          );
        })}
      </div>

      {/* Interactive Turn Box */}
      <div className="p-5 rounded-xl border border-border bg-slate-950 text-slate-100 font-mono text-xs space-y-4 shadow-inner">
        <div>
          <span className="text-rose-400 font-bold uppercase tracking-wider text-[11px] block">
            💭 Agent Thought:
          </span>
          <p className="text-slate-300 mt-1 font-sans text-xs leading-relaxed">
            {current.thought}
          </p>
        </div>

        <div className="p-3 rounded-lg bg-slate-900 border border-slate-800">
          <span className="text-amber-400 font-bold uppercase tracking-wider text-[10px] flex items-center mb-1">
            <Wrench className="h-3 w-3 mr-1" /> Action / Tool Call:
          </span>
          <code className="text-amber-200 text-xs block overflow-x-auto">
            {current.action}
          </code>
        </div>

        <div>
          <span className="text-emerald-400 font-bold uppercase tracking-wider text-[10px] block">
            👁️ Environment Observation:
          </span>
          <p className="text-emerald-300 mt-1 text-xs">
            {current.observation}
          </p>
        </div>
      </div>
    </div>
  );
}
