# translator
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishtext):
    translation = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()
   # print(json.dumps(translation, indent=2, ensure_ascii=False))
    translation= translation['translations'][0]['translation']
    return translation


def frenchToEnglish(frenchtext):
    translation = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
  #  print(json.dumps(translation, indent=2, ensure_ascii=False))
    translation= translation['translations'][0]['translation']
    return translation
