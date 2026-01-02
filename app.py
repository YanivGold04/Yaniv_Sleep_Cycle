from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def sleep_cycle():
    current_time = datetime.now() + timedelta(hours=2)
    cycle_length = 90

    result = []
    updated_time = current_time

    for cycle in range(1, 8):
        updated_time += timedelta(minutes=cycle_length)
        wake_up = updated_time.strftime("%H:%M")
        result.append((cycle, wake_up))

    return render_template(
        "index.html",
        current_time=current_time.strftime("%H:%M"),
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
