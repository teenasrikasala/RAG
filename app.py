from flask import Flask,request,jsonify,render_template
from src.llmintegration import ans_que
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat",methods=["POST"])
def chat():
    data=request.get_json(silent=True) or {}
    question=data.get("question","").strip()
    if not question:
        return jsonify({"error":"enter the question"}),400
    try:
        result=ans_que(question)
        return jsonify({"answer": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__=="__main__":
    app.run(debug=True)