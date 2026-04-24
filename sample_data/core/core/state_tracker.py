class StateTracker:
    def __init__(self):
        self.state = {}
        self.history = []

    def update(self, event):
        component = event["component"]
        new_state = event["state"]

        self.state[component] = new_state

        self.history.append({
            "t": event["t"],
            "component": component,
            "state": new_state,
            "full_state": self.state.copy()
        })

    def get_history(self):
        return self.history
