# nlp_reviews
Repository to do NLP tasks, namely the following:

- Sentiment Analysis
- Entity Extraction
- Text Summarization

## Dataset

We'll use the following publicly available dataset, from [Amazon food reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews/data).

The data dictionary is as follows:

- `Id`: Row ID (int64).
- `ProductId`: Unique identifier for Product (str).
- `UserId`: Unique identifier for the User (str).
- `ProfileName`: Profile name of the user (str).
- `HelpfulnessNumerator`: Number of users who found review helpful (int64).
- `HelpfulnessDenominator`: Number of users who indicated whether they found the review helpful or not (int64).
- `Score`: Rating between 1 and 5 (int64).
- `Time`: Timestamp for the review (int64).
- `Summary`: Brief summary of review (str).
- `Text`: Full review (str).


## EDA

Follow the notebook located on the following directory.

The main finding is with regards to the class balances of the Score.

TO DO: 

- Upload the notebook with EDA
- Write down the strategy to deal with class imbalance

## Modelling


### Sentiment Analysis

In this section I want to try different approaches to perform a sentiment analysis on the reviews:

- Bag of words model with Count Vectorizer
- TFID
- Other pretrained models