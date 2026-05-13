"use client";
import { useAgentRunStore } from "@/stores/agentRunStore";

export function AgentTimeline() {
  const steps = useAgentRunStore((s) => s.steps);
  return <pre className="h-40 overflow-auto border p-2 text-xs">{JSON.stringify(steps, null, 2)}</pre>;
}
