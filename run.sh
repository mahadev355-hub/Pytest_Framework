echo "starting my script"
echo "activating virtual environment"
source .venv/bin/activate
pytest -s -v --html reports/report.html
