import threading
from brain import think
from memory import add_task, add_goal, add_event, get_all
from integrations import get_weather
from scheduler import notify, start_scheduler

def run_scheduler():
    start_scheduler()

def main():
    print("🧠 Jarvis iniciado... (digite 'sair')\n")

    mensagens = [
        {"role": "system", "content": "Você é um assistente pessoal estilo Jarvis."}
    ]

    # inicia scheduler em background
    threading.Thread(target=run_scheduler, daemon=True).start()

    while True:
        user = input("Você: ")

        if user.lower() == "sair":
            break

        if user.lower() == "status":
            data = get_all()
            print("\n📊 STATUS:")
            print(data)
            continue

        mensagens.append({"role": "user", "content": user})

        resposta = think(mensagens)

        # 🔧 interpretação de ações
        if resposta.startswith("ADD_TASK:"):
            task = resposta.replace("ADD_TASK:", "").strip()
            add_task(task)
            print(f"✅ Tarefa adicionada: {task}")

        elif resposta.startswith("ADD_GOAL:"):
            goal = resposta.replace("ADD_GOAL:", "").strip()
            add_goal(goal)
            print(f"🎯 Meta adicionada: {goal}")

        elif resposta.startswith("ADD_EVENT:"):
            event = resposta.replace("ADD_EVENT:", "").strip()
            add_event(event)
            print(f"🗓 Evento adicionado: {event}")

        elif resposta.startswith("GET_WEATHER:"):
            city = resposta.replace("GET_WEATHER:", "").strip()
            clima = get_weather(city)
            print(f"🌤 {clima}")

        else:
            print(f"\n🤖 {resposta}\n")

        mensagens.append({"role": "assistant", "content": resposta})


if __name__ == "__main__":
    main()