
class QuoteStorage:
    def __init__(self):
        self.quotes = []

    def get_all(self):
        return self.quotes

    def add(self, quote):
        self.quotes.append(quote)

quote_storage = QuoteStorage()