import { API_PROXY_PREFIX } from "@/config/app";

export async function getTaskResult(taskId: string) {
  const res = await fetch(`${API_PROXY_PREFIX}/api/tasks/${taskId}/result`);
  if (!res.ok) {
    throw new Error(`获取任务结果失败（${res.status}）`);
  }
  return res.json();
}
