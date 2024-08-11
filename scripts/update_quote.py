import json
import random
import re

# Cargar las frases
with open('scripts/quotes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Seleccionar una frase aleatoria
frase = random.choice(data['frases'])

# Leer el contenido del archivo HTML
with open('index.html', 'r', encoding='utf-8') as f:
    contenido = f.read()

# Reemplazar la frase actual con la nueva frase
nuevo_contenido = re.sub(
    r'<h1 class="quote">.*?</h1>',
    f'<h1 class="quote">{frase}</h1>',
    contenido
)

# Actualizar el título
nuevo_contenido = re.sub(
    r'<title>Motivate 👏\|.*?</title>',
    f'<title>Motivate 👏| {frase}</title>',
    nuevo_contenido
)

# Escribir el nuevo contenido en el archivo HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(nuevo_contenido)

print(f"Frase actualizada: {frase}")
