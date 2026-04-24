def render_timeline(history, failure_point=None):
    print("\n================ LENA TIMELINE =================\n")

    for h in history:
        t = h["t"]
        comp = h["component"]
        state = h["state"]

        # Highlight failure
        if failure_point and t == failure_point:
            print(f"🔴 t={t} | {comp} → {state}  [FAILURE TRIGGER]")
        else:
            print(f"🟢 t={t} | {comp} → {state}")

    print("\n=================================================\n")
