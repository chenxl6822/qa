from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# 模拟题目数据，包含题目、选项、答案和题型
questions = [
    {
        "id": 1,
        "question": "以下哪种水果是红色的？",
        "options": ["苹果", "香蕉", "梨"],
        "answer": "苹果",
        "type": "单选题"
    },
    {
        "id": 2,
        "question": "以下哪些是蔬菜？",
        "options": ["胡萝卜", "草莓", "黄瓜"],
        "answer": ["胡萝卜", "黄瓜"],
        "type": "多选题"
    },
    {
        "id": 3,
        "question": "地球是方的。",
        "answer": False,
        "type": "判断题"
    }
]

# 存储用户做题记录，格式为 {user_id: {question_id: user_answer}}
user_answers = {}

# 获取随机题目
@app.route('/get_question', methods=['GET'])
def get_question():
    question = random.choice(questions)
    return jsonify(question)

# 提交答案
@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    user_id = data.get('user_id')
    question_id = data.get('question_id')
    user_answer = data.get('user_answer')

    if user_id not in user_answers:
        user_answers[user_id] = {}
    user_answers[user_id][question_id] = user_answer

    return jsonify({"message": "答案提交成功"})

# 获取做题结果
@app.route('/get_result', methods=['POST'])
def get_result():
    data = request.get_json()
    user_id = data.get('user_id')
    correct_count = 0
    total_count = len(user_answers[user_id])

    for question_id, user_answer in user_answers[user_id].items():
        question = next((q for q in questions if q["id"] == question_id), None)
        if question:
            if question["type"] == "单选题":
                if user_answer == question["answer"]:
                    correct_count += 1
            elif question["type"] == "多选题":
                if set(user_answer) == set(question["answer"]):
                    correct_count += 1
            elif question["type"] == "判断题":
                if user_answer == question["answer"]:
                    correct_count += 1

    score = correct_count * 100 / total_count if total_count > 0 else 0
    accuracy = correct_count / total_count if total_count > 0 else 0

    return jsonify({"score": score, "accuracy": accuracy})


if __name__ == '__main__':
    app.run(debug=True)