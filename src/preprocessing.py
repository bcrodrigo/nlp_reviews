import pandas as pd


def preprocess_dataset(csv_filename, rebalance=True):
    """
    Function to preprocess a reviews datascet in csv into a dataframe with score and text. It performs the following steps:
        1. Drop duplicate rows
        2. Map score from 1-5 to 0-2
        3. Rebalance the dataframe based on the scores

    Parameters
    ----------
    csv_filename : str
        Path to the csv file containing the data. Note the file is expected to be compressed using gzip.

    rebalance : bool, optional
        Optional flag indicates to balance the number of reviews.

    Returns
    -------
    tuple
        Pandas DataFrames (df_orig, df_rebalanced), each with two columns: text and review score.

        if rebalance is False
            df_orig : contains all records
            df_rebalanced : is an empty dataframe

        if rebalance is True
            df_orig : contains all records minus those used to rebalance the review score
            df_rebalanced : contains all records used to balanced number of reviews by score

        Note that in either case pd.concat([df_orig,df_rebalanced]) equals to all the records in the original dataset.
    """

    # Read dataframe, only two colums

    df_orig = pd.read_csv(csv_filename, compression='gzip',
        usecols=['Text','Score'])

    # Drop the duplicate rows based on reviews
    df_orig = df_orig.drop_duplicates(subset = ['Text'])
    
    # Map score from 0 to 3

    # This mapping will convert the original scores as follows
    # 1,2 -> 0 (negative review)
    # 3 -> 1 (neutral review)
    # 4,5 -> (positive review)
    mapping = {1: 0, 2: 0, 3: 1, 4: 2, 5: 2}

    # df = pd.read_csv(csv_filename, compression="gzip")

    # df_orig = df[["Text", "Score"]].copy()
    df_orig["Score"] = df_orig["Score"].map(mapping).values

    # Empty accumulator-like dataframe
    df_rebalanced = pd.DataFrame()

    if rebalance:

        score_count = df_orig["Score"].value_counts()
        num_records = min(score_count.values)

        for k in range(3):

            # sample `num_records` with given score
            tempdf = (
                df_orig.query(f"Score == {k}")
                .sample(n=num_records, random_state=10)
                .copy()
            )

            df_rebalanced = pd.concat([df_rebalanced, tempdf], axis=0)

        # Note that we did not change the index of the new df.
        # We'll filter the records in df_orig by those who don't have the same index as `df_rebalanced`

        df_orig = df_orig[~df_orig.index.isin(df_rebalanced.index)]

    return df_orig, df_rebalanced

def dataset_text_cleanup(df):
    """
    PLACEHOLDER
    
    To perform text cleanup for a preprocessed dataframe
    It assumes it has two columns 'Text'  and 'Score'
    The cleanup steps are as follows:
    1. Remove HTML tags
    2. Remove URLs
    3. Remove excessive white space
    
    Parameters
    ----------
    df : TYPE
        Description
    
    Returns
    -------
    TYPE
        Description
    """
    return True