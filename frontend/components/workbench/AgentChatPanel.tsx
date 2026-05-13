"use client";
import { useState } from "react";
import { streamChat } from "@/lib/api/chat";

export function AgentChatPanel() {
  const [message, setMessage] = useState("");
  return (
    <div className="space-y-2">
      <textarea className="w-full border p-2" value={message} onChange={(e) => setMessage(e.target.value)} />
      <button className="rounded bg-black px-3 py-2 text-white" onClick={() => streamChat({ session_id: "session_001", message, file_ids: [], context: {} })}>发送</button>
    </div>
  );
}
