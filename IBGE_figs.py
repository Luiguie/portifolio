import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go

#IBGE dados cor - Macaé
data = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/9606/periodos/2022/variaveis/93?localidades=N6[3302403]&classificacao=86[2776,2777,2778,2779,2780]")
data_json = data.json()
    
macae_cor_df = pd.DataFrame(columns=["Cor","População"])
for cor in data_json[0]["resultados"]:
    cor_v = list(cor["classificacoes"][0]["categoria"].items())[0][1]
    total_v = int(list(cor["series"][0]["serie"].items())[0][1])
    macae_cor_df = pd.concat([macae_cor_df,pd.DataFrame([{"Cor":cor_v,"População":total_v}])],ignore_index=True)
    
macae_cor_fig = px.pie(
    macae_cor_df,
    values="População",
    names="Cor",
    color_discrete_sequence=["#E6D1B1", "#1f1e1c", "#f7cd79", "#967f51", "#454128"],
    category_orders={"Cor": macae_cor_df.index.tolist()},
    title="Distribuição de Cor de Pele Macaé"
    )

#IBGE dados cor - Brasil
data = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/9606/periodos/2022/variaveis/93?localidades=N1[all]&classificacao=86[2776,2777,2778,2779,2780]")
data_json = data.json()
    
brasil_cor_df = pd.DataFrame(columns=["Cor","População"])
for cor in data_json[0]["resultados"]:
    cor_v = list(cor["classificacoes"][0]["categoria"].items())[0][1]
    total_v = int(list(cor["series"][0]["serie"].items())[0][1])
    brasil_cor_df = pd.concat([brasil_cor_df,pd.DataFrame([{"Cor":cor_v,"População":total_v}])],ignore_index=True)

brasil_cor_fig = px.pie(
    brasil_cor_df,
    values="População",
    names="Cor",
    color_discrete_sequence=["#E6D1B1", "#1f1e1c", "#f7cd79", "#967f51", "#454128"],
    category_orders={"Cor": macae_cor_df.index.tolist()},
    title="Distribuição de Cor de Pele Brasil"
    )


    
#IBGE dados crescimento população
data = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2001|2002|2003|2004|2005|2006|2008|2009|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021/variaveis/9324?localidades=N6[3302403]")
data_json = data.json()
    
macae_population_df = pd.DataFrame(columns=["Ano","População"])
for pop in list(data_json[0]["resultados"][0]["series"][0]["serie"].items()):
    year = pop[0]
    total = int(pop[1])
    macae_population_df = pd.concat([macae_population_df,pd.DataFrame([{"Ano":year,"População":total}])],ignore_index=True)
    
macae_pop_fig = px.bar(macae_population_df,x="Ano",y="População",title="População ao Longo do Tempo")

macae_pop_fig.update_xaxes(type='category', tickmode='linear', tickvals=macae_population_df['Ano'].tolist())

#IBGE dados piramide etaria
data = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/9606/periodos/2022/variaveis/93?localidades=N6[3302403]&classificacao=2[4,5]|287[93070,93084,93085,93086,93087,93088,93089,93090,93091,93092,93093,93094,93095,93096,93097,93098,49108,49109,60040,60041,6653]")
data_json = data.json()

rows = []
for resultado in data_json[0]["resultados"]:
    sexo = list(resultado['classificacoes'][0]['categoria'].values())[0]
    idade = list(resultado['classificacoes'][1]['categoria'].values())[0]
    quantidade = int(list(resultado['series'][0]['serie'].values())[0])
    rows.append([sexo, idade, quantidade])


df_dist_idade_sexo = pd.DataFrame(rows, columns=['Sexo', 'Idade', 'Quantidade'])

trace_male = go.Bar(
    y=df_dist_idade_sexo["Idade"],
    x=df_dist_idade_sexo["Quantidade"][df_dist_idade_sexo["Sexo"] == "Homens"],
    orientation='h',
    name='Homens',
    hoverinfo='x+text',
    marker=dict(color='blue')
)

trace_female = go.Bar(
    y=df_dist_idade_sexo["Idade"],
    x=df_dist_idade_sexo["Quantidade"][df_dist_idade_sexo["Sexo"] == "Mulheres"] * -1,  # Multiply by -1 to mirror the female bars
    orientation='h',
    name='Mulheres',
    hoverinfo='x',
    marker=dict(color='pink')
)

layout = go.Layout(
    title='Piramide Etaria',
    barmode='overlay',  # Overlay male and female bars
    xaxis=dict(title='População', range=[-max(max(df_dist_idade_sexo["Quantidade"][df_dist_idade_sexo["Sexo"] == "Homens"]), max(df_dist_idade_sexo["Quantidade"][df_dist_idade_sexo["Sexo"] == "Mulheres"])) * 1.1, max(max(df_dist_idade_sexo["Quantidade"][df_dist_idade_sexo["Sexo"] == "Homens"]), max(df_dist_idade_sexo["Quantidade"][df_dist_idade_sexo["Sexo"] == "Mulheres"])) * 1.1]),
    yaxis=dict(title='Faixa Etaria'),
)

piramide_etaria_fig = go.Figure(data=[trace_male, trace_female], layout=layout)

#IBGE dados para sunburst populacional
data = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/9606/periodos/2022/variaveis/93?localidades=N6[3302403]&classificacao=86[2776,2777,2778,2779,2780]|2[4,5]|287[93070,93084,93085,93086,93087,93088,93089,93090,93091,93092,93093,93094,93095,93096,93097,93098,49108,49109,60040,60041,6653]")
data_json = data.json()

data_json
complete_population_df = pd.DataFrame(columns=["População","Cor","Sexo","Idade"])

for population_data in data_json[0]["resultados"]:
    cor = list(population_data["classificacoes"][0]["categoria"].items())[0][1]
    sexo = list(population_data["classificacoes"][1]["categoria"].items())[0][1]
    range_idade = list(population_data["classificacoes"][2]["categoria"].items())[0][1]
    populacao = list(population_data["series"][0]["serie"].items())[0][1]
    
    complete_population_df = pd.concat([complete_population_df,pd.DataFrame([{"População":populacao,"Cor":cor,"Sexo":sexo,"Idade":range_idade}])],ignore_index=True)
 
complete_population_df["População"] = complete_population_df["População"].replace("-","0")
complete_population_df["População"] = complete_population_df["População"].astype(int)
complete_population_df

sun_pop_fig = px.sunburst(
    complete_population_df,
    path=['Cor', 'Sexo', 'Idade'],
    values='População',
    title='Grafico Solar da População',
    color_discrete_sequence=["#967f51", "#E6D1B1","#1f1e1c", "#f7cd79", "#454128"],#['rgb(140, 95, 6)','rgb(227, 203, 182)','rgb(51, 37, 10)','rgb(242, 180, 61)','rgb(117, 107, 16)']
    width=800,
    height=800
)

