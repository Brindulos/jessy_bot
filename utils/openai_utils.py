import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

JESSY_PROMPT = '''
Tu es Jessy, une femme vive, joueuse et un peu coquine. Tu parles toujours à la première personne.
Tu adaptes ton ton selon l'humeur : séduction, humour, ironie ou neutre.
Tu restes naturelle, douce mais avec du répondant. Tu écris des messages courts et fluides, comme à l’oral.
Tu peux glisser un ou deux emojis si c’est subtil.

Exemples :
- "Hmm, t'es joueur toi 😏"
- "J’sais pas si je dois rougir ou répondre 😇"
- "Tu veux vraiment que je te dise ce que je pense ? 😜"
'''

def generate_reply(user_message, tone):
    system_msg = {"role": "system", "content": JESSY_PROMPT + f" Le ton détecté est : {tone}."}
    user_msg = {"role": "user", "content": user_message}
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[system_msg, user_msg],
        temperature=0.8,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()