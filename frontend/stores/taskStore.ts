import { create } from "zustand";
import type { TaskState } from "@/types/task";

type TaskStore = TaskState & {
  setTask: (taskId: string) => void;
  setProgress: (progress: number, currentStep?: string) => void;
  setStatus: (status: TaskState["status"]) => void;
};

export const useTaskStore = create<TaskStore>((set) => ({
  status: "idle",
  progress: 0,
  setTask: (taskId) => set({ currentTaskId: taskId, status: "queued", progress: 0 }),
  setProgress: (progress, currentStep) => set({ progress, currentStep, status: "running" }),
  setStatus: (status) => set({ status }),
}));
