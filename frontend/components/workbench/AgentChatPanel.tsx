"use client";
import { useState } from "react";
import { streamChat } from "@/lib/api/chat";
import { useChatStore } from "@/stores/chatStore";

export function AgentChatPanel() {
  const [message, setMessage] = useState("");
  const addMessage = useChatStore((s) => s.addMessage);

  const onSend = async () => {
    try {
      await streamChat({ session_id: "session_001", message, file_ids: [], context: {} });
    } catch (error) {
      addMessage({
        id: crypto.randomUUID(),
        role: "system",
        content: error instanceof Error ? error.message : "发送失败，请稍后重试。",
        createdAt: new Date().toISOString(),
        status: "error",
      });
    }
  };

  return (
    <div className="space-y-2">
      <textarea className="w-full border p-2" value={message} onChange={(e) => setMessage(e.target.value)} />
      <button className="rounded bg-black px-3 py-2 text-white" onClick={onSend}>发送</button>
    </div>
  );
}
