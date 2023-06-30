from django.utils.safestring import mark_safe

def page6_sessions_func(sessions_lisst):
    good_list = {}

    for count in range(3):
        try:
            good_list[f'title1_{count + 1}'] = sessions_lisst[count].title1
        except:
            good_list[f'title1_{count + 1}'] = False

        try:
            good_list[f'title2_{count + 1}'] = sessions_lisst[count].title2
        except:
            good_list[f'title2_{count + 1}'] = False

        try:
            good_list[f'title3_{count + 1}'] = sessions_lisst[count].title3
        except:
            good_list[f'title3_{count + 1}'] = False

        try:
            good_list[f'title4_{count + 1}'] = mark_safe(sessions_lisst[count].title4)
        except:
            good_list[f'title4_{count + 1}'] = False

        try:
            good_list[f'image_{count + 1}'] = sessions_lisst[count].image.url
        except:
            good_list[f'image_{count + 1}'] = False


    return good_list
