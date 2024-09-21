from ortools.sat.python import cp_model

def assign_frequencies():
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    frequencies = ['f1', 'f2', 'f3']

    antennas = {i: model.NewIntVar(0, 2, f'ant{i}') for i in range(1, 10)}

    adjacencies = {
        1: [2, 3, 4],
        2: [1, 3, 5, 6],
        3: [1, 2, 6, 9],
        4: [1, 2, 5],
        5: [2, 4],
        6: [2, 7, 8],
        7: [6, 8],
        8: [7, 9],
        9: [3, 8]
    }

    for antenna, neighbors in adjacencies.items():
        for neighbor in neighbors:
            model.Add(antennas[antenna] != antennas[neighbor])

    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        for i in range(1, 10):
            freq = frequencies[solver.Value(antennas[i])]
            print(f"Antenna {i}: Frequency {freq}")
    else:
        print("No solution found.")

assign_frequencies()
