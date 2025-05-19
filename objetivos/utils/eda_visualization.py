from typing import List, Dict
import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
import scipy.stats as sts
import matplotlib.pyplot as plt
import seaborn as sns

def plot_nominal_variable_distribution(nominal_categorical_var: pd.Series, title: str= None ) -> None:
    """
    Plota a distribuição de uma variável categórica nominais em um Series utilizando gráfico de contagem.

    Parâmetros:
    -----------
    nominal_categorical_var: pd.Series
        Um Series do Pandas contendo uma única variável categórica nominal.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    var_name = nominal_categorical_var.name
    n_unique_values = nominal_categorical_var.nunique()

    # Cria figura com uma área de plotagem
    fig, ax = plt.subplots(1, 1, figsize=(16, 4.5))

    # Define a paleta de cores e a embaralhas
    palette = sns.color_palette("Spectral", n_unique_values)
    random.shuffle(palette)

    # Criação do countplot
    sns.countplot(x= nominal_categorical_var, edgecolor='black', hue= nominal_categorical_var, palette= palette, legend= False, ax=ax)
    
    # Adiciona customizações ao gráfico
    ## Adiciona título
    if not title:
        title = f"Distribuição da Variável Nominal '{var_name}'"
    fig.suptitle(title, fontsize= 14, fontweight= 'bold')
    ## Adiciona e customiza grades da horizontal
    ax.grid(color= "gray", linestyle= "dotted", linewidth= 0.5, axis= 'y')
    ax.set_axisbelow(True) # A grade fica atrás das barras
    ## Customiza labels e intervalos nos eixos verticiais dos gráficos
    ax.set_ylabel('Frequência Absoluta')
    ax.yaxis.label.set_fontstyle('italic') # Fonte itálico para label
    ax.yaxis.label.set_size(10)  # Ajusta o tamanho da label
    ax.tick_params(axis= 'y', labelsize= 9, labelrotation= 0)
    ## Customiza labels e intervalos nos eixos horizontais dos gráficos
    ax.set_xlabel(var_name)  
    ax.xaxis.label.set_fontstyle('italic') # Define a label do eixo x como itálico
    ax.xaxis.label.set_size(10)
    ax.tick_params(axis='x', labelsize= 9, labelrotation= 0)

    if len(nominal_categorical_var.unique()) > 12:
        ax.tick_params(axis='x', labelsize= 9, labelrotation= 50)
    
    # Exibe o gráfico
    plt.show()

    return None


def plot_nominal_variables_distributions(nominal_categorical_vars: pd.DataFrame) -> None:
    """
    Plota a distribuição de variáveis categóricas nominais em um DataFrame utilizando gráficos de contagem.

    Parâmetros:
    -----------
    nominal_categorical_vars : pd.DataFrame
        Um DataFrame do Pandas contendo variáveis categóricas nominais.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    # Lista de variáveis nominais
    list_nominal_vars = list(nominal_categorical_vars.columns)
    
    for var_name in list_nominal_vars:
        variable = nominal_categorical_vars[var_name]

        plot_nominal_variables_distributions(variable)

    return None


def plot_ordinal_variable_distribution(ordinal_categorical_var: pd.Series, categories_order: List, title: str = None) -> None:
    """
    Plota a distribuição de variável categórica ordinal em um Series utilizando gráficos de contagem.

    Parâmetros:
    -----------
    ordinal_categorical_var: pd.Series
        Um Series do Pandas contendo uma única variável categórica ordinal.

    categories_order : List
        Uma lista das categorias ordenadas.

    title : str
        Uma título para o gráfico.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    var_name = ordinal_categorical_var.name

    # Cria figura com uma área de plotagem
    fig, ax = plt.subplots(1, 1, figsize=(16, 4.5))

    # Define a paleta de cores
    palette = sns.color_palette("Spectral", len(categories_order))

    # Cria countplot com as categorias na ordem correta
    sns.countplot(x= ordinal_categorical_var, order= categories_order, edgecolor='black', hue= ordinal_categorical_var , palette= palette, legend= False, ax=ax)

    # Adiciona customizações aos gráficos
    ## Adiciona título
    if not title:
        title = f"Distribuição da Variável Ordinal '{var_name}'"
    fig.suptitle(title, fontsize= 14, fontweight= 'bold')
    ## Adiciona e customiza grades da horizontal
    ax.grid(color= "gray", linestyle= "dotted", linewidth= 0.5, axis= 'y')
    ax.set_axisbelow(True) # A grade fica atrás das barras
    ## Customiza labels e intervalos nos eixos verticiais dos gráficos
    ax.set_ylabel('Frequência Absoluta')
    ax.yaxis.label.set_fontstyle('italic') # Fonte itálico para label
    ax.yaxis.label.set_size(10)  # Ajusta o tamanho da label
    ax.tick_params(axis= 'y', labelsize= 9, labelrotation= 0)
    ## Customiza labels e intervalos nos eixos horizontais dos gráficos
    ax.set_xlabel(var_name)  
    ax.xaxis.label.set_fontstyle('italic') # Define a label do eixo x como itálico
    ax.xaxis.label.set_size(10)
    ax.tick_params(axis='x', labelsize= 9, labelrotation= 90)
        
    # Exibe o gráfico    
    plt.show();
        
    return None


def plot_ordinal_variables_distributions(ordinal_categorical_vars: pd.DataFrame, dict_ordinal_vars: Dict) -> None:
    """
    Plota a distribuição de variáveis categóricas ordinais em um DataFrame utilizando gráficos de contagem.

    Parâmetros:
    -----------
    ordinal_categorical_vars : pd.DataFrame
        Um DataFrame do Pandas contendo variáveis categóricas ordinais.

    dict_ordinal_vars : dict
        Um dicionário onde as chaves são os nomes das variáveis ordinais e os valores são listas que definem a ordem das categorias.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    # Lista de variáveis ordinais a partir das chaves do dicionário
    list_ordinal_vars = list(ordinal_categorical_vars.columns)
    
    for var_name in list_ordinal_vars:

        order = dict_ordinal_vars.get(var_name)

        variable = ordinal_categorical_vars[var_name]

        plot_ordinal_variable_distribution(variable, order)

    return None


def plot_discrete_variable_distribution(discrete_numeric_var: pd.Series,  title: str = None):
    """
    Plota a distribuição de variável discreta em um DSeries utilizando gráfico de barras.

    Parâmetros:
    -----------
    discrete_numeric_var: pd.Series
        Uma Series do Pandas contendo uma variável numérica discreta.

    title : str
        Uma título para o gráfico.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    var_name = discrete_numeric_var.name
    unique_values = discrete_numeric_var.unique()

    # Cria figura com uma área de plotagem
    fig, ax = plt.subplots(1, 1, figsize= (20, 4.5))

    # Define a paleta de cores
    palette = sns.color_palette("Spectral_r", len(unique_values))

    # Cria do countplot
    sns.countplot(x= discrete_numeric_var, edgecolor= 'black', hue= discrete_numeric_var, palette= palette, legend= False, ax= ax)

    # Adiciona customizações ao gráfico
    ## Adciona título ao gráfico
    if not title:
        title = f"Distribuição da Variável Discreta '{var_name}'"
    fig.suptitle(title, fontsize= 14, fontweight= 'bold')
    ## Adiciona e customiza grades da horizontal
    ax.grid(color= "gray", linestyle= "dotted", linewidth= 0.5, axis= 'y')
    ax.set_axisbelow(True) # A grade fica atrás das barras
    ## Customiza labels e intervalos nos eixos verticiais dos gráficos
    ax.set_ylabel('Frequência Absoluta')
    ax.yaxis.label.set_fontstyle('italic') # Fonte itálico para label
    ax.yaxis.label.set_size(10)  # Ajusta o tamanho da label
    ax.tick_params(axis= 'y', labelsize= 9, labelrotation= 0)
    ## Customiza labels e intervalos nos eixos horizontais dos gráficos
    ax.set_xlabel(var_name)  
    ax.xaxis.label.set_fontstyle('italic') # Define a label do eixo x como itálico
    ax.xaxis.label.set_size(10)
    ax.tick_params(axis='x', labelsize= 9, labelrotation= 0)
    # Rotaciona os rótulos no eixo x se houver mais de 12 categorias
    if discrete_numeric_var.value_counts().shape[0] > 12:
        ax.tick_params(axis= 'x', labelrotation= 90)
        
    # Exibe o gráfico
    plt.show();

    return None


def plot_discrete_variables_distributions(discrete_numeric_vars: pd.DataFrame, title: str= None):
    """
    Plota a distribuição de variáveis discretas em um DataFrame utilizando gráficos de barras.

    Parâmetros:
    -----------
    discrete_numeric_vars : pd.DataFrame
        Um DataFrame do Pandas contendo variáveis numéricas discretas.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    # Lista de variáveis discretas
    list_discrete_vars = list(discrete_numeric_vars.columns)
    
    for var_name in list_discrete_vars:
        variable = discrete_numeric_vars[var_name]
        
        plot_discrete_variable_distribution(variable)

    return None


def descriptive_statistics_continuous_variables(continuous_vars_df):
    """
    Calcula estatísticas descritivas para variáveis numéricas, incluindo teste de normalidade.

    Parâmetros:
    -----------
    continuous_vars_df : pd.DataFrame
        DataFrame contendo as variáveis numéricas para as quais as estatísticas descritivas serão calculadas.

    Retorno:
    --------
    pd.DataFrame
        DataFrame contendo as estatísticas descritivas para cada variável numérica, incluindo valores únicos,
        desvio padrão, variância, assimetria, curtose e p-valor do teste de normalidade de Kolmogorov-Smirnov.
    """
    # Padroniza os dados para o teste de Kolmogorov-Smirnov
    df_standardized = pd.DataFrame(StandardScaler().fit_transform(continuous_vars_df), columns=continuous_vars_df.columns)
    
    # Calcula estatísticas descritivas
    unique = continuous_vars_df.apply(lambda x: len(x.unique()))
    standard_deviation = continuous_vars_df.std()
    variance = continuous_vars_df.var()
    skewness = continuous_vars_df.skew()
    kurtosis = continuous_vars_df.kurtosis()
    
    # Teste de Kolmogorov-Smirnov para normalidade
    kolmogorov = df_standardized.apply(lambda x: "Distrib. Não-Normal" if sts.kstest(x, 'norm').pvalue < 0.05 else "Distrib. Normal")

    # Cria o DataFrame com as estatísticas
    stats_df = pd.DataFrame({
        'Valores Únicos': unique,
        'Desv. Padrão': standard_deviation,
        'Variância': variance,
        'Assimetria': skewness,
        'Curtose': kurtosis,
        'Normalidade': kolmogorov
    })
    
    # Arredonda os valores para melhor apresentação
    cols_to_round = ['Valores Únicos', 'Desv. Padrão', 'Variância', 'Assimetria', 'Curtose']
    stats_df[cols_to_round] = stats_df[cols_to_round].round(3)
    
    return stats_df


def __n_bins(numeric_variable: pd.Series):
    n = numeric_variable.shape[0]
    k = round(1 + (3.3 * np.log10(n)))    
        
    return k


def __calculate_continuous_variable_metrics(numeric_variable: pd.Series):
    """
    Calcula várias métricas descritivas para uma variável contínua.

    Parâmetros:
    ----------
    numeric_variable : pd.Series
        Um Series do Pandas contendo valores numéricos contínuos.

    Retorno:
    -------
    metrics_dict : dict
        Um dicionário contendo as seguintes métricas:
        - 'minimum': valor mínimo
        - 'maximum': valor máximo
        - 'mean': valor médio
        - 'median': valor mediano
        - 'mode': valor modal (se houver mais de um, retorna o menor)
        - 'first_quartile': primeiro quartil (25º percentil)
        - 'third_quartile': terceiro quartil (75º percentil)
        - 'lower_fence': limite inferior para detecção de outliers
        - 'upper_fence': limite superior para detecção de outliers
    """
    # Calcula valor mínimo e máximo
    minimum_value = numeric_variable.min()
    maximum_value = numeric_variable.max()

    # Calcula medidas de posição
    mean_value = numeric_variable.mean()
    median_value = numeric_variable.median()
    mode_value = numeric_variable.mode().min()  # Retorna o menor valor em caso de múltiplos modos

    # Calcula quartis
    first_quartile_value = numeric_variable.quantile(0.25)
    third_quartile_value = numeric_variable.quantile(0.75)
    
    # Calcula intervalo interquartil
    interquartile_range = third_quartile_value - first_quartile_value
    
    # Calcula "fences" para detecção de outliers
    lower_fence_value = max(first_quartile_value - (1.5 * interquartile_range), minimum_value)
    upper_fence_value = min(third_quartile_value + (1.5 * interquartile_range), maximum_value)
    
    # Compila todas as métricas em um dicionário
    metrics_dict = {
        'minimum': minimum_value,
        'maximum': maximum_value,
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value,
        'first_quartile': first_quartile_value,
        'third_quartile': third_quartile_value,
        'lower_fence': lower_fence_value,
        'upper_fence': upper_fence_value
    }
    
    return metrics_dict


def plot_continuous_variable_distribution(continuous_numeric_var: pd.Series, title: str = None) -> None:
    """
    Plota a distribuição de variável contínua em um Series utilizando histogramas e boxplots.

    Parâmetros:
    -----------
    continuous_numeric_var : pd.Series
        Um Series do Pandas contendo uma única variável numérica contínua.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    var_name = continuous_numeric_var.name

    # Chama n_bins para definir a quantidade de intervalos nas distribuições
    bins = __n_bins(continuous_numeric_var)
    
    # Calcula as métricas da variável
    metrics_dict = __calculate_continuous_variable_metrics(continuous_numeric_var)

    # Cria figura com duas área de plotagem
    fig, axes = plt.subplots(2, 1, figsize= (16, 4.5), gridspec_kw= {'height_ratios': [2.5, 1]})

    # Cria histograma com linhas representando as métricas
    axes[0].hist(continuous_numeric_var, color= '#5591b7', edgecolor= 'black', bins= bins)

    # Cria boxplot e adiciona customizações
    axes[1].boxplot(continuous_numeric_var, vert= False)

    # Adiciona customizações aos gáficos
    if not title:
        title = f"Distribuição da Variável Contínua '{var_name}'"

    ## Adiciona título a figura
    fig.suptitle(title, fontsize= 14, fontweight= 'bold')
    ## Adiciona linhas verticais para cada métrica no histograma
    axes[0].axvline(x=metrics_dict['minimum'], color='black', linestyle='dashed', linewidth=2, label=f"Mínimo: {metrics_dict['minimum']:.1f}")
    axes[0].axvline(x=metrics_dict['lower_fence'], color='gray', linestyle='dashed', linewidth=2, label=f"Limite Inferior: {metrics_dict['lower_fence']:.1f}")
    axes[0].axvline(x=metrics_dict['mean'], color='cyan', linestyle='dashed', linewidth=2, label=f"Média: {metrics_dict['mean']:.1f}")
    axes[0].axvline(x=metrics_dict['median'], color='red', linestyle='dashed', linewidth=2, label=f"Mediana: {metrics_dict['median']:.1f}")
    axes[0].axvline(x=metrics_dict['mode'], color='yellow', linestyle='dashed', linewidth=2, label=f"Moda: {metrics_dict['mode']:.1f}")
    axes[0].axvline(x=metrics_dict['upper_fence'], color='gray', linestyle='dashed', linewidth=2, label=f"Limite Superior: {metrics_dict['upper_fence']:.1f}")
    axes[0].axvline(x=metrics_dict['maximum'], color='black', linestyle='dashed', linewidth=2, label=f"Máximo: {metrics_dict['maximum']:.1f}")
    ## Adiciona legendas ao histograma
    axes[0].legend(loc='upper right', fontsize= 'x-small', fancybox= True, framealpha= 0.9, shadow= True, borderpad= 1)
    ## Adiciona e customiza grades
    axes[0].grid(color= "gray", linestyle= "dotted", linewidth= 0.5)
    axes[1].grid(color= "gray", linestyle= "dotted", linewidth= 0.5, axis= 'x')
    axes[0].set_axisbelow(True) # A grade fica atrás das barras
    axes[1].set_axisbelow(True)
    ## Customiza labels e intervalos nos eixos verticiais dos gráficos
    axes[0].set_ylabel('Frequência Absoluta')
    axes[0].yaxis.label.set_size(10)  # Ajusta o tamanho da label
    axes[0].yaxis.label.set_fontstyle('italic') # Fonte itálico para label
    axes[0].tick_params(axis='y', labelsize= 9, labelrotation=0)
    axes[1].yaxis.set_ticks([])
    ## Customiza labels e intervalos nos eixos horizontais dos gráficos
    axes[1].set_xlabel(var_name)  
    axes[1].xaxis.label.set_fontstyle('italic') # Define a label do eixo x como itálico
    axes[1].tick_params(axis='x', labelsize= 9, labelrotation=0)
    
    # Exibe o gráfico
    plt.show();

    return None


def plot_continuous_variables_distributions(continuous_numeric_vars: pd.DataFrame) -> None:
    """
    Plota a distribuição de variáveis contínuas em um DataFrame utilizando histogramas e boxplots.

    Parâmetros:
    -----------
    continuous_numeric_vars : pd.DataFrame
        Um DataFrame do Pandas contendo variáveis numéricas contínuas.

    Retorno:
    --------
    None
        A função não retorna nenhum valor. Ela exibe os gráficos gerados.
    """
    list_continuous_variables = list(continuous_numeric_vars.columns)
    
    for var_name in list_continuous_variables:
        variable = continuous_numeric_vars[var_name]

        plot_continuous_variable_distribution(variable)