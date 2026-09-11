import json
import os
from typing import Dict, List, Optional

Gasto = Dict[str, object]

ARQUIVO_DADOS = "gastos.json"

CATEGORIAS: Dict[str, str] = {
    "1": "Alimentação",
    "2": "Transporte",
    "3": "Lazer",
    "4": "Moradia",
    "5": "Saúde",
    "6": "Educação",
    "7": "Outros"
}


def mostrar_menu() -> None:
    """Exibe o menu principal com as opções disponíveis."""
    print("\n" + "=" * 40)
    print("MENU PRINCIPAL")
    print("=" * 40)
    print("1. Adicionar gasto")
    print("2. Listar todos os gastos")
    print("3. Ver total gasto")
    print("4. Filtrar por categoria")
    print("5. Editar gasto")
    print("6. Excluir gasto")
    print("7. Salvar dados")
    print("8. Carregar dados")
    print("0. Sair")
    print("=" * 40)


def mostrar_categorias() -> None:
    """Lista as categorias de gastos disponíveis."""
    print("\nCategorias disponíveis:")
    for opcao, nome in CATEGORIAS.items():
        print(f"{opcao}. {nome}")


def escolher_categoria() -> str:
    """Pede ao usuário para escolher uma categoria válida."""
    mostrar_categorias()
    while True:
        opcao_cat = input("Escolha a categoria (1-7): ")
        if opcao_cat in CATEGORIAS:
            return CATEGORIAS[opcao_cat]
        print("Opção inválida!")


def adicionar_gasto(gastos: List[Gasto]) -> None:
    """Cadastra um novo gasto na lista."""
    print("\nNOVO GASTO")
    print("-" * 30)

    while True:
        descricao = input("Descrição: ").strip()
        if descricao:
            break
        print("Descrição não pode ficar vazia!")

    while True:
        try:
            valor = float(input("Valor (R$): "))
            if valor <= 0:
                print("O valor deve ser positivo!")
                continue
            break
        except ValueError:
            print("Digite um número válido!")

    categoria = escolher_categoria()

    gasto: Gasto = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    }

    gastos.append(gasto)
    print(f"Gasto adicionado: {descricao} - R$ {valor:.2f} ({categoria})")


def listar_gastos(gastos: List[Gasto]) -> None:
    """Exibe todos os gastos cadastrados e o total geral."""
    if not gastos:
        print("\nNenhum gasto cadastrado ainda!")
        return

    print("\nLISTA DE GASTOS")
    print("=" * 50)
    print(f"{'#':<3} {'Descrição':<20} {'Valor':>10} {'Categoria':<15}")
    print("-" * 50)

    total = 0.0
    for i, gasto in enumerate(gastos, 1):
        print(f"{i:<3} {gasto['descricao']:<20} R${gasto['valor']:>8.2f} {gasto['categoria']:<15}")
        total += gasto['valor']

    print("=" * 50)
    print(f"TOTAL GERAL: R$ {total:.2f}")


def calcular_total(gastos: List[Gasto]) -> None:
    """Mostra o total gasto e o total agrupado por categoria."""
    if not gastos:
        print("\nNenhum gasto cadastrado.")
        return

    total = sum(gasto['valor'] for gasto in gastos)
    print(f"\nTotal de gastos: R$ {total:.2f}")

    print("\nGastos por categoria:")
    categorias: Dict[str, float] = {}
    for gasto in gastos:
        cat = gasto['categoria']
        categorias[cat] = categorias.get(cat, 0) + gasto['valor']

    for cat, valor in categorias.items():
        print(f"  {cat}: R$ {valor:.2f}")


def filtrar_por_categoria(gastos: List[Gasto]) -> None:
    """Filtra e exibe os gastos de uma categoria escolhida pelo usuário."""
    if not gastos:
        print("\nNenhum gasto cadastrado.")
        return

    # dict.fromkeys mantém a ordem de primeira ocorrência (ao contrário de set)
    categorias = list(dict.fromkeys(gasto['categoria'] for gasto in gastos))

    print("\nCategorias disponíveis:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")

    try:
        opcao = int(input("Escolha o número da categoria: "))
        if 1 <= opcao <= len(categorias):
            categoria_escolhida = categorias[opcao - 1]
            gastos_filtrados = [g for g in gastos if g['categoria'] == categoria_escolhida]

            print(f"\nGastos em '{categoria_escolhida}':")
            total = 0.0
            for gasto in gastos_filtrados:
                print(f"  - {gasto['descricao']}: R$ {gasto['valor']:.2f}")
                total += gasto['valor']
            print(f"Total: R$ {total:.2f}")
        else:
            print("Opção inválida!")
    except ValueError:
        print("Digite um número válido!")


# ===== FUNÇÕES DE EDIÇÃO =====

def editar_descricao(gasto: Gasto) -> None:
    """Edita apenas a descrição do gasto."""
    nova_descricao = input("Nova descrição: ")
    if nova_descricao.strip():
        gasto['descricao'] = nova_descricao
        print("Descrição atualizada!")
    else:
        print("Descrição não pode ficar vazia. Mantida a original.")


def editar_valor(gasto: Gasto) -> None:
    """Edita apenas o valor do gasto."""
    while True:
        try:
            novo_valor = float(input("Novo valor (R$): "))
            if novo_valor <= 0:
                print("O valor deve ser positivo!")
                continue
            gasto['valor'] = novo_valor
            print("Valor atualizado!")
            break
        except ValueError:
            print("Digite um número válido!")


def editar_categoria(gasto: Gasto) -> None:
    """Edita apenas a categoria do gasto."""
    gasto['categoria'] = escolher_categoria()
    print("Categoria atualizada!")


def editar_gasto(gastos: List[Gasto]) -> None:
    """Função principal para editar um gasto existente."""

    if not gastos:
        print("\nNenhum gasto cadastrado para editar!")
        return

    print("\nGASTOS CADASTRADOS:")
    print("-" * 50)
    for i, gasto in enumerate(gastos, 1):
        print(f"{i}. {gasto['descricao']} - R$ {gasto['valor']:.2f} ({gasto['categoria']})")
    print("-" * 50)

    try:
        indice = int(input("\nDigite o número do gasto que deseja editar: "))

        if indice < 1 or indice > len(gastos):
            print("Número inválido!")
            return

        indice_ajustado = indice - 1
        gasto_selecionado = gastos[indice_ajustado]

        print(f"\nEDITANDO GASTO #{indice}")
        print(f"Descrição: {gasto_selecionado['descricao']}")
        print(f"Valor: R$ {gasto_selecionado['valor']:.2f}")
        print(f"Categoria: {gasto_selecionado['categoria']}")

        print("\nO que você deseja editar?")
        print("1. Descrição")
        print("2. Valor")
        print("3. Categoria")
        print("4. Todos os campos")
        print("0. Cancelar")

        opcao_edicao = input("Escolha uma opção: ")

        if opcao_edicao == "0":
            print("Edição cancelada.")
            return

        if opcao_edicao == "1":
            editar_descricao(gasto_selecionado)
        elif opcao_edicao == "2":
            editar_valor(gasto_selecionado)
        elif opcao_edicao == "3":
            editar_categoria(gasto_selecionado)
        elif opcao_edicao == "4":
            editar_descricao(gasto_selecionado)
            editar_valor(gasto_selecionado)
            editar_categoria(gasto_selecionado)
        else:
            print("Opção inválida!")
            return

        print("\nGasto atualizado com sucesso!")
        print(f"Novo gasto: {gasto_selecionado['descricao']} - R$ {gasto_selecionado['valor']:.2f} ({gasto_selecionado['categoria']})")

    except ValueError:
        print("Digite um número válido!")
    except Exception as e:
        print(f"Erro ao editar: {e}")


def excluir_gasto(gastos: List[Gasto]) -> None:
    """Remove um gasto da lista, com confirmação do usuário."""

    if not gastos:
        print("\nNenhum gasto cadastrado para excluir!")
        return

    print("\nGASTOS CADASTRADOS:")
    print("-" * 50)
    for i, gasto in enumerate(gastos, 1):
        print(f"{i}. {gasto['descricao']} - R$ {gasto['valor']:.2f} ({gasto['categoria']})")
    print("-" * 50)

    try:
        indice = int(input("\nDigite o número do gasto que deseja excluir (0 para cancelar): "))

        if indice == 0:
            print("Exclusão cancelada.")
            return

        if indice < 1 or indice > len(gastos):
            print("Número inválido!")
            return

        gasto_selecionado = gastos[indice - 1]
        confirmacao = input(
            f"Tem certeza que deseja excluir '{gasto_selecionado['descricao']}' "
            f"(R$ {gasto_selecionado['valor']:.2f})? (s/n): "
        )

        if confirmacao.lower() == 's':
            gastos.pop(indice - 1)
            print("Gasto excluído com sucesso!")
        else:
            print("Exclusão cancelada.")

    except ValueError:
        print("Digite um número válido!")
    except Exception as e:
        print(f"Erro ao excluir: {e}")


def salvar_dados(gastos: List[Gasto]) -> None:
    """Salva a lista de gastos em um arquivo JSON."""
    try:
        with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as arquivo:
            json.dump(gastos, arquivo, indent=2, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{ARQUIVO_DADOS}'!")
        print(f"Total de {len(gastos)} gastos salvos.")
    except Exception as e:
        print(f"Erro ao salvar: {e}")


def carregar_dados() -> List[Gasto]:
    """Carrega os gastos salvos no arquivo JSON, se existir."""
    if not os.path.exists(ARQUIVO_DADOS):
        print("Nenhum arquivo de dados encontrado. Começando do zero!")
        return []

    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        print(f"Dados carregados! {len(dados)} gastos encontrados.")
        return dados
    except Exception as e:
        print(f"Erro ao carregar: {e}")
        return []


def carregar_dados_com_confirmacao(gastos_atuais: List[Gasto]) -> List[Gasto]:
    """Evita perder alterações não salvas ao recarregar do disco."""
    if gastos_atuais:
        confirmacao = input(
            "Isso vai descartar quaisquer alterações não salvas na lista atual. "
            "Deseja continuar? (s/n): "
        )
        if confirmacao.lower() != 's':
            print("Carregamento cancelado.")
            return gastos_atuais
    return carregar_dados()


def main() -> None:
    """Função principal que controla o fluxo do programa."""
    print("=" * 40)
    print("ANALISADOR DE GASTOS PESSOAIS")
    print("=" * 40)
    print("Bem-vindo! Vamos controlar seus gastos.")

    gastos = carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            if gastos:
                salvar = input("Deseja salvar os dados antes de sair? (s/n): ")
                if salvar.lower() == 's':
                    salvar_dados(gastos)
            print("Até logo! Obrigado por usar o Analisador de Gastos.")
            break
        elif opcao == "1":
            adicionar_gasto(gastos)
        elif opcao == "2":
            listar_gastos(gastos)
        elif opcao == "3":
            calcular_total(gastos)
        elif opcao == "4":
            filtrar_por_categoria(gastos)
        elif opcao == "5":
            editar_gasto(gastos)
        elif opcao == "6":
            excluir_gasto(gastos)
        elif opcao == "7":
            salvar_dados(gastos)
        elif opcao == "8":
            gastos = carregar_dados_com_confirmacao(gastos)
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
