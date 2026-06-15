// The three modes IRIS supports. Defining them as an array means the
// buttons are generated from data — add a mode here and a button appears,
// no JSX duplication.
const MODES = ['image', 'video', 'live']

function ModeSelector({ activeMode, setActiveMode }) {
  return (
    <div className="modes">
      {MODES.map((mode) => (
        <button
          key={mode}
          className={
            // Always 'mode mono'. Add 'mode--active' only for the active one.
            mode === activeMode ? 'mode mode--active mono' : 'mode mono'
          }
          onClick={() => setActiveMode(mode)}
        >
          {mode.toUpperCase()}
        </button>
      ))}
    </div>
  )
}

export default ModeSelector
