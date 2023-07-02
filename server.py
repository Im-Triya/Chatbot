from flask import Flask,jsonify,request
from chat import get_response

app = Flask(__name__) 


# @app.post("/predict")
# def predict():
#     text= request.get_json().get("message")
#     response = get_response(text)
#     message = {"answer": response}

#     return jsonify(message)


@app.route('/predict', methods=['POST'])
def reply():
    data = request.get_json()
    question = data.get('question', '')

    reply= get_response(question)
    
    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True)