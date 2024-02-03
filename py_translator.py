import streamlit as st
from py_trans import PyTranslator

# List of languages
def translator_app():
    languages = ['Afrikaans', 'Arabic', 'Armenian', 'Azerbaijani', 'Bangla', 'Basque', 'Bosnian', 
                'Bulgarian', 'Chinese (Simplified)', 'Chinese (Traditional)', 'Czech', 'Danish', 
                'Dutch', 'English', 'Filipino', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 
                'Hawaiian', 'Hebrew', 'Hindi', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Korean', 
                'Krio', 'Latin', 'Malayalam', 'Maltese', 'Marathi', 'Mizo', 'Mongolian', 'Nepali', 
                'Pashto', 'Persian', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Sanskrit', 'Sindhi', 
                'Spanish', 'Swedish', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese']

    # Map full language names to language codes
    language_mapping = {
        'Afrikaans': 'af',
        'Arabic': 'ar',
        'Armenian': 'hy',
        'Azerbaijani': 'az',
        'Bangla': 'bn',
        'Basque': 'eu',
        'Bosnian': 'bs',
        'Bulgarian': 'bg',
        'Chinese (Simplified)': 'zh-CN',
        'Chinese (Traditional)': 'zh-TW',
        'Czech': 'cs',
        'Danish': 'da',
        'Dutch': 'nl',
        'English': 'en',
        'Filipino': 'fil',
        'French': 'fr',
        'Georgian': 'ka',
        'German': 'de',
        'Greek': 'el',
        'Gujarati': 'gu',
        'Hawaiian': 'haw',
        'Hebrew': 'he',
        'Hindi': 'hi',
        'Indonesian': 'id',
        'Irish': 'ga',
        'Italian': 'it',
        'Japanese': 'ja',
        'Korean': 'ko',
        'Krio': 'kri',
        'Latin': 'la',
        'Malayalam': 'ml',
        'Maltese': 'mt',
        'Marathi': 'mr',
        'Mizo': 'lus',
        'Mongolian': 'mn',
        'Nepali': 'ne',
        'Pashto': 'ps',
        'Persian': 'fa',
        'Portuguese': 'pt',
        'Punjabi': 'pa',
        'Romanian': 'ro',
        'Russian': 'ru',
        'Sanskrit': 'sa',
        'Sindhi': 'sd',
        'Spanish': 'es',
        'Swedish': 'sv',
        'Turkish': 'tr',
        'Turkmen': 'tk',
        'Ukrainian': 'uk',
        'Urdu': 'ur',
        'Uzbek': 'uz',
        'Vietnamese': 'vi'
    }

    # Streamlit App
    st.markdown("<h1 style='text-align: center;'>Translator App🚀</h1>", unsafe_allow_html=True)

    # Input text
    source_text = st.text_area("Enter text to translate:")

    # Select language for translation
    target_language = st.selectbox("Select target language:", languages)

    # Button to perform translation
    translate = st.button('Translate', use_container_width=True, type="primary")

    # Perform translation when the button is clicked
    if translate:
        if source_text:
            # Get language code from the mapping
            target_language_code = language_mapping.get(target_language)
            
            if target_language_code:
                # Perform translation
                translator = PyTranslator()
                translation_output = translator.google(source_text, dest=target_language_code)
                
                # Display translated text
                st.write("Translated Text:")
                st.write(translation_output['translation'])
            else:
                st.warning("Language code not found.")
        else:
            st.warning("Please enter text to translate.")


if __name__ == "__main__":
    translator_app()