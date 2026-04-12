from index.tokenization import tokenise, stopwords, punctuation, stem, terms, edge_n_grams
def main():
    # Sample documents to index
    documents = [
        "The quick brown fox jumps over the lazy dog.",
        "The lazy dog is sleeping.",
        "The fox is quick and clever."
    ]
    for word in documents:
        indexing(word)


def indexing(text):
     print("Original Text:", text)
    
     tokens = tokenise(text)
    #  print("Tokens:", tokens)
    
     stemmed_tokens = stem(tokens)
    #  print("Stemmed Tokens:", stemmed_tokens)
    
     unique_terms = terms(text)
    #  print("Unique Terms:", unique_terms)
    
     n_grams = edge_n_grams(tokens, 3)
    #  print("Edge N-grams (n=3):", n_grams)

if __name__ == "__main__":
    main()