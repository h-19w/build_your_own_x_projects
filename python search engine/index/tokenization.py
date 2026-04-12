def tokenise(text):
    text = text.replace('\n', ' ')
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    
    text = text.strip(str(punctuation()))
    text = text.strip(str(stopwords()))
    return text.split()


def stopwords():
    return set([
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'in', 'on', 'for', 'by',
        'is', 'are', 'was', 'were', 'be', 'been', 'being',
        # not comprehensive, just a sample of common stop words
    ])

def punctuation():
    return set(['.', '!', '?', ',', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}', '"', "'", '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>'])

def stem(tokens):
    # A very basic stemming implementation that removes common suffixes.
    # removes suffixes [basic implementation, not comprehensive]
    suffixes = ['ing', 'ed', 's', 'es', 'er', 'ly', 'ment', 'ness', 'ful', 'less', 'able', 'ible', 'al', 'ial', 'tion', 'sion', ]

    stemmed_tokens = []
    for token in tokens:
        for suffix in suffixes:
            if token.endswith(suffix):
                token = token[:-len(suffix)]
                break
        stemmed_tokens.append(token)
    return stemmed_tokens

def terms(text):
    # generate a set of unique stemmed tokens from the input text
    tokens = tokenise(text)
    stemmed_tokens = stem(tokens)
    return set(stemmed_tokens)

def edge_n_grams(tokens, n):
    n_grams = set()
    for token in tokens:
        if len(token) >= n:
            n_grams.add(token[:n])
    return n_grams


# def main():
#     text = "The quick brown fox jumps over the lazy dog."
#     print("Original Text:", text)
    
#     tokens = tokenise(text)
#     print("Tokens:", tokens)
    
#     stemmed_tokens = stem(tokens)
#     print("Stemmed Tokens:", stemmed_tokens)
    
#     unique_terms = terms(text)
#     print("Unique Terms:", unique_terms)
    
#     n_grams = edge_n_grams(tokens, 3)
#     print("Edge N-grams (n=3):", n_grams)



# main()
# if __name__ == "__main__":    
#     main()