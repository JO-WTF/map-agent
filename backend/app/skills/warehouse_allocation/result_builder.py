from app.schemas.common import LogItem


def build_result(warehouses: list[dict], customers: list[dict], assignments: list[dict], stats: list[dict], file_ref: dict):
    same_day = sum(1 for r in assignments if r.get('sla') == 'T+1')
    total = len(assignments) or 1
    return {
        "summary": {
            "warehouse_count": len(warehouses),
            "customer_count": len(customers),
            "same_day_ratio": round(same_day / total, 2),
        },
        "tables": {
            "allocation_detail": assignments,
            "warehouse_sla_stats": stats,
        },
        "files": {"excel_report": file_ref},
        "logs": [LogItem(step="skill", message="warehouse allocation done", status="success")],
    }
