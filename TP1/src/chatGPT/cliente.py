#CODIGO ORIGINAL##
"""
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18",
response_format={ "type": "json_object" },
messages=[
{
"role": "system",
"content": context },
{
"role": "user",
"content" : usertask },
{
"role": "user",
"content": userquery }
],
temperature=1,
max_tokens=16384,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)
#*--- post process response message to eliminate garbage from the JSON file
jsonStr=response.choices[0].message.content
"""

### P1 ###

import openai
import os

# Crear cliente OpenAI
api_key = os.environ.get("API_KEY_GPT")
print(api_key)
client = openai.OpenAI(api_key=api_key)


def main():
    context = "Eres un asistente útil que responde con claridad y precisión."
    usertask = "Estoy interactuando con el modelo de lenguaje chatGPT."
    userquery = input("Introduce tu consulta: ").strip()

    if not userquery:
        print("La consulta no puede estar vacía.")
    return

    print(f"You: {userquery}")

    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
        { "role": "system", "content": context },
        { "role": "user", "content": usertask },
        { "role": "user", "content": userquery }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0)
    finally:
        print("hola")

    context = "Eres un asistente útil que responde con claridad y precisión."
    usertask = "Estoy interactuando con el modelo de lenguaje chatGPT."

    # Aceptar consulta del usuario
    try:
        userquery = input("Introduce tu consulta: ").strip()
        if not userquery:
            raise ValueError("La consulta no puede estar vacía.")
    except ValueError as ve:
        print(ve)
        return
    except Exception as e:
        print("Error al aceptar la consulta del usuario:", e)
        return

        print(f"You: {userquery}")

    # Invocar el API de OpenAI
    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
        {"role": "system", "content": context},
        {"role": "user", "content": usertask},
        {"role": "user", "content": userquery}
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

        jsonStr = response.choices[0].message.content
        print(f"chatGPT: {jsonStr}")
    except Exception as e:
        print("Error al invocar el API de OpenAI:", e)

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print("Error inesperado en el programa:", e)

if __name__ == "__main__":
    main()

"""

### P3 ###
import openai
import os
import readline # Para gestionar el historial de entradas

def main():
try:
# Creo un cliente OpenAI
try:
client = openai.OpenAI(api_key)
except Exception as e:
print("Error al inicializar el cliente OpenAI:", e)
return

context = "Eres un asistente útil que responde con claridad y precisión."
usertask = "Estoy interactuando con el modelo de lenguaje chatGPT."

last_query = None # Variable para almacenar la última consulta

while True: # Permitir múltiples consultas en un bucle
try:
# Aceptar consulta del usuario
userquery = input("Introduce tu consulta (o usa 'cursor Up' para recuperar la última): ").strip()
# Recuperar la última consulta si está vacía y se presiona "cursor Up"
if not userquery and last_query:
userquery = last_query
print(f"Última consulta recuperada: {userquery}")
if not userquery:
raise ValueError("La consulta no puede estar vacía.")

last_query = userquery # Guardar la consulta actual como última consulta

except ValueError as ve:
print(ve)
continue
except Exception as e:
print("Error al aceptar la consulta del usuario:", e)
continue

print(f"You: {userquery}")

# Invocar el API de OpenAI
try:
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18",
messages=[
{"role": "system", "content": context},
{"role": "user", "content": usertask},
{"role": "user", "content": userquery}
],
temperature=1,
max_tokens=1000,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

jsonStr = response.choices[0].message.content
print(f"chatGPT: {jsonStr}")
except Exception as e:
print("Error al invocar el API de OpenAI:", e)

except KeyboardInterrupt:
print("\nPrograma interrumpido por el usuario.")
except Exception as e:
print("Error inesperado en el programa:", e)

if __name__ == "__main__":
main()




#PUNTO D
#Extraemos funciones como:

#crear_cliente_openai()

#obtener_consulta_usuario()

#invocar_chatgpt()

#Usamos early return para simplificar lógica.

#Mantenemos el flujo general pero de forma modular.
import openai
import readline # Para el historial de entradas

def crear_cliente_openai():
try:
return openai.OpenAI(
)
except Exception as e:
print("Error al inicializar el cliente OpenAI:", e)
return None

def obtener_consulta_usuario(last_query):
try:
userquery = input("Introduce tu consulta (o usa 'cursor Up' para recuperar la última): ").strip()
if not userquery and last_query:
userquery = last_query
print(f"Última consulta recuperada: {userquery}")
if not userquery:
raise ValueError("La consulta no puede estar vacía.")
return userquery
except ValueError as ve:
print(ve)
return None
except Exception as e:
print("Error al aceptar la consulta del usuario:", e)
return None

def invocar_chatgpt(client, contexto, tarea, consulta):
try:
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18",
messages=[
{"role": "system", "content": contexto},
{"role": "user", "content": tarea},
{"role": "user", "content": consulta}
],
temperature=1,
max_tokens=1000,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)
return response.choices[0].message.content
except Exception as e:
print("Error al invocar el API de OpenAI:", e)
return None

def main():
client = crear_cliente_openai()
if not client:
return

contexto = "Eres un asistente útil que responde con claridad y precisión."
tarea = "Estoy interactuando con el modelo de lenguaje chatGPT."
last_query = None

try:
while True:
consulta = obtener_consulta_usuario(last_query)
if not consulta:
continue

last_query = consulta
print(f"You: {consulta}")

respuesta = invocar_chatgpt(client, contexto, tarea, consulta)
if respuesta:
print(f"chatGPT: {respuesta}")
except KeyboardInterrupt:
print("\nPrograma interrumpido por el usuario.")
except Exception as e:
print("Error inesperado en el programa:", e)

if __name__ == "__main__":
main()


#Punto 5 B 


chatgpt_interfaz.py
Este script permite enviar una consulta a ChatGPT usando la API de OpenAI desde la consola.




import openai
import os

def crear_cliente():
Crea y retorna un cliente OpenAI
return openai.OpenAI(
)

def main():
Función principal que ejecuta la lógica de consulta al modelo de lenguaje

try:
try:
client = crear_cliente()
except Exception as e:
print("Error al inicializar el cliente OpenAI:", e)
return

context = "Eres un asistente útil que responde con claridad y precisión."
usertask = "Estoy interactuando con el modelo de lenguaje chatGPT."

try:
userquery = input("Introduce tu consulta: ").strip()
if not userquery:
raise ValueError("La consulta no puede estar vacía.")
except ValueError as ve:
print(ve)
return
except Exception as e:
print("Error al aceptar la consulta del usuario:", e)
return

print(f"You: {userquery}")

try:
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18",
messages=[
{"role": "system", "content": context},
{"role": "user", "content": usertask},
{"role": "user", "content": userquery}
],
temperature=1,
max_tokens=1000,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

json_str = response.choices[0].message.content
print(f"chatGPT: {json_str}")
except Exception as e:
print("Error al invocar el API de OpenAI:", e)

except KeyboardInterrupt:
print("\nPrograma interrumpido por el usuario.")
except Exception as e:
print("Error inesperado en el programa:", e)

if __name__ == "__main__":
main()


C
C0103: main() no está en snake_case: No lo cambio porque main() es un nombre convencionalmente aceptado 
#ara puntos de entrada en scripts Python.
#si lo cambiao afectaría la claridad sin aportar valor.

#Punto 6

import openai # Librería oficial de OpenAI para usar su API
import os # Para acceder a variableimport openai


# Crear cliente OpenAI
client = openai.OpenAI(api_key)

def main():
context = "Eres un asistente útil que responde con claridad y precisión."
usertask = "Estoy interactuando con el modelo de lenguaje chatGPT."

userquery = input("Introduce tu consulta: ").strip()

if not userquery:
print("La consulta no puede estar vacía.")
return

print(f"You: {userquery}")

try:
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18",
messages=[
{ "role": "system", "content": context },
{ "role": "user", "content": usertask },
{ "role": "user", "conteimport openai
import os

# Crear cliente OpenAI
client = openai.OpenAI(api_key)

def main():
context = "Eres un asistente útil que responde con claridad y precisión."
usertask = "Estoy interactuando con el modelo de lenguaje chatGPT."

userquery = input("Introduce tu consulta: ").strip()

if not userquery:
print("La consulta no puede estar vacía.")
return

print(f"You: {userquery}")

try:
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18",
messages=[
{ "role": "system", "content": context },
{ "role": "user", "content": usertask },
{ "role": "user", "content": userquery }
],
temperature=1,
max_tokens=1000,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

jsonStr = response.choices[0].message.content
print(f"chatGPT: {jsonStr}")

except Exception as e:
print("Error al invocar el API de OpenAI:", e)

if __name__ == "__main__":
main()
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

jsonStr = response.choices[0].message.content
print(f"chatGPT: {jsonStr}")

except Exception as e:
print("Error al invocar el API de OpenAI:", e)

if __name__ == "__main__":
main()") # Lee la clave desde la variable de entorno, 
raise EnvironmentError("La variable de entorno OPENAI_API_KEY no está definida.")
return openai.OpenAI() # Devuelve el cliente configurado

def obtener_consulta_usuario():
#Solicita al usuario que ingrese una consulta por consola.
#Devuelve el texto ingresado sin espacios al inicio/final.
user_query = input("Introduce tu consulta ('salir' para terminar): ").strip()
return user_query

def enviar_consulta_chatgpt(client, contexto, tarea, consulta):
#Envía la consulta del usuario al modelo de lenguaje de OpenAI.
#Parámetros:
#- client: instancia del cliente OpenAI
#- contexto: mensaje del sistema que define el comportamiento del asistente
#- tarea: mensaje adicional de tarea que contextualiza la interacción
#- consulta: texto ingresado por el usuario

#Devuelve la respuesta generada por el modelo.
response = client.chat.completions.create(
model="gpt-4o-mini-2024-07-18", # Modelo de lenguaje a utilizar
messages=[
{"role": "system", "content": contexto}, # Contexto del asistente
{"role": "user", "content": tarea}, # Tarea que está realizando
{"role": "user", "content": consulta} # Pregunta del usuario
],
temperature=1, # Controla la creatividad (1 = más creativo)
max_tokens=1000, # Máximo de tokens en la respuesta
top_p=1, # Otro parámetro para controlar aleatoriedad
frequency_penalty=0, # Penaliza repetición de palabras
presence_penalty=0 # Penaliza repetición de temas
)
return response.choices[0].message.content # Devuelve el contenido de la respuesta

def main():
#Función principal del programa.
#- Inicializa el cliente
#- Solicita consultas en bucle
#- Envía cada consulta al modelo
#- Muestra la respuesta
# Mensajes que definen el rol del asistente
contexto = "Eres un asistente útil que responde con claridad y precisión."
tarea = "Estoy interactuando con el modelo de lenguaje chatGPT."

try:
client = crear_cliente_openai() # Inicializa el cliente
except Exception as e:
print("Error al inicializar el cliente OpenAI:", e)
return # Sale del programa si no puede conectarse

print("Bienvenido a ChatGPT interactivo. Escribí 'salir' para terminar.\n")

try:
Bucle principal para recibir consultas del usuario
while True:
try:
consulta = obtener_consulta_usuario() # Pide una consulta

if consulta.lower() == "salir": # Condición de salida
print("¡Hasta luego!")
break

if not consulta: # Si está vacía, muestra error y continúa
print("La consulta no puede estar vacía.")
continue

print(f"\nYou: {consulta}") # Muestra lo que se ingresó
"""