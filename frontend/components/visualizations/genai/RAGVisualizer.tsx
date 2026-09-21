'use client';

import * as React from 'react';
import { Wand2, Database, Search, Cpu, ArrowDown, CheckCircle2 } from 'lucide-react';

export function RAGVisualizer() {
  const [activeStep, setActiveStep] = React.useState<number>(1);

  const steps = [
    {
      num: 1,
      title: 'User Question',
      icon: <Wand2 className="h-4 w-4 text-pink-500" />,
      detail: 'The user submits: "What is the return policy for international orders?"',
      code: 'user_query = "What is the return policy for international orders?"',
    },
    {
      num: 2,
      title: 'Dense Vector Embedding',
      icon: <Cpu className="h-4 w-4 text-cyan-500" />,
      detail: 'An embedding model (e.g. text-embedding-3-small) turns the query into a 1536-dimensional semantic vector.',
      code: 'query_vector = embed_model.encode(user_query) # [0.018, -0.042, ...]',
    },
    {
      num: 3,
      title: 'Vector DB Semantic Search',
      icon: <Database className="h-4 w-4 text-blue-500" />,
      detail: 'Cosine similarity searches the vector index for the top-k most relevant indexed knowledge chunks.',
      code: 'matches = vector_db.similarity_search(query_vector, top_k=2)\n# Found: Document #402 (similarity: 0.91)',
    },
    {
      num: 4,
      title: 'Context Injection & Generation',
      icon: <CheckCircle2 className="h-4 w-4 text-emerald-500" />,
      detail: 'Retrieved text chunks are injected into the prompt, grounding the LLM to generate an accurate, hallucination-free answer.',
      code: 'prompt = f"Context: {matches}\\nQuestion: {user_query}\\nAnswer:"\nresponse = llm.generate(prompt)',
    },
  ];

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center space-x-2 pb-4 border-b border-border/60">
        <div className="p-2 rounded-lg bg-pink-500/10 text-pink-500">
          <Wand2 className="h-5 w-5" />
        </div>
        <div>
          <h4 className="text-base font-bold text-foreground">RAG: Retrieval-Augmented Generation Architecture</h4>
          <p className="text-xs text-muted-foreground">Click each stage to trace query embedding, semantic retrieval, and context injection</p>
        </div>
      </div>

      {/* 4 Interactive Step Blocks */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 my-6">
        {steps.map((st) => {
          const isActive = activeStep === st.num;

          return (
            <button
              key={st.num}
              onClick={() => setActiveStep(st.num)}
              className={`p-4 rounded-xl border text-left transition-all duration-200 ${
                isActive
                  ? 'bg-primary/10 border-primary shadow-md scale-102 ring-1 ring-primary'
                  : 'bg-muted/30 border-border hover:bg-muted/60'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <div className="p-1.5 rounded-md bg-card border border-border">
                  {st.icon}
                </div>
                <span className="text-[10px] font-mono font-bold text-muted-foreground">
                  Step {st.num}
                </span>
              </div>
              <h5 className="text-xs font-bold text-foreground">{st.title}</h5>
            </button>
          );
        })}
      </div>

      {/* Selected Step Code & Explanation */}
      {(() => {
        const curr = steps.find((s) => s.num === activeStep) || steps[0];
        return (
          <div className="p-4 rounded-xl bg-muted/20 border border-border space-y-3">
            <div>
              <span className="text-xs font-bold text-foreground">
                Step {curr.num}: {curr.title}
              </span>
              <p className="text-xs text-muted-foreground mt-1 leading-relaxed">
                {curr.detail}
              </p>
            </div>
            <pre className="p-3 rounded-lg bg-slate-950 text-slate-200 font-mono text-xs overflow-x-auto shadow-inner">
              <code>{curr.code}</code>
            </pre>
          </div>
        );
      })()}
    </div>
  );
}
