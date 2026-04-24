from flask import Flask, render_template
from core.parser import load_events
from core.replay_engine import ReplayEngine

app = Flask(__name__)

@app.route("/")
def index():
    events = load_events("sample_data/ev_failure_log.json")

    engine = ReplayEngine(events)
    result = engine.run()

    return render_template(
        "timeline.html",
        history=result["history"],
        failure_point=result["failure_point"]
    )

if __name__ == "__main__":
    app.run(debug=True)
