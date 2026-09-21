'use client';

import * as React from 'react';
import { Play, RotateCcw, Layers, CheckCircle2, ArrowRight } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface UserDoc {
  _id: string;
  name: string;
  age: number;
  role: string;
  skills: string[];
}

const SAMPLE_DOCS: UserDoc[] = [
  { _id: '6501a1f0a1', name: 'Alex River', age: 28, role: 'Fullstack Dev', skills: ['Python', 'FastAPI', 'Next.js'] },
  { _id: '6501a1f0a2', name: 'Maya Lin', age: 24, role: 'Junior ML Engineer', skills: ['Python', 'PyTorch'] },
  { _id: '6501a1f0a3', name: 'Devon Patel', age: 34, role: 'Staff Architect', skills: ['Go', 'Kubernetes', 'MongoDB'] },
  { _id: '6501a1f0a4', name: 'Chloe Vance', age: 31, role: 'Backend Lead', skills: ['Python', 'FastAPI', 'PostgreSQL'] },
  { _id: '6501a1f0a5', name: 'Kenji Sato', age: 22, role: 'Frontend Intern', skills: ['React', 'TypeScript'] },
];

export function MongoPlayground() {
  const [filterStr, setFilterStr] = React.useState<string>(
    '{\n  "skills": "Python",\n  "age": { "$gte": 25 }\n}'
  );
  const [matchedDocs, setMatchedDocs] = React.useState<UserDoc[]>([]);
  const [activeTab, setActiveTab] = React.useState<'result' | 'all'>('result');

  const executeMongoQuery = () => {
    try {
      let filtered = [...SAMPLE_DOCS];
      // Simulated filter logic
      if (filterStr.includes('Python')) {
        filtered = filtered.filter((d) => d.skills.includes('Python'));
      }
      if (filterStr.includes('$gte') || filterStr.includes('$gt')) {
        filtered = filtered.filter((d) => d.age >= 25);
      }
      setMatchedDocs(filtered);
    } catch {
      setMatchedDocs(SAMPLE_DOCS);
    }
  };

  React.useEffect(() => {
    executeMongoQuery();
  }, []);

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center justify-between pb-4 border-b border-border/60">
        <div className="flex items-center space-x-2">
          <div className="p-2 rounded-lg bg-emerald-500/10 text-emerald-500">
            <Layers className="h-5 w-5" />
          </div>
          <div>
            <h4 className="text-base font-bold text-foreground">MongoDB Document Playground</h4>
            <p className="text-xs text-muted-foreground">Collection: users (JSON documents with flexible schema)</p>
          </div>
        </div>
        <Button size="sm" onClick={executeMongoQuery}>
          <Play className="h-3.5 w-3.5 mr-1" /> Run Query
        </Button>
      </div>

      {/* Visual Pipeline Flow */}
      <div className="flex items-center justify-center space-x-2 sm:space-x-4 my-4 p-3 rounded-xl bg-muted/30 text-xs">
        <div className="px-3 py-1.5 rounded-lg bg-card border border-border font-mono text-primary font-semibold">
          db.users.find()
        </div>
        <ArrowRight className="h-4 w-4 text-muted-foreground" />
        <div className="px-3 py-1.5 rounded-lg bg-card border border-border font-mono text-amber-500 font-semibold">
          Index Scan & Filter
        </div>
        <ArrowRight className="h-4 w-4 text-muted-foreground" />
        <div className="px-3 py-1.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-600 dark:text-emerald-400 font-mono font-semibold">
          {matchedDocs.length} Documents Matched
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
        {/* Query Input */}
        <div>
          <label className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-1 block">
            Filter Document (BSON)
          </label>
          <textarea
            value={filterStr}
            onChange={(e) => setFilterStr(e.target.value)}
            rows={6}
            className="w-full p-3 rounded-xl border border-border bg-slate-950 text-emerald-400 font-mono text-xs focus:outline-none focus:ring-2 focus:ring-emerald-500 leading-relaxed shadow-inner"
          />
        </div>

        {/* JSON Results Inspector */}
        <div>
          <div className="flex items-center justify-between mb-1">
            <label className="text-xs font-semibold text-muted-foreground uppercase tracking-wider">
              Matched JSON Documents ({matchedDocs.length})
            </label>
          </div>

          <div className="h-40 overflow-y-auto p-3 rounded-xl border border-border bg-slate-950 font-mono text-xs text-slate-200 shadow-inner">
            <pre className="text-xs leading-relaxed">
              {JSON.stringify(matchedDocs, null, 2)}
            </pre>
          </div>
        </div>
      </div>
    </div>
  );
}
