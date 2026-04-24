from core.state_tracker import StateTracker

class ReplayEngine:
    def __init__(self, events):
        self.events = events
        self.tracker = StateTracker()
        self.failure_detected = False
        self.failure_point = None

    def run(self):
        for event in self.events:
            self.tracker.update(event)

            # Simple failure logic (MVP rule)
            if event["state"] in ["FAIL_SAFE_TRIGGERED", "CRITICAL_FAILURE"]:
                self.failure_detected = True
                self.failure_point = event["t"]

        return {
            "history": self.tracker.get_history(),
            "failure_detected": self.failure_detected,
            "failure_point": self.failure_point
        }
