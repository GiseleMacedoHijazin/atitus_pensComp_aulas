def senha():
  palpites = int(input("Digite um número de 0 a 10:"))
  senha = 7
  tentativas = 0
  while palpites != senha:
    print("Senha errado.Tente novamente.")
    tentativas +=1
    palpites = int(input("Digite um número de 0 a 10:"))
    print("Senha Correta! Você acertou após", tentativas, "tentativas")
  
    
                   
