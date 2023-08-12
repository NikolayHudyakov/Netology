class FlatIterator:

    def __init__(self, list_of_list: list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cnt_list = -1
        self.cnt_sub_list = -1
        self.sub_list = []
        return self

    def __next__(self):
        self.cnt_sub_list += 1

        if self.cnt_sub_list == len(self.sub_list):
            self.cnt_sub_list = 0
            self.cnt_list += 1

            if self.cnt_list == len(self.list_of_list):
                raise StopIteration

            self.sub_list = self.list_of_list[self.cnt_list]

        return self.sub_list[self.cnt_sub_list]
