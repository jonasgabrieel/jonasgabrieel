import pandas as pd
Nomes = ['João','José','Henrique','Pedro']
Idade = [12,15,54,22]
Curso = ['Medicina','Fisica','Matematica','Biologia']

df = pd.DataFrame(zip(Nomes,Idade,Curso),columns=['Nomes','Idade','Curso'])
print(df)