from django.utils.safestring import mark_safe


def contacts_func(contacts):
    good_list = {}

    if not contacts:
        return None

    try:
        good_list[f'title1'] = mark_safe(contacts.title1)
    except:
        good_list[f'title1'] = False

    try:
        good_list[f'telegram'] = contacts.telegram
    except:
        good_list[f'telegram'] = False

    return good_list
