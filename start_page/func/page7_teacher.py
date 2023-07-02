
def get_css(teachers_list, good_list):
    if len(teachers_list) < 4:
        good_list['mob'] = 0
        good_list['mob_lit'] = 0
        good_list['full'] = 0
        good_list['middle2'] = 0
        good_list['hard'] = 0

    elif len(teachers_list) == 4:
        good_list['mob'] = 650
        good_list['mob_lit'] = 460
        good_list['full'] = 670
        good_list['middle2'] = 760
        good_list['hard'] = 540
    elif len(teachers_list) == 5:
        good_list['mob'] = 1180
        good_list['mob_lit'] = 760
        good_list['full'] = 1140
        good_list['middle2'] = 1410
        good_list['hard'] = 890
    elif len(teachers_list) == 6:
        good_list['mob'] = 1715
        good_list['mob_lit'] = 1085
        good_list['full'] = 1655
        good_list['middle2'] = 2025
        good_list['hard'] = 1320

    return good_list

def page7_teacher_func(teachers_list):
    good_list = {}

    if teachers_list is None:
        return teachers_list

    good_list = get_css(teachers_list, good_list)

    for count in range(6):
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
