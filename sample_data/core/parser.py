import json

def load_events(file_path):
    with open(file_path, "r") as f:
        events = json.load(f)

    # Ensure sorted by time (deterministic)
    events.sort(key=lambda x: x["t"])
    return events
