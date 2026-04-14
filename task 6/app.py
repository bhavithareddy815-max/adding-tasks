from flask import Flask, render_template
from repository.log_repository import get_daily_activity_report, get_detailed_logs

app = Flask(__name__)

@app.route('/report')
def report():
    daily_report = get_daily_activity_report()
    detailed_logs = get_detailed_logs()

    return render_template(
        'report.html',
        daily_report=daily_report,
        detailed_logs=detailed_logs
    )

if __name__ == '__main__':
    app.run(debug=True)