export async function getTaskResult(taskId: string) {
  const res = await fetch(`/api/tasks/${taskId}/result`);
  return res.json();
}
