# Symptochatic
A telegram bot to predict illness by given symptoms.
The dataset for predicting ilness can be found at:
https://www.kaggle.com/itachi9604/disease-symptom-description-dataset?select=dataset.csv
The repository has the following structure:
> bot.py - the main file with the logic;
> mwet.pkl - stores the word tokenizer program, in binary form;
> pipeline.pkl - stores the entire pipeline structure of the project functions;
> telebot.py - contains the chatbot class definition.
> 
The user shall open the chat on telegram and tell the bot about the symptoms they experience. 
The chatbot will subsequently suggest a diagnose and recommend a clinic in Moldova which has the
department that addresses the specified condition.

Note: this chatbot is not a replacement for a face-to-face consultation with the doctors. Therefore,
a visit to the hospital is highly recommended afterwards.
