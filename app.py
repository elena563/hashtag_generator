import streamlit as st
from main import generate_hashtags

st.set_page_config(
    page_title="Generatore Hashtag per Annunci",  # page title
    page_icon="👕",  # favicon
)

st.markdown("""
    <style>
        .st-emotion-cache-1w723zb{
            padding-top: 3rem; 
        }
        h1 {
            color: #007782 !important;
        }
        button[kind="secondary"]{
            background-color: #007782;
            color: white;
        }
        button[kind="secondary"]:hover{
            background-color: #54a3ac;
        }
        pre {
            background-color: #ffffff !important;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
        }
        pre, div[data-baseweb="textarea"], div[data-baseweb="select"]{
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        .stElementContainer{
             padding: 0 10px;
            }
    </style>
""", unsafe_allow_html=True)

st.title("Genera Hashtag multilingue per i tuoi annunci su Vinted o Subito.it")
st.text("Inserisci la descrizione del tuo annuncio e scegli le lingue che desideri, di default sono selezionate le lingue degli utenti Vinted.")

description = st.text_area("Inserisci la descrizione del tuo annuncio:")
languages = st.multiselect(
    "Seleziona le lingue per gli hashtag",
    ["Italiano", "Inglese", "Francese", "Spagnolo", "Tedesco", 'Olandese', 'Portoghese', 'Polacco', 'Rumeno', 'Ceco', 'Slovacco', 'Ungherese', 'Greco', 'Sloveno', 'Croato', 'Bulgaro', 'Finlandese', 'Svedese', 'Danese', 'Norvegese'],
    default=["Italiano", "Inglese", "Francese", "Spagnolo", "Tedesco", 'Olandese'])

if st.button("Genera"):
    if description:
        with st.spinner("Generando gli hashtag..."):
            hashtags = generate_hashtags(description, languages)
        st.success("Ecco i tuoi hashtag:")
        st.code(hashtags, language="text")

        st.download_button(
            label="Scarica",
            data=hashtags,
            file_name="hashtags.txt"
        )
    else:
        st.warning("Scrivi prima una descrizione.")


