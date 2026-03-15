import json
from questions import QuestionFactory

def load_quiz(filepath):
    with open(filepath) as f:
        data = json.load(f)

    questions = []
    for q in data["questions"]:
        question = QuestionFactory.create(
            question_type=q["type"],
            question=q["question"],
            correct_answer=q["correct_answer"],
            options=q.get("options", None)
        )
        questions.append(question)

    return questions