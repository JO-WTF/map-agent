"use client";
import { useMemo } from "react";
import { useResultStore } from "@/stores/resultStore";

export function MapPanel() {
  const result = useResultStore((s) => s.result);
  const summary = useMemo(() => {
    const map = result?.map_data ?? {};
    const warehouses = Array.isArray(map.warehouses) ? map.warehouses.length : 0;
    const customers = Array.isArray(map.customers) ? map.customers.length : 0;
    const lines = Array.isArray(map.assignment_lines) ? map.assignment_lines.length : 0;
    return { warehouses, customers, lines };
  }, [result]);

  return (
    <div className="space-y-2 border p-3">
      <h3 className="font-semibold">Map View (Result Linked)</h3>
      <div className="text-sm">Warehouses: {summary.warehouses}</div>
      <div className="text-sm">Customers: {summary.customers}</div>
      <div className="text-sm">Assignment Lines: {summary.lines}</div>
    </div>
  );
}
