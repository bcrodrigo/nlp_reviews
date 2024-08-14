import pandas as pd

def values_to_update():
    """Function to generate a dictionary with the values to update in the models dataframe
    
    Returns
    -------
    dictionary
        Contains the following keys:
            - model (str)
            - train_score (float)
            - test_score (float)
            - num_features (int)
            - comments (str)
    """

    dictionary = {
        "model": "",
        "train_score": [0.0],
        "test_score": [0.0],
        "num_features": [0],
        "comments": "",
    }

    return dictionary


def model_df(df, values_to_add):
    """To update dataframe keeping track of models. The dataframe will have the following columns:
        - model (str)
        - train_score (float)
        - test_score (float)
        - num_features (int)
        - comments (str)
    
    Parameters
    ----------
    df : DataFrame
        Pandas dataframe where we're appending the new values. Note, that if we don't have a dataframe yet, we only pass pd.Dataframe()
    
    values_to_add : dictionary
        Up-to-date dictionary generated with `values_to_update()`
    
    Returns
    -------
    DataFrame
        Up-to-date dataframe containing previous and newly added values.
    """

    temp_val = values_to_update()
    df = pd.concat([df, pd.DataFrame(temp_val)], axis=0, ignore_index=True)

    max_index = max(df.index.tolist())
    
    for key,val in values_to_add.items():
        df.loc[max_index,key] = val
    
    return df