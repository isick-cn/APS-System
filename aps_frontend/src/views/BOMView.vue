<template>
  <div>
    <el-space style="margin-bottom: 12px">
      <el-button type="primary" @click="openCreate">新增 BOM 节点</el-button>
      <el-button @click="loadData">刷新</el-button>
    </el-space>

    <el-tree :data="bomTree" node-key="id" default-expand-all>
      <template #default="{ data }">
        <span>{{ data.material_name }} -> {{ data.child_material_name }} x {{ data.quantity }}</span>
        <el-button link type="primary" @click="openEdit(data)">编辑</el-button>
        <el-button link type="danger" @click="removeNode(data)">删除</el-button>
      </template>
    </el-tree>

    <el-dialog v-model="dialogVisible" :title="form.id ? '编辑 BOM' : '新增 BOM'" width="480px">
      <el-form ref="formRef" :model="form" :rules="rules" label-width="100px">
        <el-form-item label="父节点">
          <el-select v-model="form.parent" clearable placeholder="可选">
            <el-option v-for="item in flatNodes" :key="item.id" :label="nodeLabel(item)" :value="item.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="父物料">
          <el-select v-model="form.material" placeholder="请选择">
            <el-option v-for="m in materials" :key="m.id" :label="m.name" :value="m.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="子物料">
          <el-select v-model="form.child_material" placeholder="请选择">
            <el-option v-for="m in materials" :key="m.id" :label="m.name" :value="m.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="用量">
          <el-input-number v-model="form.quantity" :min="0.01" :step="0.01" />
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
import { api, getErrorMessage } from "../api";

const bomTree = ref([]);
const materials = ref([]);
const dialogVisible = ref(false);
const formRef = ref();
const form = ref({ id: null, parent: null, material: null, child_material: null, quantity: 1 });
const rules = {
  material: [{ required: true, message: "请选择父物料", trigger: "change" }],
  child_material: [{ required: true, message: "请选择子物料", trigger: "change" }],
  quantity: [{ required: true, message: "请输入用量", trigger: "blur" }]
};

const flatNodes = computed(() => {
  const result = [];
  const walk = (nodes) => {
    nodes.forEach((n) => {
      result.push(n);
      if (n.children?.length) walk(n.children);
    });
  };
  walk(bomTree.value);
  return result;
});

const nodeLabel = (n) => `${n.material_name} -> ${n.child_material_name}`;

const loadData = async () => {
  try {
    const [bomRes, mRes] = await Promise.all([api.getBOM(), api.getMaterials()]);
    bomTree.value = bomRes.data;
    materials.value = mRes.data;
  } catch (error) {
    ElMessage.error(getErrorMessage(error));
  }
};

const openCreate = () => {
  form.value = { id: null, parent: null, material: null, child_material: null, quantity: 1 };
  dialogVisible.value = true;
};

const openEdit = (row) => {
  form.value = {
    id: row.id,
    parent: row.parent,
    material: row.material,
    child_material: row.child_material,
    quantity: Number(row.quantity)
  };
  dialogVisible.value = true;
};

const submit = async () => {
  try {
    await formRef.value.validate();
    if (form.value.material === form.value.child_material) {
      ElMessage.warning("父物料与子物料不能相同");
      return;
    }
    if (form.value.id) {
      await api.updateBOM(form.value.id, form.value);
    } else {
      await api.createBOM(form.value);
    }
    dialogVisible.value = false;
    ElMessage.success("保存成功");
    loadData();
  } catch (error) {
    if (error) ElMessage.error(getErrorMessage(error));
  }
};

const removeNode = async (row) => {
  try {
    await ElMessageBox.confirm("确认删除该节点？", "提示");
    await api.deleteBOM(row.id);
    ElMessage.success("删除成功");
    loadData();
  } catch (error) {
    if (error !== "cancel") ElMessage.error(getErrorMessage(error));
  }
};

onMounted(loadData);
</script>
