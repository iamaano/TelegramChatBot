from telegram import *
from telegram.ext import * 
from requests import *

updater = Updater(token = "5567143331:AAH_j3hhyew5wor4gsW2VmTXYCOF4sNrzDU")

dispatcher = updater.dispatcher

dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_photo("https://www.cimas.co.zw/storage/app/media/CIMAS_CLINICS_001.png")
    update.message.reply_text(
        """
        Hello! Welcome To The Cimas MockUp Bot.
        /Menu -> Go to the menu
        /About -> See more about Cimas
        """
        )
def menu(update, context):
    update.message.reply_text(
        """
        Welcome to the Menu, click or type in the number with desired option
        /1 -> Go to Start
        /2 -> Who we are and what we do
        /3 -> See Cimas Packages
        /4 -> View profile
        /5 -> Order Medication
        /6 -> Book Appointment
        /7 -> View my Lab Results
        /8 -> Talk to our Support Staff
        
        """
        )

def about(update, context):
    
    update.message.reply_text(
        """
        Cimas has been Zimbabwe’s leading medical aid society for over 75 years now, preferred by corporates and families since 1945. As a medical aid that has stood the test of time, all our members are reassured through the trust and security of being looked after by a society that is professional, approachable and above all, a society whose primary care and concern is for its members.   
        https://www.cimas.co.zw/services/all
        Please visit our website: cimas.co.zw
        """)
    update.message.reply_text("https://www.cimas.co.zw/about/overview")

def seepackages(update, context):
     update.message.reply_photo("https://www.cimas.co.zw/storage/app/media/packages/all.jpg?v=2")
     update.message.reply_text(" https://www.cimas.co.zw/packages/all")


def profile(update, context):
    update.message.reply_text("Please provide your membership number")

def ordermedication(update, context):
    update.message.reply_text("Please provide your membership number and Doctor's prescription")

def bookappointment(update, context):
    update.message.reply_text("When would you like to see the doctor?")

def viewlabresults(update, context):
    update.message.reply_text("Please provide your membership number")

def help(update, context):
    update.message.reply_text(
    """
    Please Call or WhatsApp: +263772161829
    Or send an email to: connect@cimas.co.zw
    """
    )


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(CommandHandler('menu', menu))
dispatcher.add_handler(CommandHandler('1', start))
dispatcher.add_handler(CommandHandler('2', about))
dispatcher.add_handler(CommandHandler('3', seepackages))
dispatcher.add_handler(CommandHandler('4', profile))
dispatcher.add_handler(CommandHandler('5', ordermedication))
dispatcher.add_handler(CommandHandler('6', bookappointment))
dispatcher.add_handler(CommandHandler('7', viewlabresults))
dispatcher.add_handler(CommandHandler('8', help))

updater.start_polling()
updater.idle()