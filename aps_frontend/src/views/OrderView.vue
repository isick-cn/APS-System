<template>
  <div>
    <el-space style="margin-bottom: 12px">
      <el-button type="primary" @click="openCreate">新增订单</el-button>
      <el-button @click="loadData">刷新</el-button>
    </el-space>

    <el-table :data="orders" border>
      <el-table-column prop="order_no" label="订单号" />
      <el-table-column prop="product_name" label="产品" />
      <el-table-column prop="quantity" label="数量" />
      <el-table-column prop="order_date" label="订单日期" />
      <el-table-column prop="due_date" label="交货日期" />
      <el-table-column label="状态">
        <template #default="{ row }">
          <el-tag>{{ statusText(row.status) }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="260">
        <template #default="{ row }">
          <el-button link type="primary" @click="openEdit(row)">编辑</el-button>
          <el-button link type="danger" @click="removeRow(row)">删除</el-button>
          <el-button link type="success" @click="generate(row)">生成工单</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="dialogVisible" :title="form.id ? '编辑订单' : '新增订单'" width="500px">
      <el-form ref="formRef" :model="form" :rules="rules" label-width="100px">
        <el-form-item label="订单号"><el-input v-model="form.order_no" /></el-form-item>
        <el-form-item label="产品">
          <el-select v-model="form.product">
            <el-option v-for="m in finishedMaterials" :key="m.id" :label="m.name" :value="m.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="数量"><el-input-number v-model="form.quantity" :min="1" /></el-form-item>
        <el-form-item label="订单日期"><el-date-picker v-model="form.order_date" value-format="YYYY-MM-DD" /></el-form-item>
        <el-form-item label="交货日期"><el-date-picker v-model="form.due_date" value-format="YYYY-MM-DD" /></el-form-item>
        <el-form-item label="状态">
          <el-select v-model="form.status">
            <el-option label="草稿" value="draft" />
            <el-option label="已确认" value="confirmed" />
            <el-option label="生产中" value="processing" />
            <el-option label="已完成" value="completed" />
            <el-option label="已取消" value="cancelled" />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="submit">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import dayjs from "dayjs";
import { api, getErrorMessage } from "../api";

const orders = ref([]);
const materials = ref([]);
const dialogVisible = ref(false);
const formRef = ref();
const form = ref({
  id: null,
  order_no: "",
  product: null,
  quantity: 1,
  order_date: "",
  due_date: "",
  status: "draft"
});
const rules = {
  order_no: [{ required: true, message: "请输入订单号", trigger: "blur" }],
  product: [{ required: true, message: "请选择产品", trigger: "change" }],
  quantity: [{ required: true, message: "请输入数量", trigger: "blur" }],
  order_date: [{ required: true, message: "请选择订单日期", trigger: "change" }],
  due_date: [{ required: true, message: "请选择交货日期", trigger: "change" }]
};

const finishedMaterials = computed(() => materials.value.filter((m) => m.type === "finished"));

const loadData = async () => {
  try {
    const [oRes, mRes] = await Promise.all([api.getOrders(), api.getMaterials()]);
    orders.value = oRes.data;
    materials.value = mRes.data;
  } catch (error) {
    ElMessage.error(getErrorMessage(error));
  }
};

const openCreate = () => {
  form.value = { id: null, order_no: "", product: null, quantity: 1, order_date: "", due_date: "", status: "draft" };
  dialogVisible.value = true;
};

const openEdit = (row) => {
  form.value = { ...row };
  dialogVisible.value = true;
};

const submit = async () => {
  try {
    await formRef.value.validate();
    if (dayjs(form.value.due_date).isBefore(dayjs(form.value.order_date))) {
      ElMessage.warning("交货日期不能早于订单日期");
      return;
    }
    if (form.value.id) await api.updateOrder(form.value.id, form.value);
    else await api.createOrder(form.value);
    dialogVisible.value = false;
    ElMessage.success("保存成功");
    loadData();
  } catch (error) {
    if (error) ElMessage.error(getErrorMessage(error));
  }
};

const removeRow = async (row) => {
  try {
    await ElMessageBox.confirm("确认删除该订单？", "提示");
    await api.deleteOrder(row.id);
    ElMessage.success("删除成功");
    loadData();
  } catch (error) {
    if (error !== "cancel") ElMessage.error(getErrorMessage(error));
  }
};

const generate = async (row) => {
  try {
    await api.generateWorkorders(row.id);
    ElMessage.success("工单生成成功");
  } catch (error) {
    ElMessage.error(getErrorMessage(error));
  }
};

const statusText = (v) => ({
  draft: "草稿",
  confirmed: "已确认",
  processing: "生产中",
  completed: "已完成",
  cancelled: "已取消"
}[v] || v);

onMounted(loadData);
</script>
