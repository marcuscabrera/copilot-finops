from __future__ import annotations

import argparse

from dotenv import load_dotenv

from .agents import FinOpsAgentSystem


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="FinOps Agents (Python + LangChain)")
    parser.add_argument("--question", "-q", help="Pergunta para o agente")
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()
    system = FinOpsAgentSystem()

    if args.question:
        result = system.answer(args.question)
        print(f"[roteador] agente selecionado: {result.provider.value}\n")
        print(result.answer)
        return

    print("FinOps Agents pronto. Digite sua pergunta (ou 'sair/exit/quit').")
    while True:
        question = input("\n> ").strip()
        if question.lower() in {"sair", "exit", "quit"}:
            break
        if not question:
            continue
        result = system.answer(question)
        print(f"\n[roteador] agente selecionado: {result.provider.value}\n")
        print(result.answer)


if __name__ == "__main__":
    main()
