from flask import Flask, request, jsonify
from underwriting_rules import evaluate
from db import save_underwriting

app = Flask(__name__)

@app.route('/underwrite', methods=['POST'])
def underwrite():
    payload = request.json
    print(f" Evaluating Risk Score for applicant ID: {payload['applicant_info']['applicant_id']}")
    decision = evaluate(payload['applicant_info'], payload['risk_score'])
    print(f" Underwriting decision for applicant ID {payload['applicant_info']['applicant_id']}: {decision}")
    save_underwriting(payload['applicant_info']['applicant_id'], decision)
    print(f"Underwriting decision saved for applicant ID {payload['applicant_info']['applicant_id']}")
    return jsonify(decision)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)