from flask import Flask, request, jsonify
import heapq

app = Flask(__name__)

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {tuple(start): 0}

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current in came_from:
                path.append({"x": current[1] * 20, "y": current[0] * 20})
                current = came_from[current]
            path.append({"x": start[1] * 20, "y": start[0] * 20})
            path.reverse()
            return path
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                tentative_g = g_score[tuple(current)] + 1
                if tuple(neighbor) not in g_score or tentative_g < g_score[tuple(neighbor)]:
                    came_from[neighbor] = current
                    g_score[tuple(neighbor)] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score, neighbor))
    return []

@app.route("/get_path", methods=["POST"])
def get_path():
    data = request.get_json()
    grid = data.get("grid")
    start = tuple(data.get("start"))
    end = tuple(data.get("end"))
    if not grid or not start or not end:
        return jsonify({"error": "Invalid input"}), 400
    path = a_star(grid, start, end)
    return jsonify({"path": path})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
