from form import FormRegister


if __name__ == '__main__':
    form = FormRegister()

    with open("test.txt") as test_file:

        for line in test_file:
            name, gender, rut, course, section, comment = line.split(";")
            comment = comment.strip("\n")

            rut_verified = form.check_rut(rut)

            if rut_verified:
                form.add_course(course, section)

                form.register_people_info(name, gender, comment)

        form.save_data("result.txt")