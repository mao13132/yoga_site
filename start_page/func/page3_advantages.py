def page3_advantages(advantag_list):
    good_list = {}

    for count in range(6):
        try:
            good_list[f'title{count + 1}'] = advantag_list[count].title
        except:
            good_list[f'title{count + 1}'] = False

    return good_list
