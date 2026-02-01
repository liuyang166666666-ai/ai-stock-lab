# ai-stock-lab

本项目是一个 **本地优先（local-first）** 的股票事件驱动分析与决策辅助工具（MVP）。

## 目标（MVP）
- 抓取/导入新闻事件（先用本地样例 JSON）
- 事件标准化：时间、来源、类别、影响方向、涉及标的
- 生成当日报告：`report.html`
- 提供回测脚本入口：`backtest.py`（MVP 先跑通流程）

## 运行方式（本地）
> 先把仓库 clone 到本地再跑（后面我带你做）
- Python 3.10+
- 安装依赖：`pip install -r requirements.txt`
- 运行：`python daily_run.py`

## 输出
- `outputs/report.html`：当日事件与影响分析报告（MVP）

