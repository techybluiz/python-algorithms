def calcular_imc(peso, altura):
    return peso / (altura **2)
def classificar (imc):
    if imc <18.5:
        return "Abaixo do peso"
    elif 25 <= imc < 30:
        return"Sobrepeso"
    else:
        return "Obesidade"
def main():
    peso = float(input("Digite o seu peso oem quilogramas: "))
    altura = float(input("Digite sua altura em metros: "))
    