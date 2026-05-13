from app.tools.remote_api.warehouse_api import get_warehouses
from app.tools.remote_api.customer_api import get_customers
from app.tools.geo_tools import calculate_distance_matrix
from app.tools.allocation_tools import assign_nearest_warehouse
from app.tools.sla_tools import calculate_sla, aggregate_stats
from app.tools.report_tools import generate_map_data, generate_chart_data, generate_excel_report
from app.skills.warehouse_allocation.result_builder import build_result


def run(task_id: str, payload: dict) -> dict:
    warehouses = get_warehouses()
    customers = get_customers()
    matrix = calculate_distance_matrix(warehouses, customers)
    assigned = assign_nearest_warehouse(matrix)
    with_sla = calculate_sla(assigned)
    stats = aggregate_stats(with_sla)
    map_data = generate_map_data(warehouses, customers, with_sla)
    charts = generate_chart_data(stats)
    files = generate_excel_report(task_id)
    result = build_result(warehouses, customers, with_sla, stats, files)
    result["map_data"] = map_data
    result["charts"] = charts
    return result
