def flat_generator(list_of_lists: list):
    for item_list in list_of_lists:
        for item in item_list:
            yield item
