def tamanhopalavra():
  
  palavra = input(f'\nDigite uma frase (digite uma frase com apenas 5 frases): ')

  palavras = palavra.split()

  quanti_palavras = len(palavras)

  print(f'\nA frase possui {quanti_palavras} palavras')

  tamanho1 = len(palavras[0])
  tamanho2 = len(palavras[1])
  tamanho3 = len(palavras[2])
  tamanho4 = len(palavras[3])
  tamanho5 = len(palavras[4])

  if tamanho1 < tamanho2:
    print(f'A palavra {palavras[0]} é menor em relação a palavra {palavras[1]}')

  elif tamanho1 < tamanho3:
    print(print(f'A palavra {palavras[0]} é menor em relação a palavra {palavras[2]}'))

  elif tamanho1 < tamanho4:
    print(print(f'A palavra {palavras[0]} é menor em relação a palavra {palavras[3]}'))
  elif tamanho1 < tamanho5:
    print(print(f'A palavra {palavras[0]} é menor em relação a palavra {palavras[4]}'))
    print(f'A palavra {palavra[4]} é a que possui mais caracteres')


tamanhopalavra()
