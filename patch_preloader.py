import sys

filepath = 'c:/Users/dd/Desktop/app/src/components/AnimationPreloader.tsx'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update imports
content = content.replace(
    \"Sparkles, Heart, Coffee } from 'lucide-react';\",
    \"Sparkles, Heart, Building2, Briefcase } from 'lucide-react';\"
)

# 2. Add refs
refs_str = '''    const slide1Ref = useRef<HTMLDivElement>(null); // Tiga Mim
    const slide1MastautinRef = useRef<HTMLDivElement>(null);
    const slide1MukimRef = useRef<HTMLDivElement>(null);
    const slide1MusafirRef = useRef<HTMLDivElement>(null);
    const audioMastautinRef = useRef<HTMLAudioElement>(null);
    const audioMukimRef = useRef<HTMLAudioElement>(null);
    const audioMusafirRef = useRef<HTMLAudioElement>(null);'''
content = content.replace(
    \"    const slide1Ref = useRef<HTMLDivElement>(null); // Tiga Mim\",
    refs_str
)

# 3. Add to slides array
content = content.replace(
    \"const slides = [slide0Ref, slide1Ref, slide2Ref, slide345Ref, slide6Ref, slide7Ref];\",
    \"const slides = [slide0Ref, slide1Ref, slide1MastautinRef, slide1MukimRef, slide1MusafirRef, slide2Ref, slide345Ref, slide6Ref, slide7Ref];\"
)

# 4. Add timeline blocks
tl_blocks = '''        hideSlide(slide1Ref, 2.0);

        // --- SLIDE 1A: MASTAUTIN CLONE ---
        showSlide(slide1MastautinRef, 0.5);
        const masHdr = slide1MastautinRef.current?.querySelector('.mas-hdr');
        const masDesc = slide1MastautinRef.current?.querySelector('.mas-desc');
        const masImg = slide1MastautinRef.current?.querySelector('.mas-img');
        const concentricCircles = slide1MastautinRef.current?.querySelectorAll('.concentric-circle');
        tl.add(() => { if (audioMastautinRef.current) audioMastautinRef.current.play().catch(()=>{}); }, '<');
        if (concentricCircles) tl.fromTo(concentricCircles, { scale: 0, opacity: 0 }, { scale: 1, opacity: 0.15, stagger: 0.15, duration: 0.8 }, '<');
        if (masImg) tl.fromTo(masImg, { y: 50, scale: 0.8, opacity: 0 }, { y: 0, scale: 1, opacity: 1, duration: 0.7, ease: 'back.out(1.7)' }, '<+0.2');
        if (masHdr) tl.fromTo(masHdr, { y: -30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5 }, '<+0.2');
        if (masDesc) tl.fromTo(masDesc, { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4 }, '<+0.3');
        hideSlide(slide1MastautinRef, 6.0);

        // --- SLIDE 1B: MUKIM CLONE ---
        showSlide(slide1MukimRef, 0.5);
        const mukHdr = slide1MukimRef.current?.querySelector('.muk-hdr');
        const mukDesc = slide1MukimRef.current?.querySelector('.muk-desc');
        const mukImg = slide1MukimRef.current?.querySelector('.muk-img');
        tl.add(() => { if (audioMukimRef.current) audioMukimRef.current.play().catch(()=>{}); }, '<');
        if (mukHdr) tl.fromTo(mukHdr, { x: -50, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6 }, '<');
        if (mukImg) tl.fromTo(mukImg, { x: 50, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6 }, '<');
        if (mukDesc) tl.fromTo(mukDesc, { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5 }, '<+0.3');
        hideSlide(slide1MukimRef, 6.0);

        // --- SLIDE 1C: MUSAFIR CLONE ---
        showSlide(slide1MusafirRef, 0.5);
        const musHdr = slide1MusafirRef.current?.querySelector('.mus-hdr');
        const musDesc = slide1MusafirRef.current?.querySelector('.mus-desc');
        const musImg = slide1MusafirRef.current?.querySelector('.mus-img');
        const musPath = slide1MusafirRef.current?.querySelector('.mus-path');
        tl.add(() => { if (audioMusafirRef.current) audioMusafirRef.current.play().catch(()=>{}); }, '<');
        if (musHdr) tl.fromTo(musHdr, { x: -50, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6 }, '<');
        if (musImg) tl.fromTo(musImg, { x: 50, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6 }, '<');
        if (musDesc) tl.fromTo(musDesc, { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5 }, '<+0.3');
        if (musPath) {
            tl.fromTo(musPath, { strokeDashoffset: 1000 }, { strokeDashoffset: 0, duration: 1.5, ease: 'power2.out' }, '<+0.5');
        }
        hideSlide(slide1MusafirRef, 6.0);'''
content = content.replace(
    \"        hideSlide(slide1Ref, 2.0);\",
    tl_blocks
)

# 5. Handle Skip
skip_logic = '''    const handleSkip = () => {
        tlRef.current?.progress(1);
        [audioMastautinRef, audioMukimRef, audioMusafirRef].forEach(ref => {
            if (ref.current) {
                ref.current.pause();
                ref.current.currentTime = 0;
            }
        });
    };'''
content = content.replace(
    '''    const handleSkip = () => {
        tlRef.current?.progress(1);
    };''',
    skip_logic
)

# 6. Add JSX
jsx_blocks = '''            {/* ---------------- SLIDE 1A: MASTAUTIN EXACT CLONE ---------------- */}
            <div ref={slide1MastautinRef} className="absolute inset-0 flex items-center justify-center p-4 sm:p-8 text-black opacity-0 pointer-events-none" style={{ backgroundColor: '#f0faf7' }}>
                <audio ref={audioMastautinRef} src="/mastautin.mp4" preload="auto" />
                <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
                    {[...Array(3)].map((_, i) => (
                        <div key={i} className="concentric-circle absolute rounded-full border-2 border-teal/20" style={{ width: f"{300 + i * 150}px", height: f"{300 + i * 150}px" }} />
                    ))}
                </div>
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center max-w-6xl w-full z-10">
                    <div className="mas-img relative flex justify-center">
                        <div className="relative rounded-3xl overflow-hidden shadow-2xl max-w-sm lg:max-w-md">
                            <img src="/mastautin-illustration.jpg" alt="Mastautin" className="w-full h-auto" />
                        </div>
                        <div className="absolute -bottom-4 -right-4 w-16 h-16 bg-teal rounded-full flex items-center justify-center shadow-glow-teal"><Home className="w-8 h-8 text-white" /></div>
                    </div>
                    <div className="text-center lg:text-left">
                        <div className="mas-hdr">
                            <h2 className="text-4xl sm:text-5xl md:text-7xl font-display font-bold text-teal mb-2 lg:mb-4">MASTAUTIN</h2>
                            <p className="text-lg sm:text-xl text-gold font-display mb-4 lg:mb-8">Tempat Tinggal Tetap</p>
                        </div>
                        <div className="mas-desc">
                            <p className="text-base sm:text-xl text-gray-700 leading-relaxed mb-6 lg:mb-8">Mastautin ialah <span className="font-semibold text-teal">tempat tinggal tetap</span> seseorang yang menjadi pusat kehidupan dan aktiviti harian.</p>
                            <div className="flex flex-wrap justify-center lg:justify-start gap-4">
                                <div className="flex items-center gap-2 bg-white px-4 py-3 rounded-xl shadow-card"><Building2 className="w-5 h-5 text-teal" /><span className="text-gray-700 font-medium text-sm sm:text-base">Rumah sendiri</span></div>
                                <div className="flex items-center gap-2 bg-white px-4 py-3 rounded-xl shadow-card"><Briefcase className="w-5 h-5 text-teal" /><span className="text-gray-700 font-medium text-sm sm:text-base">Tempat kerja tetap</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* ---------------- SLIDE 1B: MUKIM EXACT CLONE ---------------- */}
            <div ref={slide1MukimRef} className="absolute inset-0 flex items-center justify-center p-4 sm:p-8 text-black opacity-0 pointer-events-none" style={{ background: 'linear-gradient(135deg, #ffffff 0%, #f0faf7 100%)' }}>
                <audio ref={audioMukimRef} src="/mukim.mp4" preload="auto" />
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center max-w-6xl w-full z-10">
                    <div className="muk-hdr order-2 lg:order-1 text-center lg:text-left">
                        <h2 className="text-4xl sm:text-5xl md:text-7xl font-display font-bold text-teal mb-2 lg:mb-4">MUKIM</h2>
                        <p className="text-lg sm:text-xl text-gold font-display mb-4 lg:mb-8">Tinggal Sementara</p>
                        <div className="muk-desc">
                            <p className="text-base sm:text-lg text-gray-700 leading-relaxed mb-6 lg:mb-8">Mukim bermaksud tinggal dan menetap di sesuatu tempat <span className="font-semibold text-teal">lebih dari tiga hari</span>, tetapi tidak berniat untuk menjadikannya tempat tinggal tetap selamanya.</p>
                            <div className="inline-flex items-center gap-4 bg-gradient-to-r from-teal to-teal-light rounded-2xl p-4 sm:p-6 shadow-glow-teal text-left">
                                <div className="w-16 h-16 sm:w-20 sm:h-20 rounded-full bg-white/20 flex items-center justify-center"><span className="text-3xl sm:text-5xl font-display font-bold text-white">3</span></div>
                                <div><p className="text-2xl sm:text-3xl font-display font-bold text-white">&gt; 3 Hari</p><p className="text-white/80 text-xs sm:text-sm">Tempoh minimum untuk dianggap mukim</p></div>
                            </div>
                        </div>
                    </div>
                    <div className="muk-img order-1 lg:order-2 relative flex justify-center">
                        <div className="relative rounded-3xl overflow-hidden shadow-2xl max-w-sm lg:max-w-md">
                            <img src="/mukim-illustration.jpg" alt="Mukim" className="w-full h-auto" />
                        </div>
                        <div className="absolute -bottom-6 -left-6 w-16 h-16 sm:w-20 sm:h-20 bg-white rounded-2xl shadow-card flex items-center justify-center"><CalendarDays className="w-8 h-8 sm:w-10 sm:h-10 text-teal" /></div>
                    </div>
                </div>
            </div>

            {/* ---------------- SLIDE 1C: MUSAFIR EXACT CLONE ---------------- */}
            <div ref={slide1MusafirRef} className="absolute inset-0 flex items-center justify-center p-4 sm:p-8 text-black opacity-0 pointer-events-none" style={{ background: 'linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%)' }}>
                <audio ref={audioMusafirRef} src="/musafir.mp4" preload="auto" />
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center max-w-6xl w-full z-10">
                    <div className="mus-hdr order-2 lg:order-1 text-center lg:text-left">
                        <h2 className="text-4xl sm:text-5xl md:text-7xl font-display font-bold text-teal mb-2 lg:mb-4">MUSAFIR</h2>
                        <p className="text-lg sm:text-xl text-gold font-display mb-4 lg:mb-8">Dalam Perjalanan</p>
                        <div className="mus-desc">
                            <p className="text-base sm:text-lg text-gray-700 leading-relaxed mb-6 lg:mb-8">Musafir ialah seseorang yang melakukan perjalanan melebihi <span className="font-semibold text-teal">dua marhalah</span> atau <span className="font-semibold text-teal">81 kilometer</span>.</p>
                            <div className="inline-flex items-center gap-4 sm:gap-6 bg-gradient-to-r from-gold to-gold-light rounded-2xl p-4 sm:p-6 shadow-glow-gold mb-8 text-left">
                                <div className="w-16 h-16 sm:w-24 sm:h-24 rounded-full bg-white/30 flex items-center justify-center"><Navigation className="w-8 h-8 sm:w-12 sm:h-12 text-white" /></div>
                                <div><p className="text-3xl sm:text-5xl font-display font-bold text-white">= 81</p><p className="text-white/90 text-sm sm:text-lg font-semibold">KM</p><p className="text-white/70 text-xs sm:text-sm mt-1">Jarak minimum untuk menjadi musafir</p></div>
                            </div>
                        </div>
                    </div>
                    <div className="mus-img order-1 lg:order-2 relative flex justify-center flex-col">
                        <div className="relative rounded-3xl overflow-hidden shadow-2xl max-w-sm lg:max-w-md">
                            <img src="/musafir-illustration.jpg" alt="Musafir" className="w-full h-auto" />
                        </div>
                        <div className="absolute -bottom-4 -right-4 w-16 h-16 sm:w-20 sm:h-20 bg-teal rounded-full flex items-center justify-center shadow-glow-teal"><Car className="w-8 h-8 sm:w-10 sm:h-10 text-white" /></div>
                        
                        <div className="w-full h-24 mt-8 relative hidden lg:block">
                            <svg className="w-full h-full" viewBox="0 0 800 100" preserveAspectRatio="none">
                                <path d="M 0 80 Q 200 20, 400 50 T 800 30" fill="none" stroke="#e5e5e5" strokeWidth="20" strokeLinecap="round" />
                                <path className="mus-path" d="M 0 80 Q 200 20, 400 50 T 800 30" fill="none" stroke="#d4a574" strokeWidth="4" strokeLinecap="round" strokeDasharray="10 5" style={{strokeDasharray: '1000', strokeDashoffset: '1000'}} />
                            </svg>
                        </div>
                    </div>
                </div>
            </div>'''
jsx_blocks = jsx_blocks.replace('{300 + i * 150}', '')

content = content.replace(
    \"            {/* ---------------- SLIDE 2: TEMPOH EXACT CLONE ---------------- */}\",
    jsx_blocks + \"\\n\\n            {/* ---------------- SLIDE 2: TEMPOH EXACT CLONE ---------------- */}\"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully.")
