
# Importing all needed libraries and modules.
import json
import requests
import random

# Predifined phrases.
greetings = ["Hi, how can I help you?"]
farewells = ['Bye', 'Bye-Bye', 'Goodbye', 'Have a good day', 'Stop', 'Hope I could help', 'Bye, don\'t forget to consult the real doc in case of something serious!']
thank_you = ['Thanks', 'Thank you', 'Thanks a bunch', 'Thanks a lot.', 'Thank you very much', 'Thanks so much',
             'Thank you so much']
thank_response = ['You\'re welcome.', 'No problem.', 'No worries.', ' My pleasure.', 'It was the least I could do.',
                  'Glad to help.']
illness_response = ['As far as I\'m concerned, your symptoms match with {}', 'Hmm, you may want to check for {}',
                    'Your symptoms are similar to those of {}. Please consult a doctor for more details.',
                    'From the top of my head, I would say you might have {}.']

# The telegram bot class.
class telegram_bot:
    def __init__(self, pipeline : 'sklearn.pipeline.Pipeline') -> None:
        '''
            The constructor of the telegram bot.
        :param pipeline: 'sklearn.pipeline.Pipeline'
            The sklearn Pipeline implemented for classifying messages.
        :param db: 'shelve.DbfilenameShelf'
            The data storing object from shelve.
        '''
        # Setting up the token and the url for the bot.
        self.token = '1846959466:AAGy6Y7GL1b7E0IuCF0HtEB4j0MVmr4nAtM'
        self.url = f"https://api.telegram.org/bot{self.token}"

        # Setting up the pipeline and the pseudo data base.
        self.pipeline = pipeline

        self.illness = ['(vertigo) Paroymsal  Positional Vertigo', 'AIDS', 'Acne',
                        'Alcoholic hepatitis', 'Allergy', 'Arthritis', 'Bronchial Asthma',
                        'Cervical spondylosis', 'Chicken pox', 'Chronic cholestasis',
                        'Common Cold', 'Dengue', 'Diabetes',
                        'Dimorphic hemmorhoids(piles)', 'Drug Reaction',
                        'Fungal infection', 'GERD', 'Gastroenteritis', 'Heart attack',
                        'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
                        'Hypertension', 'Hyperthyroidism', 'Hypoglycemia',
                        'Hypothyroidism', 'Impetigo', 'Jaundice', 'Malaria', 'Migraine',
                        'Osteoarthristis', 'Paralysis (brain hemorrhage)',
                        'Peptic ulcer diseae', 'Pneumonia', 'Psoriasis', 'Tuberculosis',
                        'Typhoid', 'Urinary tract infection', 'Varicose veins', 'hepatitis A', 'normal']

        self.directions = {'(vertigo) Paroymsal  Positional Vertigo':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                           'AIDS':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                           'Acne':'http://www.docdoc.md/ro/clinics/sancos-clinica',
                            'Alcoholic hepatitis':'http://www.docdoc.md/ro/clinics/centrul-medical-american-sectorul-centru',
                           'Allergy':'http://www.docdoc.md/ro/clinics/sancos-clinica',
                            "Arthritis" : 'http://www.docdoc.md/ro/clinics/clinica-adler-medical',
                           'Bronchial Asthma':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                            'Cervical spondylosis':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                            'Chicken pox':'http://www.docdoc.md/ro/clinics/sancos-clinica',
                            'Chronic cholestasis':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                            'Common Cold':'http://www.docdoc.md/ro/clinics/centrul-medical-american-sectorul-centru',
                            'Dengue':'http://www.docdoc.md/ro/clinics/centrul-medical-american-sectorul-centru',
                            'Diabetes':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                            'Dimorphic hemmorhoids(piles)':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Drug Reaction':'http://www.docdoc.md/ro/clinics/sancos-clinica',
                        'Fungal infection':'http://www.docdoc.md/ro/clinics/sancos-clinica',
                        'GERD':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Gastroenteritis':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Heart attack':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Hepatitis B':'http://www.docdoc.md/ro/clinics/centrul-medical-diagnostic-consultativ-biomed-diagnostic',
                        'Hepatitis C':'http://www.docdoc.md/ro/clinics/centrul-medical-diagnostic-consultativ-biomed-diagnostic',
                        'Hepatitis D':'http://www.docdoc.md/ro/clinics/centrul-medical-diagnostic-consultativ-biomed-diagnostic',
                        'Hepatitis E':'http://www.docdoc.md/ro/clinics/centrul-medical-diagnostic-consultativ-biomed-diagnostic',
                        'Hypertension':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Hyperthyroidism':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Hypoglycemia':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Hypothyroidism':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Impetigo':'http://www.docdoc.md/ro/clinics/sancos-clinica',
                        'Jaundice':'http://www.docdoc.md/ro/clinics/centrul-medical-diagnostic-consultativ-biomed-diagnostic',
                        'Malaria':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Migraine':'http://www.docdoc.md/ro/clinics/clinica-adler-medical',
                        'Osteoarthristis':'http://www.docdoc.md/ro/clinics/clinica-adler-medical',
                        'Paralysis (brain hemorrhage)':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Peptic ulcer diseae' : 'ADLER MEDICAL Centru Medical',
                        'Pneumonia':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Psoriasis':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Tuberculosis':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Typhoid':'http://www.docdoc.md/ro/clinics/centru-medical-sonomed',
                        'Urinary tract infection':'http://www.docdoc.md/ro/clinics/citobiomed',
                        'Varicose veins':'http://www.docdoc.md/ro/clinics/sancos-clinica',
                        'hepatitis A':'http://www.docdoc.md/ro/clinics/centrul-medical-diagnostic-consultativ-biomed-diagnostic'}

    def choose_reply(self, user_msg : str, chat_id : int, user_id : int, name : str) -> None:
        '''
            This function chooses what function to send.
        :param user_msg: str
            The user message extracted from the request.
        :param chat_id: int
            The id of the chat.
        :param user_id: int
            The id of user.
        :param name: str
            The name of the user that send this message.
        '''
        # Checking if message is not a farewell.
        if user_msg not in farewells:

            # If message is a /start command we will sent greeting message.
            if user_msg == '/start':
                bot_resp = f"""Hi! {name}. I am Dr. A.I. Bolit. \nI'll try to help you get answers. Tell me your symptoms. \nAnd remember to consult a real doctor in case of a serious illness. \nType Bye to Exit."""
                self.send_message(bot_resp, chat_id)
            # If message is a thank you form we wil send to the user a thank you response.
            elif user_msg in thank_you:
                bot_response = random.choice(thank_response)
                self.send_message(bot_response, chat_id)
            # If message is a greeting we will send the user a random greeting back.
            elif user_msg in greetings:
                bot_response = random.choice(greetings)
                self.send_message(bot_response, chat_id)
            # If the text message is nothing above we will verify if it isn't prostitute offer using the pipeline.
            else:
                # Verifying the message.
                diagnose = self.verify_msg(user_msg, chat_id, user_id, name)

                if diagnose in self.illness:
                    self.send_message(random.choice(illness_response).format(diagnose), chat_id=chat_id)
                    self.send_message('Go check this clinic, I\'m sure they can help you:\n{}'.format(self.directions[diagnose]), chat_id)
                else:
                    self.send_message('Everything looks normal to me', chat_id)
        else:
            # If message si a farewell then we will send bye to the user.
            bot_response = random.choice(farewells)
            self.send_message(bot_response, chat_id)

    def verify_msg(self, user_msg, chat_id, user_id, name):
        '''
            This function chooses finds out using the model.
        :param user_msg: str
            The user message extracted from the request.
        :param chat_id: int
            The id of the chat.
        :param user_id: int
            The id of user.
        :param name: str
            The name of the user that send this message.
        '''
        # Getting the prediction from the pipeline.
        prediction = self.pipeline.predict([user_msg])

        return prediction[0]

    def get_updates(self, offset : int =None) -> dict:
        '''
            THis function is getting the last messages in the chat
        :param offset: int
            The offset for requesting the data.
        :return: dict
            The last messages data.
        '''
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset + 1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def send_message(self, msg : str, chat_id : int) -> None:
        '''
            This function allows the chatbot to send messages in the chat.
        :param msg: str
            The user message extracted from the request.
        :param chat_id: int
            The id of the chat.
        '''
        url = self.url + f'/sendMessage?chat_id={chat_id}&text={msg}'
        if msg is not None:
            requests.get(url)
