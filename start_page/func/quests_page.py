from django.utils.safestring import mark_safe


def quest_func(quests_list):
    good_list = {}

    if not quests_list:
        return None

    for count in range(9):
        try:
            good_list[f'quest_{count + 1}'] = quests_list[count].quest
        except:
            good_list[f'quest_{count + 1}'] = False


        try:
            good_list[f'answer_{count + 1}'] = mark_safe(quests_list[count].answer)
        except:
            good_list[f'answer_{count + 1}'] = False


    return good_list

