def page4_cards(cards_list):
    good_list = {}

    for count in range(6):
        try:
            good_list[f'title{count + 1}'] = cards_list[count].title
        except:
            good_list[f'title{count + 1}'] = False

        try:
            good_list[f'desc{count + 1}'] = cards_list[count].desc
        except:
            good_list[f'desc{count + 1}'] = False

    return good_list
