def calculate_sla(assignments: list[dict]) -> list[dict]:
    result = []
    for a in assignments:
        sla = 'T+1' if a['distance'] < 1 else 'T+2'
        result.append({**a, 'sla': sla})
    return result

def aggregate_stats(rows: list[dict]) -> list[dict]:
    m = {}
    for r in rows:
        k = (r['warehouse_id'], r['sla'])
        m[k] = m.get(k, 0) + 1
    return [{"warehouse_id": k[0], "sla": k[1], "count": v} for k, v in m.items()]
