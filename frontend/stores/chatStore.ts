import { create } from "zustand";
import { createId } from "@/lib/utils/createId";

type ChatMessage = {
  id: string;
  role: "user" | "assistant" | "system";
  content: string;
  createdAt: string;
  status?: "streaming" | "done" | "error";
};

type ChatStore = {
  messages: ChatMessage[];
  addMessage: (m: ChatMessage) => void;
  appendAssistantDelta: (content: string) => void;
  finalizeLastAssistantMessage: (status: "done" | "error") => void;
};

export const useChatStore = create<ChatStore>((set) => ({
  messages: [],
  addMessage: (m) => set((s) => ({ messages: [...s.messages, m] })),
  appendAssistantDelta: (content) =>
    set((s) => {
      const last = s.messages[s.messages.length - 1];
      if (!last || last.role !== "assistant" || last.status !== "streaming") {
        return {
          messages: [
            ...s.messages,
            { id: createId("msg"), role: "assistant", content, createdAt: new Date().toISOString(), status: "streaming" },
          ],
        };
      }
      const next = [...s.messages];
      next[next.length - 1] = { ...last, content: `${last.content}${content}` };
      return { messages: next };
    }),
  finalizeLastAssistantMessage: (status) =>
    set((s) => {
      const next = [...s.messages];
      for (let i = next.length - 1; i >= 0; i -= 1) {
        if (next[i].role === "assistant" && next[i].status === "streaming") {
          next[i] = { ...next[i], status };
          break;
        }
      }
      return { messages: next };
    }),
}));
