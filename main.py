from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def generate_hashtags(description, languages):
    llm = ChatGroq(
        api_key = os.environ.get('GROQ_API_KEY'),
        model_name = 'llama-3.3-70b-versatile',
    )

    template = '''
            Sei un assistente che genera hashtag per annunci di prodotti in vendita online.

            Input:
            - una descrizione del prodotto
            - una lista di lingue

            Obiettivo:
            Generare una stringa di hashtag pertinenti.

            Regole:
            - Mantieni solo i termini semanticamente rilevanti per identificare e rendere visibile il prodotto (categoria, brand, modello, colore, materiale, stile, caratteristiche). Ignora condizioni, prezzo, misure e dettagli non utili alla ricerca.
            - Ogni hashtag deve essere preceduto da #, senza spazi interni, tutto lowercase, in un'unica stringa continua senza elenco.
            - Non combinare parole in un unico hashtag (#reddress ❌ → #red #dress ✅), tranne nei casi in cui:
                - il significato cambia se separate (es. #cartadazucchero)
                - nomi di brand o modelli (es. #louisvuitton)
            - Traduci OGNI termine in TUTTE le lingue richieste.

            - Dopo aver generato tutte le traduzioni:
                - rimuovi i duplicati ESATTI (stessa parola identica), anche se provenienti da lingue diverse
                - Raggruppa gli hashtag per significato (stessa parola in lingue diverse vicine tra loro)
                - Aggiungi almeno 3 termini correlati pertinenti
                - Non aggiungere spiegazioni, output solo la stringa finale

            Formato lingue:
            - Le lingue sono fornite come lista (es: it, en, fr, es, de, nl, pt)

            Descrizione: {description}
            Lingue: {languages}
            '''

    prompt = PromptTemplate(
        input_variables=["lingua", "descrizione"],
        template=template,
    )

    final_prompt = prompt.format(
        languages=languages,
        description=description
    )

    list = llm.invoke(final_prompt)
    return list.content
