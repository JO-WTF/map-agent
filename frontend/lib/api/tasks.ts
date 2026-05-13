import { BACKEND_BASE_URL } from "@/config/app";

export async function getTaskResult(taskId: string) {
  const res = await fetch(`${BACKEND_BASE_URL}/api/tasks/${taskId}/result`);
  return res.json();
}
