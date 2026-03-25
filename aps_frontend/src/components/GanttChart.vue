<template>
  <div ref="chartRef" style="height: 520px; width: 100%"></div>
</template>

<script setup>
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import * as echarts from "echarts";
import dayjs from "dayjs";

const props = defineProps({
  items: { type: Array, default: () => [] },
  selectedCenter: { type: String, default: "" }
});

const chartRef = ref();
let chart;

const renderChart = () => {
  const filtered = props.selectedCenter
    ? props.items.filter((x) => x.work_center === props.selectedCenter)
    : props.items;
  const centers = [...new Set(filtered.map((x) => x.work_center))];
  const seriesData = filtered.map((item) => ({
    name: item.material_name,
    value: [item.work_center, dayjs(item.start_time).valueOf(), dayjs(item.end_time).valueOf(), item.material_name]
  }));

  chart.setOption({
    tooltip: {
      formatter: (p) => {
        const v = p.data.value;
        return `${v[3]}<br/>设备: ${v[0]}<br/>${dayjs(v[1]).format("YYYY-MM-DD HH:mm")} - ${dayjs(v[2]).format("YYYY-MM-DD HH:mm")}`;
      }
    },
    grid: { left: 80, right: 30, top: 30, bottom: 30 },
    xAxis: { type: "time" },
    yAxis: { type: "category", data: centers },
    series: [
      {
        type: "custom",
        renderItem: (params, api) => {
          const categoryIndex = api.value(0);
          const start = api.coord([api.value(1), categoryIndex]);
          const end = api.coord([api.value(2), categoryIndex]);
          const height = api.size([0, 1])[1] * 0.6;
          return {
            type: "rect",
            shape: { x: start[0], y: start[1] - height / 2, width: end[0] - start[0], height },
            style: api.style()
          };
        },
        encode: { x: [1, 2], y: 0 },
        data: seriesData
      }
    ]
  });
};

onMounted(() => {
  chart = echarts.init(chartRef.value);
  renderChart();
});

watch(() => [props.items, props.selectedCenter], renderChart, { deep: true });

onBeforeUnmount(() => {
  if (chart) chart.dispose();
});
</script>
