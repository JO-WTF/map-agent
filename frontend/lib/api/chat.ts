import { parseSseEvent } from "@/lib/sse/parseSseEvent";
import { handleAgentEvent } from "@/lib/sse/handleAgentEvent";
import { API_PROXY_PREFIX } from "@/config/app";

export async function streamChat(payload: Record<string, any>) {
  let res: Response;
  try {
    res = await fetch(`${API_PROXY_PREFIX}/api/chat/stream`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "text/event-stream" },
      body: JSON.stringify(payload),
    });
  } catch {
    throw new Error("无法连接后端服务（http://localhost:3001）。请确认后端已启动。");
  }

  if (!res.ok || !res.body) {
    throw new Error(`请求失败（${res.status}）。请检查后端服务状态。`);
  }

  const reader = res.body.getReader();
  const decoder = new TextDecoder("utf-8");
  let buffer = "";
  while (true) {
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
