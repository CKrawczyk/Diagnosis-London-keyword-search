from summa import keywords as kw
from summa.preprocessing import textcleaner as tc


def clean_search_word(text, language="english", deaccent=False):
    # only search using nouns and adj.
    kw.INCLUDING_FILTER = ['NN', 'JJ']
    tokens = tc.clean_text_by_word(text, language, deacc=deaccent)
    return kw._get_words_for_graph(tokens)


def keywords(text, language="english", deaccent=False):
    # include verbs in the graph
    kw.INCLUDING_FILTER = ['NN', 'JJ', 'VB']

    if not isinstance(text, str):
        raise ValueError("Text parameter must be a Unicode object (str)!")

    # Gets a dict of word -> lemma
    tokens = tc.clean_text_by_word(text, language, deacc=deaccent)
    split_text = list(kw._tokenize_by_word(text))

    # Creates the graph and adds the edges
    graph = kw._build_graph(kw._get_words_for_graph(tokens))
    kw._set_graph_edges(graph, tokens, split_text)
    del split_text  # It's no longer used

    kw._remove_unreachable_nodes(graph)

    # PageRank cannot be run in an empty graph.
    if len(graph.nodes()) == 0:
        return {}

    # Ranks the tokens using the PageRank algorithm. Returns dict of lemma -> score
    return kw._pagerank(graph)
