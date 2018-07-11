import os
import summa_by_word as kw
from collections import defaultdict
import progressbar
import json

widgets = [
    'Building Index: ',
    progressbar.Percentage(),
    ' ', progressbar.Bar(),
    ' ', progressbar.ETA()
]

folder_name = 'text'
index = defaultdict(dict)
file_list = os.listdir(folder_name)

pbar = progressbar.ProgressBar(widgets=widgets, max_value=len(file_list))
pbar.start()
for idx, file_name in enumerate(file_list):
    if file_name.endswith('.txt'):
        with open(os.path.join(folder_name, file_name)) as file:
            text = file.read()
            try:
                rank = kw.keywords(text, deaccent=True)
            except:
                continue
            for keyword, score in rank.items():
                index[keyword][file_name] = score
    pbar.update(idx + 1)
pbar.finish()

with open('index_normalized.json', 'w') as outfile:
    json.dump(index, outfile)
