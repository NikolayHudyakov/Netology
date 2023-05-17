import json
import xml.etree.ElementTree as ET


def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open(file_path) as file:
        json_data = json.load(file)
        all_word_list = []
        for news in json_data['rss']['channel']['items']:
            word_list = news['description'].split(' ')
            word_list_top = list(filter(lambda o: len(o) > word_max_len, word_list))
            all_word_list.extend(word_list_top)
        word_dict = {}
        for word in all_word_list:
            word_dict[word] = all_word_list.count(word)
        sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))
        top_list = []
        for word in sorted_dict:
            top_list.append(word)
            if len(top_list) == top_words_amt:
                break
        return top_list


# def read_xml(file_path, word_max_len=6, top_words_amt=10):
#     tree = ET.parse(file_path)
#     root = tree.getroot()
#     xml_items = root.findall("channel/item/description")
#     map(xml_items, key=lambda o: o.text)
#     print()


if __name__ == '__main__':
    # print(read_json('newsafr.json'))
    # print(read_xml('newsafr.xml'))

    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    newlist = list(x for x in fruits if "a" in x)

    print(type(newlist))