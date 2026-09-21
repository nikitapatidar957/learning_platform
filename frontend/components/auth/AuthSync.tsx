'use client';

import * as React from 'react';
import { useAuth, useUser } from '@clerk/nextjs';
import { syncUserWithBackend } from '@/lib/api';

export function AuthSync() {
  const { isSignedIn, isLoaded, getToken } = useAuth();
  const { user } = useUser();
  const syncedUserIdRef = React.useRef<string | null>(null);

  React.useEffect(() => {
    if (!isLoaded) return;

    if (!isSignedIn || !user) {
      if (typeof window !== 'undefined') {
        localStorage.removeItem('clerk_user_id');
      }
      syncedUserIdRef.current = null;
      return;
    }

    // Prevent duplicate sync calls in the same session
    if (syncedUserIdRef.current === user.id) return;

    let isMounted = true;

    const performSync = async () => {
      try {
        const token = await getToken();
        if (!isMounted) return;

        const email = user.primaryEmailAddress?.emailAddress || '';
        const name =
          user.fullName ||
          (user.firstName ? `${user.firstName} ${user.lastName || ''}`.trim() : 'Learner');
        const profileImage = user.imageUrl || '';

        await syncUserWithBackend(
          {
            clerk_user_id: user.id,
            email,
            name,
            profile_image: profileImage,
          },
          token
        );

        syncedUserIdRef.current = user.id;
        console.log(`[learni] Synced user ${user.id} (${name}) with MongoDB.`);
      } catch (error) {
        console.error('[learni] Failed to sync user with MongoDB:', error);
      }
    };

    performSync();

    return () => {
      isMounted = false;
    };
  }, [isLoaded, isSignedIn, user, getToken]);

  return null;
}
