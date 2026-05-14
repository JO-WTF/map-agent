import { create } from "zustand";

type AgentStep = {
  id: string;
  type: string;
  title: string;
  description?: string;
  status: "running" | "success" | "failed";
  timestamp: string;
};

type AgentRunStore = {
  runId?: string;
  steps: AgentStep[];
  pushStep: (step: AgentStep) => void;
  setRunId: (id: string) => void;
};

export const useAgentRunStore = create<AgentRunStore>((set) => ({
  steps: [],
  pushStep: (step) => set((s) => ({ steps: [...s.steps, step] })),
  setRunId: (id) => set({ runId: id }),
}));
