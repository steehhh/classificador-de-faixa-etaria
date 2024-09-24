print("\nola, posso verificar em qual faixa etário voce poderá ver determinado entertenimento!\n")
respostapessoa = int(input("\npara começarmos, digite a idade determinada: "))

print("\nvoce escolheu",respostapessoa,"anos!\n\n")

if respostapessoa == 0: 
    print("a sua idade está invalida.")
    print("\npor favor insira um numero valido.")
    respostapessoa = int(input("digite novamente:\n"))
    print("\nvoce escolheu",respostapessoa,"anos!\n\n")

elif respostapessoa >= 0 and respostapessoa <= 10:
    print("entao voce está na faixa etaria:\n\nLIVRE PARA TODOS OS PUBLICOS!.")

elif respostapessoa >= 11 and respostapessoa <=11: 
    print("entao voce está na faixa etaria:\n\nEXIBIÇÃO EM QUALQUER HORARIO!.")

elif respostapessoa >= 12 and respostapessoa <= 13:
    print("entao voce está na faixa etaria:\n\nNAO RECOMENDADO PARA MENORES DE 12 ANOS!.")

elif respostapessoa >= 14 and respostapessoa <= 15:
    print("entao voce está na faixa etaria:\n\nNAO RECOMENDADO PARA MENORES DE 14 ANOS!.")

elif respostapessoa >= 16 and respostapessoa <= 17:
    print("entao voce está na faixa etaria:\n\nNAO RECOMENDADO PARA MENORES DE 16 ANOS!.")

elif respostapessoa >= 18 and respostapessoa <= 100:
    print("entao voce esta na faixa etaria:\n\nRECOMENDADO PARA MAIORES DE 18 ANOS!.")

else: 
    respostapessoa >= 100
    print("idade invalida.")