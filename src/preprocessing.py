import pandas as pd

def preprocess_dataset(csv_filename,rebalance=True):
    '''
    Function to preprocess a csv dataset into a dataframe with score and text

    Parameters
    ----------
    csv_filename : str
        Path to the csv file containing the data
    
    rebalance : bool, optional
        Optional flag indicates to balance the number of reviews.
    
    Returns
    -------
    DataFrame
        Pandas DataFrame with two columns: text and review score.
    '''

    # This mapping will convert the original scores as follows
    # 1,2 -> 0 (negative review)
    # 3 -> 1 (neutral review)
    # 4,5 -> (positive review)
    mapping = {1:0,2:0,3:1,4:2,5:2}

    df = pd.read_csv(csv_filename,compression='gzip')
    
    df_new = df[['Text','Score']].copy()
    df_new['Score'] = df_new['Score'].map(mapping).values

    if rebalance:
        score_count = df_new['Score'].value_counts()
        num_records = min(score_count.values)

        newdf = pd.DataFrame()

        for k in range(3):
            
            # sample `num_records` with given score
            tempdf = df_new.query(f'Score == {k}').sample(n = num_records, random_state = 10).copy()
    
            newdf = pd.concat([newdf,tempdf],axis = 0)

        df_new = newdf

        # here we need to add a filter so that we can return 
        # two dataframes: the balanced one, and the remaining df with the 'excluded' reviews
    

    return df_new