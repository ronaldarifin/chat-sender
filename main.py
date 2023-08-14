import pywhatkit
import schedule
import time
import threading
from datetime import datetime

from Messages import Messages
from People import People

currentDate = datetime.now()
people = People()
message = Messages()

def sendMessageWithTag(messageType,tag):
    peopleList = people.getPeopleDataFromTags(tag)
    msg = message.getMessages(messageType,peopleList)
    hour, minutes = currentDate.hour, currentDate.minute + 1
    for i in range(len(peopleList)):
        pywhatkit.sendwhatmsg(peopleList[i].phone,msg[i],hour,minutes)
        minutes += 1









# [
#     Code to run things simultaneously
#     def run_threaded(job_func, args_recieved):
#         job_thread = threading.Thread(target = job_func, args=args_recieved)
#         job_thread.start()
#     run_threaded(sendMessage,["test","Febrian",True])
#     run_threaded(sendMessage,["test","Ronald",True])
#     schedule.every(30).seconds.do(run_threaded,sendMessage,["test","Febrian"])
#     schedule.every(30).seconds.do(run_threaded,sendMessage,["test2","Ronald"])
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
# ]
# def sendMessageToPerson(messageType, personName,isInstant = False):
#     # print("This is message Type: " + messageType)
#     person = people.getPersonData(personName)
#     messagePrompt = howAreYouMsg(person)
#     hour, minutes = currentDate.hour, currentDate.minute + 1
#     if isInstant:
#         pywhatkit.sendwhatmsg_instantly(person.phone,messagePrompt)
#     else:
#         pywhatkit.sendwhatmsg(person.phone, messagePrompt, hour, minutes)