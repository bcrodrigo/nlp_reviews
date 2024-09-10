## Background

Natural language processing (NLP) is a subfield of computer science and artificial intelligence that uses machine learning to enable computers to understand and communicate with human language[^1].

In this repository, we'll implement the following NLP tasks:

- Sentiment Analysis
- Entity Extraction
- Text Summarization

## Dataset

We'll use the following publicly available dataset, from [Amazon food reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews/data).

The data dictionary is as follows:

| Column Name            | Description                                                               | Data Type |
| ---------------------- | ------------------------------------------------------------------------- | --------- |
| Id                     | Row ID                                                                    | int64     |
| ProductId              | Unique identifier for Product                                             | object    |
| UserId                 | Unique identifier for User                                                | object    |
| ProfileName            | Profile name of the user                                                  | object    |
| HelpfulnessNumerator   | Number of users who found the review helpful                              | int64     |
| HelpfulnessDenominator | Number of users who indicated wether they found the review helpful or not | int64     |
| Score                  | Rating between 1 and 5                                                    | int64     |
| Time                   | Timestamp for the review                                                  | int64     |
| Summary                | Brief summary of the review                                               | object    |
| Text                   | Full review                                                               | object    |


## EDA

Follow the notebook located on the [jupyter_notebooks](https://github.com/bcrodrigo/nlp_reviews/tree/main/jupyter_notebooks) directory. The main finding is with regards to the class balances of the review Score:
![score_dist](images/review_score_dist.png)


As seen in the graph above, the score of 5 is by far the most popular, compared to the other scores.

## Preprocessing Pipeline

**1. Balancing Data**

As noted in the EDA, there is a class imbalance in the Score of the reviews, so we'll address it by:
- Mapping the score from 1-5 to 0-2 (bad, neutral, and good respectively)
- Remove duplicate reviews
- Downsampling the category with the highest review

 **2. Text Cleaning**

In this step we'll remove text that doesn't convey any meaningful information such as
- HTML tags
- URLs
- Excessive whitespace

Note that at this point we're not removing any punctuation, numbers, or special symbols. I want to leave the text human-readable prior to the tokenization step.

**3. Tokenization**

We'll use the [spaCy](https://spacy.io/) library to perform: 
- tokenization
- stop word and punctuation removal
- lemmatization

## Modelling

### Sentiment Analysis

In this section I want to try different approaches to perform a sentiment analysis (predict if the text conveys positive, neutral, or negative sentiment) on the reviews. We'll implement and compare the following models.

- Bag of words model with Count Vectorizer
- TFID
- LSTM
- Other pre-trained models

## Work In Progress
- [ ] Finalize selecting all the model evaluation metrics
- [ ] Modelling with TFID
- [ ] Modelling with Pre-trained models

# References

[^1]: https://www.ibm.com/topics/natural-language-processing