# -*- coding: utf-8 -*-
"""MenuPucPr.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h__JzBMJF3toJsgzpsff5N67_9Y-mFKE
"""

#Opção do Menu Primario
opcao1 = '1 - Estudante'
opcao2 = '2 - Professor'
opcao3 = '3 - Matricula'
opcao4 = '4 - Turma'
opcao5 = '5 - Disciplina'
opcao6 = '6 - Sair'

#Opção do Menu Secundaria
opcao_secundaria1 = '1 - Incluir'
opcao_secundaria2 = '2 - Listar'
opcao_secundaria3 = '3 - Atualizar'
opcao_secundaria4 = '4 - Excluir'
opcao_secundaria5 = '5 - Voltar ao Menu Principal'

while True:

  print('------------------------------------------------')
  print('')

  print('Bem vindo ao Menu Principal.')
  print(opcao1)
  print(opcao2)
  print(opcao3)
  print(opcao4)
  print(opcao5)
  print(opcao6)

  opcao = int(input('Selecione uma opção do Menu principal: '))
  if opcao == 1:
    print(f'Você escolheu a opção: {opcao1}!')
  if opcao == 2:
    print(f'Você escolheu a opção: {opcao2}!')
  if opcao == 3:
    print(f'Você escolheu a opção: {opcao3}!')
  if opcao == 4:
    print(f'Você escolheu a opção: {opcao4}!')
  if opcao == 5:
    print(f'Você escolheu a opção: {opcao5}!')
  if opcao == 6:
    print(f'Você escolheu a opção: {opcao6}!')

  if(opcao not in [1,2,3,4,5,6]):
    print('Opção inválida.')
    if('Opção inválida.'):
      opcao = int(input('Selecione uma opção válida do Menu principal: '))
      print(f'Você escolheu a opção: {opcao}!')
  elif opcao == 6:
    break

  while True:

    print('')
    print('------------------------------------------------')
    print('')

    print('Bem vindo ao Menu Secundário.')
    print(opcao_secundaria1)
    print(opcao_secundaria2)
    print(opcao_secundaria3)
    print(opcao_secundaria4)
    print(opcao_secundaria5)

    opcao_secundaria = int(input('Selecione uma opção do Menu Secundário: '))
    if opcao_secundaria == 1:
      print(f'Você escolheu a opção: {opcao_secundaria1}!')
    if opcao_secundaria == 2:
      print(f'Você escolheu a opção: {opcao_secundaria2}!')
    if opcao_secundaria == 3:
      print(f'Você escolheu a opção: {opcao_secundaria3}!')
    if opcao_secundaria == 4:
      print(f'Você escolheu a opção: {opcao_secundaria4}!')
    if opcao_secundaria == 5:
      print(f'Você escolheu a opção: {opcao_secundaria5}!')
    if opcao_secundaria == 5:
      break

  if(opcao_secundaria not in [1,2,3,4,5]):
    print('Opção inválida.')