def find_schedule(t, o, constraints):
    # Initialize departure times as zero for all trains
    departure_times = [0] * t
    edges = []

    # Build the graph's edges based on constraints
    for A, B, m in constraints:
        edges.append((B - 1, A - 1, m))

    # Bellman-Ford algorithm to detect feasible schedule
    for _ in range(t - 1):
        updated = False
        for B, A, m in edges:
            if departure_times[A] < departure_times[B] + m:
                departure_times[A] = departure_times[B] + m
                updated = True
        if not updated:
            break

    # Check for negative cycles
    for B, A, m in edges:
        if departure_times[A] < departure_times[B] + m:
            return "nelze"

    return " ".join(map(str, departure_times))

data = []

while True:
    try:
        line = input()
        if line:
            data.append(line)
        else:
            break
    except EOFError:
        break

t, o = map(int, data[0].split())
constraints = [tuple(map(int, line.split())) for line in data[1:]]

print(find_schedule(t, o, constraints))