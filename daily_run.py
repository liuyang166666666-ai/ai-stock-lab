import json
from pathlib import Path
from datetime import datetime

from jinja2 import Template


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sample_events.json"
OUT_DIR = ROOT / "outputs"
REPORT = OUT_DIR / "report.html"


HTML_TMPL = Template(
    """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <title>ai-stock-lab | Daily Report</title>
  <style>
    body{font-family:Arial,Helvetica,sans-serif;margin:24px;line-height:1.5}
    .muted{color:#666}
    .card{border:1px solid #ddd;border-radius:10px;padding:14px;margin:12px 0}
    .pos{color:#0a7d2c;font-weight:700}
    .neg{color:#b00020;font-weight:700}
    code{background:#f6f6f6;padding:2px 6px;border-radius:6px}
  </style>
</head>
<body>
  <h1>Daily Report</h1>
  <div class="muted">Generated at {{ now }}</div>

  <h2>Events ({{ events|length }})</h2>
  {% for e in events %}
  <div class="card">
    <div><b>{{ e.title }}</b></div>
    <div class="muted">{{ e.ts }} | source: {{ e.source }} | category: {{ e.category }}</div>
    <p>{{ e.summary }}</p>
    <div>
      direction:
      {% if e.direction == "positive" %}
        <span class="pos">positive</span>
      {% else %}
        <span class="neg">negative</span>
      {% endif %}
      | impact_hint: <code>{{ e.impact_hint }}</code>
    </div>
    <div>tickers: <code>{{ e.tickers | join(", ") }}</code></div>
  </div>
  {% endfor %}

  <hr/>
  <div class="muted">MVP: sample data only. Next: real news parser + scoring.</div>
</body>
</html>"""
)


def main():
    if not DATA.exists():
        raise FileNotFoundError(f"Missing sample data: {DATA}")

    events = json.loads(DATA.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = HTML_TMPL.render(now=now, events=events)

    REPORT.write_text(html, encoding="utf-8")
    print(f"[OK] report generated: {REPORT}")


if __name__ == "__main__":
    main()
