import type { AgentEvent } from "@/types/agent-event";
import { useChatStore } from "@/stores/chatStore";
import { useAgentRunStore } from "@/stores/agentRunStore";
import { useResultStore } from "@/stores/resultStore";
import { useTaskStore } from "@/stores/taskStore";
import { getTaskResult } from "@/lib/api/tasks";

export async function handleAgentEvent(event: AgentEvent) {
  if (event.type === "run.started") useAgentRunStore.getState().setRunId(event.run_id);
  if (event.type === "message.delta") useChatStore.getState().appendAssistantDelta(String(event.data.content ?? ""));
  if (event.type === "task.created") useTaskStore.getState().setTask(String(event.data.task_id));
  if (event.type === "task.progress") useTaskStore.getState().setProgress(Number(event.data.progress ?? 0), String(event.data.current_step ?? ""));
  if (event.type === "input.required") useTaskStore.getState().setStatus("waiting_user_input");
  if (event.type === "run.finished") {
    useChatStore.getState().finalizeLastAssistantMessage("done");
    useTaskStore.getState().setStatus("success");
  }
  if (event.type === "error") {
    useChatStore.getState().finalizeLastAssistantMessage("error");
    useTaskStore.getState().setStatus("failed");
  }

  if (["agent.thought", "skill.selected", "tool.started", "tool.finished", "task.progress"].includes(event.type)) {
    useAgentRunStore.getState().pushStep({
      id: event.event_id,
      type: event.type,
      title: event.type,
      description: JSON.stringify(event.data),
      status: event.type === "tool.finished" ? "success" : "running",
      timestamp: event.timestamp,
    });
  }
  if (event.type === "result.ready") {
    const taskId = String(event.data.task_id);
    const payload = await getTaskResult(taskId);
    useResultStore.getState().setResult(payload.result);
  }
}
