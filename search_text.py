import json
from collections import Counter
from functools import reduce
from operator import and_
import summa_by_word as kw


with open('index_normalized.json') as file:
    index_normalized = json.load(file)


def search_and(*words, pattern=False):
    '''Find pages that contain *all* words passed into the function'''
    results = [Counter(index_normalized[w]) if w in index_normalized else Counter() for w in words]
    if len(results) == 0:
        return Counter()
    all_keys = [set(r.keys()) for r in results]
    shared_keys = reduce(and_, all_keys)
    result = Counter()
    for key in shared_keys:
        # take the average for keywords on a page
        values = [r[key] for r in results]
        result[key] = sum(values) / len(values)
    return result


def search(*words, max_number=None, pattern=False):
    '''Find pages with *any* of the words/phrases passed in'''
    results = [search_and(*kw.clean_search_word(word, deaccent=True), pattern=pattern) for word in words]
    result = sum(results, Counter())
    return result.most_common(max_number)
