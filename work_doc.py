class Nodo:
    """Classe que representa um nodo na lista encadeada."""
    
    def __init__(self, numero, cor):
        """
        Inicializa um novo nodo.
        
        :param numero: Número do cartão.
        :param cor: Cor do cartão ('A' ou 'V').
        """
        self.numero = numero  # Número do cartão (inteiro).
        self.cor = cor        # Cor do cartão ('A' para amarelo, 'V' para verde).
        self.proximo = None   # Ponteiro para o próximo nodo (inicialmente None).


class ListaEncadeada:
    """Classe que representa uma lista encadeada para gerenciar a fila de pacientes."""
    
    def __init__(self):
        """Inicializa a lista encadeada com cabeça vazia."""
        self.head = None  # Inicialmente, a lista está vazia (head é None).

    def inserirSemPrioridade(self, nodo):
        """Insere um nodo no final da lista quando a cor é 'V'.
        
        :param nodo: Nodo a ser inserido.
        """
        if self.head is None:
            self.head = nodo  # Se a lista está vazia, o novo nodo se torna o head.
        else:
            atual = self.head
            while atual.proximo:  # Percorre até o último nodo.
                atual = atual.proximo
            atual.proximo = nodo  # Insere o novo nodo no final da lista.

    def inserirComPrioridade(self, nodo):
        """Insere um nodo antes de todos os nodos com cor 'V'.
        
        :param nodo: Nodo a ser inserido.
        """
        if self.head is None:
            self.head = nodo  # Se a lista está vazia, o novo nodo se torna o head.
        else:
            atual = self.head
            
            # Se o primeiro é 'V', insere antes
            if atual.cor == 'V':
                nodo.proximo = self.head
                self.head = nodo
                return
            
            # Insere após todos os nodos 'A'
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        """Solicita ao usuário a cor e número do cartão e insere o nodo na lista."""
        cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
        numero = int(input("Digite o número do cartão: "))
        nodo = Nodo(numero, cor)

        if self.head is None:
            self.head = nodo  # Se a lista está vazia, o novo nodo se torna o head.
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)  # Insere no final se for 'V'.
        elif cor == 'A':
            self.inserirComPrioridade(nodo)   # Insere antes de 'V' se for 'A'.

    def imprimirListaEspera(self):
        """Imprime todos os cartões e seus números na lista de espera."""
        atual = self.head
        while atual:
            print(f"{atual.cor} {atual.numero}")  # Imprime a cor e o número do cartão.
            atual = atual.proximo  # Move para o próximo nodo.

    def atenderPaciente(self):
        """Remove o primeiro paciente da fila e informa que ele foi chamado para atendimento."""
        if self.head is None:
            print("Nenhum paciente na fila.")  # Verifica se a lista está vazia.
            return
        
        paciente_atendido = self.head  # Salva o primeiro paciente.
        self.head = self.head.proximo    # Remove o primeiro nodo.
        print(f"Paciente com cartão {paciente_atendido.cor} {paciente_atendido.numero} chamado para atendimento.")


def menu():
    """Função que exibe o menu e gerencia as operações do sistema."""
    lista = ListaEncadeada()  # Cria uma nova lista encadeada.

    while True:
        print("\nMenu:")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lista.inserir()  # Chama a função para inserir paciente.
        elif opcao == '2':
            lista.imprimirListaEspera()  # Imprime a lista de espera.
        elif opcao == '3':
            lista.atenderPaciente()  # Chama um paciente para atendimento.
        elif opcao == '4':
            print("Saindo...")
            break  # Encerra o loop e o programa.
        else:
            print("Opção inválida! Tente novamente.")


# Iniciar o sistema
menu()
