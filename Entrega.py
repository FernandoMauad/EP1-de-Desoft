import turtle

pen = turtle.Pen()
print(""" use F + - para fazer seu desenho
      Exemplo:
      Condição inicial: F-F-F-F
      Regra de producao: FFF----
      Interação: 3 (recomendamos numeros entre 3 e 5)
      Angulo1 = 45
      Angulo2 = 45
      """)

inicial = input("condicao inicial: ")
regra = input("regra de producao: ")
inter =int(input("interacao: "))
angulo = int(input('insira o angulo de rodagem 1: '))
angulo_novo =int(input('insira o angulo de rodagem 2: ')) 
regra_final = ""
regra_final = regra_final.split(' ')

print(inicial)
print(regra)
print(inter)

# 1. aplicar regra de producao
i = 0
while i < inter:
    regra_final = inicial.replace(regra[0], regra[1])
    inicial = regra_final*10
    i+=1
    
print(regra_final)
turtle.speed('fast')
# 2. exibir regra final com a tartaruga

obj= turtle.Turtle()
for i in regra_final.upper():
    if i == 'F':
        turtle.pendown()
        turtle.forward(100)
    elif i == '+': 
        turtle.left(angulo)
        turtle.forward(100)
    elif i == '-':
        turtle.right(angulo_novo)
        turtle.forward(100)
obj.end_fill() 
obj.color('purple', 'blue')
obj.begin_fill()

turtle.done()        