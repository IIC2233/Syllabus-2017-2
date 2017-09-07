class FormRegister:
    def __init__(self):
        """
        NO TOCAR el init
        """
        self.courses = {
            "IIC1103": [0, 0, 0],  # IIC1103 tiene 2 secciones
            "IIC2233": [0, 0, 0, 0],  # IIC2233 tiene 3 secciones
            "IIC2115": [0, 0],  # IIC2115 tiene 1 seccion
            "IIE3115": [0, 0],  # IIC2115 tiene 1 seccion
            "IIC2332": [0, 0],  # IIC2115 tiene 1 seccion
            "IIC2515": [0, 0]  # IIC2115 tiene 1 seccion
        }

        self.register_list = []  # Almacena los alumnos que se inscribieron con exito

    def check_rut(self, rut):

        digits, checker = rut.split("-")
        digits = list(digits)

        for i in range(len(digits)):
            digits[i] = int(digits[i])

        list_number = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5]

        digits.reverse()
        total = 0
        for i in range(len(list_number)):
            total += digits[i] * list_number[i]

        rest = 11 - total % 11
        if rest == 11:
            rest = "0"
        elif rest == 10:
            rest = "k"
        else:
            rest = str(rest)

        return rest == checker

    def add_course(self, course, section):
        self.courses[course][int(section)] += 1

    def register_people_info(self, student_name, gender, comment):
        self.register_list.append([student_name, gender, comment])

    def save_data(self, path):
        with open(path, "w") as file:
            for register in self.register_list:
                text = "Student: {}\nGender: {}\nComment: {}\n".format(*register)
                file.write(text + "#"*40 + "\n")

            print("Informacion guardada con exito")
