class Node:
    """Representa um nó em uma lista ligada para armazenar estados."""
    
    def __init__(self, sigla, nome_estado):
        """
        Inicializa um nó com uma sigla de estado e nome.
        
        Args:
            sigla (str): Sigla do estado.
            nome_estado (str): Nome completo do estado.
        """
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

class HashTable:
    """Representa uma tabela hash com encadeamento separado para resolução de colisões."""
    
    def __init__(self):
        """Inicializa a tabela hash com 10 posições vazias."""
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        """
        Função hash para determinar a posição para uma dada sigla de estado.
        
        Args:
            sigla (str): Sigla do estado.
        
        Returns:
            int: A posição calculada na tabela hash.
        """
        if sigla == 'DF':
            return 7
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nome_estado):
        """
        Insere um estado na tabela hash.
        
        Args:
            sigla (str): Sigla do estado.
            nome_estado (str): Nome completo do estado.
        """
        posicao = self.funcao_hash(sigla)
        novo_nodo = Node(sigla, nome_estado)
        novo_nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_nodo

    def imprimir(self):
        """Imprime a tabela hash com os estados em cada posição."""
        for i in range(10):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            while atual:
                print(atual.sigla, end=" ")
                atual = atual.proximo
            print('None')

# Teste do software
# Exigência de Saída de Console 1 de 3
print("Tabela Hash antes de inserir qualquer informação:")
tabela_hash = HashTable()
tabela_hash.imprimir()

# Inserindo os 26 estados e o Distrito Federal
estados = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), 
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), 
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), 
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), 
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), 
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), 
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

for sigla, nome in estados:
    tabela_hash.inserir(sigla, nome)

# Exigência de Saída de Console 2 de 3
print("Tabela Hash após inserir os estados e o Distrito Federal:")
tabela_hash.imprimir()

# Inserindo o estado fictício BK
tabela_hash.inserir('VB', 'Vinicius Borin')

# Exigência de Saída de Console 3 de 3
print("Tabela Hash após inserir os estados, o Distrito Federal e o estado fictício:")
tabela_hash.imprimir()
