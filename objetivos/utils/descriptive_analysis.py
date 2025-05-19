from typing import Dict, List
import json
import pandas as pd

def print_dataframes_size(dataframes: Dict[str, pd.DataFrame]) -> None:
    for key, df in dataframes.items():
        cols_len =  df.shape[1]
        row_len = df.shape[0]

        print(f'O dataset {key} possui {row_len} registros e {cols_len} variáveis.')

    return None


def print_dataframes_cols(dataframes: Dict[str, pd.DataFrame]) -> None:
    dfs_cols_list = []
    for key, df in dataframes.items():
        df_cols_dict = {
            'dataframe': key,
            'colunas': list(df.columns)
        }

        dfs_cols_list.append(df_cols_dict)

    print(json.dumps(dfs_cols_list, indent= 2, ensure_ascii= False))

    return None


def print_dataframes_types(dataframes: Dict[str, pd.DataFrame]) -> None:
    for key, df in dataframes.items():
        print(f'>>> DATASET: {key}')
        print(df.dtypes)
        print()

    return None


def check_duplicate_values_in_dataframes(dataframes: Dict[str, pd.DataFrame], datasets_primary_keys: List[Dict]) -> None:
    if not isinstance(dataframes, Dict):
        raise ValueError('O valor injetado no parâmetro "dataframes" não é um dicionário.')
    
    for key, df in dataframes.items():
        if not isinstance(df, pd.DataFrame):
            raise ValueError('{key} não é um DataFrame.')
        
        for keys_dict in datasets_primary_keys:
            primary_key = keys_dict.get('primary_key', None)
            if (key == keys_dict.get('dataframe')):
                n_duplicate_values = df.loc[df.duplicated(subset= primary_key, keep= 'first')].shape[0]
                break

        if n_duplicate_values == 0:
            print(f'O dataframe {key} não possui valores duplicados.')
            continue
        
        print(f'O dataframe {key} possui {n_duplicate_values} valores duplicados.')
    
    return None


def check_missing_values_in_dataframes(dataframes: Dict[str, pd.DataFrame]) -> None:
    if not isinstance(dataframes, dict):
        raise ValueError('O valor injetado no parâmetro "dataframes" não é um dicionário.')
    
    for key, df in dataframes.items():
        if not isinstance(df, pd.DataFrame):
            raise ValueError('{key} não é um DataFrame.')

        # Filtra variáveis que possuem valores faltantes
        na_counts = df.isna().sum()
        na_percentages = (na_counts / len(df)) * 100

        variables_with_na_values = na_counts[na_counts > 0].index.tolist()

        if len(variables_with_na_values) == 0:
            print(f'O dataset {key} não possui valores faltantes.')
            continue
        
        print(f'O dataset {key} possui valores faltantes:')

        for variable in variables_with_na_values:
            amount_na_values_in_variable = na_counts[variable]
            percentage_na_values = na_percentages[variable]
            print(f"    A '{variable}' possui {amount_na_values_in_variable} registros faltantes ({percentage_na_values:.2f}%)")
        print()

    return None


def check_zero_values_in_dataframes(dataframes: Dict[str, pd.DataFrame]):
    if not isinstance(dataframes, dict):
            raise ValueError('O valor injetado no parâmetro "dataframes" não é um dicionário.')
    
    for key, df in dataframes.items():
        if not isinstance(df, pd.DataFrame):
            raise ValueError('{key} não é um DataFrame.')

        numerical_vars = df.select_dtypes(include=['int64', 'float64'])

        if not list(numerical_vars):
             continue

        # Filtra variáveis que possuem valores zerados
        zero_mask = numerical_vars == 0
        zero_counts = zero_mask.sum()
        zero_percentages = (zero_counts / len(numerical_vars)) * 100

        variables_with_zeros = zero_counts[zero_counts > 0].index.tolist()
        
        if len(variables_with_zeros) == 0:
            print(f'O dataframe {key} não possui valores zerados.')
            continue

        print(f'O dataframe {key} possui valores zerados:')

        for variable in variables_with_zeros:
            amount_zero_values_in_variable = zero_counts[variable]
            percentage_zero_values = zero_percentages[variable]
            print(f"    A '{variable}' possui {amount_zero_values_in_variable} registros zerados ({percentage_zero_values:.2f}%)")
        print()