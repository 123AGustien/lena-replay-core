from core.parser import load_events
from core.replay_engine import ReplayEngine
from core.visualizer import render_timeline

def main():
    events = load_events("sample_data/ev_failure_log.json")

    engine = ReplayEngine(events)
    result = engine.run()

    render_timeline(result["history"], result["failure_point"])

    print("\n--- SUMMARY ---")
    print("Failure detected:", result["failure_detected"])
    print("Failure point:", result["failure_point"])

if __name__ == "__main__":
    main()
