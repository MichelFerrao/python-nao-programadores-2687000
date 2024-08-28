# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.

cursos_linkedin = ['Introdução a SQL', 'Python: Formação Básica', 'Python para Ciência de Dados: Formação Básica', 'Descubra a Linguagem de Programação R', 'Fundamentos de Programação: Algoritmos']

curso_git = 'Git e GitHub: Formação Básica'
curso_python = 'Python: Formação Básica'
curso_r = 'Descubra a Linguagem de Programação R'

avaliacoes = {}

if curso_python in cursos_linkedin:
   print(f"O curso {curso_python} está no catálogo. Por favor, avalie o curso.")
   avaliacoes[curso_python] = int (input('Qual é a nota que você dá para o curso (0 a 5)?'))
if curso_git in cursos_linkedin:
   print (f'O curso "{curso_git}" está no catálogo. Por favor, avalie o curso.')
   avaliacoes[curso_git] = int(input('Qual nota você dá para esse curso(0 a 5)?'))
if curso_r in cursos_linkedin:
   print(f'O curso "{curso_r}" está no catálogo. Por favor, avalie o curso.')
   avaliacoes[curso_r] = int(input('Qual nota você dá para esse curso (0 a 5)?'))
else:
   print("Infelizmente o curso não compõe o nosso catálogo.")       

print(avaliacoes)