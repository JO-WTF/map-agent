import { create } from "zustand";
import type { TaskState } from "@/types/task";

export const useTaskStore = create<TaskState>(() => ({
  status: "idle",
  progress: 0,
}));
