class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while (counter != len(students)):
            if (students[0]!= sandwiches[0]):
                student_value = students[0]
                students.pop(0)
                students.append(student_value)
                counter = counter +1
            else:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0
        return len(students)




        