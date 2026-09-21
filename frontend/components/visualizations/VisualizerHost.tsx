'use client';

import * as React from 'react';
import { ArrayVisualizer } from './dsa/ArrayVisualizer';
import { BinarySearchVisualizer } from './dsa/BinarySearchVisualizer';
import { SortingVisualizer } from './dsa/SortingVisualizer';
import { LinearRegressionVisualizer } from './ml/LinearRegressionVisualizer';
import { ConfusionMatrixVisualizer } from './ml/ConfusionMatrixVisualizer';
import { SQLEditor } from './sql/SQLEditor';
import { MongoPlayground } from './mongodb/MongoPlayground';
import { LLMPipelineVisualizer } from './llm/LLMPipelineVisualizer';
import { RAGVisualizer } from './genai/RAGVisualizer';
import { AgentWorkflowVisualizer } from './agentic/AgentWorkflowVisualizer';

interface VisualizerHostProps {
  componentName?: string | null;
  initialState?: Record<string, any>;
}

export function VisualizerHost({ componentName, initialState }: VisualizerHostProps) {
  if (!componentName) return null;

  switch (componentName) {
    case 'ArrayVisualizer':
      return <ArrayVisualizer initialItems={initialState?.items} />;
    case 'BinarySearchVisualizer':
      return <BinarySearchVisualizer initialItems={initialState?.items} />;
    case 'SortingVisualizer':
      return <SortingVisualizer initialItems={initialState?.items} />;
    case 'LinearRegressionVisualizer':
      return <LinearRegressionVisualizer />;
    case 'ConfusionMatrixVisualizer':
      return <ConfusionMatrixVisualizer />;
    case 'SQLEditor':
      return <SQLEditor initialQuery={initialState?.defaultQuery} />;
    case 'MongoPlayground':
      return <MongoPlayground />;
    case 'LLMPipelineVisualizer':
      return <LLMPipelineVisualizer />;
    case 'RAGVisualizer':
      return <RAGVisualizer />;
    case 'AgentWorkflowVisualizer':
      return <AgentWorkflowVisualizer />;
    default:
      return null;
  }
}
