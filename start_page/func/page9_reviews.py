def page9_reviews_func(reviews_list):
    good_list = {}

    if not reviews_list:
        return None

    for count in range(8):
        try:
            good_list[f'image_{count + 1}'] = reviews_list[count].image.url
        except:
            good_list[f'image_{count + 1}'] = False

    return good_list
