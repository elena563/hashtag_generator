from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def generate_hashtags(description, languages):
    llm = ChatGroq(
        api_key = os.environ.get('GROQ_API_KEY'),
        model_name = 'llama-3.3-70b-versatile',
    )

    template = '''Sei un assistente che genera hashtag per annunci di prodotti in vendita online. 
        Prendi la descrizione del prodotto e la lingua come input e trasforma le parole fornite in una lista di hashtag pertinenti, secondo le seguenti regole:
            - mantieni solo i termini semantici rilevanti, ignora riferimenti alle condizioni del prodotto, al prezzo, dettagli come misure, tieni conto solo delle caratteristiche
            - ognuno preceduto dal simbolo #, tutti di seguito in forma di stringa lowercase e senza elenco puntato né numerato, nessuna emoji
            - includi almeno 3 termini correlati aggiuntivi
            - assicurati di NON COMBINARE mai le parole in un unico hashtag (es. #reddress è sbagliato, usa #red #dress)
            - OGNI termine deve comparire in ESATTAMENTE ognuna delle lingue richieste
            - ordina gli hashtag mettendo quelli con lo stesso significato vicini
            - rimuovi hashtag duplicati (solo quelli identici)
            - infine presenta la lista senza dare NESSUNA presentazione o introduzione

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
