import os
import json

class Node:
    def __init__(self, name):
        self.name = name
        self.state = "OK"
        self.dependents = []

    def add(self, node):
        self.dependents.append(node)

def propagate_failure(node, log):
    if node.state == "FAIL":
        return

    node.state = "FAIL"
    log.append(f"{node.name} failed")

    for d in node.dependents:
        log.append(f"{node.name} impacts {d.name}")
        propagate_failure(d, log)

def run_simulation():
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")

    A.add(B)
    B.add(C)
    C.add(D)

    log = []

    A.state = "FAIL"

propagate_failure(A, log)

    output = {
        "log": log,
        "replay_test": True
    }

    with open("result.json", "w") as f:
        json.dump(output, f, indent=2)

    print("OUTPUT WRITTEN: result.json")

    assert os.path.exists("result.json")

if __name__ == "__main__":
    run_simulation()
