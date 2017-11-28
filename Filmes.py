import telebot 

from telebot import types 

import time

import json

import requests

import urllib



bot = telebot.TeleBot("460186647:AAF1e1bqfTiBoJArULum8AaI2AIOmQY7f6A") 



def obtener(m,namex,cid):

    boolxd = namex[:21] == '/score@imdb_score_bot'

    

    if boolxd == True:

        name = namex[22:]

       

    else:

        name = namex[7:]

        

    url = 'http://www.omdbapi.com/?t=' + name 

    r = requests.get(url)



    json_object = r.json()

    parsed_data = json.dumps(json_object)



    lol = json.loads(parsed_data)



    if lol["Response"]=='True':

            caption = 'Title: ' + (lol["Title"]) + '\n' +  '\n' + 'IMDb:  ' + (lol["imdbRating"]) + '/10   (' + lol["imdbVotes"] + ' votes)'

            bot.send_message(cid,caption)

    else:

        bot.reply_to(m,'Content not found in IMDb!')





 

@bot.message_handler(commands=['score']) 

def command_score(m):  

    cid = m.chat.id

    obtener(m,m.text,cid)

@bot.message_handler(commands=['breakingbad'])
def command_breakingbad(m):
    cid = m.chat.id
    bot.send_message(cid,"Breaking Bad\nScore:9,5\nIMDb: 1.038.783 usuários votaram\nAno de Lançamento: 2008")


@bot.message_handler(commands=['godfather'])
def command_breakingbad(m):
    cid = m.chat.id
    bot.send_message(cid,"The Godfather\nScore:9,2\nIMDb: 1.284.266 usuários votaram\nAno de Lançamento: 1972")


@bot.message_handler(commands=['natalee'])
def command_breakingbad(m):
    cid = m.chat.id
    bot.send_message(cid,"Natalee Holloway\nScore:5,5\nIMDb: 833 usuários votaram\nAno de Lançamento: 2009")
    


 

@bot.message_handler(commands=['start']) 

def command_bisi(m): 

    cid = m.chat.id 

    bot.send_message(cid, "Use o comando /score e o nome do filme/serie para pegar o score. Obs: O nome do filme deverá ser escrito em inglês!")



bot.polling(none_stop=True)

while True: 

    time.sleep(300)
