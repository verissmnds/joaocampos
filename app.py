import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="A Campanha Permanente do Prefeito João Campos: dados extraídos das suas publicações.", page_icon="📐", layout="wide")

df = pd.read_excel('JoaoCampos.xlsx')
df['Total Interactions'] = df['Total Interactions'].apply(lambda x: x.replace(',', '')).astype(int)

# Lista de temas
economia = 'economia|dinheiro|finança|emprego|taxa|imposto|sal.rio'
educacao = 'educa..o|escola|estudante|alun.|ensino|aprend|profess|aula|rede p.blica'
infraestrutura = 'infraestrutura|estrutura|constru..o|obra|asfalto|pavimenta..o|cal..ada|ponte|viaduto|t..nel|buraco|bueiro|esgoto|luz|energia|ilumina..o|lumin.r|pra[çc]a|limpeza|canal|chuva|barreira|lixo'
seguranca = 'segurança|crime|vigil.ncia|pol.cia|b.o|boletim|ocorrência|assalto|roubo|furto|tráfico|droga|arma|tiro|bala|assassinato|assassino|assassinar|assassina|assassine|assassinei|assassineis|assassinar|assassinar|assassinaram|assassinaram|assassin'
saude = 'saúde|hospital|vacina|cl.nica|preven'
religiao = 'fé|sant[ao]|igreja|relig.|divina|orat.ri.|nossa senhora|aparecida'

# Condições
condicoes = [df['Description'].str.contains(economia, na=False, case=False, regex=True),
                df['Description'].str.contains(educacao, na=False, case=False, regex=True),
                df['Description'].str.contains(infraestrutura, na=False, case=False, regex=True),
                df['Description'].str.contains(saude, na=False, case=False, regex=True),
                df['Description'].str.contains(seguranca, na=False, case=False, regex=True),
                df['Description'].str.contains(religiao, na=False, case=False, regex=True)]

# Escolhas
choices = ['Economia', 'Educacao', 'Infraestrutura', 'Saúde', 'Segurança', 'Religião']

# Cria a variável TEMAS
df['Temas'] = np.select(condicoes, choices, default='Outros')

df2 = df[['Account', 'Post Created', 'Type', 'Total Interactions', 'Description', 'Temas', 'Link']]
def main():

    st.title('A Campanha Permanente do Prefeito João Campos no Instagram: dados extraídos das suas publicações.')
    st.caption('Por Bruna Verissimo, graduanda em Comunicação Digital na Fundação Getúlio Vargas')
    st.markdown("""
    Abaixo a organização dos dados está feita de modo que você consiga ter acesso a cada uma das publicações e entenda melhor a maneira como elas estão dispostas. Como dito no artigo, cada assunto foi filtrado a partir de palavras-chave, mas não espere encontrar uma total precisão nesses filtros, pois os termos que coincidem com saúde, por exemplo, podem estar presentes em publicações relacionadas à segurança, ou em muitos outros contextos diferentes. Nossa língua portuguesa é diversa e variada. Fique à vontade para me enviar qualquer sugestão para aprimorar o programa, meu e-mail é: brunaverissimoecmi@gmail.com  :)
    """)

    
    st.header("Todas as publicações analisadas")
    st.dataframe(df)
    
    st.header("10 publicações com mais engajamento")
    st.dataframe(df2.sort_values(by='Total Interactions', ascending=False).head(10))
    st.markdown("Escreva a análise aqui")

    st.header('Economia')
    st.dataframe(df2[df2['Temas'] == 'Economia'])
    st.markdown("Escreva a análise aqui")


    st.header('Educação')
    st.dataframe(df2[df2['Temas'] == 'Educacao'])
    st.markdown("Escreva a análise aqui")


    st.header('Infraestrutura')
    st.dataframe(df2[df2['Temas'] == 'Infraestrutura'])
    st.markdown("Escreva a análise aqui")


    st.header('Segurança')
    st.dataframe(df2[df2['Temas'] == 'Seguranca'])
    st.markdown("Escreva a análise aqui")

    st.header('Saúde')
    st.dataframe(df2[df2['Temas'] == 'Saúde'])
    st.markdown("Escreva a análise aqui")

    st.header('Religião')
    st.dataframe(df2[df2['Temas'] == 'Religião'])
    st.markdown("Escreva a análise aqui")



if __name__ == '__main__':
    main()
