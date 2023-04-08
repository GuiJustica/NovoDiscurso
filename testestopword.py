import pandas as pd
import nltk
from nltk.corpus import stopwords
# baixar os recursos necessários para a análise de texto em português
nltk.download('stopwords')
nltk.download('punkt')



print("teste")


# lê o arquivo CSV
df = pd.read_csv('C:\\Users\\Cliente\\Desktop\\GuilhermeProgramacao\\MercadoEmJava\\TweetsIc\\tweet.csv', sep=',', encoding='utf-8')

# Define as stopwords em português
stopwords = nltk.corpus.stopwords.words('portuguese')
print(stopwords)
# Aplica as stopwords a uma coluna do DataFrame
df['tweet_sem_stopwords'] = df['tweet'].head(2).apply(lambda x: ' '.join([word for word in x.lower().split() if word not in stopwords]))

# Imprime o novo DataFrame com a coluna de tweets sem stopwords
print(df['tweet_sem_stopwords'])

# Pega uma linha especifica da coluna selecionada
tweetespecifico = df.iloc[1]['tweet']
print(tweetespecifico)

print()
print()

# Pega uma palavra especifica da coluna selecionada
df_palavra_especifica = df[df['tweet'].str.contains('fudeu', case=False)]
print(df_palavra_especifica)

print()
print()

# Pega uma palavra especifica da coluna selecionada
# tweet 183 - discurso de odio
tweetespecifico = df.iloc[5]['tweet']
print(tweetespecifico)

# cria uma lista para armazenar o número de ocorrências de cada palavra
num_ocorrencias = []

# define a palavra que você quer contar as ocorrências
palavra = 'quieto'

# Verifica se há valores faltantes na coluna "tweet"
mask = df['tweet'].isna()

# Remove os valores faltantes da coluna "tweet"
df = df[~mask]

# Aplica o método "lower()" na coluna "tweet"
df['tweet'] = df['tweet'].apply(lambda x: x.lower())
# percorre cada tweet da base de dados
for tweet in df['tweet']:
    # converte o tweet para minúsculas para facilitar a busca
    tweet = tweet.lower()
    # conta o número de ocorrências da palavra no tweet e adiciona na lista
    num_ocorrencias.append(tweet.count(palavra))

# imprime a lista com o número que palavra aparece em cada tweet
print(num_ocorrencias)
# imprime quantas vezes a palavra aparece
print(sum(num_ocorrencias))

# imprime o index que apareceu a palavra especificada
index_da_palavra = []

for i in range(len(num_ocorrencias)):
    if num_ocorrencias[i] == 1:
        index_da_palavra.append(i)

print(index_da_palavra)
# imprime quantos tweets aparece a palavra especificada
print(len(index_da_palavra))
# imprime os tweet que apareceram a palavra
for i in index_da_palavra:
    print(df['tweet'][i])


