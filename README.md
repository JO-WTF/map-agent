# 多 Agent 业务分析工作台（架构方案）

## 项目定位

这是一个**支持多 Agent 自由规划**的业务分析工作台，而不是单纯聊天机器人或单一物流计算工具。

核心目标：
- 一站式工作台：对话、地图、图表、表格、日志、下载、历史任务
- Agent 自由规划：按问题动态选择 Skill / Tool
- 可扩展：从物流场景扩展到更多业务分析场景

---

## 一、总体架构

```text
Next.js 前端
  ↓
FastAPI 后端
  ↓
LangGraph Agent Runtime
  ↓
Skill Registry / Tool Registry
  ↓
业务 Tools / Skills
  ↓
PostgreSQL + PostGIS / Redis / MinIO / 外部接口
```

### 分层职责

1. **前端（Next.js）**
   - 提供业务分析工作台 UI
   - 发起任务、展示实时状态、可视化结果

2. **后端 API（FastAPI）**
   - 处理文件上传、参数校验、任务编排入口
   - 调用 Agent Runtime 执行分析流程

3. **Agent Runtime（LangGraph）**
   - 承载自由规划、多步执行、缺参追问
   - 支持未来多 Agent 协作

4. **治理层（Registry）**
   - 管理 Tool/Skill 注册、版本、权限、审计

5. **业务能力层（Tools/Skills）**
   - 原子工具（Atomic Tools）
   - 组合技能（Composite Skills）

6. **基础设施层**
   - PostgreSQL/PostGIS：业务数据+空间能力
   - Redis + RQ/Celery：异步任务与状态
   - MinIO：上传文件与结果文件存储

---

## 二、前端设计

### 典型页面布局

- **左侧**：Agent 对话、文件上传、参数配置
- **中间**：Mapbox 地图（仓库、客户、分配连线）
- **右侧**：ECharts 图表（时效分布、仓库负载、客户统计）
- **底部**：明细表格、任务日志、结果下载

### 前端功能清单

- Agent 对话
- 文件上传
- Mapbox 地图展示
- ECharts 图表展示
- 结果表格
- 任务日志
- 任务状态
- 结果下载
- Skill / Tool 管理
- 任务历史

### 推荐技术栈

- Next.js
- TypeScript
- shadcn/ui
- Tailwind CSS
- Mapbox GL JS
- ECharts
- TanStack Table
- assistant-ui（或自研 ChatPanel）

---

## 三、后端设计

### 后端功能清单

- 上传文件
- 调用远程接口获取仓库信息
- 调用远程接口获取客户信息
- 执行地理计算
- 执行客户分配
- 执行时效计算
- 执行统计聚合
- 生成地图数据
- 生成图表数据
- 生成表格数据
- 支持 Agent 自由选择 Tool / Skill
- 支持多场景扩展
- 支持任务状态和任务历史

### 推荐技术栈

- FastAPI
- Pydantic
- LangGraph
- LangChain Tools
- PostgreSQL + PostGIS
- Redis
- Celery 或 RQ
- MinIO
- SQLAlchemy
- Alembic

---

## 四、Agent 运行时设计

### 为什么优先 LangGraph

你需要的是：
- 自由规划
- 动态工具选择
- 多场景扩展
- 缺参数追问
- 多 Agent 协作扩展

LangGraph 能直接支撑多步骤状态机与可控编排，比纯自研固定流程更适合当前目标。

### 自研与框架的边界

- **LangGraph 负责**：Agent 编排与执行路径控制
- **自研负责**：
  - Skill Registry
  - Tool Registry
  - 权限控制
  - 工具审计
  - 结果协议
  - 任务管理

---

## 五、Skill / Tool 体系

建议采用：**Atomic Tools + Composite Skills**

### 1）物流组合 Skill

`warehouse_customer_allocation_skill`

内部流程：
1. 获取仓库信息
2. 获取客户信息
3. 计算仓库 x 客户距离矩阵
4. 客户分配到最近仓库
5. 根据标准计算配送时效
6. 统计每个仓库、每个时效层的客户数量
7. 返回地图、图表、表格结果

### 2）原子 Tools

- `get_warehouses`
- `get_customers`
- `read_uploaded_file`
- `calculate_distance_matrix`
- `assign_nearest_warehouse`
- `calculate_delivery_sla`
- `aggregate_warehouse_sla_stats`
- `generate_map_data`
- `generate_chart_data`
- `generate_excel_report`

### 3）调用策略

- Agent 优先调用已验证的组合 Skill
- Skill 不覆盖的细分需求再回退到原子 Tool
- 通过 Registry 做版本、权限、审计与灰度发布

---

## 六、分阶段落地路线

### 阶段 1：最小可用版（MVP）

技术：
- Next.js + shadcn/ui + Mapbox + ECharts
- FastAPI + LangGraph
- 自研 Tool/Skill Registry
- Redis + RQ
- PostgreSQL
- 本地文件存储（或 MinIO）

实现能力：
- Agent 对话
- 文件上传
- 调用物流 Skill
- 地图展示仓库与客户
- 图表展示时效分布
- 表格展示分配明细
- 任务状态与日志

### 阶段 2：平台化增强

新增能力：
- Skill 管理
- Tool 管理
- 任务历史
- 结果下载
- PostGIS 空间查询
- MinIO 文件存储
- 工具权限与审计

### 阶段 3：多 Agent 化

新增能力：
- Supervisor Agent
- Data Agent
- Geo Agent
- Logistics Agent
- Analysis Agent
- Report Agent
- Visualization Agent
- Human-in-the-loop
- Checkpoint
- 任务恢复
- 调用链路回放

---

## 七、一句话结论

该项目应定位为：

> 基于 LangGraph 的多 Agent 业务分析工作台。前端用 Next.js 承载对话、地图、图表与任务管理；后端用 FastAPI 承载 API、文件、任务与业务 Skill；Tool/Skill 采用自研注册与治理机制。

最推荐组合：

- Next.js + shadcn/ui + Mapbox + ECharts
- FastAPI + LangGraph + PostgreSQL/PostGIS + Redis + MinIO
