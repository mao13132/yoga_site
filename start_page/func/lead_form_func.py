from django.utils.safestring import mark_safe


def lead_form_func(from_title_list):
    good_list = {}

    if not from_title_list:
        return None

    for count in range(3):
        try:
            good_list[f'title1_{count + 1}'] = from_title_list[count].title1
        except:
            good_list[f'title1_{count + 1}'] = False

        try:
            good_list[f'title2_{count + 1}'] = from_title_list[count].title2
        except:
            good_list[f'title2_{count + 1}'] = False

        try:
            good_list[f'desc_{count + 1}'] = mark_safe(from_title_list[count].desc)
        except:
            good_list[f'desc_{count + 1}'] = False

        try:
            good_list[f'button_{count + 1}'] = from_title_list[count].button
        except:
            good_list[f'button_{count + 1}'] = False

    return good_list
