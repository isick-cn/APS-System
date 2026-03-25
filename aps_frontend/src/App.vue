<template>
  <el-container style="height: 100vh">
    <el-aside width="220px">
      <el-menu :default-active="$route.path" router>
        <el-menu-item index="/bom">BOM 管理</el-menu-item>
        <el-menu-item index="/orders">订单管理</el-menu-item>
        <el-menu-item index="/workorders">工单管理</el-menu-item>
        <el-menu-item index="/schedule">排程甘特图</el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header style="font-size: 18px; font-weight: bold">APS 生产排程系统</el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>
