import { createContext, useContext, useState, useCallback, type ReactNode } from 'react';

interface AutoPlayContextType {
    isAutoPlay: boolean;
    startAutoPlay: () => void;
    stopAutoPlay: () => void;
    // Used by manager to tell SituasiPerjalanan to start its sequence
    situasiReady: boolean;
    setSituasiReady: (ready: boolean) => void;
    // Used by SituasiPerjalanan to tell manager it's done cycling scenarios
    situasiDone: boolean;
    setSituasiDone: (done: boolean) => void;
}

const AutoPlayContext = createContext<AutoPlayContextType | undefined>(undefined);

export function AutoPlayProvider({ children }: { children: ReactNode }) {
    const [isAutoPlay, setIsAutoPlay] = useState(false);
    const [situasiReady, setSituasiReady] = useState(false);
    const [situasiDone, setSituasiDone] = useState(false);

    const startAutoPlay = useCallback(() => {
        setIsAutoPlay(true);
        setSituasiReady(false);
        setSituasiDone(false);
    }, []);

    const stopAutoPlay = useCallback(() => {
        setIsAutoPlay(false);
        setSituasiReady(false);
        setSituasiDone(false);
    }, []);

    return (
        <AutoPlayContext.Provider
            value={{
                isAutoPlay,
                startAutoPlay,
                stopAutoPlay,
                situasiReady,
                setSituasiReady,
                situasiDone,
                setSituasiDone,
            }}
        >
            {children}
        </AutoPlayContext.Provider>
    );
}

export function useAutoPlay() {
    const context = useContext(AutoPlayContext);
    if (context === undefined) {
        throw new Error('useAutoPlay must be used within an AutoPlayProvider');
    }
    return context;
}
