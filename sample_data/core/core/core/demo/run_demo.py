from core.parser import load_events
from core.replay_engine import ReplayEngine

def main():
    events = load_events("sample_data/ev_failure_log.json")

    engine = ReplayEngine(events)
    result = engine.run()

    print("\n=== LENA REPLAY OUTPUT ===\n")

    for h in result["history"]:
        print(f"t={h['t']} | {h['component']} -> {h['state']} | system={h['full_state']}")

    print("\n--- SUMMARY ---")
    print("Failure detected:", result["failure_detected"])
    print("Failure point:", result["failure_point"])

if __name__ == "__main__":
    main()
