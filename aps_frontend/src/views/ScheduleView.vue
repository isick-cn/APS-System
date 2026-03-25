<template>
  <div>
    <el-space style="margin-bottom: 12px">
      <el-button type="primary" @click="runSchedule">执行排程</el-button>
      <el-select v-model="selectedCenter" clearable placeholder="按设备筛选" style="width: 200px">
        <el-option v-for="c in centers" :key="c" :label="c" :value="c" />
      </el-select>
    </el-space>

    <GanttChart :items="scheduleResults" :selected-center="selectedCenter" />
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { ElMessage } from "element-plus";
import { api, getErrorMessage } from "../api";
import GanttChart from "../components/GanttChart.vue";

const scheduleResults = ref([]);
const selectedCenter = ref("");

const centers = computed(() => [...new Set(scheduleResults.value.map((x) => x.work_center))]);

const flattenTree = (nodes) => {
  const result = [];
  const walk = (list) => {
    list.forEach((item) => {
      result.push(item);
      if (item.children?.length) walk(item.children);
    });
  };
  walk(nodes);
  return result;
};

const loadData = async () => {
  try {
    const res = await api.getWorkorders();
    scheduleResults.value = flattenTree(res.data)
      .filter((x) => x.start_time && x.end_time)
      .map((x) => ({
        work_order_id: x.id,
        material_name: x.material_name,
        work_center: x.assigned_work_center,
        start_time: x.start_time,
        end_time: x.end_time
      }));
  } catch (error) {
    ElMessage.error(getErrorMessage(error));
  }
};

const runSchedule = async () => {
  try {
    const res = await api.schedule();
    scheduleResults.value = res.data;
    ElMessage.success("排程完成");
  } catch (error) {
    ElMessage.error(getErrorMessage(error));
  }
};

onMounted(loadData);
</script>
