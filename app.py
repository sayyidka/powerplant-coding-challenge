import json
import logging

from flask import Flask, request
import waitress

from ProductionPlanService import ProductionPlanService

app = Flask(__name__)

# Logger
logging.basicConfig(
    filename="logs/filelog.log",
    level=logging.WARNING,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


@app.post("/productionplan")
def give_production_plan():
    data = request.get_json()
    service = ProductionPlanService(data)
    try:
        return json.dumps(service.give_production_plan())
    except Exception as e:
        app.logger.error(e.with_traceback())


if __name__ == "__main__":
    # Production WSGI server
    waitress.serve(app, host="0.0.0.0", port="8888")
