import type { AgentEvent } from "@/types/agent-event";

export function parseSseEvent(raw: string): AgentEvent | null {
  const lines = raw.split("\n");
  const dataLine = lines.find((l) => l.startsWith("data: "));
  if (!dataLine) return null;
  return JSON.parse(dataLine.slice(6)) as AgentEvent;
}
