"use client";
import { useTaskStore } from "@/stores/taskStore";

export function TaskStatusBar() {
  const { status, progress, currentTaskId, currentStep } = useTaskStore();
  return (
    <div className="mb-3 rounded border p-2 text-sm">
      <span className="mr-3">Task: {currentTaskId ?? "-"}</span>
      <span className="mr-3">Status: {status}</span>
      <span className="mr-3">Progress: {progress}%</span>
      <span>Step: {currentStep ?? "-"}</span>
    </div>
  );
}
