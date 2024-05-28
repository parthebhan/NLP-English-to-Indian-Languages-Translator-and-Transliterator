import streamlit as st
from googletrans import Translator
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Create a translator object
translator = Translator()

# List of languages with their language codes and transliteration schemes
languages = {
    'Tamil': {'code': 'ta', 'scheme': sanscript.TAMIL},
    'Hindi': {'code': 'hi', 'scheme': sanscript.DEVANAGARI},
    'Bengali': {'code': 'bn', 'scheme': sanscript.BENGALI},
    'Telugu': {'code': 'te', 'scheme': sanscript.TELUGU},
    'Marathi': {'code': 'mr', 'scheme': sanscript.DEVANAGARI},
    'Gujarati': {'code': 'gu', 'scheme': sanscript.GUJARATI},
    'Kannada': {'code': 'kn', 'scheme': sanscript.KANNADA},
    'Malayalam': {'code': 'ml', 'scheme': sanscript.MALAYALAM},
    'Odia': {'code': 'or', 'scheme': sanscript.ORIYA},
    'Punjabi': {'code': 'pa', 'scheme': sanscript.GURMUKHI},
    'Assamese': {'code': 'as', 'scheme': sanscript.BENGALI},
  }

# Set up the Streamlit app
st.title("English to Indian Languages - Translator and Transliterator")
st.write("")
st.write("Done by: Parthebhan Pari")
st.write("")
st.write("Enter your query below and click 'Submit' to get a response:")

# Input text area
text_input = st.text_area("Enter English Text:")

# Dropdown to select target language
language_option = st.selectbox("Select Target Language:", list(languages.keys()))

# Translation and Transliteration buttons
translate_button = st.button("Translate")
transliterate_button = st.button("Transliterate")

if text_input:
    if translate_button:
        try:
            # Perform translation
            target_language = languages[language_option]['code']
            translation = translator.translate(text_input, src='en', dest=target_language)

            # Display translated text
            st.header("Translation:")
            st.write(translation.text)

        except Exception as e:
            st.error(f"Translation Error: {e}")
    elif transliterate_button:
        try:
            # Perform transliteration
            transliteration_scheme = languages[language_option]['scheme']
            transliterated_text = transliterate(text_input, sanscript.ITRANS, transliteration_scheme)

            # Display transliterated text
            st.header("Transliteration:")
            st.write(transliterated_text)

        except Exception as e:
            st.error(f"Transliteration Error: {e}")
    else:
        st.warning("Please click a button to translate or transliterate.")
else:
    st.warning("Please enter some text.")
