from .models import QuizStudent

class Quiz():
    def __init__(self, request):
        self.session = request.session
        quiz = self.session.get('sessionid')
        if 'sessionid' not in request.session:
            quiz = self.session['sessionid'] = {}
        self.quiz = quiz

    def answer(self, q, option):
        question_value = q
        question_option = option
        print(question_value)
        print(question_option)
        if question_value in self.quiz:
            self.quiz['question_value']['ans'] = option
        self.save()

    def update_answer(self, q, option, **args):
        question_value = q.question
        if question_value in self.quiz:
            self.quiz[question_value]['ans'] = option
        self.save()

    def score(self, option, correct):
        score = 0
        question_option = option
        question_answer = correct
        if question_option == question_answer:
            score+= 1
        return score
    
    def save(self):
        self.session.modified = True