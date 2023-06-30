from django.utils.safestring import mark_safe


def page8_cars_func(aboniment_list):
    good_list = {}

    if aboniment_list is None:
        return aboniment_list

    for count in range(3):
        try:
            good_list[f'title1_{count + 1}'] = aboniment_list[count].title1
        except:
            good_list[f'title1_{count + 1}'] = False

        try:
            good_list[f'title2_{count + 1}'] = aboniment_list[count].title2
        except:
            good_list[f'title2_{count + 1}'] = False

        try:
            good_list[f'birka_{count + 1}'] = mark_safe(aboniment_list[count].birka)
        except:
            good_list[f'birka_{count + 1}'] = False

        try:
            good_list[f'desc_{count + 1}'] = mark_safe(aboniment_list[count].desc)
        except:
            good_list[f'desc_{count + 1}'] = False

        try:
            good_list[f'bonus_{count + 1}'] = mark_safe(aboniment_list[count].bonus)
        except:
            good_list[f'bonus_{count + 1}'] = False

        try:
            good_list[f'price_{count + 1}'] = aboniment_list[count].price
        except:
            good_list[f'price_{count + 1}'] = False

        try:
            good_list[f'button_{count + 1}'] = aboniment_list[count].button
        except:
            good_list[f'button_{count + 1}'] = False

        try:
            good_list[f'old_price_{count + 1}'] = aboniment_list[count].old_price
        except:
            good_list[f'old_price_{count + 1}'] = False

    return good_list
