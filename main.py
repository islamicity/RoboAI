import Constants as keys
import Responses as R
from telegram.ext import *

import time
import random

print("Robo AI just started...")

def intro_command(update, context):

    update.message.reply_text("Halo kak, salam kenal aku Robo AI!")

    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo="https://www.onfore.com/wp-content/uploads/2017/05/Cute-Robot.jpg")

    time.sleep(3)

    update.message.reply_text("Aku bisa membantu apa saja untuk kakak di group ini melalui /AskRoboAI yah. Atau sst, mau DM Robo AI juga boleh di @RoboAIBot...")

def what_command(update, context):

    update.message.reply_text("""
                                Robo AI kasih saran ke kakak untuk cek informasi berikut untuk kenal lebih jauh dengan Indonesia AI: 
                                \n1. bit.ly/TentangIndonesiaAI \n2. bit.ly/TentangAIMentorship \n3. bit.ly/TentangMentorMuda \n\n/AskRoboAI
                              """)

def quote_command(update, context):

    list_of_quotes = ["\"If we can make computers more intelligent - and I want to be careful of AI hype - and understand the world and the environment better, it can make life so much better for many of us.\"\n\n- Prof. Andrew Ng. (Co-Founder and Head of Google Brain)", 
                      "\"We're making this analogy that AI is the new electricity. Electricity transformed industries: agriculture, transportation, communication, manufacturing.\"\n\n- Prof. Andrew Ng. (Co-Founder and Head of Google Brain)", 
                      "\"It is difficult to think of a major industry that AI will not transform. This includes healthcare, education, transportation, retail, communications, and agriculture.\"\n\n- Prof. Andrew Ng. (Co-Founder and Head of Google Brain)", 

                      "\"AI is made by humans, intended to behave by humans, and, ultimately, to impact humans' lives and human society.\"\n\n- Prof. Fei-Fei Lie (AI Professor at Stanford)",
                      "\"The tools and technologies we've developed are really the first few drops of water in the vast ocean of what AI can do.\"\n\n- Prof. Fei-Fei Lie (AI Professor at Stanford)",
                      "\"As a technologist, I see how AI and the fourth industrial revolution will impact every aspect of people's lives.\"\n\n- Prof. Fei-Fei Lie (AI Professor at Stanford)", 
                      
                      "\"I have always been convinced that the only way to get artificial intelligence to work is to do the computation in a way similar to the human brain. That is the goal I have been pursuing. We are making progress, though we still have lots to learn about how the brain actually works.\"\n\n- Prof. Geoffrey Hinton (The godfather of Deep Learning)",
                      "\"Deep learning is already working in Google search and in image search; it allows you to image-search a term like 'hug'.\"\n\n- Prof. Geoffrey Hinton (The godfather of Deep Learning)",
                      "\"Take any old classification problem where you have a lot of data, and it's going to be solved by deep learning. There's going to be thousands of applications of deep learning.\"\n\n- Prof. Geoffrey Hinton (The godfather of Deep Learning)",

                      "\"Our intelligence is what makes us human, and AI is an extension of that quality.\"\n\n- Prof. Yann LeCun (VP & Chief AI Scientist at Facebook Inc.)"]

    chosen_quote = list_of_quotes[random.randint(0, len(list_of_quotes)-1)]

    update.message.reply_text(chosen_quote)
    # update.message.reply_text("%s\n\n/quote /AskRoboAI" % chosen_quote)
    # update.message.reply_text(f"{chosen_quote}\n\n/quote /AskRoboAI")

def chat_command(update, context):

    update.message.reply_text("Fitur ini masih dalam pengembangan dengan bantuan teknologi Text Processing & NLP stack (Word2Vec, GloVe, GPT2). Yuk bantu Robo AI bisa makin pintar kak...")

def help_command(update, context):

    update.message.reply_text("""
                                Robo AI selalu hadir untuk membantu kakak dimanapun berada. Nah, kakak bisa coba pilih beberapa menu berikut yang sesuai dengan kebutuhan kakak nih: 
                                \n1. /intro - kenalan dengan Robo AI \n2. /what - apa itu Indonesia AI \n3. /quote - kutipan terbaik tentang AI \n4. /chat - ngobrol dengan Robo AI \n5. /AskRoboAI - perintah untuk membantu
                              """)

def handle_message(update, context):

    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):

     print(f"Maaf kak, ada kesalahan {context.error} terjadi karena {update}. :(")

def main():

    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('intro', intro_command))
    dp.add_handler(CommandHandler('what', what_command))
    dp.add_handler(CommandHandler('quote', quote_command))
    dp.add_handler(CommandHandler('chat', chat_command))
    dp.add_handler(CommandHandler('AskRoboAI', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()