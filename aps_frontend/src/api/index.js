import axios from "axios";

const request = axios.create({
  baseURL: "/",
  timeout: 10000
});

export const getErrorMessage = (error) => {
  const data = error?.response?.data;
  if (!data) return error?.message || "请求失败，请稍后重试";
  if (typeof data === "string") return data;
  if (data.detail) return data.detail;
  const firstKey = Object.keys(data)[0];
  if (firstKey) {
    const value = data[firstKey];
    if (Array.isArray(value)) return `${firstKey}: ${value.join("，")}`;
    return `${firstKey}: ${value}`;
  }
  return "请求失败，请检查输入";
};

export const api = {
  getMaterials: () => request.get("/api/materials/"),
  createMaterial: (data) => request.post("/api/materials/", data),
  getBOM: () => request.get("/api/bom/"),
  createBOM: (data) => request.post("/api/bom/", data),
  updateBOM: (id, data) => request.put(`/api/bom/${id}/`, data),
  deleteBOM: (id) => request.delete(`/api/bom/${id}/`),
  getOrders: () => request.get("/api/orders/"),
  createOrder: (data) => request.post("/api/orders/", data),
  updateOrder: (id, data) => request.put(`/api/orders/${id}/`, data),
  deleteOrder: (id) => request.delete(`/api/orders/${id}/`),
  generateWorkorders: (id) => request.post(`/api/orders/${id}/generate_workorders/`),
  getWorkorders: () => request.get("/api/workorders/"),
  getWorkCenters: () => request.get("/api/workcenters/"),
  createWorkCenter: (data) => request.post("/api/workcenters/", data),
  schedule: () => request.post("/api/schedule/")
};

export default request;
