# Criação da classe
class Animal:
    # Criação do método construtor
    def __init__(self, gen, esp, dieta, estado):
        # Criação dos atributos
        self.genero = gen
        self.especie = esp
        self.dieta = dieta
        self.estado = estado
        self.movimento = "Parado"

    # Criação das funções para o objeto
    def exibirDados(self):
        print("--- INFORMAÇÕES DO ANIMAL ---")
        print(f"Gênero: {self.genero}")
        print(f"Espécie: {self.especie}")
        print(f"Dieta: {self.dieta}")
        print(f"Estado: {self.estado}")
        print(f"Movimento: {self.movimento}")


    def movimentacao(self, movimento):
        if movimento == "parado":
            self.movimento = "Parado"
            print("O animal agora está parado!")
        elif movimento == "andando":
            self.movimento = "Andando"
            print("O animal agora está andando!")
        elif movimento == "correndo":
            self.movimento = "Correndo"
            print("O animal agora está correndo!")
        else:
            print("Comando inválido!!")

    def acordarDormir(self, estado):
        if estado == "acordar":
            self.estado = "Acordado"
            print(f"O animal agora está acordado!")
        elif estado == "dormir":
            self.estado = "Dormindo"
            print(f"O animal agora está dormindo!")
        else:
            print(f"Comando inválido!")

# Criação do objeto
animal1 = Animal("Felis", "silvestris", "Carnívoro", "Acordado")

print(animal1.exibirDados())

# Acessando os atributos e métodos de um objeto
print(f"Estado do animal1: {animal1.estado}")
# Modificando o valor de um atributo
animal1.movimento = "correndo"
print(f"Movimento do animal1 agora: {animal1.movimento}")


animal1.exibirDados()
print("----------")
animal1.movimentacao("andando")
print("----------")
animal1.exibirDados()
print("----------")
animal1.movimentacao("parado")
animal1.acordarDormir("dormir")
print("----------")
animal1.exibirDados()