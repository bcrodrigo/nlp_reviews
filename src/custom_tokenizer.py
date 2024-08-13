import spacy

# this acts as a global variable for the tokenizer
nlp = spacy.load("en_core_web_sm")


def tokenizer_and_lemma(sentence):
    """
    Function to perform tokenization and lemmatization using the spaCy library.
    The tokenizer removes the following from an input sentence:
        - punctuation
        - stop words
        - blank spaces
        - digits
        - currency symbols

    Parameters
    ----------
    sentence : str
        A single string containing a sentence to be tokenized

    Returns
    -------
    List
        A list of lemmatized tokens
    """

    document = nlp(sentence)

    token_list = [
        token.lemma_
        for token in document
        if not token.is_punct
        and not token.is_stop
        and not token.is_space
        and not token.is_digit
        and not token.is_currency
    ]

    return token_list
