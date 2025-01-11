import streamlit as st
import openai

# OpenAI API-Schlüssel
openai.api_key = "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"

st.title("Einfacher Frage-Antwort-Assistent")

# Eingabe eines Textes
st.header("1. Gebe den Text ein")
input_text = st.text_area("Füge hier den Text ein, auf den sich die Fragen beziehen sollen")

# Eingabe einer Frage
st.header("2. Frage eingeben")
question = st.text_input("Stelle eine Frage zu dem oben eingegebenen Text")

# Verarbeite die Frage
if input_text and question:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein hilfsbereiter Assistent."},
                {"role": "user", "content": f"Text: {input_text}\n\nFrage: {question}"},
            ]
        )
        st.header("Antwort der KI")
        st.write(response['choices'][0]['message']['content'].strip())
    except Exception as e:
        st.error(f"Ein Fehler ist aufgetreten: {e}")
