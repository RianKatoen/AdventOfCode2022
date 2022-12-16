import re

def input(file: str):
    lines = sorted([re.match("Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnel[s]? lead[s]? to valve[s]? ((?:[A-Z]{2},?\s?)+)", line.strip()).groups() for line in open("day16/" + file + ".txt", "r")], key=lambda x : x[0], reverse=True)
    valves, edges = {}, {}
    for valve in lines:
        valves.update({ valve[0]: int(valve[1]) })
        edges.update({ valve[0]: sorted([v for v in valve[2].split(', ')]) })
    return valves, edges

def pressures(valves: dict[int, int], edges: dict[int, set[int]], scores: dict[tuple[str, str], int] = {('AA', 'AA', ''): 0}, t: int = 0, T: int = 30, my_turn: bool = True):
    new_scores = {}
    delta_t, max_pressure = T - t + 1, max(scores.values())
    for info, pressure in scores.items():
        opened_list = [info[2].split(',')]
        max_remaining_pressure = max([p * delta_t for v, p in valves.items() if not(v in opened_list)])
        if max_remaining_pressure <= max_pressure - pressure:
            continue

        valve_me, valve_el, opened = info[0], info[1], info[2]
        valve = valve_me if my_turn else valve_el
        if valves[valve] > 0 and not(valve in opened):
            new_opened = valve if len(opened) == 0 else str.join(',', (opened + ',' + valve).split(','))
            key, new_pressure = (valve_me, valve_el, new_opened), pressure + (T - t - 1) * valves[valve]
            new_scores.update({ key: new_pressure })

        for edge in edges[valve]:
            if my_turn:
                new_scores.update({ (edge, valve_el, opened): pressure })
            else:
                new_scores.update({ (valve_me, edge, opened): pressure })
                
    return new_scores

def total_pressure(file: str, T: int = 30, use_elephant: bool = False):
    valves, edges = input(file)
    states = [pressures(valves, edges, T=T)]
    if use_elephant:
        states.append(pressures(valves, edges, states[-1], T=T, my_turn=False))

    for t in range(1, T, 1):
        states.append(pressures(valves, edges, states[-1], t=t, T=T))
        if use_elephant:
            states.append(pressures(valves, edges, states[-1], t=t, T=T, my_turn=False))

    return max([max(state.values()) for state in states])

# Part 1
print("example 1:", total_pressure("example"))
print("part 1:", total_pressure("input"))

# Part 2
print("example 2:", total_pressure("example", T=26, use_elephant=True))
print("part 2:", total_pressure("input", T=26, use_elephant=True))