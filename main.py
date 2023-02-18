from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from random import shuffle

question_bank = [Question(question['text'], question['answer']) for question in question_data]
shuffle(question_bank)
quiz = QuizBrain(question_bank)

quiz.start()
