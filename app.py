import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Publicação de João Campos", page_icon="📐", layout="wide")

df = pd.read_excel('JoaoCampos.xlsx')
df['Total Interactions'] = df['Total Interactions'].apply(lambda x: x.replace(',', '')).astype(int)

# Lista de temas
economia = 'economia|dinheiro|finança|emprego|taxa|imposto|sal.rio'
educacao = 'educa..o|escola|estudante|alun.|ensino|aprend|profess|aula|rede p.blica'
infraestrutura = 'infraestrutura|estrutura|constru..o|obra|asfalto|pavimenta..o|cal..ada|ponte|viaduto|t..nel|buraco|bueiro|esgoto|luz|energia|ilumina..o|lumin.r|pra[çc]a|limpeza|canal|chuva|barreira|lixo'
seguranca = 'segurança|crime|vigil.ncia|pol.cia|b.o|boletim|ocorrência|assalto|roubo|furto|tráfico|droga|arma|tiro|bala|assassinato|assassino|assassinar|assassina|assassine|assassinei|assassineis|assassinar|assassinar|assassinaram|assassinaram|assassin'
saude = 'saúde|hospital|prevenção|vacina|cl.nica|preven'
religiao = 'fé|sant[ao]|igreja|relig.|divina|orat.ri.|nossa senhora|aparecida'

# Condições
condicoes = [df['Description'].str.contains(economia, na=False, case=False, regex=True),
                df['Description'].str.contains(educacao, na=False, case=False, regex=True),
                df['Description'].str.contains(infraestrutura, na=False, case=False, regex=True),
                df['Description'].str.contains(seguranca, na=False, case=False, regex=True),
                df['Description'].str.contains(saude, na=False, case=False, regex=True),
                df['Description'].str.contains(religiao, na=False, case=False, regex=True)]

# Escolhas
choices = ['Economia', 'Educacao', 'Infraestrutura', 'Seguranca', 'Saúde', 'Religião']

# Cria a variável TEMAS
df['Temas'] = np.select(condicoes, choices, default='Outros')

df2 = df[['Account', 'Post Created', 'Type', 'Total Interactions', 'Description', 'Temas', 'Link']]
def main():

    st.title('Publicações de João Campos')
    st.caption('Por: Bruna VerIssimo')
    st.markdown("""
    Aqui estão todas as publicações de João Campos, organizadas cronologicamente, etc etc etc
    """)

    st.header("10 publicações com mais engajamento")
    st.dataframe(df2.sort_values(by='Total Interactions', ascending=False).head(10))
    st.markdown("Escreva a análise aqui")

    st.header('Tema: Economia')
    st.dataframe(df2[df2['Temas'] == 'Economia'])
    st.markdown("Escreva a análise aqui")


    st.header('Tema: Educação')
    st.dataframe(df2[df2['Temas'] == 'Educacao'])
    st.markdown("Escreva a análise aqui")


    st.header('Tema: Infraestrutura')
    st.dataframe(df2[df2['Temas'] == 'Infraestrutura'])
    st.markdown("Escreva a análise aqui")


    st.header('Tema: Segurança')
    st.dataframe(df2[df2['Temas'] == 'Seguranca'])
    st.markdown("Escreva a análise aqui")

    st.header('Tema: Saúde')
    st.dataframe(df2[df2['Temas'] == 'Saúde'])
    st.markdown("Escreva a análise aqui")

    st.header('Tema: Religião')
    st.dataframe(df2[df2['Temas'] == 'Religião'])
    st.markdown("Escreva a análise aqui")



if __name__ == '__main__':
    main()
