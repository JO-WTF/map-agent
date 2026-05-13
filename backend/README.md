# Backend

实现了以下模块：
- FastAPI API 层（chat/files/tasks/skills/tools/results）
- Supervisor Agent Runtime（简化 LangGraph 风格节点规划）
- Skill / Tool Registry
- warehouse_customer_allocation_skill
- 统一结果包（summary/map_data/charts/tables/files/logs）

运行：
```bash
cd backend
pip install -r requirements.txt
PYTHONPATH=. uvicorn app.main:app --reload
```
