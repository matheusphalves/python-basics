idade  = int(input("Informe a sua idade: "))

if(idade > 18):
    #bloco de código
    print("Eu tenho:", idade, "anos")
elif(idade==18):
    #outro bloco condicional
    print("A pessoa tem exatamente ", idade, " anos")
else:
    #outro bloco de código
    print("A pessoa tem menos de 18 anos")
    print("Eu tenho:", idade, "anos")

print("Fim do programa")