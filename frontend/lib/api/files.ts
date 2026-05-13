import { BACKEND_BASE_URL } from "@/config/app";

export async function uploadFile(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BACKEND_BASE_URL}/api/files/upload`, {
    method: "POST",
    body: formData,
  });

  return res.json();
}
