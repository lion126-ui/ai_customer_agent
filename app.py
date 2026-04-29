
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def intent_agent(message):
    if "投诉" in message:
        return "complaint"
    elif "故障" in message:
        return "issue"
    else:
        return "faq"

def routing_agent(intent):
    if intent == "faq":
        return "L1"
    elif intent == "issue":
        return "L2"
    else:
        return "L3"

def ai_response(message):
    return "AI回复：我们已收到您的问题：" + message

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message")

    intent = intent_agent(msg)
    level = routing_agent(intent)

    if level == "L1":
        reply = ai_response(msg)
        status = "AI已解决"
    else:
        reply = "已为您转人工客服（级别：%s）" % level
        status = "转人工"

    result = {
        "intent": intent,
        "level": level,
        "reply": reply,
        "status": status
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=5000)
