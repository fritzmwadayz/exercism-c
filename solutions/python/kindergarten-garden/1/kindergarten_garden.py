STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
MAPPING = {
    "G":"Grass",
    "C":"Clover",
    "R":"Radishes",
    "V":"Violets"
}
class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.students = sorted(students)
        self.diagram = diagram
    def plants(self, student):
        rows = self.diagram.splitlines()
        start = 2 * self.students.index(student)
        result = []
        for row in rows:
            plant_codes = row[start:start+2]
            result.extend([MAPPING[code] for code in plant_codes])
        return result