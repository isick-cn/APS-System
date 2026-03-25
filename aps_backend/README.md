# APS 生产排程系统（Django + Vue 3）

本项目包含：

- 后端：`aps_backend`（Django + DRF + SQLite）
- 前端：`aps_frontend`（Vue 3 + Element Plus + ECharts）

## 后端安装与启动（Django）

1. 创建并激活虚拟环境（在 `d:\aps_backend`）

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 迁移数据库（SQLite）

```bash
python manage.py makemigrations
python manage.py migrate
```

4. 创建超级用户

```bash
python manage.py createsuperuser
```

5. 启动后端

```bash
python manage.py runserver 0.0.0.0:8000
```

## 前端安装与启动（Vue 3）

在 `d:\aps_frontend`：

```bash
npm install
npm run dev
```

## 初始化测试数据

推荐顺序：

1. 创建物料（至少 1 个成品）
2. 创建 BOM
3. 创建工作中心
4. 创建生产订单
5. 点击订单页“生成工单”
6. 点击排程页“执行排程”

也可一键初始化（推荐）：

```bash
python manage.py init_test_data
```

Shell 示例（`python manage.py shell`）：

```python
from apps.products.models import Material, BOM
from apps.orders.models import ProductionOrder
from apps.scheduling.models import WorkCenter
from datetime import date

p = Material.objects.create(code="FG001", name="成品A", type="finished")
s = Material.objects.create(code="SM001", name="半成品B", type="semi")
r = Material.objects.create(code="RM001", name="原料C", type="raw")
BOM.objects.create(material=p, child_material=s, quantity=2)
BOM.objects.create(material=s, child_material=r, quantity=3)
WorkCenter.objects.create(code="WC01", name="一号线")
ProductionOrder.objects.create(
    order_no="PO20260324001",
    product=p,
    quantity=10,
    order_date=date.today(),
    due_date=date.today(),
    status="confirmed"
)
```

## 访问地址

- 后端 Admin：`http://127.0.0.1:8000/admin/`
- API 文档（Swagger）：`http://127.0.0.1:8000/swagger/`
- API 文档（ReDoc）：`http://127.0.0.1:8000/redoc/`
- 前端：`http://127.0.0.1:5173`

## API 端点

- `GET/POST /api/materials/`
- `GET/POST /api/bom/`
- `GET/POST /api/orders/`
- `POST /api/orders/{id}/generate_workorders/`
- `GET /api/workorders/`
- `GET/POST /api/workcenters/`
- `POST /api/schedule/`
