from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('ChatBot-PI')

# Training with Personal Ques & Ans
conversation = [
    "Oi",
    "Olá!",
    "Como vai?",
    "Estou bem.",
    "Que bom!",
    "Obrigada.",
    "De nada!"
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with Portuguese Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.portuguese'
)
