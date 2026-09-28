'use client';

import * as React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { usePathname } from 'next/navigation';
import {
  BookOpen,
  LayoutDashboard,
  Search,
  Menu,
  X,
  Sparkles,
  User,
  GraduationCap,
} from 'lucide-react';
import {
  SignedIn,
  SignedOut,
  SignInButton,
  SignUpButton,
  UserButton,
} from '@clerk/nextjs';
import { ThemeToggle } from './ThemeToggle';
import { SearchDialog } from '@/components/search/SearchDialog';
import { Button } from '@/components/ui/Button';

export function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = React.useState(false);
  const [searchOpen, setSearchOpen] = React.useState(false);
  const pathname = usePathname();

  const navLinks = [
    { label: 'Home', href: '/' },
    { label: 'Courses', href: '/courses' },
    { label: 'Dashboard', href: '/dashboard', authRequired: true },
  ];

  const isActive = (href: string) => {
    if (href === '/' && pathname === '/') return true;
    if (href !== '/' && pathname?.startsWith(href)) return true;
    return false;
  };

  return (
    <>
      <header className="sticky top-0 z-40 w-full border-b border-border/80 bg-background/80 backdrop-blur-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2.5 group">
            <div className="relative h-9 w-9 flex items-center justify-center group-hover:scale-105 transition-transform">
              <Image
                src="/images/small_logo.png"
                alt="learni logo"
                width={36}
                height={36}
                className="object-contain"
                priority
              />
            </div>
            <div className="flex items-center">
              <span className="font-extrabold text-2xl tracking-tight text-foreground lowercase">
                learn<span className="text-[#ec4899]">i</span>
              </span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-8">
            <Link
              href="/"
              className={`relative py-1 text-sm font-medium transition-colors ${
                isActive('/')
                  ? 'text-primary font-bold after:absolute after:-bottom-2 after:left-1/2 after:-translate-x-1/2 after:w-6 after:h-[2.5px] after:bg-primary after:rounded-full'
                  : 'text-muted-foreground hover:text-foreground'
              }`}
            >
              Home
            </Link>
            <Link
              href="/courses"
              className={`relative py-1 text-sm font-medium transition-colors ${
                isActive('/courses')
                  ? 'text-primary font-bold after:absolute after:-bottom-2 after:left-1/2 after:-translate-x-1/2 after:w-6 after:h-[2.5px] after:bg-primary after:rounded-full'
                  : 'text-muted-foreground hover:text-foreground'
              }`}
            >
              Courses
            </Link>
            <Link
              href="/revision"
              className={`relative py-1 text-sm font-medium transition-colors flex items-center space-x-1.5 ${
                isActive('/revision')
                  ? 'text-primary font-bold after:absolute after:-bottom-2 after:left-1/2 after:-translate-x-1/2 after:w-6 after:h-[2.5px] after:bg-primary after:rounded-full'
                  : 'text-muted-foreground hover:text-foreground'
              }`}
            >
              <span>Revision Hub</span>
              <span className="px-1.5 py-0.2 rounded-full text-[10px] font-bold bg-primary/15 text-primary border border-primary/20">
                Verbatim
              </span>
            </Link>
            <Link
              href="/#playground"
              className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
            >
              Playgrounds
            </Link>
            <SignedIn>
              <Link
                href="/dashboard"
                className={`relative py-1 text-sm font-medium transition-colors ${
                  isActive('/dashboard')
                    ? 'text-primary font-bold after:absolute after:-bottom-2 after:left-1/2 after:-translate-x-1/2 after:w-6 after:h-[2.5px] after:bg-primary after:rounded-full'
                    : 'text-muted-foreground hover:text-foreground'
                }`}
              >
                Dashboard
              </Link>
            </SignedIn>
          </nav>

          {/* Right Actions */}
          <div className="flex items-center space-x-2 sm:space-x-3">
            {/* Global Search Button (Circle icon matching reference) */}
            <button
              onClick={() => setSearchOpen(true)}
              className="h-9 w-9 rounded-full border border-border/80 bg-card/60 hover:bg-muted text-muted-foreground hover:text-foreground flex items-center justify-center transition-colors shadow-sm"
              aria-label="Search curriculum"
            >
              <Search className="h-4 w-4" />
            </button>

            {/* Theme Toggle */}
            <ThemeToggle />

            {/* Auth States */}
            <div className="flex items-center">
              <SignedIn>
                <div className="flex items-center space-x-2">
                  <UserButton
                    afterSignOutUrl="/"
                    appearance={{
                      elements: {
                        avatarBox: 'w-8 h-8 rounded-full',
                      },
                    }}
                  />
                </div>
              </SignedIn>

              <SignedOut>
                <div className="hidden sm:flex items-center space-x-2">
                  <SignInButton mode="modal">
                    <button className="px-4 py-2 text-sm font-semibold text-foreground/80 hover:text-foreground rounded-full transition-colors">
                      Log in
                    </button>
                  </SignInButton>
                  <SignUpButton mode="modal">
                    <button className="px-5 py-2 text-sm font-semibold text-white bg-[#5046e5] hover:bg-[#4338ca] rounded-full shadow-md shadow-indigo-500/25 hover:shadow-indigo-500/40 transition-all hover:scale-[1.02] active:scale-[0.98]">
                      Get Started
                    </button>
                  </SignUpButton>
                </div>
                <div className="sm:hidden">
                  <SignInButton mode="modal">
                    <button className="px-3.5 py-1.5 text-xs font-semibold text-white bg-[#5046e5] rounded-full shadow-md">
                      Log in
                    </button>
                  </SignInButton>
                </div>
              </SignedOut>
            </div>

            {/* Mobile menu trigger */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 rounded-lg text-muted-foreground hover:text-foreground hover:bg-muted"
            >
              {mobileMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
            </button>
          </div>
        </div>

        {/* Mobile Dropdown */}
        {mobileMenuOpen && (
          <div className="md:hidden border-b border-border bg-background p-4 space-y-3 animate-fade-in">
            <Link
              href="/"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-muted"
            >
              Home
            </Link>
            <Link
              href="/courses"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-muted"
            >
              Courses
            </Link>
            <Link
              href="/revision"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-muted text-primary font-semibold"
            >
              Revision Hub (All Concepts)
            </Link>
            <SignedIn>
              <Link
                href="/dashboard"
                onClick={() => setMobileMenuOpen(false)}
                className="block px-3 py-2 rounded-lg text-sm font-medium hover:bg-muted"
              >
                Dashboard
              </Link>
            </SignedIn>
          </div>
        )}

      </header>

      {/* Global Search Dialog */}
      <SearchDialog isOpen={searchOpen} onClose={() => setSearchOpen(false)} />
    </>
  );
}
