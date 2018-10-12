import pandas as pd


# creating my CSV file with data and returning it's name
def create_mycsv():
    
    file_name_with_path = "Created_files/2010WinterOlympics.csv"
    
    df_data_dict = pd.DataFrame({
        'countries': ['Canada', 'Germany', 'UnitedStates', 'Norway', 'SouthKorea'],
        'countries_abbr': ['CAN', 'GER', 'USA', 'NOR', 'KOR'],
        'gold_medals': [14, 10, 9, 9, 6],
        'silver_medals': [7, 13, 15, 8, 6],
        'bronze_medals': [5, 7, 13, 6, 2],
        'total_medals': [26, 30, 37, 23, 14]
        })

    df_data_dict.to_csv(file_name_with_path, index=False)

    return file_name_with_path


# creating DICT from CSV file taking as an argument CSV file name. returning dict
def get_dict_from_csv(filename):
    
    read_df = pd.read_csv(filename)
    
    back_to_dict = read_df.to_dict('list')

    return back_to_dict


