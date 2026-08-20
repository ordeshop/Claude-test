import { useEffect, useRef, useState } from 'react'
import { Phone, Menu, X, Sparkles } from 'lucide-react'

/* ------------------------------------------------------------------ */
/* Media — generated with Kling (documentary-style, no faces/hands so   */
/* it does not read as an AI render). Each video has a matching poster   */
/* still so nothing flashes black before the clip loads.                 */
/*                                                                       */
/* NOTE: these are temporary Kling delivery URLs and expire ~24h after   */
/* generation. For a persistent demo, download the eight assets and      */
/* re-host them (e.g. drop them in /public/media and point these         */
/* constants at the local paths), then swap for real footage later.      */
/* ------------------------------------------------------------------ */
const VIDEO_URL_1 =
  'https://v15-kling.klingai.com/bs2/upload-ylab-stunt-sgp/0968ebcb-e2be-4234-9039-a7197942f005-lyIBl9i3mkdXPNsDc8FxUg-output.mp4?x-kcdn-pid=112372' // Empfang — bright reception, morning daylight
const VIDEO_URL_2 =
  'https://v15-kling.klingai.com/bs2/upload-ylab-stunt-sgp/3e982bd7-cb4a-4833-99ea-5b23e236782d-0O4bt_xn2m0evEXxp4jRpQ-output.mp4?x-kcdn-pid=112372' // Präzision — instruments on a tray, no hands
const VIDEO_URL_3 =
  'https://v15-kling.klingai.com/bs2/upload-ylab-stunt-sgp/f90ba3b2-c4d4-41d5-8120-9e41c2dc53d5-tqhTcVugQ9F_sWqvXWd0uQ-output.mp4?x-kcdn-pid=112372' // Behandlung — dark treatment room (triggers dark mode)
const VIDEO_URL_4 =
  'https://v15-kling.klingai.com/bs2/upload-ylab-stunt-sgp/7005c6e1-0d5f-4755-8f67-fcd00e0efe87-DFjp7h4VE68NK0qaDOGZvg-output.mp4?x-kcdn-pid=112372' // Ihr Team — figures in scrubs from behind

const POSTER_URL_1 =
  'https://s15-kling.klingai.com/kimg/EMXN1y8qngEKBnVwbG9hZBIOeWxhYi1zdHVudC1zZ3AagwFLbGluZ0FJX0tvbG9yc19EaVRfSDgwMF8xX0tvbG9ycy12Ml82LXQyaS1vbW5pLXJlZmluZXItdjNfU0dQX1BST0RfYWlfd2ViXzMxOTE4MTkxMDMwMzM3MV8yNDBiYTZlOGIxOTJmN2Y0YjM0OTk0YzkxMDE1Y2FlN2dmZ2d4LnBuZw.origin?x-kcdn-pid=112372'
const POSTER_URL_2 =
  'https://s15-kling.klingai.com/kimg/EMXN1y8qngEKBnVwbG9hZBIOeWxhYi1zdHVudC1zZ3AagwFLbGluZ0FJX0tvbG9yc19EaVRfSDgwMF8xX0tvbG9ycy12Ml82LXQyaS1vbW5pLXJlZmluZXItdjNfU0dQX1BST0RfYWlfd2ViXzMxOTE4MTkxMzMyNDI5OF80Y2ZhNzFjZGY0Y2MyMjg4Yzk2M2VlNTZmMGQ0OWU3Zmx5aWV6LnBuZw.origin?x-kcdn-pid=112372'
const POSTER_URL_3 =
  'https://s15-kling.klingai.com/kimg/EMXN1y8qngEKBnVwbG9hZBIOeWxhYi1zdHVudC1zZ3AagwFLbGluZ0FJX0tvbG9yc19EaVRfSDgwMF8xX0tvbG9ycy12Ml82LXQyaS1vbW5pLXJlZmluZXItdjNfU0dQX1BST0RfYWlfd2ViXzMxOTE4MTkxNjMwMjI3NV8xN2UyMDYwMzg4YTYyMzBkMzU4YzM4ZDIzNjZkMzAxYTkxZzBiLnBuZw.origin?x-kcdn-pid=112372'
const POSTER_URL_4 =
  'https://s15-kling.klingai.com/kimg/EMXN1y8qngEKBnVwbG9hZBIOeWxhYi1zdHVudC1zZ3AagwFLbGluZ0FJX0tvbG9yc19EaVRfSDgwMF8xX0tvbG9ycy12Ml82LXQyaS1vbW5pLXJlZmluZXItdjNfU0dQX1BST0RfYWlfd2ViXzMxOTE4MTkxODMyNzkxMV82YTk3OGNjNDU3ZDlhZTg2ODFiM2QyNzdhMjljNDc2MGR5aXh3LnBuZw.origin?x-kcdn-pid=112372'

type Scene = {
  src: string
  poster: string
  label: string
  alt: string
}

const SCENES: Scene[] = [
  {
    src: VIDEO_URL_1,
    poster: POSTER_URL_1,
    label: 'Empfang',
    alt: 'Heller Empfangsbereich der Praxis im Morgenlicht',
  },
  {
    src: VIDEO_URL_2,
    poster: POSTER_URL_2,
    label: 'Präzision',
    alt: 'Sterile Instrumente ordentlich auf einem Tablett',
  },
  {
    src: VIDEO_URL_3,
    poster: POSTER_URL_3,
    label: 'Behandlung',
    alt: 'Ruhiges, abgedunkeltes Behandlungszimmer',
  },
  {
    src: VIDEO_URL_4,
    poster: POSTER_URL_4,
    label: 'Ihr Team',
    alt: 'Team in Praxiskleidung, von hinten im Flur',
  },
]

// Dark-mode brand colour applied to the hero text over the moody clip.
const DARK_TEXT = '#182C41'

const CROSSFADE_MS = 1000
const AUTO_ADVANCE_MS = 8000

// system-ui stack for all body text (everything except the serif logo/headline).
const BODY_FONT = 'system-ui, sans-serif'

const NAV_LINKS = [
  { label: 'Leistungen', href: '#' },
  { label: 'Praxis', href: '#' },
  { label: 'Team', href: '#' },
  { label: 'Kontakt', href: '#' },
]

const PHONE_DISPLAY = '0821 / 123 456 78'
const PHONE_TEL = 'tel:+4982112345678' // fictional demo number

const STATS = [
  'Über 15 Jahre Erfahrung',
  '4,9 ★ auf Google',
  'Angstpatienten willkommen',
  'Alle Kassen & privat',
]

function usePrefersReducedMotion() {
  const [reduced, setReduced] = useState(false)
  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)')
    const update = () => setReduced(mq.matches)
    update()
    mq.addEventListener('change', update)
    return () => mq.removeEventListener('change', update)
  }, [])
  return reduced
}

export default function App() {
  const [activeVideo, setActiveVideo] = useState(0)
  const [isTransitioning, setIsTransitioning] = useState(false)
  const [userInteracted, setUserInteracted] = useState(false)
  const [menuOpen, setMenuOpen] = useState(false)
  const [email, setEmail] = useState('')
  const [showConfirm, setShowConfirm] = useState(false)

  const reducedMotion = usePrefersReducedMotion()
  const isDark = activeVideo === 2 // "Behandlung" clip triggers dark text.

  const transitionTimer = useRef<number | null>(null)
  const confirmTimer = useRef<number | null>(null)

  /* -------- Video switching -------- */
  const switchTo = (index: number, manual = false) => {
    if (index === activeVideo || isTransitioning) return
    if (manual) setUserInteracted(true)
    setActiveVideo(index)
    setIsTransitioning(true)
    if (transitionTimer.current) window.clearTimeout(transitionTimer.current)
    transitionTimer.current = window.setTimeout(() => {
      setIsTransitioning(false)
    }, CROSSFADE_MS)
  }

  // Auto-advance every 8s until the user picks a scene (and never with reduced motion).
  useEffect(() => {
    if (userInteracted || reducedMotion) return
    const id = window.setInterval(() => {
      setActiveVideo((prev) => {
        const next = (prev + 1) % SCENES.length
        setIsTransitioning(true)
        if (transitionTimer.current) window.clearTimeout(transitionTimer.current)
        transitionTimer.current = window.setTimeout(
          () => setIsTransitioning(false),
          CROSSFADE_MS,
        )
        return next
      })
    }, AUTO_ADVANCE_MS)
    return () => window.clearInterval(id)
  }, [userInteracted, reducedMotion])

  /* -------- Demo form: confirm, then reset after 4s. Nothing is sent. -------- */
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    setShowConfirm(true)
    setEmail('')
    if (confirmTimer.current) window.clearTimeout(confirmTimer.current)
    confirmTimer.current = window.setTimeout(() => setShowConfirm(false), 4000)
  }

  /* -------- Lock body scroll while the mobile menu is open. -------- */
  useEffect(() => {
    document.body.style.overflow = menuOpen ? 'hidden' : ''
    return () => {
      document.body.style.overflow = ''
    }
  }, [menuOpen])

  // Close the menu with Escape.
  useEffect(() => {
    if (!menuOpen) return
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setMenuOpen(false)
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [menuOpen])

  useEffect(() => {
    return () => {
      if (transitionTimer.current) window.clearTimeout(transitionTimer.current)
      if (confirmTimer.current) window.clearTimeout(confirmTimer.current)
    }
  }, [])

  // Hero text colour transitions to the dark brand colour over the moody clip.
  const heroTextStyle = {
    color: isDark ? DARK_TEXT : '#ffffff',
    transition: 'color 700ms ease-in-out',
  }

  return (
    <section className="relative w-full h-screen overflow-hidden bg-black">
      {/* ---------- Layer 0: stacked background videos ---------- */}
      <div className="absolute inset-0 z-0">
        {SCENES.map((scene, i) => (
          <video
            key={i}
            className={`absolute inset-0 h-full w-full object-cover transition-opacity duration-1000 ease-in-out ${
              i === activeVideo ? 'opacity-100' : 'opacity-0'
            }`}
            src={scene.src}
            poster={scene.poster}
            aria-label={scene.alt}
            autoPlay
            muted
            loop
            playsInline
            preload="auto"
          />
        ))}
      </div>

      {/* ---------- Layer 1: readability scrim (breathing) ---------- */}
      <div
        aria-hidden="true"
        className="scrim-breathe pointer-events-none absolute inset-0 z-[1] bg-gradient-to-b from-black/50 via-black/20 to-black/60"
      />

      {/* ---------- Layer 2: content ---------- */}
      <div className="relative z-[2] flex h-full flex-col">
        {/* ===== Navigation ===== */}
        <nav className="flex items-center justify-between px-5 pt-5 sm:px-8 sm:pt-7">
          <a
            href="#"
            className="text-xl italic text-white sm:text-2xl"
            aria-label="Praxis Lindenhof — Startseite"
          >
            Praxis Lindenhof
          </a>

          {/* Desktop nav (md+) */}
          <div className="hidden items-center gap-4 md:flex">
            {/* Phone (lg+ only) */}
            <a
              href={PHONE_TEL}
              className="hidden items-center gap-2 text-white/80 transition-colors hover:text-white lg:flex"
              style={{ fontFamily: BODY_FONT }}
              aria-label={`Anrufen unter ${PHONE_DISPLAY}`}
            >
              <Phone size={16} aria-hidden="true" />
              <span className="text-sm">{PHONE_DISPLAY}</span>
            </a>

            {/* Liquid-glass pill with links + booking button */}
            <div
              className="liquid-glass flex items-center gap-1 rounded-full py-1.5 pl-2 pr-1.5"
              style={{ fontFamily: BODY_FONT }}
            >
              {NAV_LINKS.map((link) => (
                <a
                  key={link.label}
                  href={link.href}
                  className="rounded-full px-3 py-1.5 text-sm text-white/90 transition-colors hover:text-white"
                >
                  {link.label}
                </a>
              ))}
              <a
                href="#"
                className="ml-1 rounded-full bg-white px-4 py-1.5 text-sm font-medium transition-transform hover:scale-[1.03]"
                style={{ color: DARK_TEXT }}
              >
                Termin buchen
              </a>
            </div>
          </div>

          {/* Mobile hamburger */}
          <button
            type="button"
            onClick={() => setMenuOpen((v) => !v)}
            className="liquid-glass relative flex h-11 w-11 items-center justify-center rounded-full text-white md:hidden"
            aria-label={menuOpen ? 'Menü schließen' : 'Menü öffnen'}
            aria-expanded={menuOpen}
          >
            {/* Crossfade + rotate between Menu and X */}
            <Menu
              size={22}
              aria-hidden="true"
              className={`absolute transition-all duration-300 ${
                menuOpen ? 'rotate-90 scale-75 opacity-0' : 'rotate-0 scale-100 opacity-100'
              }`}
            />
            <X
              size={22}
              aria-hidden="true"
              className={`absolute transition-all duration-300 ${
                menuOpen ? 'rotate-0 scale-100 opacity-100' : '-rotate-90 scale-75 opacity-0'
              }`}
            />
          </button>
        </nav>

        {/* ===== Hero content ===== */}
        <div className="flex flex-1 flex-col items-center justify-center px-5 text-center sm:px-8">
          {/* Badge */}
          <div
            className="liquid-glass mb-6 inline-flex items-center gap-2 rounded-full px-4 py-2"
            style={{ ...heroTextStyle, fontFamily: BODY_FONT }}
          >
            <Sparkles size={15} aria-hidden="true" />
            <span className="text-xs sm:text-sm">
              Über 4.000 Patientinnen und Patienten seit 2009
            </span>
          </div>

          {/* Heading (serif) */}
          <h1
            className="max-w-4xl text-4xl leading-[1.1] tracking-tight sm:text-5xl md:text-7xl lg:text-[5.5rem]"
            style={heroTextStyle}
          >
            Zahnmedizin, die
            <br />
            sich leicht anfühlt
          </h1>

          {/* Subtext */}
          <p
            className="mt-6 max-w-xl text-base leading-relaxed sm:text-lg"
            style={{
              fontFamily: BODY_FONT,
              color: isDark ? DARK_TEXT : 'rgba(255,255,255,0.85)',
              transition: 'color 700ms ease-in-out',
            }}
          >
            Ruhige Behandlung, moderne Technik und ein Team, das zuhört. Für alle,
            die den Zahnarztbesuch bisher lieber verschoben haben.
          </p>

          {/* CTA — demo form (does not submit anywhere) */}
          <form
            onSubmit={handleSubmit}
            className="mt-8 w-full max-w-[320px] sm:max-w-sm"
            style={{ fontFamily: BODY_FONT }}
          >
            <div className="liquid-glass flex items-center gap-1 rounded-full py-1.5 pl-4 pr-1.5">
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Ihre E-Mail-Adresse"
                aria-label="Ihre E-Mail-Adresse"
                className="email-input min-w-0 flex-1 bg-transparent text-sm outline-none"
                style={{
                  color: isDark ? DARK_TEXT : '#ffffff',
                  transition: 'color 700ms ease-in-out',
                }}
              />
              <button
                type="submit"
                className="shrink-0 rounded-full bg-white px-4 py-2 text-sm font-medium transition-transform hover:scale-[1.03]"
                style={{ color: DARK_TEXT }}
              >
                Termin anfragen
              </button>
            </div>
            {/* Inline demo confirmation — nothing is actually sent. */}
            <p
              role="status"
              aria-live="polite"
              className={`mt-3 text-xs transition-opacity duration-300 ${
                showConfirm ? 'opacity-100' : 'opacity-0'
              }`}
              style={{
                color: isDark ? DARK_TEXT : 'rgba(255,255,255,0.85)',
              }}
            >
              {showConfirm
                ? 'Danke! Das ist eine Demo — es wurde nichts gesendet.'
                : ' '}
            </p>
          </form>

          {/* Video switcher */}
          <div
            className="mt-8 flex items-center gap-4 sm:gap-6"
            role="tablist"
            aria-label="Hintergrundszene wählen"
            style={{ fontFamily: BODY_FONT }}
          >
            {SCENES.map((scene, i) => {
              const active = i === activeVideo
              return (
                <button
                  key={scene.label}
                  type="button"
                  role="tab"
                  aria-selected={active}
                  onClick={() => switchTo(i, true)}
                  className="border-b pb-0.5 text-xs transition-all duration-700 ease-in-out hover:opacity-80 sm:text-sm"
                  style={{
                    color: isDark ? DARK_TEXT : '#ffffff',
                    opacity: active ? 1 : 0.5,
                    borderColor: active ? 'currentColor' : 'transparent',
                  }}
                >
                  {scene.label}
                </button>
              )
            })}
          </div>
        </div>

        {/* ===== Bottom stats (stays white regardless of scene) ===== */}
        <div className="px-5 pb-6 sm:px-8 sm:pb-8">
          <div
            className="flex flex-wrap items-center justify-center gap-x-3 gap-y-1 text-xs text-white/70 sm:text-sm"
            style={{ fontFamily: BODY_FONT }}
          >
            {STATS.map((stat, i) => (
              <span key={stat} className="flex items-center gap-3">
                {stat}
                {i < STATS.length - 1 && (
                  <span aria-hidden="true" className="hidden text-white/30 sm:inline">
                    |
                  </span>
                )}
              </span>
            ))}
          </div>
          {/* A real German site would legally require these pages — placeholders only. */}
          <div
            className="mt-2 text-center text-[10px] text-white/40"
            style={{ fontFamily: BODY_FONT }}
          >
            <a href="#" className="hover:text-white/60">
              Impressum
            </a>{' '}
            ·{' '}
            <a href="#" className="hover:text-white/60">
              Datenschutz
            </a>
          </div>
        </div>
      </div>

      {/* ---------- Mobile menu overlay ---------- */}
      {menuOpen && (
        <div className="fixed inset-0 z-50 md:hidden">
          <div
            className="absolute inset-0 bg-black/60 backdrop-blur-sm"
            onClick={() => setMenuOpen(false)}
            aria-hidden="true"
          />
          <div
            className="relative flex h-full flex-col items-center justify-center gap-6 px-8"
            style={{ fontFamily: BODY_FONT }}
          >
            {NAV_LINKS.map((link, i) => (
              <a
                key={link.label}
                href={link.href}
                onClick={() => setMenuOpen(false)}
                className="text-3xl text-white"
                style={{
                  animation: `menuIn 500ms cubic-bezier(0.4,0,0.2,1) both`,
                  animationDelay: `${100 + i * 50}ms`,
                }}
              >
                {link.label}
              </a>
            ))}

            <a
              href="#"
              onClick={() => setMenuOpen(false)}
              className="mt-4 rounded-full bg-white px-8 py-3 text-lg font-medium transition-transform hover:scale-105"
              style={{
                color: DARK_TEXT,
                animation: `menuIn 500ms cubic-bezier(0.4,0,0.2,1) both`,
                animationDelay: '300ms',
              }}
            >
              Termin buchen
            </a>
            <a
              href={PHONE_TEL}
              className="flex items-center gap-2 text-white/80"
              aria-label={`Anrufen unter ${PHONE_DISPLAY}`}
            >
              <Phone size={16} aria-hidden="true" />
              {PHONE_DISPLAY}
            </a>
            <div className="text-[11px] text-white/40">
              <a href="#" className="hover:text-white/60">
                Impressum
              </a>{' '}
              ·{' '}
              <a href="#" className="hover:text-white/60">
                Datenschutz
              </a>
            </div>
          </div>
        </div>
      )}

      {/* ---------- Demo badge (fixed, bottom-right) ---------- */}
      <div
        className="liquid-glass fixed bottom-4 right-4 z-40 rounded-full px-3 py-1.5 text-[11px] text-white/70"
        style={{ fontFamily: BODY_FONT }}
      >
        Demo-Website · fiktive Praxis
      </div>
    </section>
  )
}
