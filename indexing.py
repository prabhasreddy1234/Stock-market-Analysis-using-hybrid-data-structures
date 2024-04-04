from collections import defaultdict


class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)
        self.document_metadata = {}

    def add_document(self, document_id, content, metadata=None):
        tokens = content.lower().split()  # Convert to lowercase for case-insensitive search
        for token in tokens:
            self.index[token].append(document_id)
        if metadata:
            self.document_metadata[document_id] = metadata

    def search_documents(self, keywords):
        keyword_set = set(keywords)
        matching_documents = defaultdict(int)
        for keyword in keyword_set:
            if keyword in self.index:
                for document_id in self.index[keyword]:
                    matching_documents[document_id] += 1
        sorted_results = sorted(matching_documents.items(), key=lambda x: x[1], reverse=True)
        return [result[0] for result in sorted_results]

    def remove_document(self, document_id):
        for postings in self.index.values():
            if document_id in postings:
                postings.remove(document_id)
                if not postings:
                    del postings
        if document_id in self.document_metadata:
            del self.document_metadata[document_id]

index = InvertedIndex()

index.add_document(1, "Apple Inc. announces new product lineup.", {"date": "2023-06-15", "source": "PR Newswire"})
index.add_document(2, "Google reports strong financial results for Q2.",
                   {"date": "2023-06-16", "source": "Business Insider"})
index.add_document(3, "Amazon launches new subscription service.", {"date": "2023-06-14", "source": "Reuters"})
index.add_document(4, "Microsoft introduces new cloud computing solution.",
                   {"date": "2023-06-17", "source": "TechCrunch"})
index.add_document(5, "Tesla unveils new electric vehicle model.", {"date": "2023-06-17", "source": "CNN"})
index.add_document(6, "Facebook announces expansion into virtual reality market.",
                   {"date": "2023-06-16", "source": "The Verge"})
index.add_document(7, "Samsung releases latest smartphone with advanced features.",
                   {"date": "2023-06-15", "source": "Gizmodo"})
index.add_document(8, "Netflix reports record-breaking subscriber growth.", {"date": "2023-06-18", "source": "Variety"})
index.add_document(9, "IBM introduces new AI-powered analytics platform.", {"date": "2023-06-18", "source": "Forbes"})
index.add_document(10, "General Electric announces major renewable energy project.",
                   {"date": "2023-06-19", "source": "CNBC"})
index.add_document(11, "Toyota unveils all-electric SUV with impressive range.",
                   {"date": "2023-06-19", "source": "The Guardian"})
index.add_document(12, "Intel launches revolutionary processor for high-performance computing.",
                   {"date": "2023-06-20", "source": "PCMag"})
index.add_document(13, "SpaceX successfully launches satellite into orbit.",
                   {"date": "2023-06-20", "source": "Space.com"})
index.add_document(14, "Coca-Cola introduces new line of healthy beverages.",
                   {"date": "2023-06-21", "source": "Bloomberg"})
index.add_document(15, "Adobe releases latest version of creative software suite.",
                   {"date": "2023-06-21", "source": "Engadget"})
index.add_document(16, "Walmart announces expansion into online grocery delivery.",
                   {"date": "2023-06-22", "source": "TechRadar"})
index.add_document(17, "Volkswagen unveils electric vehicle charging infrastructure plan.",
                   {"date": "2023-06-22", "source": "Reuters"})
index.add_document(18, "Twitter introduces new feature to combat misinformation.",
                   {"date": "2023-06-23", "source": "The New York Times"})
index.add_document(19, "JPMorgan Chase reports strong quarterly earnings.",
                   {"date": "2023-06-23", "source": "Financial Times"})
index.add_document(20, "Boeing showcases next-generation aircraft with advanced technologies.",
                   {"date": "2023-06-24", "source": "Aviation Week"})
