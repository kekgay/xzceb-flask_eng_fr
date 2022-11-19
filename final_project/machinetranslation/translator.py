import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#import os
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('utcK4-RDfOMGk4UR30LZF8JGLWYCEuuzsVGtNki1eQs1')
language_translator = LanguageTranslatorV3(version = '2018-05-01', authenticator= authenticator)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/18087175-55be-4954-acdd-d8208bacb108')

def english_to_french(english_text):
    """ translate English to French """
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")


def french_to_english(french_text):
    """translate French to English"""
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")