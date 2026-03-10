import { useEffect, useRef } from 'react';
import { gsap } from 'gsap';
import { ScrollToPlugin } from 'gsap/ScrollToPlugin';
import { useAutoPlay } from '../hooks/AutoPlayContext';

gsap.registerPlugin(ScrollToPlugin);

export default function AutoPlayManager() {
    const { isAutoPlay, stopAutoPlay, setSituasiReady, situasiDone } = useAutoPlay();
    const tlRef = useRef<gsap.core.Timeline | null>(null);

    useEffect(() => {
        if (!isAutoPlay) {
            if (tlRef.current) tlRef.current.kill();
            // Only unlock scroll if not animating natively by other features, or we just leave it default
            document.body.style.overflow = '';
            return;
        }

        // Scroll back to top immediately before animating
        window.scrollTo({ top: 0, behavior: 'auto' });
        document.body.style.overflow = 'hidden'; // Optional: Lock manual scroll during autoplay

        const tl = gsap.timeline({
            onComplete: () => {
                stopAutoPlay();
            },
        });

        tlRef.current = tl;

        // Timeline steps for the main page

        // 1. Scroll safely down past Hero
        tl.to(window, {
            scrollTo: 0, // start top
            duration: 1,
        });

        // 2. Scroll into 3 MIM pin section slowly
        tl.to(window, {
            scrollTo: '#tiga-mim-container',
            duration: 2.5,
            ease: 'power2.inOut',
        });

        // Calculate total horizontal scroll distance for 3 MIM (it's pinned for 4 viewport heights)
        const mimDistance = window.innerHeight * 4;
        tl.to(window, {
            scrollTo: { y: `+=${mimDistance}`, autoKill: false },
            duration: 12, // slow tour through the 3 cards
            ease: 'none',
        });

        // 3. Scroll to Tempoh map section
        tl.to(window, {
            scrollTo: { y: '#tempoh', offsetY: 0, autoKill: false },
            duration: 3,
            ease: 'power2.inOut',
        });
        tl.to({}, { duration: 2.5 }); // pause to read

        // 4. Scroll to Situasi Perjalanan
        tl.to(window, {
            scrollTo: { y: '#situasi-perjalanan', offsetY: 0, autoKill: false },
            duration: 3,
            ease: 'power2.inOut',
            onComplete: () => {
                // Now trigger the Situasi section's internal scenarios
                setSituasiReady(true);
            }
        });

        // Pause the scroll timeline here; it will resume when situasiDone = true
        tl.addPause();

        // 5. Scroll to QA
        tl.to(window, {
            scrollTo: { y: '#qa', offsetY: 0, autoKill: false },
            duration: 3,
            ease: 'power2.inOut',
        });
        tl.to({}, { duration: 3 }); // pause to read

        // 6. Scroll to Closing
        tl.to(window, {
            scrollTo: { y: '#closing', offsetY: 0, autoKill: false },
            duration: 3,
            ease: 'power2.inOut',
        });
        tl.to({}, { duration: 2 }); // pause

        return () => {
            tl.kill();
            document.body.style.overflow = '';
        };
    }, [isAutoPlay, setSituasiReady, stopAutoPlay]);

    // Handle resuming when Situasi is done
    useEffect(() => {
        if (isAutoPlay && situasiDone && tlRef.current) {
            tlRef.current.play(); // Resume scrolling
        }
    }, [isAutoPlay, situasiDone]);

    if (!isAutoPlay) return null;

    return (
        <div style={{ position: 'fixed', top: 20, right: 20, zIndex: 9999 }}>
            <button
                onClick={stopAutoPlay}
                style={{
                    background: 'rgba(212,175,55,0.1)',
                    border: '1px solid rgba(212,175,55,0.6)',
                    backdropFilter: 'blur(8px)',
                    color: '#D4AF37',
                    padding: '10px 24px',
                    borderRadius: 30,
                    fontWeight: 600,
                    fontSize: '0.8rem',
                    letterSpacing: '0.1em',
                    cursor: 'pointer',
                    boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
                    transition: 'all 0.2s ease',
                }}
                onMouseEnter={e => {
                    (e.currentTarget as HTMLButtonElement).style.background = 'rgba(212,175,55,0.2)';
                }}
                onMouseLeave={e => {
                    (e.currentTarget as HTMLButtonElement).style.background = 'rgba(212,175,55,0.1)';
                }}
            >
                ⏹ BERHENTI ANIMASI
            </button>
        </div>
    );
}
