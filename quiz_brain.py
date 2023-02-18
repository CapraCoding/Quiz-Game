class QuizBrain:

    def start(self):
        print('The Quiz Game will start ')
        print('To stop answer "STOP" ')
        print('')
        # Call next question
        self.next_question()

    def next_question(self):

        #Define the current question from the original list
        current_question = self.q_list[self.question_number]

        #Get the number 1 to show correctly in terminal
        self.question_number += 1

        #Print The question and get/validate the answer
        print(f'Q.{self.question_number}: {current_question.text}')
        self.validate_answer(input('True OR False? '), current_question.answer)
        print('')

        #Validate if there is more questions
        while self.still_has_questions() == True:
            self.next_question()
        else:
            self.finish()

    def still_has_questions(self):
        if self.question_number <= len(self.q_list):
            return True
        else:
            return False

    def validate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Your answer was correct!')
            print(f'Your score is: {self.score}/{self.question_number}')

        elif user_answer.lower() == 'stop':
            self.finish()
        else:
            print('Your answer was wrong!')
            print(f'Your score is: {self.score}/{self.question_number}')

    def finish(self):
        if self.score >= 3:
            print('Congratulations!')
            print(f'Your score was: {self.score}/{self.question_number}')
        else:
            print(f'Your score was: {self.score}/{self.question_number}')

        exit()

    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0
