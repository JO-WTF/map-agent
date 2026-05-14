from math import sqrt

def calculate_distance_matrix(warehouses: list[dict], customers: list[dict]) -> list[dict]:
    out = []
    for c in customers:
        for w in warehouses:
            d = sqrt((w['lng']-c['lng'])**2 + (w['lat']-c['lat'])**2)
            out.append({"warehouse_id": w["id"], "customer_id": c["id"], "distance": round(d, 4)})
    return out
