from collections import defaultdict

jug1, jug2, aim = 4, 3, 2
visited = defaultdict(bool)

def waterJugSolver(amt1, amt2):
    if (amt1, amt2) in visited:
        return False
    if amt1 == aim or amt2 == aim:
        print(amt1, amt2)
        return True

    visited[(amt1, amt2)] = True
    print(amt1, amt2)

    actions = [
        (0, amt2), (amt1, 0), (jug1, amt2), (amt1, jug2),
        (amt1 + min(amt2, jug1 - amt1), amt2 - min(amt2, jug1 - amt1)),
        (amt1 - min(amt1, jug2 - amt2), amt2 + min(amt1, jug2 - amt2))
    ]
    
    return any(waterJugSolver(a, b) for a, b in actions)

print("Steps:")
waterJugSolver(0, 0)