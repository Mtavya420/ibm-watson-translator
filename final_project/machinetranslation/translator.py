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

def english_to_french(english_text):
    """
    This function takes english text and translate it to french
    """
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def french_to_english(french_text):
    """
    This function takes french_text and translate it to english
    """
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation['translations'][0]['translation']


if __name__ == "__main__":
    res = english_to_french("Hi, My name is Dullah. I am software engineer at Google")
    print(res)