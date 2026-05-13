def assign_nearest_warehouse(distance_rows: list[dict]) -> list[dict]:
    best = {}
    for r in distance_rows:
        cid = r['customer_id']
        if cid not in best or r['distance'] < best[cid]['distance']:
            best[cid] = r
    return list(best.values())
