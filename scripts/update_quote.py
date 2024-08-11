import json
import random

with open('scripts/quotes.json', 'r') as f:
    data = json.load(f)

frase = random.choice(data['frases'])

with open('../index.html', 'r') as f:
    contenido = f.read()

nuevo_contenido = contenido.replace('<h1>Frase actual</h1>', f'<h1>{frase}</h1>')

with open('../index.html', 'w') as f:
    f.write(nuevo_contenido)
