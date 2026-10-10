'use client';

import * as React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import {
  Search,
  BookOpen,
  Terminal,
  GitBranch,
  Cloud,
  Binary,
  Brain,
  Database,
  Layers,
  Sparkles,
  Wand2,
  Bot,
  Cpu,
  BarChart2,
  Rocket,
  Copy,
  Check,
  ChevronRight,
  List,
  ArrowUp,
  FileText,
  Clock,
  ExternalLink,
  Flame,
  Bookmark,
  CheckCircle2,
  X,
  Filter,
  Edit3,
  Save,
  Plus,
  Eye,
  Columns,
  Code,
  Bold,
  Italic,
  ListOrdered,
  Quote,
  Table,
  RotateCcw,
  PlusCircle,
} from 'lucide-react';
import {
  fetchContentTree,
  fetchContentFile,
  searchContentNotes,
  saveContentFile,
  createContentFile,
} from '@/lib/api';
import {
  ContentSubject,
  ContentFileSummary,
  ContentFileDetail,
  ContentSearchResult,
} from '@/lib/types';
import { CodeBlock } from '@/components/code/CodeBlock';

const SUBJECT_ICONS: Record<string, React.ReactNode> = {
  python: <Terminal className="h-4 w-4" />,
  statistics: <BarChart2 className="h-4 w-4" />,
  git: <GitBranch className="h-4 w-4" />,
  aws: <Cloud className="h-4 w-4" />,
  dsa: <Binary className="h-4 w-4" />,
  'machine-learning': <Brain className="h-4 w-4" />,
  sql: <Database className="h-4 w-4" />,
  mongodb: <Layers className="h-4 w-4" />,
  llm: <Sparkles className="h-4 w-4" />,
  'generative-ai': <Wand2 className="h-4 w-4" />,
  'agentic-ai': <Bot className="h-4 w-4" />,
  'deep-learning': <Cpu className="h-4 w-4" />,
  nlp: <FileText className="h-4 w-4" />,
  deployment: <Rocket className="h-4 w-4" />,
};

const SUBJECT_COLORS: Record<string, { bg: string; text: string; border: string }> = {
  python: { bg: 'bg-emerald-500/10', text: 'text-emerald-500 dark:text-emerald-400', border: 'border-emerald-500/30' },
  statistics: { bg: 'bg-teal-500/10', text: 'text-teal-500 dark:text-teal-400', border: 'border-teal-500/30' },
  git: { bg: 'bg-orange-500/10', text: 'text-orange-500 dark:text-orange-400', border: 'border-orange-500/30' },
  aws: { bg: 'bg-amber-500/10', text: 'text-amber-500 dark:text-amber-400', border: 'border-amber-500/30' },
  dsa: { bg: 'bg-blue-500/10', text: 'text-blue-500 dark:text-blue-400', border: 'border-blue-500/30' },
  'machine-learning': { bg: 'bg-purple-500/10', text: 'text-purple-500 dark:text-purple-400', border: 'border-purple-500/30' },
  sql: { bg: 'bg-cyan-500/10', text: 'text-cyan-500 dark:text-cyan-400', border: 'border-cyan-500/30' },
  mongodb: { bg: 'bg-green-500/10', text: 'text-green-500 dark:text-green-400', border: 'border-green-500/30' },
  llm: { bg: 'bg-indigo-500/10', text: 'text-indigo-500 dark:text-indigo-400', border: 'border-indigo-500/30' },
  'generative-ai': { bg: 'bg-pink-500/10', text: 'text-pink-500 dark:text-pink-400', border: 'border-pink-500/30' },
  'agentic-ai': { bg: 'bg-violet-500/10', text: 'text-violet-500 dark:text-violet-400', border: 'border-violet-500/30' },
  'deep-learning': { bg: 'bg-rose-500/10', text: 'text-rose-500 dark:text-rose-400', border: 'border-rose-500/30' },
  nlp: { bg: 'bg-emerald-500/10', text: 'text-emerald-500 dark:text-emerald-400', border: 'border-emerald-500/30' },
  deployment: { bg: 'bg-rose-500/10', text: 'text-rose-500 dark:text-rose-400', border: 'border-rose-500/30' },
};

/**
 * Reusable Markdown renderer component with syntax highlighting, styled tables, and jump-to headings.
 */
function MarkdownRenderer({ content }: { content: string }) {
  return (
    <div className="prose dark:prose-invert max-w-none space-y-4">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          h1: ({ children }) => {
            const title = String(children);
            const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
            return (
              <h1
                id={slug}
                className="text-2xl sm:text-3xl font-extrabold text-foreground border-b border-border pb-3 pt-6 tracking-tight mt-6 scroll-mt-24 first:mt-0"
              >
                {children}
              </h1>
            );
          },
          h2: ({ children }) => {
            const title = String(children);
            const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
            return (
              <h2
                id={slug}
                className="text-xl sm:text-2xl font-bold text-foreground border-b border-border/50 pb-2 pt-5 tracking-tight mt-6 scroll-mt-24 flex items-center space-x-2"
              >
                <span className="w-1.5 h-5 rounded-full bg-primary inline-block mr-2" />
                <span>{children}</span>
              </h2>
            );
          },
          h3: ({ children }) => {
            const title = String(children);
            const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
            return (
              <h3
                id={slug}
                className="text-lg sm:text-xl font-semibold text-foreground pt-4 tracking-tight scroll-mt-24"
              >
                {children}
              </h3>
            );
          },
          h4: ({ children }) => (
            <h4 className="text-base font-semibold text-primary pt-3">
              {children}
            </h4>
          ),
          p: ({ children }) => (
            <p className="text-foreground/90 leading-relaxed my-3 font-normal">
              {children}
            </p>
          ),
          ul: ({ children }) => (
            <ul className="list-disc list-inside space-y-2 my-3 pl-2 text-foreground/90">
              {children}
            </ul>
          ),
          ol: ({ children }) => (
            <ol className="list-decimal list-inside space-y-2 my-3 pl-2 text-foreground/90 font-medium">
              {children}
            </ol>
          ),
          li: ({ children }) => (
            <li className="leading-relaxed text-foreground/85">
              {children}
            </li>
          ),
          blockquote: ({ children }) => (
            <blockquote className="border-l-4 border-primary pl-4 py-2 my-4 bg-primary/5 rounded-r-xl text-foreground/90 italic">
              {children}
            </blockquote>
          ),
          hr: () => <hr className="border-border my-6" />,
          table: ({ children }) => (
            <div className="overflow-x-auto my-6 rounded-xl border border-border">
              <table className="min-w-full divide-y divide-border text-xs sm:text-sm">
                {children}
              </table>
            </div>
          ),
          thead: ({ children }) => (
            <thead className="bg-muted text-foreground font-semibold">
              {children}
            </thead>
          ),
          tbody: ({ children }) => (
            <tbody className="divide-y divide-border bg-card">
              {children}
            </tbody>
          ),
          tr: ({ children }) => (
            <tr className="hover:bg-muted/40 transition-colors">
              {children}
            </tr>
          ),
          th: ({ children }) => (
            <th className="px-4 py-2.5 text-left font-semibold text-foreground">
              {children}
            </th>
          ),
          td: ({ children }) => (
            <td className="px-4 py-2.5 text-foreground/90 align-top">
              {children}
            </td>
          ),
          code: ({ node, inline, className, children, ...props }: any) => {
            const match = /language-(\w+)/.exec(className || '');
            const codeText = String(children).replace(/\n$/, '');
            if (!inline && (match || codeText.includes('\n'))) {
              return (
                <CodeBlock
                  code={codeText}
                  language={match ? match[1] : 'text'}
                />
              );
            }
            return (
              <code
                className="px-1.5 py-0.5 rounded-md bg-muted text-primary font-mono text-xs font-medium border border-border"
                {...props}
              >
                {children}
              </code>
            );
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}

export default function RevisionHubPage() {
  const [tree, setTree] = React.useState<ContentSubject[]>([]);
  const [selectedSubject, setSelectedSubject] = React.useState<string>('all');
  const [selectedFile, setSelectedFile] = React.useState<{ subjectSlug: string; fileSlug: string } | null>(null);
  const [activeFileDetail, setActiveFileDetail] = React.useState<ContentFileDetail | null>(null);
  const [loading, setLoading] = React.useState<boolean>(true);
  const [contentLoading, setContentLoading] = React.useState<boolean>(false);
  const [searchQuery, setSearchQuery] = React.useState<string>('');
  const [searchResults, setSearchResults] = React.useState<ContentSearchResult[]>([]);
  const [isSearching, setIsSearching] = React.useState<boolean>(false);
  const [copied, setCopied] = React.useState<boolean>(false);
  const [fontSize, setFontSize] = React.useState<'sm' | 'md' | 'lg'>('md');
  const [mobileTocOpen, setMobileTocOpen] = React.useState<boolean>(false);

  // Markdown Editing & Authoring State
  const [isEditing, setIsEditing] = React.useState<boolean>(false);
  const [editedContent, setEditedContent] = React.useState<string>('');
  const [editViewMode, setEditViewMode] = React.useState<'write' | 'preview' | 'split'>('split');
  const [isSaving, setIsSaving] = React.useState<boolean>(false);
  const [saveFeedback, setSaveFeedback] = React.useState<{ type: 'success' | 'error'; message: string } | null>(null);
  const textareaRef = React.useRef<HTMLTextAreaElement>(null);

  // Quick Append state
  const [quickAppendText, setQuickAppendText] = React.useState<string>('');
  const [isQuickAppendOpen, setIsQuickAppendOpen] = React.useState<boolean>(false);

  // New Note Modal state
  const [isNewNoteModalOpen, setIsNewNoteModalOpen] = React.useState<boolean>(false);
  const [newNoteSubject, setNewNoteSubject] = React.useState<string>('python');
  const [newNoteTitle, setNewNoteTitle] = React.useState<string>('');
  const [newNoteSlug, setNewNoteSlug] = React.useState<string>('');
  const [newNoteContent, setNewNoteContent] = React.useState<string>('');
  const [isCreatingNote, setIsCreatingNote] = React.useState<boolean>(false);

  // Load subject tree on mount
  React.useEffect(() => {
    async function loadTree() {
      try {
        setLoading(true);
        const data = await fetchContentTree();
        setTree(data);
        if (data.length > 0 && data[0].files.length > 0) {
          const firstSubject = data[0];
          const firstFile = firstSubject.files[0];
          setSelectedFile({
            subjectSlug: firstSubject.subjectSlug,
            fileSlug: firstFile.slug,
          });
        }
      } catch (err) {
        console.error('Failed to load revision tree:', err);
      } finally {
        setLoading(false);
      }
    }
    loadTree();
  }, []);

  // Load file content when selectedFile changes
  React.useEffect(() => {
    if (!selectedFile) return;
    async function loadFile() {
      try {
        setContentLoading(true);
        const detail = await fetchContentFile(selectedFile.subjectSlug, selectedFile.fileSlug);
        setActiveFileDetail(detail);
        setEditedContent(detail.content);
        setIsEditing(false); // Close editor on switching file
      } catch (err) {
        console.error('Failed to load file content:', err);
      } finally {
        setContentLoading(false);
      }
    }
    loadFile();
  }, [selectedFile]);

  // Debounced search across all files
  React.useEffect(() => {
    if (!searchQuery.trim() || searchQuery.trim().length < 2) {
      setSearchResults([]);
      setIsSearching(false);
      return;
    }

    const timer = setTimeout(async () => {
      try {
        setIsSearching(true);
        const data = await searchContentNotes(searchQuery);
        setSearchResults(data.results);
      } catch (err) {
        console.error('Search failed:', err);
      } finally {
        setIsSearching(false);
      }
    }, 300);

    return () => clearTimeout(timer);
  }, [searchQuery]);

  // Copy full note to clipboard
  const handleCopyAll = async () => {
    const textToCopy = isEditing ? editedContent : activeFileDetail?.content;
    if (!textToCopy) return;
    try {
      await navigator.clipboard.writeText(textToCopy);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // ignore
    }
  };

  // Scroll to heading
  const scrollToHeading = (slug: string) => {
    const el = document.getElementById(slug);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      setMobileTocOpen(false);
    }
  };

  // Save edited markdown directly to its respective file
  const handleSave = async () => {
    if (!selectedFile) return;
    try {
      setIsSaving(true);
      const updated = await saveContentFile(selectedFile.subjectSlug, selectedFile.fileSlug, editedContent);
      setActiveFileDetail(updated);
      setSaveFeedback({ type: 'success', message: `Saved directly to ${selectedFile.fileSlug}.md!` });
      // Refresh tree to update file sizes and headings
      const freshTree = await fetchContentTree();
      setTree(freshTree);
      setTimeout(() => setSaveFeedback(null), 4000);
    } catch (err: any) {
      console.error('Failed to save file:', err);
      setSaveFeedback({ type: 'error', message: err.message || 'Failed to save changes' });
    } finally {
      setIsSaving(false);
    }
  };

  // Quick Append to end of file
  const handleQuickAppend = async () => {
    if (!selectedFile || !quickAppendText.trim() || !activeFileDetail) return;
    try {
      setIsSaving(true);
      const newFullContent = `${activeFileDetail.content.trimEnd()}\n\n---\n\n${quickAppendText.trim()}\n`;
      const updated = await saveContentFile(selectedFile.subjectSlug, selectedFile.fileSlug, newFullContent);
      setActiveFileDetail(updated);
      setEditedContent(newFullContent);
      setQuickAppendText('');
      setIsQuickAppendOpen(false);
      setSaveFeedback({ type: 'success', message: `Appended notes to ${selectedFile.fileSlug}.md!` });
      const freshTree = await fetchContentTree();
      setTree(freshTree);
      setTimeout(() => setSaveFeedback(null), 4000);
    } catch (err: any) {
      console.error('Failed to append:', err);
      setSaveFeedback({ type: 'error', message: err.message || 'Failed to append notes' });
    } finally {
      setIsSaving(false);
    }
  };

  // Create new markdown file in selected subject
  const handleCreateNote = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newNoteTitle.trim() || !newNoteSubject) return;
    try {
      setIsCreatingNote(true);
      const autoSlug = newNoteSlug.trim() || newNoteTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
      const initialContent = newNoteContent.trim() || `# ${newNoteTitle}\n\n`;
      const created = await createContentFile(newNoteSubject, autoSlug, initialContent, newNoteTitle);

      const freshTree = await fetchContentTree();
      setTree(freshTree);
      setSelectedSubject(newNoteSubject);
      setSelectedFile({ subjectSlug: newNoteSubject, fileSlug: created.fileSlug });
      setActiveFileDetail(created);
      setEditedContent(created.content);
      setIsNewNoteModalOpen(false);
      setSaveFeedback({ type: 'success', message: `Created new file ${created.fileSlug}.md successfully!` });
      setTimeout(() => setSaveFeedback(null), 4000);
    } catch (err: any) {
      console.error('Failed to create note:', err);
      setSaveFeedback({ type: 'error', message: err.message || 'Failed to create note' });
    } finally {
      setIsCreatingNote(false);
    }
  };

  // Markdown Toolbar helper to insert syntax at cursor
  const insertMarkdown = (before: string, after: string = '') => {
    const textarea = textareaRef.current;
    if (!textarea) return;
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const text = textarea.value;
    const selection = text.substring(start, end);
    const replacement = before + (selection || '') + after;
    const newText = text.substring(0, start) + replacement + text.substring(end);
    setEditedContent(newText);
    setTimeout(() => {
      textarea.focus();
      textarea.setSelectionRange(start + before.length, start + before.length + selection.length);
    }, 0);
  };

  // Filtered files for the left sidebar
  const filteredFiles: { subject: ContentSubject; file: ContentFileSummary }[] = React.useMemo(() => {
    const list: { subject: ContentSubject; file: ContentFileSummary }[] = [];
    tree.forEach((subject) => {
      if (selectedSubject === 'all' || selectedSubject === subject.subjectSlug) {
        subject.files.forEach((file) => {
          list.push({ subject, file });
        });
      }
    });
    return list;
  }, [tree, selectedSubject]);

  // Total stats
  const totalNotesCount = React.useMemo(() => {
    return tree.reduce((acc, sub) => acc + sub.files.length, 0);
  }, [tree]);

  return (
    <div className="min-h-screen bg-background flex flex-col">
      {/* Top Banner & Header */}
      <section className="border-b border-border/80 bg-card/60 backdrop-blur-md px-4 sm:px-6 lg:px-8 py-6">
        <div className="max-w-7xl mx-auto space-y-4">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-primary/10 border border-primary/20 text-xs font-semibold text-primary mb-2">
                <Flame className="h-3.5 w-3.5" />
                <span>Unified Interview Revision Hub</span>
              </div>
              <h1 className="text-2xl sm:text-3xl font-extrabold text-foreground tracking-tight">
                Complete Revision Notes & Interview Concepts
              </h1>
              <p className="text-sm text-muted-foreground mt-1 max-w-3xl">
                All study notes, cross-examination questions, architecture internals, and code examples
                preserved verbatim across 14 core engineering courses.
              </p>
            </div>

            {/* Quick Metrics & Add Note Button */}
            <div className="flex flex-wrap items-center gap-3 text-xs text-muted-foreground shrink-0">
              <button
                onClick={() => {
                  setNewNoteSubject(selectedSubject !== 'all' ? selectedSubject : (tree[0]?.subjectSlug || 'python'));
                  setNewNoteTitle('');
                  setNewNoteSlug('');
                  setNewNoteContent('# New Topic Title\n\nWrite your concepts, formulas, questions, or code here...\n');
                  setIsNewNoteModalOpen(true);
                }}
                className="px-3.5 py-2 rounded-xl bg-primary hover:bg-primary/90 text-primary-foreground font-semibold flex items-center space-x-1.5 shadow-sm transition-all"
                title="Create new markdown note"
              >
                <Plus className="h-4 w-4" />
                <span>New .md Note</span>
              </button>

              <div className="px-3 py-2 rounded-xl bg-muted/60 border border-border flex items-center space-x-2">
                <BookOpen className="h-4 w-4 text-primary" />
                <span>
                  <strong className="text-foreground">{tree.length}</strong> Courses
                </span>
              </div>
              <div className="px-3 py-2 rounded-xl bg-muted/60 border border-border flex items-center space-x-2">
                <FileText className="h-4 w-4 text-emerald-500" />
                <span>
                  <strong className="text-foreground">{totalNotesCount}</strong> Notes
                </span>
              </div>
            </div>
          </div>

          {/* Search Bar */}
          <div className="relative">
            <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search concepts, interview questions, algorithms, keywords (e.g. 'shallow copy', 'rebase', 'EC2', 'ReAct', 'BERT', 'overfitting')..."
              className="w-full pl-10 pr-10 py-2.5 rounded-xl border border-border bg-background/90 text-sm placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/40 transition-all shadow-sm"
            />
            {searchQuery && (
              <button
                onClick={() => setSearchQuery('')}
                className="absolute right-3.5 top-1/2 -translate-y-1/2 text-muted-foreground hover:text-foreground"
              >
                <X className="h-4 w-4" />
              </button>
            )}
          </div>
        </div>
      </section>

      {/* Main 3-Column Workspace */}
      <div className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column: Subject Filter + Notes List (3 Cols) */}
        <aside className="lg:col-span-4 xl:col-span-3 space-y-4">
          {/* Subject Pills Filter */}
          <div className="space-y-1.5">
            <div className="flex items-center justify-between text-xs font-semibold uppercase tracking-wider text-muted-foreground px-1">
              <span>Courses ({tree.length})</span>
              {selectedSubject !== 'all' && (
                <button
                  onClick={() => setSelectedSubject('all')}
                  className="text-primary hover:underline text-[11px] capitalize"
                >
                  Clear filter
                </button>
              )}
            </div>

            <div className="flex lg:flex-col gap-1.5 overflow-x-auto lg:overflow-visible pb-2 lg:pb-0 scrollbar-none">
              <button
                onClick={() => setSelectedSubject('all')}
                className={`px-3 py-2 rounded-lg text-xs font-medium text-left transition-colors whitespace-nowrap flex items-center justify-between ${
                  selectedSubject === 'all'
                    ? 'bg-primary text-primary-foreground font-semibold shadow-sm'
                    : 'bg-card hover:bg-muted text-foreground/80 border border-border'
                }`}
              >
                <div className="flex items-center space-x-2">
                  <Bookmark className="h-3.5 w-3.5" />
                  <span>All Courses</span>
                </div>
                <span className="text-[10px] opacity-75 ml-2">{totalNotesCount}</span>
              </button>

              {tree.map((sub) => {
                const isSelected = selectedSubject === sub.subjectSlug;
                return (
                  <button
                    key={sub.subjectSlug}
                    onClick={() => setSelectedSubject(sub.subjectSlug)}
                    className={`px-3 py-2 rounded-lg text-xs font-medium text-left transition-colors whitespace-nowrap flex items-center justify-between ${
                      isSelected
                        ? 'bg-primary text-primary-foreground font-semibold shadow-sm'
                        : 'bg-card hover:bg-muted text-foreground/80 border border-border'
                    }`}
                  >
                    <div className="flex items-center space-x-2">
                      <span className={isSelected ? 'text-white' : ''}>
                        {SUBJECT_ICONS[sub.subjectSlug] || <BookOpen className="h-3.5 w-3.5" />}
                      </span>
                      <span className="truncate">{sub.subjectName}</span>
                    </div>
                    <span className="text-[10px] opacity-75 ml-2">{sub.files.length}</span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Notes Explorer List */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs font-semibold uppercase tracking-wider text-muted-foreground px-1">
              <span>Note Modules ({filteredFiles.length})</span>
              <button
                onClick={() => {
                  setNewNoteSubject(selectedSubject !== 'all' ? selectedSubject : (tree[0]?.subjectSlug || 'python'));
                  setNewNoteTitle('');
                  setNewNoteSlug('');
                  setNewNoteContent('# New Topic Title\n\nAdd your interview concepts and notes here...\n');
                  setIsNewNoteModalOpen(true);
                }}
                className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-md bg-primary/10 hover:bg-primary/20 text-primary text-[11px] font-medium transition-colors"
                title="Create new markdown note"
              >
                <Plus className="h-3 w-3" />
                <span>Add .md</span>
              </button>
            </div>

            <div className="space-y-2 max-h-[calc(100vh-280px)] overflow-y-auto pr-1">
              {filteredFiles.map(({ subject, file }) => {
                const isCurrent =
                  selectedFile?.subjectSlug === subject.subjectSlug &&
                  selectedFile?.fileSlug === file.slug;
                const colors = SUBJECT_COLORS[subject.subjectSlug] || {
                  bg: 'bg-muted',
                  text: 'text-foreground',
                  border: 'border-border',
                };

                return (
                  <button
                    key={`${subject.subjectSlug}-${file.slug}`}
                    onClick={() => {
                      setSelectedFile({ subjectSlug: subject.subjectSlug, fileSlug: file.slug });
                      setSearchQuery('');
                    }}
                    className={`w-full text-left p-3 rounded-xl border transition-all text-xs space-y-1.5 ${
                      isCurrent
                        ? 'border-primary ring-1 ring-primary bg-primary/5 shadow-sm'
                        : 'border-border bg-card hover:border-primary/40 hover:bg-muted/50'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span
                        className={`inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[10px] font-semibold border ${colors.bg} ${colors.text} ${colors.border}`}
                      >
                        {SUBJECT_ICONS[subject.subjectSlug]}
                        <span>{subject.subjectName.split(' ')[0]}</span>
                      </span>
                      <span className="text-[10px] text-muted-foreground flex items-center space-x-1">
                        <Clock className="h-3 w-3" />
                        <span>{file.estimatedReadTime}</span>
                      </span>
                    </div>

                    <h4
                      className={`font-semibold line-clamp-2 leading-snug ${
                        isCurrent ? 'text-primary font-bold' : 'text-foreground'
                      }`}
                    >
                      {file.title}
                    </h4>

                    <div className="flex items-center justify-between text-[11px] text-muted-foreground pt-1">
                      <span>{(file.sizeBytes / 1024).toFixed(1)} KB</span>
                      <span className="text-primary font-medium flex items-center space-x-0.5">
                        <span>Read</span>
                        <ChevronRight className="h-3 w-3" />
                      </span>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>
        </aside>

        {/* Center Column: Active Note Content & Editor (6 or 7 Cols) */}
        <main className="lg:col-span-8 xl:col-span-6 space-y-4">
          {/* Notification Feedback Banner */}
          {saveFeedback && (
            <div
              className={`p-3.5 rounded-xl border text-xs font-medium flex items-center justify-between shadow-sm transition-all ${
                saveFeedback.type === 'success'
                  ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-600 dark:text-emerald-400'
                  : 'bg-red-500/10 border-red-500/30 text-red-600 dark:text-red-400'
              }`}
            >
              <div className="flex items-center space-x-2">
                {saveFeedback.type === 'success' ? (
                  <CheckCircle2 className="h-4 w-4" />
                ) : (
                  <X className="h-4 w-4" />
                )}
                <span>{saveFeedback.message}</span>
              </div>
              <button
                onClick={() => setSaveFeedback(null)}
                className="opacity-70 hover:opacity-100"
              >
                <X className="h-3.5 w-3.5" />
              </button>
            </div>
          )}

          {/* Search Result Overlay if Searching */}
          {searchQuery.trim().length >= 2 ? (
            <div className="bg-card border border-border rounded-2xl p-6 space-y-4">
              <div className="flex items-center justify-between border-b border-border pb-3">
                <div className="space-y-0.5">
                  <h2 className="text-lg font-bold text-foreground">
                    Search Results for &ldquo;{searchQuery}&rdquo;
                  </h2>
                  <p className="text-xs text-muted-foreground">
                    Found {searchResults.length} note modules with matching interview concepts
                  </p>
                </div>
                {isSearching && (
                  <span className="text-xs text-primary animate-pulse">Searching notes...</span>
                )}
              </div>

              {searchResults.length === 0 && !isSearching && (
                <div className="text-center py-12 text-sm text-muted-foreground">
                  No direct matches found. Try searching general keywords like &ldquo;memory&rdquo;, &ldquo;index&rdquo;, &ldquo;copy&rdquo;, or &ldquo;attention&rdquo;.
                </div>
              )}

              <div className="space-y-3">
                {searchResults.map((res) => (
                  <div
                    key={`${res.subjectSlug}-${res.fileSlug}`}
                    className="p-4 rounded-xl border border-border bg-background/50 hover:border-primary/50 transition-all space-y-2 cursor-pointer"
                    onClick={() => {
                      setSelectedFile({ subjectSlug: res.subjectSlug, fileSlug: res.fileSlug });
                      setSearchQuery('');
                    }}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-2">
                        <span className="text-xs font-semibold text-primary">{res.subjectName}</span>
                        <span className="text-muted-foreground text-xs">•</span>
                        <h4 className="text-sm font-bold text-foreground">{res.fileTitle}</h4>
                      </div>
                      <span className="text-[11px] px-2 py-0.5 rounded-full bg-primary/10 text-primary font-medium">
                        {res.matchCount} match{res.matchCount > 1 ? 'es' : ''}
                      </span>
                    </div>

                    <div className="space-y-1.5 pl-2 border-l-2 border-primary/30">
                      {res.matches.map((m, idx) => (
                        <div key={idx} className="text-xs text-muted-foreground font-mono">
                          <span className="text-primary mr-2">L{m.lineNumber}:</span>
                          <span className="text-foreground/90">{m.line}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ) : (
            /* Active Markdown Note Workspace (Reader or Full Editor) */
            <div className="bg-card border border-border rounded-2xl shadow-sm overflow-hidden">
              {/* Document Header Controls */}
              <div className="p-4 sm:p-5 border-b border-border bg-muted/30 flex flex-wrap items-center justify-between gap-3">
                <div className="space-y-1">
                  <div className="flex items-center space-x-2 text-xs text-muted-foreground">
                    <span className="font-semibold text-primary">
                      {activeFileDetail?.subjectName || 'Course'}
                    </span>
                    <span>/</span>
                    <span className="font-mono text-[11px]">
                      {activeFileDetail?.fileSlug}.md
                    </span>
                  </div>
                  <h2 className="text-xl sm:text-2xl font-extrabold text-foreground tracking-tight">
                    {activeFileDetail?.title || 'Loading Note...'}
                  </h2>
                </div>

                {/* Reader & Editor Controls */}
                <div className="flex flex-wrap items-center gap-2">
                  {/* EDIT NOTE BUTTON */}
                  <button
                    onClick={() => {
                      setIsEditing(!isEditing);
                      if (!isEditing && activeFileDetail) {
                        setEditedContent(activeFileDetail.content);
                      }
                    }}
                    className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border text-xs font-semibold transition-all ${
                      isEditing
                        ? 'border-primary bg-primary text-primary-foreground shadow-sm'
                        : 'border-primary/50 bg-primary/10 hover:bg-primary/20 text-primary'
                    }`}
                    title="Toggle Markdown Editor"
                  >
                    <Edit3 className="h-3.5 w-3.5" />
                    <span>{isEditing ? 'Exit Editor' : 'Edit Note (.md)'}</span>
                  </button>

                  {/* Font Size Selector (in read mode) */}
                  {!isEditing && (
                    <div className="flex items-center bg-background border border-border rounded-lg p-0.5 text-xs">
                      <button
                        onClick={() => setFontSize('sm')}
                        className={`px-2 py-1 rounded ${fontSize === 'sm' ? 'bg-primary text-primary-foreground font-bold' : 'text-muted-foreground'}`}
                      >
                        A-
                      </button>
                      <button
                        onClick={() => setFontSize('md')}
                        className={`px-2 py-1 rounded ${fontSize === 'md' ? 'bg-primary text-primary-foreground font-bold' : 'text-muted-foreground'}`}
                      >
                        A
                      </button>
                      <button
                        onClick={() => setFontSize('lg')}
                        className={`px-2 py-1 rounded ${fontSize === 'lg' ? 'bg-primary text-primary-foreground font-bold' : 'text-muted-foreground'}`}
                      >
                        A+
                      </button>
                    </div>
                  )}

                  {/* Copy All Button */}
                  <button
                    onClick={handleCopyAll}
                    className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-border bg-background hover:bg-muted text-xs font-medium text-foreground transition-colors"
                    title="Copy note markdown"
                  >
                    {copied ? (
                      <>
                        <Check className="h-3.5 w-3.5 text-emerald-500" />
                        <span className="text-emerald-500">Copied</span>
                      </>
                    ) : (
                      <>
                        <Copy className="h-3.5 w-3.5" />
                        <span>Copy All</span>
                      </>
                    )}
                  </button>

                  {/* Mobile Table of Contents Toggle */}
                  {!isEditing && (
                    <button
                      onClick={() => setMobileTocOpen(!mobileTocOpen)}
                      className="xl:hidden flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-border bg-background hover:bg-muted text-xs font-medium text-foreground"
                    >
                      <List className="h-3.5 w-3.5" />
                      <span>Sections</span>
                    </button>
                  )}
                </div>
              </div>

              {/* Mobile Table of Contents Dropdown */}
              {!isEditing && mobileTocOpen && activeFileDetail?.headings && (
                <div className="xl:hidden p-4 border-b border-border bg-muted/40 max-h-60 overflow-y-auto space-y-1">
                  <div className="text-xs font-bold uppercase tracking-wider text-muted-foreground mb-2">
                    Quick Jump to Section:
                  </div>
                  {activeFileDetail.headings.map((h, idx) => (
                    <button
                      key={idx}
                      onClick={() => scrollToHeading(h.slug)}
                      className={`block w-full text-left text-xs py-1 px-2 rounded hover:bg-muted text-foreground/80 truncate ${
                        h.level === 1 ? 'font-bold' : h.level === 2 ? 'pl-4' : 'pl-6 text-muted-foreground'
                      }`}
                    >
                      {h.title}
                    </button>
                  ))}
                </div>
              )}

              {/* Workspace Content: Editor or Reader */}
              {isEditing ? (
                /* ================= EDIT MODE ================= */
                <div className="p-4 sm:p-6 space-y-4">
                  {/* Editor Bar: View Mode Switcher and Actions */}
                  <div className="flex flex-wrap items-center justify-between gap-3 p-3 bg-muted/40 rounded-xl border border-border">
                    <div className="flex items-center space-x-2">
                      <span className="inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-md bg-primary/10 text-primary text-xs font-semibold">
                        <Edit3 className="h-3.5 w-3.5" />
                        <span>Editing File: {activeFileDetail?.fileSlug}.md</span>
                      </span>
                    </div>

                    {/* View Mode Tabs: Write / Split / Preview */}
                    <div className="flex items-center bg-background border border-border rounded-lg p-0.5 text-xs">
                      <button
                        type="button"
                        onClick={() => setEditViewMode('write')}
                        className={`flex items-center space-x-1 px-2.5 py-1 rounded transition-colors ${
                          editViewMode === 'write' ? 'bg-primary text-primary-foreground font-semibold' : 'text-muted-foreground hover:text-foreground'
                        }`}
                      >
                        <Edit3 className="h-3 w-3" />
                        <span>Write</span>
                      </button>
                      <button
                        type="button"
                        onClick={() => setEditViewMode('split')}
                        className={`hidden md:flex items-center space-x-1 px-2.5 py-1 rounded transition-colors ${
                          editViewMode === 'split' ? 'bg-primary text-primary-foreground font-semibold' : 'text-muted-foreground hover:text-foreground'
                        }`}
                      >
                        <Columns className="h-3 w-3" />
                        <span>Split</span>
                      </button>
                      <button
                        type="button"
                        onClick={() => setEditViewMode('preview')}
                        className={`flex items-center space-x-1 px-2.5 py-1 rounded transition-colors ${
                          editViewMode === 'preview' ? 'bg-primary text-primary-foreground font-semibold' : 'text-muted-foreground hover:text-foreground'
                        }`}
                      >
                        <Eye className="h-3 w-3" />
                        <span>Preview</span>
                      </button>
                    </div>

                    {/* Cancel & Save Buttons */}
                    <div className="flex items-center space-x-2">
                      <button
                        type="button"
                        onClick={() => {
                          setIsEditing(false);
                          if (activeFileDetail) setEditedContent(activeFileDetail.content);
                        }}
                        className="px-3 py-1.5 rounded-lg border border-border bg-background hover:bg-muted text-xs font-medium text-foreground transition-colors"
                      >
                        Cancel
                      </button>
                      <button
                        type="button"
                        onClick={handleSave}
                        disabled={isSaving}
                        className="flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-primary hover:bg-primary/90 text-primary-foreground text-xs font-semibold shadow-sm transition-all disabled:opacity-50"
                      >
                        {isSaving ? (
                          <>
                            <div className="animate-spin rounded-full h-3 w-3 border-b-2 border-white" />
                            <span>Saving...</span>
                          </>
                        ) : (
                          <>
                            <Save className="h-3.5 w-3.5" />
                            <span>Save to File</span>
                          </>
                        )}
                      </button>
                    </div>
                  </div>

                  {/* Formatting Toolbar */}
                  {editViewMode !== 'preview' && (
                    <div className="flex flex-wrap items-center gap-1 p-2 bg-muted/20 border border-border rounded-xl text-xs">
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n# ')}
                        className="px-2 py-1 rounded hover:bg-muted text-foreground font-bold"
                        title="Heading 1"
                      >
                        H1
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n## ')}
                        className="px-2 py-1 rounded hover:bg-muted text-foreground font-bold"
                        title="Heading 2"
                      >
                        H2
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n### ')}
                        className="px-2 py-1 rounded hover:bg-muted text-foreground font-bold"
                        title="Heading 3"
                      >
                        H3
                      </button>
                      <div className="w-[1px] h-4 bg-border mx-1" />
                      <button
                        type="button"
                        onClick={() => insertMarkdown('**', '**')}
                        className="p-1.5 rounded hover:bg-muted text-foreground"
                        title="Bold (**text**)"
                      >
                        <Bold className="h-3.5 w-3.5" />
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('*', '*')}
                        className="p-1.5 rounded hover:bg-muted text-foreground"
                        title="Italic (*text*)"
                      >
                        <Italic className="h-3.5 w-3.5" />
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('`', '`')}
                        className="p-1.5 rounded hover:bg-muted text-foreground"
                        title="Inline Code (`code`)"
                      >
                        <Code className="h-3.5 w-3.5" />
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n```python\n# Add your code here\n', '\n```\n')}
                        className="px-2 py-1 rounded hover:bg-muted text-foreground font-mono text-xs"
                        title="Code Block"
                      >
                        ```code```
                      </button>
                      <div className="w-[1px] h-4 bg-border mx-1" />
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n- ')}
                        className="px-2 py-1 rounded hover:bg-muted text-foreground"
                        title="Bullet List"
                      >
                        • List
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n1. ')}
                        className="p-1.5 rounded hover:bg-muted text-foreground"
                        title="Numbered List"
                      >
                        <ListOrdered className="h-3.5 w-3.5" />
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n> ')}
                        className="p-1.5 rounded hover:bg-muted text-foreground"
                        title="Blockquote"
                      >
                        <Quote className="h-3.5 w-3.5" />
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n| Column 1 | Column 2 |\n| :--- | :--- |\n| Data 1 | Data 2 |\n')}
                        className="p-1.5 rounded hover:bg-muted text-foreground"
                        title="Table"
                      >
                        <Table className="h-3.5 w-3.5" />
                      </button>
                      <button
                        type="button"
                        onClick={() => insertMarkdown('\n$$\n', '\n$$\n')}
                        className="px-2 py-1 rounded hover:bg-muted text-foreground font-mono text-xs"
                        title="Math Formula"
                      >
                        $$ Math
                      </button>
                      <div className="w-[1px] h-4 bg-border mx-1" />
                      <button
                        type="button"
                        onClick={() => activeFileDetail && setEditedContent(activeFileDetail.content)}
                        className="flex items-center space-x-1 px-2 py-1 rounded hover:bg-muted text-muted-foreground hover:text-foreground text-[11px]"
                        title="Reset to Original"
                      >
                        <RotateCcw className="h-3 w-3" />
                        <span>Reset</span>
                      </button>
                      <span className="ml-auto text-[11px] text-muted-foreground pr-1 hidden sm:inline">
                        Press <kbd className="px-1 py-0.5 rounded bg-muted font-mono text-[10px]">Cmd+S</kbd> to save
                      </span>
                    </div>
                  )}

                  {/* Main Editor View */}
                  <div className="grid grid-cols-1 md:grid-cols-12 gap-4">
                    {/* Textarea */}
                    {(editViewMode === 'write' || editViewMode === 'split') && (
                      <div className={editViewMode === 'split' ? 'md:col-span-6 space-y-2' : 'md:col-span-12 space-y-2'}>
                        <textarea
                          ref={textareaRef}
                          value={editedContent}
                          onChange={(e) => setEditedContent(e.target.value)}
                          onKeyDown={(e) => {
                            if ((e.metaKey || e.ctrlKey) && e.key === 's') {
                              e.preventDefault();
                              handleSave();
                            }
                            if (e.key === 'Tab') {
                              e.preventDefault();
                              const start = e.currentTarget.selectionStart;
                              const end = e.currentTarget.selectionEnd;
                              setEditedContent(
                                editedContent.substring(0, start) + '  ' + editedContent.substring(end)
                              );
                              setTimeout(() => {
                                if (textareaRef.current) {
                                  textareaRef.current.selectionStart = textareaRef.current.selectionEnd = start + 2;
                                }
                              }, 0);
                            }
                          }}
                          placeholder="Write markdown content here..."
                          className="w-full h-[calc(100vh-380px)] min-h-[480px] p-4 rounded-xl border border-border bg-background font-mono text-xs sm:text-sm leading-relaxed focus:outline-none focus:ring-2 focus:ring-primary/40 resize-y shadow-inner text-foreground placeholder:text-muted-foreground"
                          spellCheck={false}
                        />
                        <div className="flex items-center justify-between text-[11px] text-muted-foreground px-1">
                          <span>
                            {editedContent.length.toLocaleString()} characters • {editedContent.split(/\s+/).filter(Boolean).length.toLocaleString()} words
                          </span>
                          <span className="font-mono">content/{activeFileDetail?.subjectSlug}/{activeFileDetail?.fileSlug}.md</span>
                        </div>
                      </div>
                    )}

                    {/* Live Preview */}
                    {(editViewMode === 'preview' || editViewMode === 'split') && (
                      <div className={editViewMode === 'split' ? 'md:col-span-6' : 'md:col-span-12'}>
                        <div className="h-[calc(100vh-380px)] min-h-[480px] p-6 rounded-xl border border-border bg-card overflow-y-auto">
                          <div className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-4 border-b border-border pb-2 flex items-center justify-between">
                            <span>Live Markdown Preview</span>
                            <span className="text-[10px] text-primary font-medium">Auto-rendered</span>
                          </div>
                          <MarkdownRenderer content={editedContent} />
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              ) : (
                /* ================= READ MODE ================= */
                <div
                  className={`p-6 sm:p-8 space-y-6 overflow-x-hidden ${
                    fontSize === 'sm'
                      ? 'text-xs sm:text-sm leading-relaxed'
                      : fontSize === 'lg'
                      ? 'text-base sm:text-lg leading-loose'
                      : 'text-sm sm:text-base leading-relaxed'
                  }`}
                >
                  {contentLoading ? (
                    <div className="py-20 text-center space-y-3">
                      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary mx-auto" />
                      <p className="text-sm text-muted-foreground">Loading revision note...</p>
                    </div>
                  ) : activeFileDetail?.content ? (
                    <>
                      <MarkdownRenderer content={activeFileDetail.content} />

                      {/* Quick Append Box at Bottom of Note */}
                      <div className="mt-10 pt-6 border-t border-border">
                        <div className="bg-muted/20 border border-border/80 rounded-xl p-4 sm:p-5 space-y-3">
                          <div className="flex items-center justify-between">
                            <div className="flex items-center space-x-2">
                              <PlusCircle className="h-4 w-4 text-primary" />
                              <span className="text-xs font-bold text-foreground">
                                Quick Append: Add Notes to {activeFileDetail.fileSlug}.md
                              </span>
                            </div>
                            <button
                              onClick={() => {
                                setIsEditing(true);
                                setEditedContent(activeFileDetail.content);
                              }}
                              className="text-xs text-primary hover:underline flex items-center space-x-1"
                            >
                              <Edit3 className="h-3 w-3" />
                              <span>Full Editor</span>
                            </button>
                          </div>
                          <textarea
                            value={quickAppendText}
                            onChange={(e) => setQuickAppendText(e.target.value)}
                            placeholder="Quickly type or paste interview questions, notes, code snippets, or formulas to append directly to this file..."
                            rows={3}
                            className="w-full p-3 rounded-lg border border-border bg-background text-xs sm:text-sm font-mono leading-relaxed focus:outline-none focus:ring-2 focus:ring-primary/40 resize-y"
                          />
                          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                            <span className="text-[11px] text-muted-foreground">
                              Appends markdown content directly to <code className="text-primary font-mono">{activeFileDetail.fileSlug}.md</code>.
                            </span>
                            <button
                              type="button"
                              onClick={handleQuickAppend}
                              disabled={isSaving || !quickAppendText.trim()}
                              className="flex items-center justify-center space-x-1.5 px-3.5 py-1.5 rounded-lg bg-primary hover:bg-primary/90 text-primary-foreground text-xs font-semibold transition-all disabled:opacity-50 shrink-0"
                            >
                              {isSaving ? (
                                <>
                                  <div className="animate-spin rounded-full h-3 w-3 border-b-2 border-white" />
                                  <span>Saving...</span>
                                </>
                              ) : (
                                <>
                                  <Plus className="h-3.5 w-3.5" />
                                  <span>Append & Save</span>
                                </>
                              )}
                            </button>
                          </div>
                        </div>
                      </div>
                    </>
                  ) : (
                    <div className="py-20 text-center text-sm text-muted-foreground">
                      Select a note module from the left sidebar to view its full revision contents.
                    </div>
                  )}
                </div>
              )}
            </div>
          )}
        </main>

        {/* Right Column: Table of Contents & Navigation (3 Cols, Sticky) */}
        <aside className="hidden xl:block xl:col-span-3 space-y-4">
          <div className="sticky top-24 space-y-4">
            <div className="bg-card border border-border rounded-2xl p-4 shadow-sm space-y-3">
              <div className="flex items-center justify-between border-b border-border pb-2.5">
                <div className="flex items-center space-x-2 text-xs font-bold uppercase tracking-wider text-muted-foreground">
                  <List className="h-3.5 w-3.5 text-primary" />
                  <span>On This Page</span>
                </div>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-muted text-muted-foreground">
                  {activeFileDetail?.headings?.length || 0} sections
                </span>
              </div>

              {/* Headings List */}
              <div className="space-y-1 max-h-[calc(100vh-260px)] overflow-y-auto pr-1">
                {activeFileDetail?.headings && activeFileDetail.headings.length > 0 ? (
                  activeFileDetail.headings.map((h, idx) => (
                    <button
                      key={idx}
                      onClick={() => scrollToHeading(h.slug)}
                      className={`block w-full text-left text-xs py-1.5 px-2 rounded-lg transition-colors text-muted-foreground hover:text-foreground hover:bg-muted truncate ${
                        h.level === 1
                          ? 'font-bold text-foreground'
                          : h.level === 2
                          ? 'pl-3 font-medium'
                          : 'pl-5 text-[11px] opacity-80'
                      }`}
                      title={h.title}
                    >
                      {h.title}
                    </button>
                  ))
                ) : (
                  <p className="text-xs text-muted-foreground italic py-4">
                    No section headings in this note.
                  </p>
                )}
              </div>

              {/* Back to top */}
              <div className="border-t border-border pt-2.5">
                <button
                  onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
                  className="w-full flex items-center justify-center space-x-1.5 py-1.5 rounded-lg text-xs font-medium text-muted-foreground hover:text-foreground hover:bg-muted transition-colors"
                >
                  <ArrowUp className="h-3.5 w-3.5" />
                  <span>Back to Top</span>
                </button>
              </div>
            </div>
          </div>
        </aside>
      </div>

      {/* ================= CREATE NEW NOTE MODAL ================= */}
      {isNewNoteModalOpen && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-card border border-border rounded-2xl w-full max-w-2xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-200">
            <div className="p-4 sm:p-5 border-b border-border flex items-center justify-between bg-muted/30">
              <div className="space-y-0.5">
                <div className="flex items-center space-x-2">
                  <PlusCircle className="h-4 w-4 text-primary" />
                  <h3 className="text-base font-bold text-foreground">Add New Revision Note (.md)</h3>
                </div>
                <p className="text-xs text-muted-foreground">
                  Create a new markdown note file that saves directly into its course folder.
                </p>
              </div>
              <button
                onClick={() => setIsNewNoteModalOpen(false)}
                className="text-muted-foreground hover:text-foreground p-1 rounded-lg hover:bg-muted"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            <form onSubmit={handleCreateNote} className="p-5 space-y-4 overflow-y-auto flex-1">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="space-y-1.5">
                  <label className="text-xs font-semibold text-foreground">Course / Tab</label>
                  <select
                    value={newNoteSubject}
                    onChange={(e) => setNewNoteSubject(e.target.value)}
                    className="w-full px-3 py-2 rounded-xl border border-border bg-background text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-primary/40"
                  >
                    {tree.map((sub) => (
                      <option key={sub.subjectSlug} value={sub.subjectSlug}>
                        {sub.subjectName}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="space-y-1.5">
                  <label className="text-xs font-semibold text-foreground">Note Title</label>
                  <input
                    type="text"
                    value={newNoteTitle}
                    onChange={(e) => {
                      setNewNoteTitle(e.target.value);
                      if (!newNoteSlug || newNoteSlug === newNoteTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')) {
                        setNewNoteSlug(e.target.value.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, ''));
                      }
                    }}
                    placeholder="e.g. Transformers & Self Attention"
                    required
                    className="w-full px-3 py-2 rounded-xl border border-border bg-background text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-primary/40"
                  />
                </div>
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-semibold text-foreground">
                  File Slug (.md file name)
                </label>
                <div className="flex items-center">
                  <span className="px-3 py-2 rounded-l-xl border border-r-0 border-border bg-muted text-xs text-muted-foreground font-mono">
                    content/{newNoteSubject}/
                  </span>
                  <input
                    type="text"
                    value={newNoteSlug}
                    onChange={(e) => setNewNoteSlug(e.target.value.toLowerCase().replace(/[^a-z0-9_-]/g, ''))}
                    placeholder="e.g. transformers-self-attention"
                    required
                    className="flex-1 px-3 py-2 border border-border bg-background text-xs sm:text-sm font-mono focus:outline-none focus:ring-2 focus:ring-primary/40"
                  />
                  <span className="px-3 py-2 rounded-r-xl border border-l-0 border-border bg-muted text-xs text-muted-foreground font-mono">
                    .md
                  </span>
                </div>
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-semibold text-foreground">
                  Initial Content (Markdown format)
                </label>
                <textarea
                  value={newNoteContent}
                  onChange={(e) => setNewNoteContent(e.target.value)}
                  placeholder="# Note Title\n\nWrite your concepts, explanations, formulas, or code examples..."
                  rows={8}
                  className="w-full p-3 rounded-xl border border-border bg-background text-xs sm:text-sm font-mono leading-relaxed focus:outline-none focus:ring-2 focus:ring-primary/40"
                />
              </div>

              <div className="pt-2 border-t border-border flex items-center justify-end space-x-2">
                <button
                  type="button"
                  onClick={() => setIsNewNoteModalOpen(false)}
                  className="px-4 py-2 rounded-xl border border-border bg-background hover:bg-muted text-xs font-medium text-foreground transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={isCreatingNote}
                  className="flex items-center space-x-1.5 px-4 py-2 rounded-xl bg-primary hover:bg-primary/90 text-primary-foreground text-xs font-semibold shadow-sm transition-all disabled:opacity-50"
                >
                  {isCreatingNote ? (
                    <>
                      <div className="animate-spin rounded-full h-3.5 w-3.5 border-b-2 border-white" />
                      <span>Creating...</span>
                    </>
                  ) : (
                    <>
                      <Plus className="h-3.5 w-3.5" />
                      <span>Create & Save .md File</span>
                    </>
                  )}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
