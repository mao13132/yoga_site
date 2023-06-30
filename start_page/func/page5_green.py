def page5_green(page5_row):
    good_list = {}

    if page5_row is None:
        return page5_row

    try:
        keyb = page5_row.title1.split()
    except:
        pass


    good_list['title2'] = page5_row.title2
    good_list['desc'] = page5_row.desc

    try:
        good_list['image'] = page5_row.image.url
    except:
        good_list['image'] = False

    try:
        good_list['title1_1'] = keyb[0]
    except:
        good_list['title1_1'] = False

    try:
        good_list['title1_2'] = keyb[1]
    except:
        good_list['title1_2'] = False

    try:
        good_list['title1_3'] = ' '.join(x for x in keyb[2:])
    except:
        good_list['title1_3'] = False

    try:
        if good_list['title1_3'] == []:
            good_list['title1_3'] = False
    except:
        good_list['title1_3'] = False

    return good_list
