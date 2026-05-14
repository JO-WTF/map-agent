"use client";
import { useMemo } from "react";
import { useResultStore } from "@/stores/resultStore";

export function ChartPanel() {
  const result = useResultStore((s) => s.result);
  const chartInfo = useMemo(() => {
    const charts = result?.charts ?? {};
    const keys = Object.keys(charts);
    return { keys, count: keys.length };
  }, [result]);

  return (
    <div className="space-y-2 border p-3">
      <h3 className="font-semibold">Chart View (Result Linked)</h3>
      <div className="text-sm">Loaded chart groups: {chartInfo.count}</div>
      <div className="text-xs text-gray-600">{chartInfo.keys.join(", ") || "No charts yet"}</div>
    </div>
  );
}
