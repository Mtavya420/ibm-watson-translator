import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('url')

def englishToFrench(english_text):
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
    