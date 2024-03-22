import asyncio
from flask import Flask, render_template, request, jsonify
from policyguard import PolicyGuard

app = Flask(__name__)

# Async function to use the PolicyGuard library
async def use_policy_guard(password):
    pg = PolicyGuard()
    policy_name = "password"
    input_json = {
        "input": {
            "password": password
        }
    }
    result = await pg.send_policy_request(policy_name, input_json)
    return result

@app.route("/")
async def render_index():
    return render_template("index.html")

@app.route("/check_password", methods=["POST"])
async def check_password():
    password = request.json.get("password")
    result = await use_policy_guard(password)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
