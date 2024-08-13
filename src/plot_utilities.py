import pandas as pd
import matplotlib.pyplot as plt


def top_words(Xtransf, bagofwords, num_words=20):
    """Function to plot the top and bottom words used in a vocabulary

    Parameters
    ----------
    Xtransf : CSR matrix
        Sparse matrix with the transformed text
    bagofwords : object
        Instance of bag-of-words count vectorizer
    num_words : int, optional
        Number of words to plot, default is 20
    """
    assert isinstance(num_words, int), "num_words must be an integer"

    word_counts = pd.DataFrame(
        {"counts": Xtransf.toarray().sum(axis=0)},
        index=bagofwords.get_feature_names_out(),
    ).sort_values("counts", ascending=False)

    # plot top words first
    plt.figure(1)
    word_counts.head(num_words).plot(kind="bar", figsize=(15, 5), legend=False)

    plt.title(f"Top {num_words} most frequently occurring words")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

    # plot bottom words
    plt.figure(2)

    word_counts.tail(num_words).plot(kind="bar", figsize=(15, 5), legend=False)

    plt.title(f"Bottom {num_words} least frequently occurring words")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()
