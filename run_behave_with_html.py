# run_behave_with_html.py
from behave.__main__ import main

main([
    'features/',
    '-f', 'behave_html_formatter.HTMLFormatter',
    '-o', 'reports/behave_report.html'
])
