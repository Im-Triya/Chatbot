from flask import Flask,jsonify,request
from flask_cors import CORS
from chat import get_response

app = Flask(__name__) 
CORS(app)
 


@app.route('/predict', methods=['POST'])
def reply():
    data = request.get_json()
    question = data.get('question', '')

    reply= get_response(question)
    
    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True)