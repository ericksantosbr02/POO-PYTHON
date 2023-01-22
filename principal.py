from poo import Pessoas,Gerente

dados = Pessoas('erick','santos',21,'avenida silva','aruja')
print(f'Nome: {dados.get_nome()}')
print(f'Sobrenome: {dados.get_sobrenome()}')
print(f'Idade: {dados.get_idade()}')
print(f'Endereco: {dados.get_endereco()}')
print(f'Bairro: {dados.get_bairro()}')
# alterando a unica variavel que é possivel isso com o set
dados.set_endereco('avenida railda alves')
print(dados.get_endereco())

dados.funcionario_faz()
dados1 = Gerente('joão','silva',23,'avenida silva','aruja')
dados1.funcionario_faz('materias sa')