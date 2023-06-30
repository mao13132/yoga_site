def func_page5_cards(cards_List):
    good_list = {}

    for count in range(4):
        try:
            good_list[f'title1_{count + 1}'] = cards_List[count].title1
        except:
            good_list[f'title1_{count + 1}'] = False


        try:
            good_list[f'title2_{count + 1}'] = cards_List[count].title2
        except:
            good_list[f'title2_{count + 1}'] = False

        try:
            good_list[f'desc_{count + 1}'] = cards_List[count].title2
        except:
            good_list[f'desc_{count + 1}'] = False

    return good_list
