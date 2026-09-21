'use client';

import * as React from 'react';
import { Play, RotateCcw, Database, Table } from 'lucide-react';
import { Button } from '@/components/ui/Button';

interface SQLEditorProps {
  initialQuery?: string;
}

interface EmployeeRecord {
  id: number;
  name: string;
  department: string;
  salary: number;
  experience_years: number;
}

const SAMPLE_EMPLOYEES: EmployeeRecord[] = [
  { id: 101, name: 'Alice Chen', department: 'Engineering', salary: 95000, experience_years: 5 },
  { id: 102, name: 'Bob Smith', department: 'Product', salary: 88000, experience_years: 4 },
  { id: 103, name: 'Carol Danvers', department: 'Engineering', salary: 115000, experience_years: 8 },
  { id: 104, name: 'David Lee', department: 'Marketing', salary: 62000, experience_years: 2 },
  { id: 105, name: 'Elena Rostova', department: 'Engineering', salary: 105000, experience_years: 6 },
  { id: 106, name: 'Frank Wright', department: 'Finance', salary: 72000, experience_years: 3 },
];

export function SQLEditor({
  initialQuery = 'SELECT name, department, salary, experience_years\nFROM employees\nWHERE salary > 70000\nORDER BY salary DESC;',
}: SQLEditorProps) {
  const [query, setQuery] = React.useState(initialQuery);
  const [results, setResults] = React.useState<any[]>([]);
  const [execTime, setExecTime] = React.useState<number | null>(null);
  const [error, setError] = React.useState<string | null>(null);

  const runQuery = () => {
    setError(null);
    const start = performance.now();

    try {
      const q = query.toLowerCase();
      let filtered = [...SAMPLE_EMPLOYEES];

      // Parse WHERE clause mock
      if (q.includes('where')) {
        if (q.includes('salary > 70000') || q.includes('salary > 65000')) {
          filtered = filtered.filter((e) => e.salary > 70000);
        } else if (q.includes("department = 'engineering'") || q.includes('engineering')) {
          filtered = filtered.filter((e) => e.department.toLowerCase() === 'engineering');
        } else if (q.includes('experience_years >= 5') || q.includes('experience > 4')) {
          filtered = filtered.filter((e) => e.experience_years >= 5);
        }
      }

      // Parse ORDER BY mock
      if (q.includes('order by')) {
        if (q.includes('salary desc')) {
          filtered.sort((a, b) => b.salary - a.salary);
        } else if (q.includes('salary asc') || q.includes('salary')) {
          filtered.sort((a, b) => a.salary - b.salary);
        }
      }

      const elapsed = Math.round((performance.now() - start) * 10) / 10;
      setExecTime(elapsed);
      setResults(filtered);
    } catch {
      setError('Query parsing error: Please verify SQL syntax.');
    }
  };

  React.useEffect(() => {
    runQuery();
  }, []);

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center justify-between pb-4 border-b border-border/60">
        <div className="flex items-center space-x-2">
          <div className="p-2 rounded-lg bg-blue-500/10 text-blue-500">
            <Database className="h-5 w-5" />
          </div>
          <div>
            <h4 className="text-base font-bold text-foreground">Interactive SQL Query Engine</h4>
            <p className="text-xs text-muted-foreground">Sample table: employees (id, name, department, salary, experience_years)</p>
          </div>
        </div>
        <Button size="sm" onClick={runQuery}>
          <Play className="h-3.5 w-3.5 mr-1" /> Run Query
        </Button>
      </div>

      {/* Editor area */}
      <div className="mt-4">
        <label className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-1 block">
          SQL Query Editor
        </label>
        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          rows={4}
          className="w-full p-3.5 rounded-xl border border-border bg-slate-950 text-slate-100 font-mono text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-primary leading-relaxed shadow-inner"
        />
      </div>

      {/* Quick query presets */}
      <div className="flex flex-wrap gap-2 mt-2">
        <button
          onClick={() => {
            setQuery("SELECT * FROM employees WHERE department = 'Engineering';");
          }}
          className="text-[11px] px-2.5 py-1 rounded-md bg-muted text-muted-foreground hover:text-foreground transition-colors"
        >
          Preset: Engineering Only
        </button>
        <button
          onClick={() => {
            setQuery('SELECT name, salary FROM employees WHERE salary > 90000 ORDER BY salary DESC;');
          }}
          className="text-[11px] px-2.5 py-1 rounded-md bg-muted text-muted-foreground hover:text-foreground transition-colors"
        >
          Preset: High Earners (&gt; 90k)
        </button>
      </div>

      {/* Query Results */}
      <div className="mt-6 pt-4 border-t border-border/60">
        <div className="flex items-center justify-between mb-3 text-xs">
          <span className="font-semibold text-foreground flex items-center">
            <Table className="h-3.5 w-3.5 mr-1 text-primary" />
            Query Result ({results.length} rows)
          </span>
          {execTime !== null && (
            <span className="text-muted-foreground font-mono">Executed in {execTime} ms</span>
          )}
        </div>

        {error ? (
          <div className="p-3 rounded-lg bg-destructive/10 text-destructive text-xs">
            {error}
          </div>
        ) : (
          <div className="overflow-x-auto rounded-xl border border-border">
            <table className="w-full text-left text-xs font-mono">
              <thead className="bg-muted/60 border-b border-border text-foreground">
                <tr>
                  <th className="py-2.5 px-3">id</th>
                  <th className="py-2.5 px-3">name</th>
                  <th className="py-2.5 px-3">department</th>
                  <th className="py-2.5 px-3">salary ($)</th>
                  <th className="py-2.5 px-3">experience</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border/60 bg-card">
                {results.map((r, i) => (
                  <tr key={i} className="hover:bg-muted/30 transition-colors">
                    <td className="py-2 px-3 text-muted-foreground">{r.id}</td>
                    <td className="py-2 px-3 font-semibold text-foreground">{r.name}</td>
                    <td className="py-2 px-3 text-foreground">{r.department}</td>
                    <td className="py-2 px-3 text-emerald-600 dark:text-emerald-400 font-bold">
                      ${r.salary.toLocaleString()}
                    </td>
                    <td className="py-2 px-3 text-muted-foreground">{r.experience_years} yrs</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
