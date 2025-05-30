import os
from langchain_groq import ChatGroq

PUBLIC_API_KEY='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'

os.environ['GROQ_API_KEY'] = PUBLIC_API_KEY

chat = ChatGroq(model='llama3-70b-8192') 

resposta = chat.invoke('Olá mundo! Quem é você?')

print(resposta.content)

