class School:
    def __init__(self):
        self._students = {}
        self._add_history = []

    def add_student(self, name, grade):
        for students in self._students.values():
            if name in students:
                self._add_history.append(False)
                return
        if grade not in self._students:
            self._students[grade] = set()
        self._students[grade].add(name)
        self._add_history.append(True)
    def roster(self):
        result = []
        for grade in sorted(self._students.keys()):
            for name in sorted(self._students[grade]):
                result.append(name)
        return result

    def grade(self, grade_number):
        return sorted(self._students.get(grade_number, set()))

    def added(self):
        return self._add_history
