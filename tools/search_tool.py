from googlesearch import search

class SearchTool:
    def __init__(self):
        self.name = "Google Search"

    def search(self, query, num_results=3):
        try:
            results = list(search(query, num_results=num_results, advanced=True))
            formatted_results = []
            for result in results:
                formatted_results.append(f"Title: {result.title}\nURL: {result.url}\nDescription: {result.description}")
            return "\n\n".join(formatted_results)
        except Exception as e:
            return f"Search failed: {str(e)}"
