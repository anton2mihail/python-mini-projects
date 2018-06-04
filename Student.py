class Student():
    def __init__(self, name):
        self._name = name
        self._score = 0
        self._num_quizzes = 0

    def getName(self):
        return self._name

    def addQuiz(self, score):
        self._score = self._score + score
        self._num_quizzes = self._num_quizzes + 1

    def getTotalScore(self):
        return self._score

    def getAverageScore(self):
        return self._score/self._num_quizzes
