from math import sqrt


def get_warehouses() -> list[dict]:
    return [
        {"warehouse_id": "W1", "name": "East Hub", "x": 10.0, "y": 12.0},
        {"warehouse_id": "W2", "name": "West Hub", "x": 80.0, "y": 25.0},
    ]


def get_customers() -> list[dict]:
    return [
        {"customer_id": "C1", "x": 12.0, "y": 10.0},
        {"customer_id": "C2", "x": 15.0, "y": 20.0},
        {"customer_id": "C3", "x": 70.0, "y": 20.0},
    ]


def calculate_distance_matrix(warehouses: list[dict], customers: list[dict]) -> list[dict]:
    rows: list[dict] = []
    for customer in customers:
        for warehouse in warehouses:
            dx = warehouse["x"] - customer["x"]
            dy = warehouse["y"] - customer["y"]
            rows.append(
                {
                    "warehouse_id": warehouse["warehouse_id"],
                    "customer_id": customer["customer_id"],
                    "distance": round(sqrt(dx * dx + dy * dy), 2),
                }
            )
    return rows


def assign_nearest_warehouse(distance_rows: list[dict]) -> list[dict]:
    best: dict[str, dict] = {}
    for row in distance_rows:
        cid = row["customer_id"]
        if cid not in best or row["distance"] < best[cid]["distance"]:
            best[cid] = row
    return list(best.values())


def calculate_delivery_sla(assignments: list[dict]) -> list[dict]:
    out: list[dict] = []
    for item in assignments:
        distance = item["distance"]
        if distance <= 15:
            sla = "T+1"
        elif distance <= 40:
            sla = "T+2"
        else:
            sla = "T+3"
        out.append({**item, "sla": sla})
    return out


def aggregate_warehouse_sla_stats(assignment_sla: list[dict]) -> list[dict]:
    counter: dict[tuple[str, str], int] = {}
    for row in assignment_sla:
        key = (row["warehouse_id"], row["sla"])
        counter[key] = counter.get(key, 0) + 1
    return [
        {"warehouse_id": wh, "sla": sla, "count": cnt}
        for (wh, sla), cnt in sorted(counter.items())
    ]


def generate_map_data(assignments: list[dict]) -> dict:
    return {"connections": assignments}


def generate_chart_data(stats: list[dict]) -> dict:
    return {
        "warehouse_sla": [
            {"name": f"{row['warehouse_id']}-{row['sla']}", "value": row["count"]}
            for row in stats
        ]
    }
