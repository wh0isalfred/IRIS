import { useState } from 'react'
import ModeSelector from './features/ModeSelector/ModeSelector'
import ImageUpload from './features/ImageUpload/ImageUpload'
import './App.css'

function App() {
  // Single source of truth for which mode is active.
  // Lives here because ModeSelector AND the feed both need it.
  const [activeMode, setActiveMode] = useState('image')
  const [resultImage, setResultImage] = useState(null)       // detection result

  return (
    <div className="iris">
      {/* ── Top bar ─────────────────────────────── */}
      <header className="topbar">
        <div className="brand">
          <span className="brand__mark" aria-hidden="true" />
          <h1 className="brand__name">IRIS</h1>
          <span className="brand__sub mono">
            Intelligence &amp; Recognition Identification System
          </span>
        </div>

        <div className="status">
          <span className="status__dot" />
          <span className="status__label mono">SYSTEM ONLINE</span>
          <span className="status__faces mono">
            FACES&nbsp;<strong>00</strong>
          </span>
        </div>
      </header>

      {/* ── Three panels ────────────────────────── */}
      <main className="grid">
        {/* Left — input controls */}
        <section className="panel panel--controls">
          <div className="panel__head mono">INPUT</div>
          <div className="panel__body">
            <ModeSelector
              activeMode={activeMode}
              setActiveMode={setActiveMode}
            />
            <div className="placeholder mono">controls go here</div>
            {activeMode === 'image' && <ImageUpload setResultImage={setResultImage} />}
          </div>
        </section>

        {/* Center — the feed */}
        <section className="panel panel--feed">
          <div className="panel__head mono">FEED</div>
          <div className="panel__body feed__body">
            <div className="feed__frame">
              {resultImage
                ? <img src={resultImage} alt="Detection result" />
                : <span className="feed__idle mono">NO SIGNAL</span>
              }
            </div>
          </div>
        </section>

        {/* Right — detection log */}
        <section className="panel panel--log">
          <div className="panel__head mono">DETECTION LOG</div>
          <div className="panel__body">
            <div className="placeholder mono">awaiting detections…</div>
          </div>
        </section>
      </main>
    </div>
  )
}

export default App
