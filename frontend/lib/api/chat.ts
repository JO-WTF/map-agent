import { parseSseEvent } from "@/lib/sse/parseSseEvent";
import { handleAgentEvent } from "@/lib/sse/handleAgentEvent";
import { API_PROXY_PREFIX, BACKEND_BASE_URL } from "@/config/app";

export async function streamChat(payload: Record<string, any>) {
  let res: Response;
  try {
    res = await fetch(`${API_PROXY_PREFIX}/api/chat/stream`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "text/event-stream" },
      body: JSON.stringify(payload),
    });
  } catch {
    throw new Error(`无法连接后端服务（${BACKEND_BASE_URL}）。请确认后端已启动。`);
  }

  if (!res.ok || !res.body) {
    const detail = await res.text().catch(() => "");
    throw new Error(`请求失败（${res.status}）。${detail || "请检查前端代理与后端服务状态。"}`);
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
