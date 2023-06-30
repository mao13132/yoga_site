def lead_page_func(lead_page):
    good_list = {}

    if lead_page is None:
        return lead_page

    try:
        keyb = lead_page.title1.split()
    except:
        pass

    good_list['title2'] = lead_page.title2
    good_list['button'] = lead_page.button

    try:
        good_list['image'] = lead_page.image.url
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
        good_list['title1_3'] = keyb[2]
    except:
        good_list['title1_3'] = False

    try:
        good_list['title1_4'] = ' '.join(x for x in keyb[3:])
    except:
        good_list['title1_4'] = False

    try:
        if good_list['title1_4'] == []:
            good_list['title1_4'] = False
    except:
        good_list['title1_4'] = False

    return good_list
