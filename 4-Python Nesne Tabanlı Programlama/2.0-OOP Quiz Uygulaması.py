# Question
class Question():
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    # Kullanıcı doğru cevabı verirse true değer göndericek (self.answer == answer)
    def checckAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz():
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0  # listenin ilk elemanını işleme almak için (q1)

    def getQuestion(self):
        return self.questions[self.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print("Soru",self.questionsIndex + 1,":",question.text)

        for q in question.choices:
            print("-",q)

        answer = input("Cevap: ")
        self.quess(answer)
        self.loadQuestion()

    def quess(self, answer):
        question = self.getQuestion()

        if question.checckAnswer(answer):
            self.score += 1
        self.questionsIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score:",self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionsIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print("".center(10,"*"),"Question",questionNumber, "of", totalQuestion, "".center(10,"*"))


q1 = Question("En iyi programlama dili nedir ?", ["C#", "Python", "JavaScript", "Java"], "Python")
q2 = Question("En popüler programlama dili nedir ?", ["Python", "JavaScript", "C#", "Java"], "Python")
q3 = Question("En çok kazandıran programlama dili nedir ?", ["C#", "JavaScript", "Java", "Python"], "Python")
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()