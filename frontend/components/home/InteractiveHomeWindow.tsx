'use client';

import * as React from 'react';
import Link from 'next/link';
import {
  Terminal,
  Play,
  Pause,
  RotateCcw,
  Sparkles,
  Zap,
  Brain,
  Database,
  Bot,
  ArrowRight,
  CheckCircle2,
  Cpu,
  Layers,
  Activity,
  Code2,
  Sliders,
  ChevronRight,
  CornerDownLeft,
} from 'lucide-react';
import { Button } from '@/components/ui/Button';

type WindowTab = 'dsa' | 'ml' | 'data' | 'agents';

export function InteractiveHomeWindow() {
  const [activeTab, setActiveTab] = React.useState<WindowTab>('dsa');

  // ----------------------------------------------------
  // 1. DSA State & Animation Logic
  // ----------------------------------------------------
  const defaultDsaArray = [45, 18, 85, 32, 92, 12, 64, 27, 73, 50];
  const [dsaArray, setDsaArray] = React.useState<number[]>(defaultDsaArray);
  const [dsaComparing, setDsaComparing] = React.useState<[number, number] | null>(null);
  const [dsaSortedIndices, setDsaSortedIndices] = React.useState<number[]>([]);
  const [dsaIsRunning, setDsaIsRunning] = React.useState<boolean>(false);
  const [dsaSpeed, setDsaSpeed] = React.useState<number>(180);
  const [dsaComparisons, setDsaComparisons] = React.useState<number>(0);
  const [dsaSwaps, setDsaSwaps] = React.useState<number>(0);
  const dsaIntervalRef = React.useRef<NodeJS.Timeout | null>(null);

  const shuffleDsa = () => {
    if (dsaIntervalRef.current) clearInterval(dsaIntervalRef.current);
    setDsaIsRunning(false);
    setDsaComparing(null);
    setDsaSortedIndices([]);
    setDsaComparisons(0);
    setDsaSwaps(0);
    const shuffled = Array.from({ length: 10 }, () => Math.floor(Math.random() * 85) + 15);
    setDsaArray(shuffled);
  };

  const runBubbleSortStepByStep = () => {
    if (dsaIsRunning) {
      if (dsaIntervalRef.current) clearInterval(dsaIntervalRef.current);
      setDsaIsRunning(false);
      return;
    }

    setDsaIsRunning(true);
    let arr = [...dsaArray];
    let i = 0;
    let j = 0;
    let compCount = dsaComparisons;
    let swapCount = dsaSwaps;
    let sorted: number[] = [...dsaSortedIndices];

    dsaIntervalRef.current = setInterval(() => {
      if (i < arr.length - 1) {
        if (j < arr.length - i - 1) {
          compCount++;
          setDsaComparisons(compCount);
          setDsaComparing([j, j + 1]);

          if (arr[j] > arr[j + 1]) {
            swapCount++;
            setDsaSwaps(swapCount);
            const temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
            setDsaArray([...arr]);
          }
          j++;
        } else {
          sorted.push(arr.length - i - 1);
          setDsaSortedIndices([...sorted]);
          j = 0;
          i++;
        }
      } else {
        sorted = arr.map((_, idx) => idx);
        setDsaSortedIndices(sorted);
        setDsaComparing(null);
        setDsaIsRunning(false);
        if (dsaIntervalRef.current) clearInterval(dsaIntervalRef.current);
      }
    }, dsaSpeed);
  };

  React.useEffect(() => {
    return () => {
      if (dsaIntervalRef.current) clearInterval(dsaIntervalRef.current);
    };
  }, []);

  // ----------------------------------------------------
  // 2. ML & Neural Pipeline State
  // ----------------------------------------------------
  const [mlPoints, setMlPoints] = React.useState<Array<{ x: number; y: number; label: number }>>([
    { x: 25, y: 30, label: 0 },
    { x: 35, y: 45, label: 0 },
    { x: 20, y: 60, label: 0 },
    { x: 40, y: 25, label: 0 },
    { x: 70, y: 75, label: 1 },
    { x: 80, y: 65, label: 1 },
    { x: 65, y: 85, label: 1 },
    { x: 85, y: 80, label: 1 },
  ]);
  const [mlWeight, setMlWeight] = React.useState<number>(1.2);
  const [mlBias, setMlBias] = React.useState<number>(-15);
  const [mlEpoch, setMlEpoch] = React.useState<number>(42);
  const [mlLoss, setMlLoss] = React.useState<number>(0.042);
  const [mlIsTraining, setMlIsTraining] = React.useState<boolean>(false);

  const trainMlModel = () => {
    setMlIsTraining(true);
    let epochCount = mlEpoch;
    let curLoss = mlLoss;
    let curWeight = mlWeight;
    let curBias = mlBias;

    const interval = setInterval(() => {
      epochCount += 5;
      curLoss = Math.max(0.008, curLoss * 0.88);
      curWeight += (Math.random() - 0.48) * 0.1;
      curBias += (Math.random() - 0.5) * 1.2;

      setMlEpoch(epochCount);
      setMlLoss(Number(curLoss.toFixed(4)));
      setMlWeight(Number(curWeight.toFixed(2)));
      setMlBias(Number(curBias.toFixed(1)));

      if (epochCount >= 100 || curLoss <= 0.012) {
        clearInterval(interval);
        setMlIsTraining(false);
      }
    }, 120);
  };

  // ----------------------------------------------------
  // 3. SQL & Mongo Sandbox State
  // ----------------------------------------------------
  type DbFlavor = 'sql' | 'mongo';
  const [dbFlavor, setDbFlavor] = React.useState<DbFlavor>('sql');
  const [sqlQuery, setSqlQuery] = React.useState(
    "SELECT id, username, track, xp FROM learners WHERE track = 'AI' ORDER BY xp DESC LIMIT 3;"
  );
  const [mongoQuery, setMongoQuery] = React.useState(
    `db.learners.aggregate([\n  { $match: { track: "AI", xp: { $gte: 2400 } } },\n  { $sort: { xp: -1 } }\n])`
  );
  const [dbResults, setDbResults] = React.useState<any[]>([
    { id: '101', username: 'alex_dev', track: 'AI', xp: 4820, status: 'Master' },
    { id: '104', username: 'priya_ai', track: 'AI', xp: 3910, status: 'Advanced' },
    { id: '108', username: 'chen_dsa', track: 'AI', xp: 3450, status: 'Proficient' },
  ]);
  const [dbExecutionTime, setDbExecutionTime] = React.useState<number>(1.6);
  const [dbExecuting, setDbExecuting] = React.useState<boolean>(false);

  const executeDbQuery = () => {
    setDbExecuting(true);
    setTimeout(() => {
      setDbExecutionTime(Number((Math.random() * 1.5 + 0.8).toFixed(2)));
      setDbExecuting(false);
    }, 300);
  };

  // ----------------------------------------------------
  // 4. Agentic AI ReAct Swarm State
  // ----------------------------------------------------
  const agentTasks = [
    'Deploy self-correcting RAG pipeline with vector embeddings',
    'Synthesize deep learning loss landscape & hyperparameter tuning',
    'Auto-optimize MongoDB sharding and execution indexes',
  ];
  const [selectedAgentTask, setSelectedAgentTask] = React.useState(agentTasks[0]);
  const [agentStep, setAgentStep] = React.useState<number>(3);
  const [agentIsRunning, setAgentIsRunning] = React.useState<boolean>(false);

  const runAgentWorkflow = () => {
    setAgentIsRunning(true);
    setAgentStep(0);
    const interval = setInterval(() => {
      setAgentStep((prev) => {
        if (prev >= 3) {
          clearInterval(interval);
          setAgentIsRunning(false);
          return 3;
        }
        return prev + 1;
      });
    }, 600);
  };

  return (
    <div className="w-full max-w-4xl mx-auto my-4 animate-fade-in">
      {/* Outer Glow Card Container */}
      <div className="window-glow-border rounded-2xl bg-card/90 backdrop-blur-2xl border border-border shadow-xl shadow-primary/10 overflow-hidden transition-all duration-300">
        {/* Window Top Titlebar */}
        <div className="px-3.5 py-2.5 border-b border-border/80 bg-muted/40 flex flex-wrap items-center justify-between gap-2.5">
          {/* Traffic light dots + Clean Status */}
          <div className="flex items-center space-x-2.5">
            <div className="flex items-center space-x-1.5">
              <span className="h-2.5 w-2.5 rounded-full bg-rose-500/90 shadow-xs inline-block" />
              <span className="h-2.5 w-2.5 rounded-full bg-amber-500/90 shadow-xs inline-block" />
              <span className="h-2.5 w-2.5 rounded-full bg-emerald-500/90 shadow-xs inline-block" />
            </div>
            <div className="h-3.5 w-[1px] bg-border mx-1" />
            <div className="flex items-center space-x-1.5 text-xs font-mono text-muted-foreground">
              <Terminal className="h-3.5 w-3.5 text-primary" />
              <span className="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 font-medium">
                <span className="h-1.5 w-1.5 rounded-full bg-emerald-500 mr-1.5 animate-pulse" />
                Live Playground
              </span>
            </div>
          </div>

          {/* Interactive Mode Tabs */}
          <div className="flex items-center bg-background/80 p-0.5 rounded-lg border border-border/80 text-xs font-medium space-x-0.5">
            <button
              onClick={() => setActiveTab('dsa')}
              className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md text-xs transition-all ${
                activeTab === 'dsa'
                  ? 'bg-primary text-primary-foreground shadow-sm shadow-primary/25 font-bold'
                  : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'
              }`}
            >
              <Zap className="h-3 w-3" />
              <span>DSA</span>
            </button>

            <button
              onClick={() => setActiveTab('ml')}
              className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md text-xs transition-all ${
                activeTab === 'ml'
                  ? 'bg-primary text-primary-foreground shadow-sm shadow-primary/25 font-bold'
                  : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'
              }`}
            >
              <Brain className="h-3 w-3" />
              <span>ML & Neural</span>
            </button>

            <button
              onClick={() => setActiveTab('data')}
              className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md text-xs transition-all ${
                activeTab === 'data'
                  ? 'bg-primary text-primary-foreground shadow-sm shadow-primary/25 font-bold'
                  : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'
              }`}
            >
              <Database className="h-3 w-3" />
              <span>SQL & Mongo</span>
            </button>

            <button
              onClick={() => setActiveTab('agents')}
              className={`flex items-center space-x-1.5 px-2.5 py-1 rounded-md text-xs transition-all ${
                activeTab === 'agents'
                  ? 'bg-primary text-primary-foreground shadow-sm shadow-primary/25 font-bold'
                  : 'text-muted-foreground hover:text-foreground hover:bg-muted/50'
              }`}
            >
              <Bot className="h-3 w-3" />
              <span>Agentic AI</span>
            </button>
          </div>
        </div>

        {/* Dynamic Interactive Studio Canvas */}
        <div className="p-4 sm:p-5 min-h-[300px] flex flex-col justify-between">
          {/* TAB 1: DSA SORTING ALGORITHM */}
          {activeTab === 'dsa' && (
            <div className="space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <h3 className="text-sm sm:text-base font-bold text-foreground flex items-center gap-2">
                    <Zap className="h-4 w-4 text-amber-500" />
                    Bubble Sort & Array Memory Visualizer
                  </h3>
                  <p className="text-[11px] text-muted-foreground mt-0.5">
                    Live algorithmic array sorting with real-time comparisons and in-place memory swaps.
                  </p>
                </div>

                {/* Metrics Badges */}
                <div className="flex items-center space-x-2 text-xs font-mono">
                  <div className="px-2.5 py-1 rounded-lg border border-border bg-muted/40 text-[11px]">
                    <span className="text-muted-foreground">Comparisons: </span>
                    <span className="font-bold text-primary">{dsaComparisons}</span>
                  </div>
                  <div className="px-2.5 py-1 rounded-lg border border-border bg-muted/40 text-[11px]">
                    <span className="text-muted-foreground">Swaps: </span>
                    <span className="font-bold text-emerald-500">{dsaSwaps}</span>
                  </div>
                </div>
              </div>

              {/* Array Bars Visualization Canvas - Compact height */}
              <div className="h-32 w-full rounded-xl border border-border/80 bg-background/50 p-3 flex items-end justify-between gap-1.5 sm:gap-2">
                {dsaArray.map((val, idx) => {
                  const isComparing = dsaComparing && (dsaComparing[0] === idx || dsaComparing[1] === idx);
                  const isSorted = dsaSortedIndices.includes(idx);

                  return (
                    <div
                      key={idx}
                      className="flex-1 flex flex-col items-center justify-end h-full group relative"
                    >
                      <span className="text-[9px] font-mono text-muted-foreground mb-1">
                        {val}
                      </span>
                      <div
                        style={{ height: `${val}%` }}
                        className={`w-full rounded-t-md transition-all duration-150 shadow-sm ${
                          isComparing
                            ? 'bg-amber-500 scale-105 shadow-amber-500/50'
                            : isSorted
                            ? 'bg-emerald-500 shadow-emerald-500/30'
                            : 'bg-gradient-to-t from-primary/70 to-indigo-500/90'
                        }`}
                      />
                      <span className="text-[8px] font-mono text-muted-foreground mt-1 opacity-60">
                        [{idx}]
                      </span>
                    </div>
                  );
                })}
              </div>

              {/* DSA Interactive Controls */}
              <div className="flex flex-wrap items-center justify-between gap-2.5 pt-1">
                <div className="flex items-center space-x-2">
                  <Button
                    size="sm"
                    onClick={runBubbleSortStepByStep}
                    className="shadow-sm shadow-primary/20 text-xs py-1.5 px-3"
                  >
                    {dsaIsRunning ? (
                      <>
                        <Pause className="h-3.5 w-3.5 mr-1" /> Pause
                      </>
                    ) : (
                      <>
                        <Play className="h-3.5 w-3.5 mr-1" /> Run Sort
                      </>
                    )}
                  </Button>
                  <Button size="sm" variant="outline" onClick={shuffleDsa} className="text-xs py-1.5 px-3">
                    <RotateCcw className="h-3 w-3 mr-1" /> Shuffle
                  </Button>
                </div>

                <div className="flex items-center space-x-1.5 text-xs text-muted-foreground">
                  <span className="text-[11px]">Speed:</span>
                  <button
                    onClick={() => setDsaSpeed(280)}
                    className={`px-2 py-0.5 rounded border text-[10px] ${
                      dsaSpeed === 280 ? 'bg-primary text-primary-foreground' : 'bg-muted'
                    }`}
                  >
                    0.5x
                  </button>
                  <button
                    onClick={() => setDsaSpeed(180)}
                    className={`px-2 py-0.5 rounded border text-[10px] ${
                      dsaSpeed === 180 ? 'bg-primary text-primary-foreground' : 'bg-muted'
                    }`}
                  >
                    1.0x
                  </button>
                  <button
                    onClick={() => setDsaSpeed(80)}
                    className={`px-2 py-0.5 rounded border text-[10px] ${
                      dsaSpeed === 80 ? 'bg-primary text-primary-foreground' : 'bg-muted'
                    }`}
                  >
                    2.0x
                  </button>
                </div>

                <Link href="/courses/dsa">
                  <Button size="sm" variant="ghost" className="text-primary font-semibold text-xs py-1 px-2">
                    DSA Curriculum →
                  </Button>
                </Link>
              </div>
            </div>
          )}

          {/* TAB 2: ML & NEURAL DECISION BOUNDARY */}
          {activeTab === 'ml' && (
            <div className="space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <h3 className="text-sm sm:text-base font-bold text-foreground flex items-center gap-2">
                    <Brain className="h-4 w-4 text-indigo-500" />
                    Neural Classifier & Decision Boundary
                  </h3>
                  <p className="text-[11px] text-muted-foreground mt-0.5">
                    Simulate real-time gradient descent convergence, loss reduction, and hyperparameter tuning.
                  </p>
                </div>

                {/* Training Metrics */}
                <div className="flex items-center space-x-2 text-xs font-mono">
                  <div className="px-2.5 py-1 rounded-lg border border-border bg-muted/40 text-[11px]">
                    <span className="text-muted-foreground">Epoch: </span>
                    <span className="font-bold text-primary">{mlEpoch}</span>
                  </div>
                  <div className="px-2.5 py-1 rounded-lg border border-border bg-muted/40 text-[11px]">
                    <span className="text-muted-foreground">MSE Loss: </span>
                    <span className="font-bold text-emerald-500">{mlLoss}</span>
                  </div>
                </div>
              </div>

              {/* 2D Coordinate Plane Visualization - Compact height */}
              <div className="relative h-32 w-full rounded-xl border border-border/80 bg-background/50 overflow-hidden p-3">
                {/* Decision Line */}
                <div
                  style={{
                    transform: `rotate(${-mlWeight * 18}deg) translateY(${mlBias * 0.7}px)`,
                  }}
                  className="absolute inset-x-0 top-1/2 h-0.5 bg-gradient-to-r from-transparent via-primary to-transparent transition-all duration-200 shadow-md shadow-primary"
                />

                {/* Scatter Data Points */}
                {mlPoints.map((pt, idx) => (
                  <div
                    key={idx}
                    style={{ left: `${pt.x}%`, top: `${pt.y}%` }}
                    className={`absolute -translate-x-1/2 -translate-y-1/2 h-3.5 w-3.5 rounded-full border-2 transition-transform duration-200 ${
                      pt.label === 0
                        ? 'bg-rose-500/80 border-rose-400 shadow-sm shadow-rose-500/40'
                        : 'bg-sky-500/80 border-sky-400 shadow-sm shadow-sky-500/40'
                    }`}
                  />
                ))}

                <div className="absolute bottom-1.5 left-2.5 text-[9px] font-mono text-muted-foreground">
                  Class 0: Red • Class 1: Cyan • Hyperplane
                </div>
              </div>

              {/* ML Interactive Controls */}
              <div className="flex flex-wrap items-center justify-between gap-2.5 pt-1">
                <Button
                  size="sm"
                  onClick={trainMlModel}
                  disabled={mlIsTraining}
                  className="shadow-sm shadow-primary/20 text-xs py-1.5 px-3"
                >
                  <Sparkles className="h-3.5 w-3.5 mr-1" />
                  {mlIsTraining ? 'Optimizing...' : 'Train Epoch'}
                </Button>

                <div className="flex items-center space-x-3 text-xs font-mono text-muted-foreground text-[11px]">
                  <span>Weight: <strong className="text-foreground">{mlWeight}</strong></span>
                  <span>Bias: <strong className="text-foreground">{mlBias}</strong></span>
                </div>

                <Link href="/courses/machine-learning">
                  <Button size="sm" variant="ghost" className="text-primary font-semibold text-xs py-1 px-2">
                    Machine Learning Track →
                  </Button>
                </Link>
              </div>
            </div>
          )}

          {/* TAB 3: SQL & MONGODB QUERY SANDBOX */}
          {activeTab === 'data' && (
            <div className="space-y-3.5">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <h3 className="text-sm sm:text-base font-bold text-foreground flex items-center gap-2">
                    <Database className="h-4 w-4 text-emerald-500" />
                    SQL & MongoDB Query Console
                  </h3>
                  <p className="text-[11px] text-muted-foreground mt-0.5">
                    Toggle relational SQL and document MongoDB aggregation pipelines with instant execution.
                  </p>
                </div>

                {/* Sub-toggle: SQL vs Mongo */}
                <div className="flex items-center bg-muted p-0.5 rounded-lg text-xs font-mono">
                  <button
                    onClick={() => setDbFlavor('sql')}
                    className={`px-2.5 py-1 rounded-md text-[11px] transition-colors ${
                      dbFlavor === 'sql' ? 'bg-primary text-primary-foreground font-bold' : 'text-muted-foreground'
                    }`}
                  >
                    PostgreSQL
                  </button>
                  <button
                    onClick={() => setDbFlavor('mongo')}
                    className={`px-2.5 py-1 rounded-md text-[11px] transition-colors ${
                      dbFlavor === 'mongo' ? 'bg-primary text-primary-foreground font-bold' : 'text-muted-foreground'
                    }`}
                  >
                    MongoDB MQL
                  </button>
                </div>
              </div>

              {/* Code Input Box - Compact */}
              <div className="rounded-xl border border-border/80 bg-background/80 p-2.5 font-mono text-xs text-foreground/90 relative">
                <span className="text-[9px] text-muted-foreground uppercase absolute top-1.5 right-2.5">
                  {dbFlavor === 'sql' ? 'SQL' : 'JSON'}
                </span>
                <pre className="overflow-x-auto text-primary/90 font-medium text-[11px]">
                  {dbFlavor === 'sql' ? sqlQuery : mongoQuery}
                </pre>
              </div>

              {/* Interactive Result Table - Compact */}
              <div className="rounded-xl border border-border/80 bg-background/40 overflow-hidden text-xs">
                <div className="px-3 py-1.5 bg-muted/40 border-b border-border/60 flex items-center justify-between font-mono text-[10px] text-muted-foreground">
                  <span>RESULTS (3 ROWS)</span>
                  <span className="text-emerald-500 font-semibold">Execution: {dbExecutionTime}ms</span>
                </div>
                <table className="w-full text-left font-mono text-[11px]">
                  <thead className="bg-muted/20 text-muted-foreground border-b border-border/40 text-[10px]">
                    <tr>
                      <th className="p-2">ID</th>
                      <th className="p-2">USERNAME</th>
                      <th className="p-2">TRACK</th>
                      <th className="p-2">XP</th>
                      <th className="p-2">STATUS</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-border/30">
                    {dbResults.map((r) => (
                      <tr key={r.id} className="hover:bg-primary/5 transition-colors">
                        <td className="p-2 text-muted-foreground">#{r.id}</td>
                        <td className="p-2 font-bold text-foreground">{r.username}</td>
                        <td className="p-2 text-primary">{r.track}</td>
                        <td className="p-2 font-semibold text-emerald-500">{r.xp}</td>
                        <td className="p-2 text-muted-foreground">{r.status}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              {/* Query Action bar */}
              <div className="flex flex-wrap items-center justify-between gap-2.5 pt-0.5">
                <Button
                  size="sm"
                  onClick={executeDbQuery}
                  disabled={dbExecuting}
                  className="shadow-sm shadow-primary/20 text-xs py-1.5 px-3"
                >
                  <Play className="h-3.5 w-3.5 mr-1" />
                  {dbExecuting ? 'Executing...' : 'Run Query ⚡'}
                </Button>

                <div className="flex items-center space-x-2">
                  <Link href="/courses/sql">
                    <Button size="sm" variant="ghost" className="text-xs py-1 px-2">
                      SQL Course →
                    </Button>
                  </Link>
                  <Link href="/courses/mongodb">
                    <Button size="sm" variant="ghost" className="text-xs py-1 px-2">
                      MongoDB Track →
                    </Button>
                  </Link>
                </div>
              </div>
            </div>
          )}

          {/* TAB 4: AGENTIC AI RE-ACT SWARM */}
          {activeTab === 'agents' && (
            <div className="space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <h3 className="text-sm sm:text-base font-bold text-foreground flex items-center gap-2">
                    <Bot className="h-4 w-4 text-purple-500" />
                    Autonomous ReAct Agent Loop Simulation
                  </h3>
                  <p className="text-[11px] text-muted-foreground mt-0.5">
                    Observe dynamic planning, tool selection, and autonomous task execution.
                  </p>
                </div>

                <span className="text-[10px] font-mono text-purple-400 bg-purple-500/10 px-2.5 py-0.5 rounded-full border border-purple-500/20 font-semibold">
                  Multi-Agent Swarm
                </span>
              </div>

              {/* Step Flow Nodes - Compact */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                {[
                  { title: '1. User Goal', sub: 'Task query', icon: Sparkles },
                  { title: '2. Planner Agent', sub: 'Subtasks', icon: Brain },
                  { title: '3. Tool Call', sub: 'VectorDB & JIT', icon: Cpu },
                  { title: '4. Synthesis', sub: 'Verified output', icon: CheckCircle2 },
                ].map((st, idx) => {
                  const isActive = agentStep >= idx;
                  const Icon = st.icon;
                  return (
                    <div
                      key={idx}
                      className={`p-2.5 rounded-xl border transition-all duration-300 ${
                        isActive
                          ? 'border-purple-500/60 bg-purple-500/10 shadow-xs'
                          : 'border-border/60 bg-muted/20 opacity-50'
                      }`}
                    >
                      <div className="flex items-center space-x-1.5 text-xs font-bold text-foreground">
                        <Icon className={`h-3.5 w-3.5 ${isActive ? 'text-purple-400' : 'text-muted-foreground'}`} />
                        <span>{st.title}</span>
                      </div>
                      <p className="text-[10px] text-muted-foreground mt-0.5">{st.sub}</p>
                    </div>
                  );
                })}
              </div>

              {/* Real-time Agent Log Stream - Compact */}
              <div className="rounded-xl border border-border/80 bg-background/80 p-2.5 font-mono text-xs space-y-1">
                <div className="text-muted-foreground text-[10px] flex items-center justify-between">
                  <span>AGENT THOUGHT STREAM</span>
                  <span className="text-purple-400">STATE: {agentIsRunning ? 'EXECUTING' : 'COMPLETED'}</span>
                </div>
                <div className="text-foreground/90 space-y-1">
                  <p className="text-purple-400">
                    &gt; Thought: User requested "{selectedAgentTask}". Initiating multi-step decomposition...
                  </p>
                  {agentStep >= 1 && (
                    <p className="text-sky-400">
                      &gt; Action: Executed tool `retrieve_embeddings(query="vector cosine", top_k=5)`.
                    </p>
                  )}
                  {agentStep >= 2 && (
                    <p className="text-amber-400">
                      &gt; Observation: Received semantic context nodes. Evaluating confidence score: 0.964.
                    </p>
                  )}
                  {agentStep >= 3 && (
                    <p className="text-emerald-400 font-semibold">
                      &gt; Final Answer: Pipeline initialized with FAISS index, LangGraph agent loop, and evaluation metric.
                    </p>
                  )}
                </div>
              </div>

              {/* Agent Controls */}
              <div className="flex flex-wrap items-center justify-between gap-3 pt-1">
                <Button
                  size="sm"
                  onClick={runAgentWorkflow}
                  disabled={agentIsRunning}
                  className="shadow-md shadow-purple-500/20 bg-purple-600 hover:bg-purple-700 text-white"
                >
                  <Bot className="h-4 w-4 mr-1.5" />
                  {agentIsRunning ? 'Simulating Swarm...' : 'Trigger Autonomous Loop'}
                </Button>

                <Link href="/courses/agentic-ai">
                  <Button size="sm" variant="ghost" className="text-purple-400 font-semibold text-xs">
                    Learn Agentic AI Curriculum →
                  </Button>
                </Link>
              </div>
            </div>
          )}
        </div>

        {/* Window Bottom Status Bar */}
        <div className="px-5 py-3 border-t border-border/70 bg-muted/30 flex flex-wrap items-center justify-between text-xs text-muted-foreground gap-3">
          <div className="flex items-center space-x-4 font-mono text-[11px]">
            <span className="flex items-center">
              <Cpu className="h-3.5 w-3.5 text-primary mr-1" />
              Engine: WebAssembly JIT
            </span>
            <span className="hidden sm:inline-flex items-center">
              <Activity className="h-3.5 w-3.5 text-emerald-500 mr-1" />
              Frame Latency: 1.4ms
            </span>
            <span className="hidden md:inline">Memory: 16.4 MB</span>
          </div>

          <div className="flex items-center space-x-2 text-[11px]">
            <span className="text-foreground font-semibold">Free & Open Access</span>
            <span>•</span>
            <Link href="/courses" className="text-primary hover:underline font-semibold flex items-center">
              Explore All 8 Courses <ArrowRight className="h-3 w-3 ml-0.5" />
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
