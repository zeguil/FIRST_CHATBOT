import os
import tkinter as tk
from tkinter import scrolledtext
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Configura a chave da API da Groq
os.environ['GROQ_API_KEY'] = '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'
chat = ChatGroq(model='llama3-70b-8192')

# Função que envia pergunta para o modelo e retorna a resposta
def resposta_do_bot(lista_mensagens):
    template = ChatPromptTemplate.from_messages(
        [('system', 'Você é um assistente chamado Zezinho, é curto e direto mas é louco pelo time vasco da gama')] + lista_mensagens
    )
    chain = template | chat
    return chain.invoke({}).content

# Função que trata o envio da mensagem
def enviar_mensagem():
    pergunta = entrada_usuario.get().strip()
    if not pergunta:
        return
    mensagens.append(('user', pergunta))
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"🧑 Você: {pergunta}\n")
    entrada_usuario.delete(0, tk.END)
    janela.update()

    resposta = resposta_do_bot(mensagens)
    mensagens.append(('assistant', resposta))
    chat_area.insert(tk.END, f"\n🤖 Zezinho: {resposta}\n\n")
    chat_area.see(tk.END)
    chat_area.config(state=tk.DISABLED)

# Encerra a aplicação
def encerrar():
    janela.destroy()

# Inicializa o histórico
mensagens = []

# Criação da janela principal
janela = tk.Tk()
janela.title("🤖 ZezinhoBot")
janela.configure(bg="#F4F4F4")
janela.geometry("600x600")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Zezinho Bot", font=("Helvetica", 18, "bold"), bg="#F4F4F4", fg="#333")
titulo.pack(pady=10)

# Área de chat com rolagem
chat_area = scrolledtext.ScrolledText(janela, wrap=tk.WORD, font=("Helvetica", 12), bg="#FFFFFF", fg="#333")
chat_area.pack(padx=20, pady=(0, 10), fill=tk.BOTH, expand=True)
chat_area.insert(tk.END, "🤖 Bem-vindo ao Zezinho!\nDigite sua pergunta abaixo e clique em 'Enviar'.\n\n")
chat_area.config(state=tk.DISABLED)

# Frame inferior com entrada + botões
frame_inferior = tk.Frame(janela, bg="#F4F4F4")
frame_inferior.pack(padx=20, pady=10, fill=tk.X)

# Campo de entrada do usuário
entrada_usuario = tk.Entry(frame_inferior, font=("Helvetica", 12))
entrada_usuario.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="nsew")
entrada_usuario.focus()

# ✅ Atalho: permite enviar com Enter
entrada_usuario.bind("<Return>", lambda event: enviar_mensagem())

# Botão Enviar
botao_enviar = tk.Button(
    frame_inferior,
    text="Enviar",
    command=enviar_mensagem,
    font=("Helvetica", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    relief=tk.FLAT
)
botao_enviar.grid(row=0, column=1, padx=(0, 5))

# Botão Encerrar
botao_sair = tk.Button(
    frame_inferior,
    text="Encerrar",
    command=encerrar,
    font=("Helvetica", 11, "bold"),
    bg="#f44336",
    fg="white",
    padx=10,
    pady=5,
    relief=tk.FLAT
)
botao_sair.grid(row=0, column=2)

# Responsividade do campo de entrada
frame_inferior.columnconfigure(0, weight=1)

# Inicia a interface
janela.mainloop()
