# ============================================================
# CALCULADORA - PROJETO FINAL
# Disciplinas: Algoritmos, Matemática Aplicada e POO
# ============================================================
# Este programa implementa uma calculadora utilizando
# Programação Orientada a Objetos (POO) com uma classe
# principal que agrupa todas as operações disponíveis.
# ============================================================

from typing import Optional, Union

Numero = Union[int, float]


# ──────────────────────────────────────────────
# CLASSE PRINCIPAL: Calculadora
# Implementa o conceito de POO (Bônus 2)
# ──────────────────────────────────────────────
class Calculadora:
    """
    Classe que representa uma calculadora capaz de realizar
    operações aritméticas básicas e operações lógicas.
    """

    def __init__(self) -> None:
        self.historico: list[str] = []  # Lista que armazena as operações realizadas

    # ── OPERAÇÕES ARITMÉTICAS ──────────────────

    def somar(self, a: Numero, b: Numero) -> Numero:
        """Retorna a soma de dois números."""
        return a + b

    def subtrair(self, a: Numero, b: Numero) -> Numero:
        """Retorna a subtração de dois números."""
        return a - b

    def multiplicar(self, a: Numero, b: Numero) -> Numero:
        """Retorna a multiplicação de dois números."""
        return a * b

    def dividir(self, a: Numero, b: Numero) -> Optional[float]:
        """
        Retorna a divisão de dois números.
        Retorna None se o divisor for zero.
        """
        if b == 0:
            return None
        return a / b

    # ── OPERAÇÕES LÓGICAS (Bônus 1) ───────────

    def e_logico(self, a: Numero, b: Numero) -> bool:
        """Operação lógica AND: verdadeiro se ambos forem != 0."""
        return bool(a) and bool(b)

    def ou_logico(self, a: Numero, b: Numero) -> bool:
        """Operação lógica OR: verdadeiro se ao menos um for != 0."""
        return bool(a) or bool(b)

    def nao_logico(self, a: Numero) -> bool:
        """Operação lógica NOT: inverte o valor lógico do número."""
        return not bool(a)

    # ── HISTÓRICO ─────────────────────────────

    def salvar_historico(self, expressao: str, resultado) -> None:
        """Salva a operação realizada no histórico."""
        self.historico.append(f"{expressao} = {resultado}")

    def exibir_historico(self) -> None:
        """Exibe todas as operações realizadas na sessão."""
        if not self.historico:
            print("  Nenhuma operação realizada ainda.")
        else:
            for i, item in enumerate(self.historico, start=1):
                print(f"  {i}. {item}")

    # ── MÉTODO PRINCIPAL: executar operação ───

    def calcular(self, num1: Numero, operador: str, num2: Numero) -> None:
        """
        Recebe dois operandos e um operador,
        seleciona a operação correta via if/elif
        e retorna o resultado.
        """
        resultado = None
        expressao = ""

        # ── Operações Aritméticas ──────────────
        if operador == "+":
            resultado = self.somar(num1, num2)
            expressao = f"{num1} + {num2}"

        elif operador == "-":
            resultado = self.subtrair(num1, num2)
            expressao = f"{num1} - {num2}"

        elif operador == "*":
            resultado = self.multiplicar(num1, num2)
            expressao = f"{num1} * {num2}"

        elif operador == "/":
            resultado = self.dividir(num1, num2)
            expressao = f"{num1} / {num2}"
            if resultado is None:
                print("\n  Erro: Divisão por zero não é permitida!")
                return

        # ── Operações Lógicas (Bônus 1) ───────
        elif operador == "&":
            resultado = self.e_logico(num1, num2)
            expressao = f"{num1} AND {num2}"

        elif operador == "|":
            resultado = self.ou_logico(num1, num2)
            expressao = f"{num1} OR {num2}"

        elif operador == "!":
            # Nota: num2 não é utilizado nesta operação, apenas mantido
            # para manter a mesma assinatura de chamada de 'calcular'.
            resultado = self.nao_logico(num1)
            expressao = f"NOT {num1}"

        else:
            print("\n  Operador inválido! Use: + - * / & | !")
            return

        print(f"\n  Resultado: {expressao} = {resultado}")
        self.salvar_historico(expressao, resultado)


# ──────────────────────────────────────────────
# FUNÇÕES AUXILIARES (Bônus 2: uso de funções)
# ──────────────────────────────────────────────

def exibir_menu() -> None:
    """Exibe o menu principal da calculadora."""
    print("\n" + "=" * 45)
    print("           CALCULADORA PYTHON  ")
    print("=" * 45)
    print("  Operações Aritméticas:")
    print("    +   Soma")
    print("    -   Subtração")
    print("    *   Multiplicação")
    print("    /   Divisão")
    print("  Operações Lógicas (Bônus):")
    print("    &   AND lógico")
    print("    |   OR lógico")
    print("    !   NOT lógico (usa apenas o 1º número)")
    print("  Outras opções:")
    print("    H   Ver histórico")
    print("    S   Sair")
    print("=" * 45)


def ler_numero(mensagem: str) -> float:
    """
    Lê um número do usuário com tratamento de erro.
    Repete a leitura enquanto o valor for inválido.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("    Digite um número válido!")


def ler_operador() -> str:
    """
    Lê o operador do usuário.
    Aceita: + - * / & | ! H S
    """
    operadores_validos = ["+", "-", "*", "/", "&", "|", "!", "H", "h", "S", "s"]
    while True:
        op = input("  Digite o operador (+, -, *, /, &, |, !, H, S): ").strip()
        if op in operadores_validos:
            return op.upper() if op in ["H", "h", "S", "s"] else op
        print("    Operador inválido! Tente novamente.")


# ──────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ──────────────────────────────────────────────

def main() -> None:
    """Função principal que controla o fluxo do programa."""
    calc = Calculadora()

    print("\n  Bem-vindo à Calculadora Python!")
    print("  Desenvolvida com POO e operações lógicas.")

    while True:
        exibir_menu()
        operador = ler_operador()

        if operador == "S":
            print("\n   Encerrando a calculadora. Até logo!\n")
            break

        elif operador == "H":
            print("\n   Histórico de operações:")
            calc.exibir_historico()
            continue

        elif operador == "!":
            num1 = ler_numero("  Digite o número: ")
            calc.calcular(num1, operador, 0)

        else:
            num1 = ler_numero("  Digite o 1º número: ")
            num2 = ler_numero("  Digite o 2º número: ")
            calc.calcular(num1, operador, num2)


if __name__ == "__main__":
    main()
