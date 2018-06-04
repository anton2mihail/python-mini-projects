class Profile:
    def __init__(self, name, age, id, city):
        self._id = id
        self._name = name
        self._age = age
        self._city = city

    def setRelationshipStatus(self, status):
        self._status = status

    def getRelationshipStatus(self):
        return self._status

    def setProfileStatus(self, prof):
        self._prof = prof

    def getProfileStatus(self):
        return self._prof

    def printProfile(self):
        return self._name+", "+self._age+", "+self._city+", "+self._status+", "+self._prof
