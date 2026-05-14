"use client";
import { useResultStore } from "@/stores/resultStore";

export function ResultTable() {
  const result = useResultStore((s) => s.result);
  return <pre className="h-40 overflow-auto border p-2 text-xs">{JSON.stringify(result?.tables ?? {}, null, 2)}</pre>;
}
