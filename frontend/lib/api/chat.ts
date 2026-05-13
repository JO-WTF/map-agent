import { parseSseEvent } from "@/lib/sse/parseSseEvent";
import { handleAgentEvent } from "@/lib/sse/handleAgentEvent";
import { BACKEND_BASE_URL } from "@/config/app";

export async function streamChat(payload: Record<string, any>) {
  const res = await fetch(`${BACKEND_BASE_URL}/api/chat/stream`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "text/event-stream" },
    body: JSON.stringify(payload),
  });

  const reader = res.body?.getReader();
  const decoder = new TextDecoder("utf-8");
  let buffer = "";
  while (reader) {
    const { value, done } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    const chunks = buffer.split("\n\n");
    buffer = chunks.pop() || "";
    for (const raw of chunks) {
      const event = parseSseEvent(raw);
      if (event) await handleAgentEvent(event);
    }
  }
}
