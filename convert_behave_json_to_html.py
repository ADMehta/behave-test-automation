# convert_behave_json_to_html.py
import json
from behave_json_formatter import BehaveHtmlFormatter

with open("reports/behave_report.json") as f:
    data = json.load(f)

formatter = BehaveHtmlFormatter()
html = formatter.format(data)

with open("reports/behave_report.html", "w") as f:
    f.write(html)
