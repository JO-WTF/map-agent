export type TaskState = {
  currentTaskId?: string;
  status: "idle" | "queued" | "running" | "waiting_user_input" | "success" | "failed";
  progress: number;
  currentStep?: string;
};
