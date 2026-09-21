import Link from 'next/link';
import Image from 'next/image';
import { Heart } from 'lucide-react';

export function Footer() {
  return (
    <footer className="border-t border-border bg-card/40 mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="space-y-3">
            <div className="flex items-center space-x-2">
              <Image
                src="/images/small_logo.png"
                alt="learni logo"
                width={28}
                height={28}
                className="object-contain"
              />
              <span className="font-extrabold text-xl tracking-tight text-foreground lowercase">
                learn<span className="text-[#ec4899]">i</span>
              </span>
            </div>
            <p className="text-xs text-muted-foreground leading-relaxed">
              A simple, interactive learning space with structured courses to help you understand, revise, and grow at your own pace.
            </p>
          </div>

          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-foreground mb-3">
              Curriculum
            </h4>
            <ul className="space-y-2 text-xs text-muted-foreground">
              <li>
                <Link href="/courses/dsa" className="hover:text-primary transition-colors">
                  Data Structures & Algorithms
                </Link>
              </li>
              <li>
                <Link href="/courses/machine-learning" className="hover:text-primary transition-colors">
                  Machine Learning
                </Link>
              </li>
              <li>
                <Link href="/courses/deep-learning" className="hover:text-primary transition-colors">
                  Deep Learning
                </Link>
              </li>
              <li>
                <Link href="/courses/sql" className="hover:text-primary transition-colors">
                  SQL & Databases
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-foreground mb-3">
              Modern AI
            </h4>
            <ul className="space-y-2 text-xs text-muted-foreground">
              <li>
                <Link href="/courses/mongodb" className="hover:text-primary transition-colors">
                  MongoDB & NoSQL
                </Link>
              </li>
              <li>
                <Link href="/courses/llm" className="hover:text-primary transition-colors">
                  Large Language Models
                </Link>
              </li>
              <li>
                <Link href="/courses/generative-ai" className="hover:text-primary transition-colors">
                  Generative AI & RAG
                </Link>
              </li>
              <li>
                <Link href="/courses/agentic-ai" className="hover:text-primary transition-colors">
                  Autonomous Agentic AI
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-foreground mb-3">
              Platform
            </h4>
            <p className="text-xs text-muted-foreground leading-relaxed">
              All learning material is 100% free. Master DSA, Machine Learning, SQL, and Agentic AI at your own pace.
            </p>
            <div className="mt-4 flex items-center space-x-1 text-xs text-muted-foreground">
              <span>Crafted with</span>
              <Heart className="h-3.5 w-3.5 text-red-500 fill-red-500 inline" />
              <span>for curious learners.</span>
            </div>
          </div>
        </div>

        <div className="mt-8 pt-6 border-t border-border flex flex-col sm:flex-row items-center justify-between text-xs text-muted-foreground">
          <p>© {new Date().getFullYear()} learni. All rights reserved.</p>
          <div className="flex space-x-4 mt-2 sm:mt-0">
            <span className="hover:text-foreground cursor-pointer">Privacy</span>
            <span className="hover:text-foreground cursor-pointer">Terms</span>
            <span className="hover:text-foreground cursor-pointer">Security</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
