# APS Scheduling System

[![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-5.0+-green.svg)](https://www.djangoproject.com/)
[![Vue Version](https://img.shields.io/badge/vue-3.x-brightgreen.svg)](https://vuejs.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> 高级计划与排程系统 - 为企业提供智能生产计划与排程管理解决方案

## 📋 项目简介

APS (Advanced Planning and Scheduling) 系统是一个基于 Web 的智能生产计划与排程管理系统。系统通过先进的排程算法，帮助企业优化生产计划，提高设备利用率，缩短订单交付周期。

### 🎯 核心功能

| 模块 | 功能 | 说明 |
|------|------|------|
| **订单管理** | 订单录入、状态跟踪、优先级管理 | 全生命周期订单管理 |
| **产品管理** | 产品信息、BOM 管理、工艺路线 | 产品数据统一维护 |
| **生产排程** | 智能排程算法、可视化甘特图 | 自动生成优化排程方案 |
| **工单管理** | 工单生成、进度跟踪、资源分配 | 生产过程实时监控 |

### 🏗️ 技术架构

#### 前端层 (Vue 3 + Vite)
- 订单管理模块
- 产品管理模块
- 排程视图模块
- 工单管理模块

#### API 层 (Django REST Framework)
- RESTful API 接口
- JWT 身份认证
- 接口权限控制

#### 业务逻辑层 (Django)
- 订单服务
- 产品服务
- 排程引擎
- 工单服务

#### 数据层
- 开发环境：SQLite
- 生产环境：PostgreSQL

### 🛠️ 技术栈

#### 后端
| 技术 | 版本 | 用途 |
|------|------|------|
| Python | 3.14+ | 核心编程语言 |
| Django | 5.0+ | Web 框架 |
| Django REST Framework | 3.14+ | API 框架 |
| APScheduler | 3.10+ | 定时任务调度 |
| PyMySQL | 1.1+ | MySQL 驱动 |

#### 前端
| 技术 | 版本 | 用途 |
|------|------|------|
| Vue | 3.4+ | 渐进式框架 |
| Vite | 5.0+ | 构建工具 |
| Element Plus | 2.5+ | UI 组件库 |
| Axios | 1.6+ | HTTP 客户端 |
| ECharts | 5.5+ | 图表可视化 |
| Pinia | 2.1+ | 状态管理 |

#### 数据库
| 环境 | 数据库 | 说明 |
|------|--------|------|
| 开发环境 | SQLite | 轻量级，无需配置 |
| 生产环境 | PostgreSQL | 性能稳定，功能强大 |

## 🚀 快速开始

### 环境要求

| 环境 | 版本要求 |
|------|----------|
| Python | 3.14 或更高版本 |
| Node.js | 18.x 或更高版本 |
| npm | 9.x 或更高版本 |
| Git | 2.x 或更高版本 |

### 安装步骤

#### 1. 克隆项目

```bash
git clone https://github.com/isick-cn/APS-System.git
cd APS-System
2. 后端配置
bash
# 进入后端目录
cd aps_backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver
后端服务将在 http://localhost:8000 启动

3. 前端配置
bash
# 打开新的终端，进入前端目录
cd aps_frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
前端服务将在 http://localhost:5173 启动

访问系统
服务	地址
前端页面	http://localhost:5173
API 接口	http://localhost:8000/api/
后台管理	http://localhost:8000/admin
API 文档	http://localhost:8000/api/docs/
📁 项目结构
text
APS-System/
├── aps_backend/                 # Django 后端项目
│   ├── apps/                    # 应用模块
│   │   ├── orders/              # 订单管理模块
│   │   ├── products/            # 产品管理模块
│   │   └── scheduling/          # 排程调度模块
│   ├── aps_backend/             # 项目配置
│   │   ├── settings.py          # 配置文件
│   │   ├── urls.py              # 路由配置
│   │   └── wsgi.py              # WSGI 入口
│   ├── manage.py                # Django 管理脚本
│   └── requirements.txt         # Python 依赖
├── aps_frontend/                # Vue 前端项目
│   ├── src/
│   │   ├── api/                 # API 接口
│   │   ├── components/          # 公共组件
│   │   ├── router/              # 路由配置
│   │   ├── stores/              # Pinia 状态管理
│   │   ├── views/               # 页面组件
│   │   ├── App.vue              # 根组件
│   │   └── main.js              # 入口文件
│   ├── index.html               # HTML 模板
│   ├── package.json             # npm 依赖
│   └── vite.config.js           # Vite 配置
├── .gitignore                   # Git 忽略文件
└── README.md                    # 项目文档
🔧 配置说明
环境变量
创建 .env 文件配置敏感信息：

bash
# Django 配置
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# 数据库配置 (生产环境)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=aps_db
DB_USER=aps_user
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
生产环境部署
bash
# 1. 收集静态文件
python manage.py collectstatic

# 2. 配置 Gunicorn
pip install gunicorn
gunicorn aps_backend.wsgi:application --bind 0.0.0.0:8000

# 3. 前端构建
cd aps_frontend
npm run build

# 4. 使用 Nginx 部署静态文件
Docker 部署 (可选)
bash
# 构建镜像
docker build -t aps-system .

# 运行容器
docker run -d -p 8000:8000 -p 5173:5173 aps-system
📊 数据库模型
订单表 (orders)
字段	类型	说明
id	Integer	主键
order_no	CharField(50)	订单编号
product	ForeignKey	关联产品
quantity	IntegerField	订单数量
due_date	DateTimeField	交货日期
priority	IntegerField	优先级 (1-10)
status	CharField(20)	订单状态
created_at	DateTimeField	创建时间
updated_at	DateTimeField	更新时间
产品表 (products)
字段	类型	说明
id	Integer	主键
product_code	CharField(50)	产品编码
name	CharField(100)	产品名称
bom	JSONField	BOM 结构
process_time	IntegerField	工艺时间(分钟)
created_at	DateTimeField	创建时间
工单表 (work_orders)
字段	类型	说明
id	Integer	主键
order	ForeignKey	关联订单
work_order_no	CharField(50)	工单编号
start_time	DateTimeField	计划开始时间
end_time	DateTimeField	计划结束时间
status	CharField(20)	工单状态
actual_start	DateTimeField	实际开始时间
actual_end	DateTimeField	实际结束时间
🔌 API 接口文档
模块	方法	端点	说明
订单	GET	/api/orders/	获取订单列表
订单	POST	/api/orders/	创建订单
订单	PUT	/api/orders/{id}/	更新订单
订单	DELETE	/api/orders/{id}/	删除订单
产品	GET	/api/products/	获取产品列表
产品	POST	/api/products/	创建产品
排程	GET	/api/schedule/	获取排程结果
排程	POST	/api/schedule/generate/	生成排程
工单	GET	/api/work-orders/	获取工单列表
🤝 贡献指南
Fork 本仓库

创建特性分支 (git checkout -b feature/AmazingFeature)

提交更改 (git commit -m 'Add some AmazingFeature')

推送到分支 (git push origin feature/AmazingFeature)

提交 Pull Request

代码规范
后端：遵循 PEP 8 规范

前端：使用 ESLint + Prettier

提交信息：遵循 Conventional Commits 规范

📝 版本历史
版本	日期	更新内容
v1.0.0	2026-03-25	初始版本发布
v1.0.0	2026-03-25	基础订单管理功能
v1.0.0	2026-03-25	产品 BOM 管理
v1.0.0	2026-03-25	可视化甘特图排程
📄 许可证
本项目采用 MIT 许可证 - 详见 LICENSE 文件

📧 联系方式
项目地址: https://github.com/isick-cn/APS-System

问题反馈: Issues