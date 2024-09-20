from algoliasearch_django import algolia_engine

def get_client():
    """
    Returns the Algolia search client.
    Returns:
        algoliasearch.client.Client: The Algolia search client
    """
    return algolia_engine.client


def get_index(index_name="blogs_BlogPost"):
    """
    Returns an Algolia index object.
    Args:
        index_name (str): The name of the index to retrieve.
    Returns:
        algoliasearch.index.Index: The Algolia index object
    """
    client = get_client()
    index = client.init_index(index_name)
    return index


def perform_search(query, **kwargs):
    """
    Performs a search query in Algolia.
    Args:
        query (str): The query string to search for.
        **kwargs: Additional parameters to pass to the Algolia search method.
    Keyword Args:
        tags (list[str]): A list of tags to filter by.
        published (bool): If True, only published blogs will be returned.
        user (str): If provided, only blogs created by the specified user will be returned.
    Returns:
        algoliasearch.response.SearchResponse: The results of the search query.
    Example:
    >>> results = perform_search("hello", tags=["Reality"], published=True, user="john")
    """
    index = get_index()
    params = {}
    tags = ""
    # for tag filtering
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params["tagFilters"] = tags
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]

    # for "published" filtering
    if len(index_filters) != 0:
        params["facetFilters"] = index_filters
    results = index.search(query, params)
    return results
