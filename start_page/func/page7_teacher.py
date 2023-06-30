def page7_teacher_func(teachers_list):
    good_list = {}

    for count in range(3):
        try:
            good_list[f'name_{count + 1}'] = teachers_list[count].name
        except:
            good_list[f'name_{count + 1}'] = False

        try:
            good_list[f'desc_{count + 1}'] = teachers_list[count].desc
        except:
            good_list[f'desc_{count + 1}'] = False

        try:
            good_list[f'image_{count + 1}'] = teachers_list[count].image.url
        except:
            good_list[f'image_{count + 1}'] = False

    return good_list
