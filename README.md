# 🧠 Jarvis - Assistente Pessoal com OpenAI (Python)

Um assistente pessoal inspirado no Jarvis, capaz de interpretar comandos em linguagem natural e executar ações como gerenciar tarefas, metas, agenda, notificações e consumir APIs externas.

Este projeto foi criado para ser simples, modular e altamente escalável, servindo como base para sistemas mais avançados de automação pessoal.

---

## 🚀 Funcionalidades

- 💬 Chat inteligente com IA (OpenAI)
- 📋 Gerenciamento de tarefas
- 🎯 Criação e acompanhamento de metas
- 🗓 Organização de agenda
- 🔔 Sistema de notificações simples
- 🌐 Integração com API externa (ex: clima)
- 🧠 Interpretação de comandos em linguagem natural

---

## 🧠 Como funciona

O Jarvis utiliza a API da OpenAI para interpretar o que o usuário deseja e transformar isso em ações estruturadas.

Exemplo:

Usuário: "preciso estudar inglês amanhã"  
→ IA responde: ADD_TASK: estudar inglês amanhã  
→ O sistema salva automaticamente como tarefa  

Usuário: "como está o clima em São Paulo?"  
→ IA responde: GET_WEATHER: São Paulo  
→ O sistema chama uma API externa e retorna o resultado  

---

## 📁 Estrutura do Projeto

src/
│── app.py             # Núcleo do sistema
│── brain.py           # Integração com OpenAI (inteligência)
│── memory.py          # Armazenamento local
│── scheduler.py       # Sistema de notificações
│── integrations.py    # Integração com APIs externas
│── memory.json        # Base de dados local (gerado automaticamente)
│── requirements.txt
│── .env

---

## ⚙️ Instalação

### 1. Clone o projeto

git clone https://github.com/seu-usuario/jarvis-assistente.git  
cd jarvis-assistente  

---

### 2. Crie um ambiente virtual (opcional)

python -m venv venv  

# Linux/Mac  
source venv/bin/activate  

# Windows  
venv\Scripts\activate  

---

### 3. Instale as dependências

pip install -r requirements.txt  

---

## 🔐 Configuração

Crie um arquivo `.env` na raiz do projeto:

OPENAI_API_KEY=sua_chave_aqui  

---

## ▶️ Como executar

python app.py  

---

## 💬 Exemplos de uso

Você pode interagir com o Jarvis de forma natural:

Você: "preciso estudar .NET hoje"  
→ Adiciona uma tarefa  

Você: "minha meta é ganhar 10k por mês"  
→ Adiciona uma meta  

Você: "tenho reunião às 15h"  
→ Adiciona um evento na agenda  

Você: "como está o clima no Rio de Janeiro?"  
→ Retorna o clima via API externa  

Você: "status"  
→ Mostra todos os dados armazenados  

---

## 🧩 Comandos especiais

status → Exibe tarefas, metas e agenda  
sair   → Encerra o programa  

---

## 💾 Armazenamento

Os dados são salvos localmente no arquivo:

memory.json  

Exemplo:

{
  "tasks": ["Estudar inglês"],
  "goals": ["Ganhar 10k/mês"],
  "agenda": ["Reunião às 15h"]
}

---

## 🌐 Integrações

Atualmente o sistema possui integração com API de clima usando:

https://wttr.in/

Você pode facilmente adicionar novas integrações no arquivo:

integrations.py  

Exemplos futuros:

- Google Calendar  
- APIs financeiras  
- Sistemas internos  
- Automação de tarefas  

---

## 🔔 Notificações

O sistema utiliza uma abordagem simples com agendamentos locais usando a biblioteca:

schedule  

Atualmente imprime notificações no terminal, mas pode ser evoluído para:

- WhatsApp  
- Telegram  
- Email  
- Push notifications  

---

## 🔧 Tecnologias utilizadas

- Python  
- OpenAI API  
- python-dotenv  
- requests  
- schedule  
- JSON (armazenamento local)  

---

## 🚀 Roadmap (próximos passos)

- 🌐 Criar API com FastAPI  
- 🧠 Implementar memória inteligente (RAG + embeddings)  
- 📱 Integração com WhatsApp / Telegram  
- 🎙 Suporte a voz (Speech-to-Text + TTS)  
- 🖥 Interface web (estilo ChatGPT)  
- ☁️ Persistência em banco de dados (MongoDB, PostgreSQL)  

---

## 💡 Possibilidades de uso

- Assistente pessoal completo  
- Organização de rotina  
- Gestão de metas  
- Automação de tarefas  
- Base para SaaS  
- Ferramenta interna para produtividade  

---

## 📄 Licença

Este projeto é livre para uso e modificação.

---

## ⭐ Contribuição

Sinta-se à vontade para melhorar este projeto, adicionar integrações ou evoluir o Jarvis para algo ainda mais poderoso.

Se esse projeto te ajudou, considere dar uma estrela ⭐ no repositório!