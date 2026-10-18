from flask import Flask
import random
app = Flask(__name__)
facts_list = [
    'Saber o que tem no seu prato é essencial para uma alimentação saudável.',
    'A sua alimentação é a sua vida, se alimente conscientemente e com qualidade.',
    'Cosumir menos que 2 litros de água por dia pode levar a desidratação, fadiga e problemas de concentração.'
]
facts_list2 = [
    'A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos',
    'De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.',
    'O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna'
]
@app.route("/")
def home():
    return "<h1>Bem-vindo ao site de fatos aleatórios!</h1><p>Visite <a href='/random_fact'>/random_fact</a> para ver um fato aleatório sobre alimentação ou visite <a href='/random_fact2'>/random_fact2</a> para ver fatos sobre a dependencia tecnológica.</p>"

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/random_fact2")
def random_fact2():
    return f'<p>{random.choice(facts_list2)}</p>'

app.run(debug=True)

