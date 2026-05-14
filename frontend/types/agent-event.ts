export type AgentEventType =
  | "run.started"
  | "message.delta"
  | "agent.thought"
  | "skill.selected"
  | "tool.started"
  | "tool.finished"
  | "task.created"
  | "task.progress"
  | "input.required"
  | "result.ready"
  | "run.finished"
  | "error";

export type AgentEvent = {
  event_id: string;
  type: AgentEventType;
  timestamp: string;
  run_id: string;
  session_id: string;
  data: Record<string, any>;
};
