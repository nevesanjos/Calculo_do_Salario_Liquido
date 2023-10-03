class Funcionario:
    def __init__(self, salario, dependentes, outros_descontos, simplificado):
        self.salario = salario
        self.dependentes = dependentes
        self.outros_descontos = outros_descontos
        self.simplificado = simplificado
        self.desconto_inss = 0
        self.desconto_ir = 0

    def desconto_INSS(self):
            porcentagens = [7.5/100, 9/100, 12/100, 14/100]
            valores = [1320, 2571.29, 3856.94, 7507.49]
            d = 0
            
            for i, v in enumerate(valores):
                if self.salario < v:
                    break

            for j, p in enumerate(porcentagens):
                if (j < i):
                    if(j > 0):
                        d += p * (valores[j] - (valores[j-1] + 0.01))
                    else:
                        d += p * (valores[j])
                elif(j == i):
                    if(self.salario > valores[-1]):
                        d += p*(valores[j] - (valores[j-1] + 0.01))
                    else:
                        d += p*(self.salario - (valores[j-1] + 0.01))
            self.desconto_inss = d
            return d

    def desconto_IRRF(self):
            
            porcentagens = [0/100, 7.5/100, 15/100, 22.5/100, 27.5/100]
            valores = [2112, 2826.65, 3751.05, 4664.68]
            d = 0
            isento = self.desconto_inss + self.dependentes*189.59 + self.outros_descontos
            
            if(self.simplificado == 'N' or self.simplificado == 'n'):
                scd = self.salario - isento
                if(isento < 528):
                    print("Tá perdendo dinheiro! porque R$ %.2f"%(isento), "< 528")
            else:
                scd = self.salario - 528
                if(isento > 528):
                    print("Tá perdendo dinheiro! porque R$ %.2f"%(isento), "> 528")

            for i, v in enumerate(valores):
                if scd < v:
                    break

            for j, p in enumerate(porcentagens):
                if (j < i):
                    if(j > 0):
                        d += p * (valores[j] - (valores[j-1] + 0.01))
                    else:
                        d += p * (valores[j])
                elif(j == i and scd <= valores[j]):
                    d += p * (scd - (valores[j-1] + 0.01))
                elif(j == i and scd > valores[j]):
                    d += p * (valores[j] - (valores[j-1] + 0.01))
                elif(j > i and scd > valores[j-1]):
                    if(scd > valores[-1]):
                        d += p*(scd - (valores[j-1] + 0.01))
                    else:
                        d += p * (valores[j-1] - (valores[j-2] + 0.01))
                self.desconto_ir = d
            return d
    
salario_bruto = float(input("Digite seu salário bruto: "))
dependentes = int(input("Digite o número de seus dependentes: "))
outros_descontos = float(input("Digite outros descontos isentos de imposto: "))
simplificado = str(input("Simplificado? (S/N): "))

pessoa = Funcionario(salario_bruto, dependentes, outros_descontos, simplificado)
desconto_INSS = pessoa.desconto_INSS()
desconto_IRRF = pessoa.desconto_IRRF()
salario_liquido = salario_bruto - desconto_INSS - desconto_IRRF

print("Desconto de INSS: R$ %.2f" %(desconto_INSS))
print("Desconto de IRFF: R$ %.2f" %(desconto_IRRF))
print("Salário liquído: R$ %.2f" %(salario_liquido))
