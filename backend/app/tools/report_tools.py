def generate_map_data(warehouses: list[dict], customers: list[dict], assignments: list[dict]) -> dict:
    return {"warehouses": warehouses, "customers": customers, "assignment_lines": assignments}

def generate_chart_data(stats: list[dict]) -> dict:
    return {"warehouse_sla_distribution": stats}

def generate_excel_report(task_id: str) -> dict:
    return {"file_id": f"report_{task_id}", "download_url": f"/api/files/report_{task_id}/download"}
