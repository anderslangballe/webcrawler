import pickle

from loguru import logger

from indexing.indexer import Indexer
from querying.free_text_query import FreeTextQuery
from ranking.content_ranker import ContentRanker
from ranking.pagerank import PageRank

if __name__ == "__main__":
    # Load corpus from file
    url_contents_dict = pickle.load(open('contents.pkl', 'rb'))

    # Load URl references from file (used for link analysis)
    url_references = pickle.load(open('references.pkl', 'rb'))

    # Perform indexing on the corpus
    logger.info(f'Indexing {len(url_contents_dict)} documents')
    indexer = Indexer()
    indexer.index_corpus(url_contents_dict)

    # Compute champion list
    logger.info('Updating champion list')
    indexer.term_dict.update_champions(r=50)

    # PageRank the URL references
    logger.info('Performing PageRank')
    page_rank = PageRank(url_references)
    rank_result = page_rank.rank()
    for index, url in enumerate(rank_result[:10]):
        print(f'{index + 1}. {url[0]}')

    # Make dictionary from URL to PageRank score (for combined score)
    url_pagerank = {tup[0]: tup[1] for tup in rank_result}

    # Repeatedly accept user input
    while True:
        query = FreeTextQuery(indexer, input('Enter query:'))

        # Rank with cosine similarity
        content_ranker = ContentRanker(query)

        # Print results
        for idx, document in enumerate(content_ranker.top(10)):
            print(f'{idx + 1}. {document[0]}')
