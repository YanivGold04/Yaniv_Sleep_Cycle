from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/')
def sleep_cycle():
    current_time = datetime.now()
    cycle_length = 90
    updated_time = current_time

    result = []
    for cycle in range(1, 8):
        wake_up = (updated_time + timedelta(minutes=cycle_length)).strftime("%H:%M")
        result.append(f"Wake up {cycle}: {wake_up}")
        updated_time += timedelta(minutes=cycle_length)

    return "<br>".join(result)




