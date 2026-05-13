import { create } from "zustand";
import type { TaskResult } from "@/types/result";

type ResultStore = {
  result?: TaskResult;
  setResult: (r: TaskResult) => void;
};

export const useResultStore = create<ResultStore>((set) => ({
  setResult: (r) => set({ result: r }),
}));
