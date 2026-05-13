import { API_PROXY_PREFIX } from "@/config/app";

export async function uploadFile(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_PROXY_PREFIX}/api/files/upload`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error(`文件上传失败（${res.status}）`);
  }
  return res.json();
}
