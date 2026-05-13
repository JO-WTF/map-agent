from app.tools import logistics_tools as t


def warehouse_customer_allocation_skill() -> dict:
    warehouses = t.get_warehouses()
    customers = t.get_customers()
    matrix = t.calculate_distance_matrix(warehouses, customers)
    assignment = t.assign_nearest_warehouse(matrix)
    assignment_sla = t.calculate_delivery_sla(assignment)
    stats = t.aggregate_warehouse_sla_stats(assignment_sla)
    return {
        "map_data": t.generate_map_data(assignment_sla),
        "chart_data": t.generate_chart_data(stats),
        "table_data": assignment_sla,
        "logs": [
            "get_warehouses",
            "get_customers",
            "calculate_distance_matrix",
            "assign_nearest_warehouse",
            "calculate_delivery_sla",
            "aggregate_warehouse_sla_stats",
            "generate_map_data",
            "generate_chart_data",
        ],
    }
