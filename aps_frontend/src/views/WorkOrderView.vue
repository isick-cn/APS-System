<template>
  <div>
    <el-space style="margin-bottom: 12px">
      <el-button @click="loadData">刷新</el-button>
    </el-space>

    <el-table :data="workorders" row-key="id" border default-expand-all :tree-props="{ children: 'children' }">
      <el-table-column prop="order_no" label="订单号" />
      <el-table-column prop="material_name" label="物料" />
      <el-table-column prop="quantity" label="数量" />
      <el-table-column prop="level" label="层级" />
      <el-table-column prop="status" label="状态" />
      <el-table-column prop="assigned_work_center" label="设备" />
      <el-table-column prop="start_time" label="开始时间" />
      <el-table-column prop="end_time" label="结束时间" />
    </el-table>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { ElMessage } from "element-plus";
import { api, getErrorMessage } from "../api";

const workorders = ref([]);

const loadData = async () => {
  try {
    const res = await api.getWorkorders();
    workorders.value = res.data;
  } catch (error) {
    ElMessage.error(getErrorMessage(error));
  }
};

onMounted(loadData);
</script>
