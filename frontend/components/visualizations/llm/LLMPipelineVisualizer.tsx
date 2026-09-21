'use client';

import * as React from 'react';
import { Sparkles, ArrowRight, CheckCircle2, ChevronRight } from 'lucide-react';

interface StageInfo {
  id: string;
  name: string;
  shortDesc: string;
  details: string;
  outputSample: string;
}

const STAGES: StageInfo[] = [
  {
    id: 'prompt',
    name: '1. User Prompt',
    shortDesc: 'Raw natural language input',
    details: 'The user enters arbitrary text, system instructions, and optional chat history.',
    outputSample: '"Explain neural networks in simple terms."',
  },
  {
    id: 'tokenization',
    name: '2. BPE Tokenization',
    shortDesc: 'Splitting text into discrete tokens',
    details: 'Byte-Pair Encoding (BPE) breaks words and subwords into integer token IDs recognized by the model dictionary vocabulary (e.g. 50k - 100k tokens).',
    outputSample: '[18204, 3819, 7812, 304, 3491, 2419, 13]',
  },
  {
    id: 'embeddings',
    name: '3. Vector Embeddings',
    shortDesc: 'Converting token IDs to dense vectors',
    details: 'Each token ID maps to a high-dimensional vector (e.g. 4096 dimensions) plus positional encoding vectors to retain sequence order.',
    outputSample: '[[0.024, -0.412, ...], [0.183, 0.091, ...], ...]',
  },
  {
    id: 'attention',
    name: '4. Multi-Head Attention',
    shortDesc: 'Computing contextual relationships',
    details: 'Query, Key, and Value projections compute softmax attention weights: Attention(Q, K, V) = softmax(QK^T / √d_k)V so every token attends to all relevant context.',
    outputSample: 'Attention Matrix: [7 x 7 tokens weighted scores]',
  },
  {
    id: 'transformer',
    name: '5. Feed-Forward Layers',
    shortDesc: 'Deep non-linear feature transformation',
    details: 'Repeated transformer blocks (RMSNorm, SwiGLU, MLP) project token representations through billions of learned parameters.',
    outputSample: 'Hidden State Vector: [batch, seq_len, 4096]',
  },
  {
    id: 'generation',
    name: '6. Generation & Softmax',
    shortDesc: 'Next-token probability prediction',
    details: 'Final linear projection produces logits over vocabulary. Softmax temperature sampling selects the next token, autoregressively feeding it back.',
    outputSample: 'Predicted: "Neural" (p=0.94) → "networks" (p=0.98)',
  },
];

export function LLMPipelineVisualizer() {
  const [selectedStage, setSelectedStage] = React.useState<StageInfo>(STAGES[0]);

  return (
    <div className="rounded-2xl border border-border/80 bg-card p-6 shadow-lg my-6">
      <div className="flex items-center space-x-2 pb-4 border-b border-border/60">
        <div className="p-2 rounded-lg bg-purple-500/10 text-purple-500">
          <Sparkles className="h-5 w-5" />
        </div>
        <div>
          <h4 className="text-base font-bold text-foreground">Interactive LLM Pipeline Visualizer</h4>
          <p className="text-xs text-muted-foreground">
            Click any stage in the pipeline to examine internal transformer representations
          </p>
        </div>
      </div>

      {/* Horizontal Pipeline Steps */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 my-6">
        {STAGES.map((st) => {
          const isSelected = selectedStage.id === st.id;

          return (
            <button
              key={st.id}
              onClick={() => setSelectedStage(st)}
              className={`p-3 rounded-xl border text-left transition-all duration-200 ${
                isSelected
                  ? 'bg-primary/10 border-primary shadow-sm scale-102 ring-1 ring-primary'
                  : 'bg-muted/30 border-border hover:bg-muted/60 hover:border-primary/40'
              }`}
            >
              <span className="text-[10px] font-mono uppercase tracking-wider text-muted-foreground block">
                {st.id}
              </span>
              <span className={`text-xs font-bold block mt-1 ${isSelected ? 'text-primary' : 'text-foreground'}`}>
                {st.name}
              </span>
            </button>
          );
        })}
      </div>

      {/* Stage Detail Inspector */}
      <div className="p-5 rounded-xl border border-border bg-muted/20">
        <div className="flex items-start justify-between">
          <div>
            <h5 className="text-sm font-bold text-foreground flex items-center">
              {selectedStage.name}
              <span className="ml-2 text-xs font-normal text-muted-foreground">— {selectedStage.shortDesc}</span>
            </h5>
            <p className="text-xs text-foreground/80 mt-2 leading-relaxed max-w-2xl">
              {selectedStage.details}
            </p>
          </div>
        </div>

        <div className="mt-4 pt-3 border-t border-border/60">
          <span className="text-[11px] font-semibold text-muted-foreground uppercase tracking-wider block mb-1.5">
            Internal Representation / Output:
          </span>
          <pre className="p-3 rounded-lg bg-slate-950 text-emerald-400 font-mono text-xs overflow-x-auto shadow-inner">
            {selectedStage.outputSample}
          </pre>
        </div>
      </div>
    </div>
  );
}
