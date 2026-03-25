from fastapi import FastAPI
from pydantic import BaseModel
import random

class Frase(BaseModel):
        texto: str

frases = [
    "Funciona na minha máquina 🤡",
    "Bug? Não, é feature.",
    "Programar é transformar café em código.",
    "Nada é mais permanente que uma gambiarra temporária.",
    "Se debug é remover bugs, então programar é criar bugs.",
    "99 pequenos bugs no código, corrija um... 127 bugs no código.",
    "Stack Overflow salvando vidas desde sempre.",
    "Eu não quebrei o código, só testei um cenário alternativo.",
    "Compilou? Então sobe pra produção.",
    "Na dúvida, reinicia.",
    "Isso não é um bug, é comportamento inesperado.",
    "Já tentou desligar e ligar de novo?",
    "Meu código funciona, só não sei por quê.",
    "Eu entendo o código que escrevi... às vezes.",
    "Deploy de sexta-feira é emoção pura.",
    "Código limpo é aquele que você ainda entende amanhã.",
    "Refatorar: mexer no código e torcer pra não quebrar.",
    "Só mais um ajuste rapidinho...",
    "Se está funcionando, não encosta!",
    "Documentação? A gente vê isso depois.",
    "Código sem comentário é um enigma.",
    "Frontend bonito, backend chorando.",
    "Backend sólido, frontend quebrado.",
    "JSON é só um XML que foi pra academia.",
    "CSS: agora vai!",
    "Centralizar div: missão impossível.",
    "Esse erro não estava aqui ontem...",
    "Quem fez isso? (fui eu mesmo)",
    "Uma linha de código, mil possibilidades de erro.",
    "Prod tá quebrado? Deve ser cache.",
    "Funciona em dev, quebra em prod — clássico.",
    "Teste em produção é coragem.",
    "Versão final FINAL mesmo agora vai.",
    "Só vou mudar isso aqui rapidinho... 3 horas depois...",
    "Sem tempo pra testar, manda assim mesmo.",
    "Código bom é código que funciona.",
    "Código perfeito é aquele que você não precisa mexer.",
    "O problema não é o código, é o requisito.",
    "Na teoria é simples.",
    "Na prática é outro projeto.",
    "Isso aqui era pra ser rápido.",
    "Era só um projetinho...",
    "Eu sei o que estou fazendo (não sei).",
    "Debugger: melhor amigo do dev.",
    "Console.log resolve tudo.",
    "Se não deu erro, talvez esteja errado.",
    "Quanto mais mexe, mais quebra.",
    "Um bug corrigido, dois surgem.",
    "A culpa é sempre do backend (ou do frontend).",
    "Se ninguém reclamar, tá funcionando."
]

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois você pode restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# retorna frase aleatoria
@app.get("/")
def home():
        return {"frase": random.choice(frases)}


# adiciona uma frase
@app.post("/addfrase")
def add_Frase(frase:Frase):
        frases.append(frase.texto)
        return {"msg": "Frase adicionada"}

# retorna todas as frases
@app.get("/frases")
def return_Frases():
        return{"frases": frases}

# retorna frase expecifica
@app.get("/frase/{id}")
def return_frase_Id(id: int):
        if id < 0 or id >= len(frases):
                return {"erro": "Frase nao encontrada"}
        return {"msg": frases[id]}
        
                