def senha():
  palpites = int(input("Digite um número de 0 a 10:"))
  senha = 7
  tentativas = 1
  while palpites != senha:
    print("Senha errada.Tente novamente.")
    tentativas +=1
    palpites = int(input("Digite um número de 0 a 10:"))
  print("Senha Correta! Você acertou após", tentativas, "tentativas")
senha()
  
    
                   
