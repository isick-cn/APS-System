import { createRouter, createWebHistory } from "vue-router";
import BOMView from "../views/BOMView.vue";
import OrderView from "../views/OrderView.vue";
import WorkOrderView from "../views/WorkOrderView.vue";
import ScheduleView from "../views/ScheduleView.vue";

const routes = [
  { path: "/", redirect: "/orders" },
  { path: "/bom", component: BOMView },
  { path: "/orders", component: OrderView },
  { path: "/workorders", component: WorkOrderView },
  { path: "/schedule", component: ScheduleView }
];

export default createRouter({
  history: createWebHistory(),
  routes
});
