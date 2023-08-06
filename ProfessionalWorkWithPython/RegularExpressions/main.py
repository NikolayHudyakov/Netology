from pprint import pprint
import csv
import re
from itertools import groupby

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pattern = r'(\+7|8)\s*\(?(\d{3})\)?[-\s]*(\d{3})-?(\d{2})-?(\d+)\s*\(?(доб.\s\d+)?\)?'
pattern_comp = re.compile(pattern)
replace = r'+7(\2)\3-\4-\5 \6'

new_contacts_list = []

for contact in contacts_list[1:]:
  contact_list = []
  lfs = ' '.join(contact[:3]).split()
  for i in range(3):
    if len(lfs) != 0:
      contact_list.append(lfs.pop(0))
    else:
      contact_list.append('')
  contact_list.append(contact[3])
  contact_list.append(contact[4])
  contact_list.append(pattern_comp.sub(replace, contact[5]))
  contact_list.append(contact[6])
  new_contacts_list.append(contact_list)

group_contacts_list = groupby(sorted(new_contacts_list, key=lambda item: item[:3]), key=lambda item: item[:2])

f_list = []
f_list.append(contacts_list[0])
for g in group_contacts_list:
  cur_list = []
  for sub_g in g[1]:
    cur_list.append(sub_g)

  if len(cur_list) == 1:
    lst = []
    for i in range(7):
      lst.append(cur_list[0][i])
    f_list.append(lst)
  else:
    lst = []
    for i in range(7):
      if cur_list[0][i] != '':
        lst.append(cur_list[0][i])
      else:
        lst.append(cur_list[1][i])
    f_list.append(lst)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(f_list)