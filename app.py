from flask import Flask, request, jsonify
from underwriting_rules import evaluate
from db import save_underwriting
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/underwrite', methods=['POST'])
def underwrite():
    start_time = time.time()
    payload = request.json
    logger.info(f" Evaluating Risk Score for applicant ID: {payload['applicant_info']['applicant_id']}")
    decision = evaluate(payload['applicant_info'], payload['risk_score'])
    save_underwriting(payload['applicant_info']['applicant_id'], decision)
    logger.info(f"Underwriting decision saved for applicant ID {payload['applicant_info']['applicant_id']}")
    logger.info(f"Underwriting decision took {time.time() - start_time:.2f}s")
    return jsonify(decision)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)