import pyttsx3
#import speech_recognition as sr
import webbrowser  
import datetime
from datetime import datetime as dt
from datetime import timedelta as td
#import wikipedia 
import os
import time
import pygame as pg
import requests,json
import serpapi
#import PySimpleGUI as psg
from pyjokes import get_joke
from bs4 import BeautifulSoup
from subprocess import call
import socket
import platform
import psutil
import subprocess
import tkinter as tk                  
from tkinter import ttk     
from PIL import ImageTk,Image
from PIL import *
import PIL.Image
from tkinter import *         
from tkinter import messagebox   
import ttkbootstrap as tb       
import sqlite3 as sql    
from ttkthemes import ThemedStyle 
#import GPUtil
#from tabulate import tabulate
#import openai
#from langchain.llms import OpenAI
import smtplib 
import turtle
#import aspose-words as aw
#doc = aw.Document("Input.docx")
#doc.save("Output.pdf")
#import requests_with_caching
from googlesearch import search
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle
import tzlocal  # $ pip install tzlocal

# display "human-readable" name (tzid)

#nPwoNHGZCqsNkk9G3eCOM5GGTZo69AIG

list_main=["PRESS CTRL+ENTER FOR MULTILINE INPUT","TYPE /// FOR COMMANDS OR GO TO HELP SECTION",""]

list_help=["Command list:","","","—"*140,
        "| keyword                          |  function".upper(),"—"*130,
        "| time                             |  tells the current time","|",
        "| day                              |  tell the current day","|",
        "| weather + <cityname>             |  tells the current weather of a city  [ CITY NAME ALWAYS LAST ]","|",
        "|     + forecast                   |  gives weather forecast of a city of that day (min/max temp and rain probability)","|",
        "|           + detail               |  additionally includes sunset time, sunrise time, moonphase, Air quality and uv index ","|",   
        "|     + daily forecast             |  gives weather forecast of a city for 5 days (min/max temp and rain probability)","|",
        "|           + detail               |  additionally includes sunset time, sunrise time, moonphase, Air quality and uv index ","|",   
        "| todo/tasks                       |  opens to-do list application","|",
        "| email/mail                       |  starts a mail correspondance","|",
        "| music                            |  opens music command series [for more info look at MUSIC section below]","|",
        "| open <website-name>              |  opens the website on default browser","|",
        "| search google <question>         |  searchs answer for question on google","|",
        "| bye                              |  exits application",
        "—"*140,"","","","","","","",
        "misc features:".upper(),
        " >>> pointer automatically goes to entry box on startup and immediately after swithing tabs",
        " >>> program runs on startup of laptop",
        ""
        ]

pg.init()

pwd='jnel wpcu jlxn zpny '

WORK_TIME = 50 * 60
SHORT_BREAK_TIME = int(5 * 60)
LONG_BREAK_TIME = int(25* 60)
POMO_FLAG=False

SCOPES = ['https://www.googleapis.com/auth/calendar']

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.root.title("Pomodoro Timer")

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 60))
        self.timer_label.place(x=135,y=15)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.place(x=130,y=135)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer,state=tk.DISABLED)
        self.stop_button.place(x=300,y=135)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()
    
    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Great job!" if self.pomodoros_completed % 4 == 0
                                        else "Good job!", "Take a long break and rest your mind."
                                        if self.pomodoros_completed % 4 == 0
                                        else "Take a short break and strech your legs!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Work TIie", "Get back to work!")        
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)

def calender(query):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no creds let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save creds for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    tz=tzlocal.get_localzone_name()
    while True:
        global created_calendar,new_calendar,created_event,updated_event,event
        if "-1" in query.split(" "):
            list_main.append("")
            list_main.append("Fetching all calendars:")
            #print("\nFetching all calendars:")
            calendar_list = service.calendarList().list().execute().get('items', [])
            for calendar in calendar_list:
                list_main.append(calendar['summary'])
                #print(calendar['summary'])
            list_main.append("")
            #print()
            break
        elif "-2" in query.split(" "):
        # Feature 2: Create a new calendar
            namec=query.split(" ")[-1]
            new_calendar = {
                'summary': namec,
                'timeZone': tz,
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 1 * 60},
                    ],
                },
            }
            created_calendar = service.calendars().insert(body=new_calendar).execute()
            list_main.append("")
            list_main.append(f"Created calendar: {created_calendar['id']} -> {created_calendar['summary']}")
            #print(f"Created calendar: {created_calendar['id']} -> {created_calendar['summary']}")
            list_main.append("")
            break
        elif "-3" in query.split(" "):
            try:
                abab=query.split(" -3 ")[-1].split(" ")
                namc=abab[0]
                cal="primary"
                if namc!=None:
                    cal=namc
                    for i in service.calendarList().list().execute().get('items', []):
                        if i["summary"]==cal:
                            cal=i["id"]
                            break
                namee=abab[1]
                event={
                    'summary': namee,
                }
                tlen=int(abab[2])
                rec=abab[3]
                if rec=="y":
                    freq=["WEEKLY","DAILY"]
                    interval=["1","2"]
                    until="20271231"
                    if abab[4]=="WEEKLY":
                        startday=abab[6]
                        event["recurrence"]=[f'RRULE:FREQ={abab[4]};BYDAY={startday};INTERVAL={abab[5]};UNTIL={until}']
                a,b,c,d,e=[int(i) for i in abab[-1].split("-")]
                enddatetime='-'.join([str(a),str(b),str(c)])+f'T{str(d+tlen)}:{str(e)}:00+05:30'
                startdatetime='-'.join([str(a),str(b),str(c)])+f'T{str(d)}:{str(e)}:00+05:30'
            except:
                list_main.append("Invalid syntax for calender command")
            
            
            print(startdatetime,enddatetime,tz)
            event['start']={
            'dateTime': startdatetime,
            'timeZone': tz,
            }
            event['end']={
            'dateTime': enddatetime,
            'timeZone': tz,
            }
            created_event = service.events().insert(calendarId=cal, body=event).execute()
            list_main.append("")
            list_main.append(f"Created event: {created_event['id']} -> {created_event['summary']}")
            print(f"Created event: {created_event['id']}")
            list_main.append("")
            break
        elif "-4" in query.split(" "):
            # Feature 4: Update an event
            global updated_event
            updated_event = created_event
            updated_event['description'] = 'Updated text'
            updated_event = service.events().update(calendarId=created_calendar['id'], eventId=created_event['id'], body=updated_event).execute()
            list_main.append("")
            list_main.append(f"Updated event: {updated_event['id']}")
            print(f"Updated event: {updated_event['id']}")
            list_main.append("")
            break
        elif "-5" in query.split(" "):
            # Feature 5: Delete an event
            service.events().delete(calendarId=created_calendar['id'], eventId=updated_event['id']).execute()
            list_main.append("")
            list_main.append(f"Deleted event: {updated_event['id']}")
            print(f"Deleted event: {updated_event['id']}")
            list_main.append("")
            break
        elif "-6" in query.split(" "):
            list_main.append("")
            ran="all"
            xx=query.split(" ")[-1]
            #print(xx)
            if xx!=None:
                for i in service.calendarList().list().execute().get('items', []):
                    if i["summary"]==xx:
                        xx=i["id"]
                        ran=None
                        break
            #print(xx,ran)
            now = datetime.datetime.now().isoformat().split(".")[0] + '.000Z' # 'Z' indicates UTC time
            eventsx=[]
            if ran=="all":
                for i in service.calendarList().list().execute().get('items', []):
                    ttt=service.events().list(calendarId=i["id"], timeMin=now,maxResults=15, singleEvents=True,orderBy='startTime').execute()
                    for t in ttt.get('items', []):
                        eventsx.append([t["start"]["dateTime"],t["summary"]])
                eventsx= sorted(eventsx, key=lambda x: x[0])
            else:
                ttt=service.events().list(calendarId=xx, timeMin=now,maxResults=15, singleEvents=True,orderBy='startTime').execute()
                for t in ttt.get('items', []):
                    eventsx.append([t["start"]["dateTime"],t["summary"]])
            if not eventsx:
                list_main.append("No upcoming events found.")
                print('No upcoming events found.')
            else:
                try:
                    for i in range(15):
                        list_main.append(eventsx[i][0]+"\t"+eventsx[i][1])
                        #print(eventsx[i][0],eventsx[i][1])
                except:
                    pass
            list_main.append("")
            break
        else:
            list_main.append("")
            list_main.append("Invalid flag")
            list_main.append("")
            print("invalid")
            break
    update_main()

def games(query):
    player_a_score=0
    player_b_score=0
    
    window=turtle.Screen()
    window.title("The Pong Game")
    window.bgcolor("lightblue")
    window.setup(width=800,height=600)
    window.tracer(0)
    
    leftpaddle=turtle.Turtle()
    leftpaddle.speed(0)
    leftpaddle.shape("square")
    leftpaddle.color("white")
    leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
    leftpaddle.penup()
    leftpaddle.goto(-350,0)
    
    rightpaddle=turtle.Turtle()
    rightpaddle.speed(0)
    rightpaddle.shape("square")
    rightpaddle.color("white")
    rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
    rightpaddle.penup()
    rightpaddle.goto(350,0)

    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(5,5)
    ballxdirection=0.2
    ballydirection=0.2
    
    #Code for creating pen for scorecard update
    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("Blue")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("score",align="center",font=('Arial',24,'normal'))
    
    def leftpaddleup():
        y=leftpaddle.ycor()
        y=y+90
        leftpaddle.sety(y)
    def leftpaddledown():
        y=leftpaddle.ycor()
        y=y-90
        leftpaddle.sety(y)
    
    def rightpaddleup():
        y=rightpaddle.ycor()
        y=y+90
        rightpaddle.sety(y)
    def rightpaddledown():
        y=rightpaddle.ycor()
        y=y-90
        rightpaddle.sety(y)
    
    window.listen()
    window.onkeypress(leftpaddleup,'w')
    window.onkeypress(leftpaddledown,'s')
    window.onkeypress(rightpaddleup,'Up')
    window.onkeypress(rightpaddledown,'Down')
    
    while True:
        window.update()
        #moving the ball
        ball.setx(ball.xcor()+ballxdirection)
        ball.sety(ball.ycor()+ballydirection)
    
        #border set up
        if ball.ycor()>290:
            ball.sety(290)
            ballydirection=ballydirection*-1
        if ball.ycor()<-290:
            ball.sety(-290)
            ballydirection=ballydirection*-1
            
        if ball.xcor() > 390:
            ball.goto(0,0)
            ballxdirection = ballxdirection * -1
            player_a_score = player_a_score + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
            #os.system("afplay wallhit.wav&")
    
    
    
        if(ball.xcor()) < -390: # Left width paddle Border
            ball.goto(0,0)
            ballxdirection = ballxdirection * -1
            player_b_score = player_b_score + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
            #os.system("afplay wallhit.wav&")
    
        # Handling the collisions with paddles.
    
        if(ball.xcor() > 340) and (ball.xcor() < 360) and (ball.ycor() < rightpaddle.ycor() + 45 and ball.ycor() > rightpaddle.ycor() - 45):
            ball.setx(340)
            ballxdirection= ballxdirection * -1
    
        if(ball.xcor() < -340) and (ball.xcor() > -360) and (ball.ycor() < leftpaddle.ycor() + 45 and ball.ycor() > leftpaddle.ycor() - 45):
            ball.setx(-340)
            ballxdirection= ballxdirection * -1

'''def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again please")
            return "None"
        return Query'''

def speak(audio):
    engine = pyttsx3.init("espeak")
    voices = engine.getProperty('voices')
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-25)
    #engine.say('Sally sells seashells by the seashore.')
    #engine.say('The quick brown fox jumped over the lazy dog.') 
    engine.setProperty('voice', 'english_rp+f3')
    engine.say(audio)  
    engine.runAndWait()

    '''engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        #engine.setProperty('voice', voice.id)  # changes the voice
        #engine.say('The quick brown fox jumped over the lazy dog.')
        print(voice)
        #engine.runAndWait()'''

def tellDay():
    day = dt.today().weekday() + 1
    Day_dict = {1: 'Monday', 
                2: 'Tuesday', 
                3: 'Wednesday', 
                4: 'Thursday', 
                5: 'Friday', 
                6: 'Saturday',
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        list_main.append(day_of_the_week)
        update_main()
        speak("The day is " + day_of_the_week)

def tellDate(x,y):
    #today=str(dt.today().strftime('%d'))+str(dt.today().strftime('%b'))+str(dt.today().strftime('%Y'))
    date=dt.today()
    #print(date)
    #09-07-2024
    #09Jul2024
    #print(str(datetime.today().strftime('%d'))+str(datetime.today().strftime('%b'))+str(datetime.today().strftime('%Y')))
    day=int(dt.today().strftime('%d').lstrip("0"))
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    if y==0:
        list_main.append(str(dt.today().strftime('%d')).lstrip("0")+suffix+" "+str(dt.today().strftime('%B'))+" "+str(dt.today().strftime('%Y')))
    update_main()
    #speak(str(dt.today().strftime('%d')).lstrip("0")+suffix+" "+str(dt.today().strftime('%B'))+" "+str(dt.today().strftime('%Y')))
    #print((date+td(days=x)).strftime('%d-%m-%Y'))
    #print(str(dt.today().strftime('%d')).lstrip("0")+suffix+" "+str(dt.today().strftime('%B'))+" "+str(dt.today().strftime('%Y'))+td(days=x))
    return str((date+td(days=x)).strftime('%d')).lstrip("0")+suffix+" "+str((date+td(days=x)).strftime('%B'))+" "+str((date+td(days=x)).strftime('%Y'))
    #return .strftime('%d-%m-%Y')

def tellTime():
    time = str(dt.now())
    #print(time)
    hour = time[11:13]
    min = time[14:16]
    #print(hour,min)
    end=""
    if 12<=int(hour)<24:
        end=" P M"
    else:
        end=" A M"
    list_main.append("The time is " + hour + " : " + min+end)  
    update_main()
    
    
    if int(hour)>12:
        speak("The time is " + str(int(hour)-12) + " " + min.lstrip("0")+end)  
    else:
        speak("The time is " + str(int(hour)) + " " + min.lstrip("0")+end)

def Hello():
    global list_main
    speak("Hello, I am your desktop assistant.\nHow may I help you")
    list_main.append("Hello, I am your desktop assistant.How may I help you")

def setalarm():
    pass

def notemake():
    pass

def sgoogle(x):
    ak="bbbdd0bbba50f684aa7dd744ab6ce4c68344d52767cb1013e1ff1db97af289fb"
    p={
        "engine":"google",
        "q":x.replace("search","")
            }
    s=serpapi.Client(api_key=ak)
    res=s.search(q=x.replace("search",""),engine="google",hl="en",gl="us",num=10)
    #print(res[""])
    list_main.append(res["answer_box"]["answer"])
    update_main()
    speak(res["answer_box"]["answer"])
    # type calculator_result -> result
    # type weather_result -> temperature unit precipitation humidity wind location date weather forecast-> day weather temp. -> high low
    # type finance_result -> title enxhange stock currency price price_movement-> price percentage movement date

def todo():
    root=tk.Tk()
    root.geometry('800x600')
    root.config(bg='lavender')
    global todolist
    todolist=["finish todo list","take a walk"]
    global xy
    xy=Entry(root,width = 30,background = "#FFF8DC",foreground = "#A52A2A")
    xy.focus_set()
    xy.place(x=25,y=75)
    #print(xy.get())
    B1=Button(root,width=30,height=2,background='lightblue',text="add task",command=lambda:b1())
    B1.place(x=25,y=150)
    B2=Button(root,width=30,height=2,background='lightblue',text="remove task",command=lambda:b2())
    B2.place(x=25,y=225)
    B3=Button(root,width=30,height=2,background='lightblue',text="remove all task",command=lambda:b3())
    B3.place(x=25,y=300)
    b4=Button(root,width=30,height=2,background='lightblue',text="exit",command=root.destroy)
    b4.place(x=25,y=375)
    global a
    a=Listbox(root,width=55,height=30,background='#fff1dc')
    a.place(x=325,y=25) 
    a.insert('end', " ")
    upl()
    root.mainloop()

def upl():
    a.delete(0,a.size())
    for task in todolist:
        a.insert('end', "  ➤ "+task)

def b1():
    x=xy.get()
    todolist.append(x)
    upl()

def b2():
    x=a.get(a.curselection()).replace("  ➤ ","")
    if x in todolist:
        todolist.remove(x)
        upl()
    else:
        print("unable to remove")

def b3():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True: 
        todolist.clear()
        upl()
    else:
        pass

def joke():
    
    x=get_joke(language="en",category="all")
    list_main.append(x)
    update_main()
    speak(x)

def news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url) 
    h=[]
    soup = BeautifulSoup(response.text, 'html.parser') 
    headlines = soup.find('body').find_all('h2') 
    #unwanted = ['BBC World News TV', 'BBC World Service Radio', 'News daily newsletter', 'Mobile app', 'Get in touch'] 
    for i in range(5):
        list_main.append(headlines[i].text)
        update_main()
        speak(headlines[i].text)

    
    # trending / all(tv/person)
    #get/trending/movie/day
    #get movie/movieid
    #get movie/movieid/recommendations - params key language en-US page 1
    
def recs(x):
    if "movie" in x:
        t="movie"
    if "tv" in x:
        t="tv"
    if "trending" in x or "top rated" in x:
        if "day" in x:
            time="day"
        if "week" in x:
            time="week"
        if "trending" in x:
            type="trending"
            url="https://api.themoviedb.org/3/"+type+"/"+t+"/"+time+"?language=en-US&api_key=0cb3908e51cc8ecae008170b7b2a32d6&p=1"
        if "top rated" in x:
            type="top-rated"
            url="https://api.themoviedb.org/3/discover/"+t+"?include_adult=false&language=en-US&page=1&sort_by=vote_average.desc&vote_count.gte=200&api_key=0cb3908e51cc8ecae008170b7b2a32d6"
            #print(url)
    if "similiar" in x:
        y=x.split(" similiar to ")[-1]
        url0="https://api.themoviedb.org/3/search/"+t+"?query="+y+"&language=en-US&api_key=0cb3908e51cc8ecae008170b7b2a32d6&p=1"
        try:
            r0=requests.get(url0)
        except ConnectionError and ConnectionAbortedError and ConnectionResetError and ConnectionRefusedError:
            print("connection error try again later")
            return
        id=str(r0.json()["results"][0]["id"])
        url="https://api.themoviedb.org/3/"+t+"/"+id+"/recommendations?language=en-US&api_key=0cb3908e51cc8ecae008170b7b2a32d6&p=1"

    head={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2IzOTA4ZTUxY2M4ZWNhZTAwODE3MGI3YjJhMzJkNiIsIm5iZiI6MTcxOTMwNjM2Mi43MDA1NTIsInN1YiI6IjY2N2E4N2FiMDk0MWQxNTIxNDE1OTUwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._8yoDF-OqMRQzuPzxiV3Odqug5tckWfek4UmstY6gwg',
        'accept': 'application/json'}
    try:
        r=requests.get(url,headers=head)
    except ConnectionError and ConnectionAbortedError and ConnectionResetError and ConnectionRefusedError:
        list_main.append("connection error try again later")
        update_main()
        return
    #url="https://tastedive.com/api/similiar?apikey=1029871-personal-DA648730&limit=3&q="+y
    #url="http://www.omdbapi.com/?i=tt3896198&apikey=70849d77&plot=short&r=json&type="+t+"&t="+y
    #dp={'q':y,'type':t,'limit':3,'apikey':'1029871-personal-DA648730'}
    #r=requests_with_caching.get(url,dp)
    #apitmbd="0cb3908e51cc8ecae008170b7b2a32d6"
    #print(r)
    genre_dict_m={
        28:"Action",
        12:"Adventure",
        16:"Animation",
        35:"Comedy",
        80:"Crime",
        99:"Documentary",
        18:"Drama",
        10751:"Family",
        14:"Fantasy",
        36:"History",
        27:"Horror",
        10402:"Music",
        9648:"Mystery",
        10749:"Romance",
        878:"Science Fiction",
        10770:"TV Movie",
        53:"Thriller",
        10752:"War",
        37:"Western"
    }
    genre_dict_t={
        10759:"Action and Adventure",
        16:"Animation",
        35:"Comedy",
        80:"Crime",
        99:"Documentary",
        18:"Drama",
        10751:"Family",
        10762:"Kids",
        9648:"Mystery",
        10763:"News",
        10764:"Reality",
        10765:"SciFi and Fantasy",
        10766:"Soap",
        10767:"Talk",
        10768:"War and Politics",
        37:"Western"
    }
    try:
        #w=r.json()
        w=r.json()
        if t=="movie":
            xy="title"
        elif t=="tv":
            xy="name"
        for i in range(5):
            ttl=w["results"][i][xy]
            ovw=w["results"][i]["overview"]
            gid=w["results"][i]["genre_ids"]
            abc1="Title: "+ttl
            abc2="Summary: "+ovw
            abc3="Genres: "
            for i in gid:
                if t=="movie":
                    abc3+=genre_dict_m[i]+", "
                if t=="tv":
                    abc3+=genre_dict_t[i]+", "
            list_main.append(abc1)
            list_main.append(abc2)
            list_main.append(abc3)
            list_main.append("")
            update_main()
            speak(ttl)
            #print("Title: "+w["results"][i]["original_title"]+"\ngenres: "+w["results"][i]["genre_ids"]+"\nSummary: "+w["results"][i]["overview"])
    except: 
        print(r.json())
        list_main.append("ERROR")
        return
    
def mail():
    global pwd
    #list_main.append("What is the subject?")
    speak("What is the subject?")
    sub=input("sub: ")
    #time.sleep(3)
    #sub=inp.get("1.0",'end-1c')
    #list_main.append("---->"+sub)
    #inp.delete("1.0",END)
    #update_main()
    #list_main.append("what is the context?")
    speak("what is the context?")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    #cline=inp.get("1.0",END)
    #list_main.append("---->"+cline)
    #update_main()
    #inp.delete("1.0",END)
    cline=''
    for i in contents:
        cline+=i
        cline+='\n'
    #list_main.append("who is the recipient? ignore if default")
    #update_main()
    speak("who is the recipient? ignore if default")
    recp=input("To: ")
    if recp=="":
        recp='monishasharma134@gmail.com'
    name="Monisha Sharma"
    m=f'Subject: {sub}\n\nHello,\n\n{cline}\n\nKind Regards\n{name}'
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('nightowlsibling333@gmail.com',pwd)
    mail.sendmail('nightowlsibling333@gmail.com',recp,m)
    mail.close()
    #list_main.append("Email sent succesfully!")
    #update_main()
    speak("email sent")

def music():
    while(True):
        xyz=input("music command: ")
        if "play" in xyz:
            y=xyz.split(" ").index("play")
            x="/home/monisha/Music/"+xyz.split(" ")[y+1]+".mp3"
            sound=pg.mixer.Sound(x).play()
        elif xyz=="stop":
            sound.stop()
            continue
        elif xyz=="exit":
            sound.stop()
            break

def sysinf():
    my_system = platform.uname()
    list_main.append(f"System: {my_system.system}")
    list_main.append(f"Node Name: {my_system.node}")
    list_main.append(f"Release: {my_system.release}")
    list_main.append(f"Version: {my_system.version}")
    list_main.append(f"Machine: {my_system.machine}")
    list_main.append(f"Processor: {my_system.processor}")
    list_main.append(f"Memory :{psutil.virtual_memory()}")

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def compsi():
    list_main.append("="*40+"System Information"+"="*40)
    uname = platform.uname()
    list_main.append(f"System: {uname.system}")
    list_main.append(f"Node Name: {uname.node}")
    list_main.append(f"Release: {uname.release}")
    list_main.append(f"Version: {uname.version}")
    list_main.append(f"Machine: {uname.machine}")
    list_main.append(f"Processor: {uname.processor}")
    list_main.append("="*40+"Boot Time"+"="*40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    list_main.append(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    list_main.append("="*40+"CPU Info"+"="*40)
    list_main.append("Physical cores:"+str(psutil.cpu_count(logical=False)))
    list_main.append("Total cores:"+str(psutil.cpu_count(logical=True)))
    cpufreq = psutil.cpu_freq()
    list_main.append(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    list_main.append(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    list_main.append(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    list_main.append("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        list_main.append(f"Core {i}: {percentage}%")
    list_main.append(f"Total CPU Usage: {psutil.cpu_percent()}%")
    list_main.append("="*40+"Memory Information"+"="*40)
    svmem = psutil.virtual_memory()
    list_main.append(f"Total: {get_size(svmem.total)}")
    list_main.append(f"Available: {get_size(svmem.available)}")
    list_main.append(f"Used: {get_size(svmem.used)}")
    list_main.append(f"Percentage: {svmem.percent}%")
    list_main.append("="*20+"SWAP"+"="*20)
    swap = psutil.swap_memory()
    list_main.append(f"Total: {get_size(swap.total)}")
    list_main.append(f"Free: {get_size(swap.free)}")
    list_main.append(f"Used: {get_size(swap.used)}")
    list_main.append(f"Percentage: {swap.percent}%")
    list_main.append("="*40+"Disk Information"+"="*40)
    list_main.append("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        list_main.append(f"=== Device: {partition.device} ===")
        list_main.append(f"  Mountpoint: {partition.mountpoint}")
        list_main.append(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        list_main.append(f"  Total Size: {get_size(partition_usage.total)}")
        list_main.append(f"  Used: {get_size(partition_usage.used)}")
        list_main.append(f"  Free: {get_size(partition_usage.free)}")
        list_main.append(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    list_main.append(f"Total read: {get_size(disk_io.read_bytes)}")
    list_main.append(f"Total write: {get_size(disk_io.write_bytes)}")

    # Network information
    list_main.append("="*40+"Network Information"+"="*40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            list_main.append(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                list_main.append(f"  IP Address: {address.address}")
                list_main.append(f"  Netmask: {address.netmask}")
                list_main.append(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                list_main.append(f"  MAC Address: {address.address}")
                list_main.append(f"  Netmask: {address.netmask}")
                list_main.append(f"  Broadcast MAC: {address.broadcast}")
    net_io = psutil.net_io_counters()
    list_main.append(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    list_main.append(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    '''
    print("="*40, "GPU Details", "="*40)
    gpus = GPUtil.getGPUs()
    print(gpus)
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,gpu_total_memory, gpu_temperature, gpu_uuid))
        #print(gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,gpu_total_memory, gpu_temperature, gpu_uuid)
    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory", "temperature", "uuid")))'''

def musicstop():
    pg.mixer.music.stop()

def ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    list_main.append("Your Computer Name is:" + hostname)
    list_main.append("Your Computer IP Address is:" + IPAddr)

def vol():
    valid = False
    while not valid:
        volume = input('What volume? > ')
        try:
            volume = int(volume)
            if (volume <= 100) and (volume >= 0):
                call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
                valid = True
        except ValueError:
            pass
    speak("volume has changed")

def openfile(x):
    fname="/home/monisha/Documents/"+x
    #os.system(r"/home/monisha/Documents/"+fname)
    webbrowser.open_new_tab(fname)

def weather(x):
    apikey='c2bebfdb84d0a020444d24d453296434'
    cityname=x.split(" ")[-1]
    url1="https://api.openweathermap.org/data/2.5/weather?appid="+apikey+"&q="+cityname+"&units=metric"
    url2=f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=nPwoNHGZCqsNkk9G3eCOM5GGTZo69AIG&q={cityname}&language=en-US&details=false'
    res1=requests.get(url1)
    w=res1.json()
    xyz=requests.get(url2).json()
    if w["cod"]!="404":
        y=w["main"]
        temp=y["temp"]
        pres=y["pressure"]
        humi=y["humidity"]
        z=w["weather"]
        wdesc=z[0]["description"]
        #list_main.append(f'Temperature = {temp}°C;\nDescription = {wdesc}\nMax temp = {tmax}°C\nMin temp = {tmin}°C\nPressure = {pres}mbar\nHumidity = {humi}%')
        list_main.append(f'Current weather conditions in {cityname}:')
        list_main.append(f'   Temperature: {temp} °C')
        list_main.append(f'   Description: {wdesc}')
        list_main.append(f'   Pressure: {pres} millibar')
        list_main.append(f'   Humidity: {humi}%')
        update_main()
        speak(f'Temperature is {temp}°Celsius')
        #print(url)
    else:
        list_main.append("city not found")
        update_main()
    if "forecast" in x and "daily" not in x:
        try:
            
            res2=xyz[0]["Key"]
            url3=f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{res2}?apikey=nPwoNHGZCqsNkk9G3eCOM5GGTZo69AIG&language=en-US&details=true&metric=true'
            res3=requests.get(url3)
            ww=res3.json()
            print(ww)
            if "detail" in x:
                try:
                    list_main.append(ww["Headline"]["Text"])
                    list_main.append("   Sunrise at "+str(ww["DailyForecasts"][0]["Sun"]["Rise"][11:16]))
                    list_main.append("   Sunset at "+str(ww["DailyForecasts"][0]["Sun"]["Set"][11:16]))
                    list_main.append("   Moon Phase: "+str(ww["DailyForecasts"][0]["Moon"]["Phase"]))
                    list_main.append("   Minimun temp: "+str(ww["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])+" °C")
                    list_main.append("   Maximum temp: "+str(ww["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"])+" °C")
                    list_main.append("   Rain probability: "+str(ww["DailyForecasts"][0]["Day"]["RainProbability"])+"% during daytime and "+str(ww["DailyForecasts"][0]["Night"]["RainProbability"])+"% during nighttime")
                    list_main.append("   Air Quality: "+ww["DailyForecasts"][0]["AirAndPollen"][0]["Category"])
                    list_main.append("   UV Index: "+ww["DailyForecasts"][0]["AirAndPollen"][5]["Category"])
                    update_main()
                except:
                    list_main.append("error")
                    update_main()
            else:
                try:
                    list_main.append(ww["Headline"]["Text"])
                    list_main.append("   Minimun temp: "+str(ww["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])+" °C")
                    list_main.append("   Maximum temp: "+str(ww["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"])+" °C")
                    list_main.append("   Rain probability: "+str(ww["DailyForecasts"][0]["Day"]["RainProbability"])+"% during daytime and "+str(ww["DailyForecasts"][0]["Night"]["RainProbability"])+"% during nighttime")
                    update_main()
                except:
                    list_main.append("error")
                    update_main()
        except:
            speak(xyz["Message"])
            list_main.append(xyz["Code"])
            list_main.append(xyz["Message"])
            update_main()
            return
    elif "daily" in x:
        try:
            print(url2)
            res2=xyz[0]["Key"]
            url3=f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{res2}?apikey=nPwoNHGZCqsNkk9G3eCOM5GGTZo69AIG&language=en-US&details=true&metric=true'
            res3=requests.get(url3)
            ww=res3.json()
            print(ww)
            if "detail" in x:
                try:
                    list_main.append(ww["Headline"]["Text"])
                    list_main.append("Date               "+str(tellDate(0,1))+"          "+str(tellDate(1,1))+"          "+str(tellDate(2,1))+"          "+str(tellDate(3,1)+"          ")+str(tellDate(4,1)))
                    list_main.append("Minimum T              "+str(ww["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][1]["Temperature"]["Minimum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][2]["Temperature"]["Minimum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][3]["Temperature"]["Minimum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][4]["Temperature"]["Minimum"]["Value"])+" °C")
                    list_main.append("Maximum T              "+str(ww["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][1]["Temperature"]["Maximum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][2]["Temperature"]["Maximum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][3]["Temperature"]["Maximum"]["Value"])+" °C                 "+str(ww["DailyForecasts"][4]["Temperature"]["Maximum"]["Value"])+" °C")
                    
                    list_main.append("Sunrise                "+str(ww["DailyForecasts"][0]["Sun"]["Rise"][11:16])+"                   "+str(ww["DailyForecasts"][1]["Sun"]["Rise"][11:16])+"                   "+str(ww["DailyForecasts"][2]["Sun"]["Rise"][11:16])+"                   "+str(ww["DailyForecasts"][3]["Sun"]["Rise"][11:16])+"                   "+str(ww["DailyForecasts"][4]["Sun"]["Rise"][11:16]))
                    list_main.append("Sunset                 "+str(ww["DailyForecasts"][0]["Sun"]["Set"][11:16])+"                   "+str(ww["DailyForecasts"][1]["Sun"]["Set"][11:16])+"                   "+str(ww["DailyForecasts"][2]["Sun"]["Set"][11:16])+"                   "+str(ww["DailyForecasts"][3]["Sun"]["Set"][11:16])+"                   "+str(ww["DailyForecasts"][4]["Sun"]["Set"][11:16]))
                    list_main.append("Moon Phase         "+str(ww["DailyForecasts"][0]["Moon"]["Phase"])+"          "+str(ww["DailyForecasts"][1]["Moon"]["Phase"])+"          "+str(ww["DailyForecasts"][2]["Moon"]["Phase"])+"          "+str(ww["DailyForecasts"][3]["Moon"]["Phase"])+"          "+str(ww["DailyForecasts"][4]["Moon"]["Phase"]))
                    list_main.append("Rain probability(D)    "+str(ww["DailyForecasts"][0]["Day"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][1]["Day"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][2]["Day"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][3]["Day"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][4]["Day"]["RainProbability"])+"%")
                    list_main.append("Rain probability(N)    "+str(ww["DailyForecasts"][0]["Night"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][1]["Night"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][2]["Night"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][3]["Night"]["RainProbability"])+"%                     "+str(ww["DailyForecasts"][4]["Night"]["RainProbability"])+"%")
                    list_main.append("Air Quality            "+ww["DailyForecasts"][0]["AirAndPollen"][0]["Category"]+"                    "+ww["DailyForecasts"][1]["AirAndPollen"][0]["Category"]+"                    "+ww["DailyForecasts"][2]["AirAndPollen"][0]["Category"]+"                    "+ww["DailyForecasts"][3]["AirAndPollen"][0]["Category"]+"                    "+ww["DailyForecasts"][4]["AirAndPollen"][0]["Category"])
                    list_main.append("UV Index              "+ww["DailyForecasts"][0]["AirAndPollen"][5]["Category"]+"                    "+ww["DailyForecasts"][1]["AirAndPollen"][5]["Category"]+"                    "+ww["DailyForecasts"][2]["AirAndPollen"][5]["Category"]+"                    "+ww["DailyForecasts"][3]["AirAndPollen"][5]["Category"]+"                    "+ww["DailyForecasts"][4]["AirAndPollen"][5]["Category"])
                    update_main()
                except:
                    list_main.append("error")
                    update_main()
            else:
                try:
                    list_main.append(ww["Headline"]["Text"])
                    '''list_main.append("   "+str(tellDate(0,1))+" "+str(ww["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])+" °C / "+str(ww["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"])+" °C")
                    list_main.append("   "+str(tellDate(1,1))+" "+str(ww["DailyForecasts"][1]["Temperature"]["Minimum"]["Value"])+" °C / "+str(ww["DailyForecasts"][1]["Temperature"]["Maximum"]["Value"])+" °C")
                    list_main.append("   "+str(tellDate(2,1))+" "+str(ww["DailyForecasts"][2]["Temperature"]["Minimum"]["Value"])+" °C / "+str(ww["DailyForecasts"][2]["Temperature"]["Maximum"]["Value"])+" °C")
                    list_main.append("   "+str(tellDate(3,1))+" "+str(ww["DailyForecasts"][3]["Temperature"]["Minimum"]["Value"])+" °C / "+str(ww["DailyForecasts"][3]["Temperature"]["Maximum"]["Value"])+" °C")
                    list_main.append("   "+str(tellDate(4,1))+" "+str(ww["DailyForecasts"][4]["Temperature"]["Minimum"]["Value"])+" °C / "+str(ww["DailyForecasts"][4]["Temperature"]["Maximum"]["Value"])+" °C")'''
                    list_main.append("Date          "+str(tellDate(0,1))+"      "+str(tellDate(1,1))+"      "+str(tellDate(2,1))+"      "+str(tellDate(3,1)+"      ")+str(tellDate(4,1)))
                    list_main.append("Minimum T"+"       "+str(ww["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"])+" °C            "+str(ww["DailyForecasts"][1]["Temperature"]["Minimum"]["Value"])+" °C            "+str(ww["DailyForecasts"][2]["Temperature"]["Minimum"]["Value"])+" °C            "+str(ww["DailyForecasts"][3]["Temperature"]["Minimum"]["Value"])+" °C            "+str(ww["DailyForecasts"][4]["Temperature"]["Minimum"]["Value"])+" °C            ")
                    list_main.append("Maximum T"+"       "+str(ww["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"])+" °C            "+str(ww["DailyForecasts"][1]["Temperature"]["Maximum"]["Value"])+" °C            "+str(ww["DailyForecasts"][2]["Temperature"]["Maximum"]["Value"])+" °C            "+str(ww["DailyForecasts"][3]["Temperature"]["Maximum"]["Value"])+" °C            "+str(ww["DailyForecasts"][4]["Temperature"]["Maximum"]["Value"])+" °C            ")
                    update_main()
                except:
                    list_main.append("error")
                    update_main()
        except:
            speak(xyz["Message"])
            list_main.append(xyz["Code"])
            list_main.append(xyz["Message"])
            update_main()
            return
    update_main()
    #"1-204108_1_AL"

def changepd(q):
    q=inp.get("1.0",'end-1c')
    global WORK_TIME,SHORT_BREAK_TIME,LONG_BREAK_TIME
    WORK_TIME=int(q.split(" ")[0])*60
    SHORT_BREAK_TIME=int(q.split(" ")[1])*60
    LONG_BREAK_TIME=int(q.split(" ")[2])*60

def Take_query():
    inp.focus()
    while(True):
        #query = takeCommand().lower()
        query=inp.get("1.0",'end-1c')
        inp.delete("1.0",END)
        list_main.append("")
        update_main()
        if query.startswith("\n"):
            list_main.append("  >>> "+query[1:])
        else:
            list_main.append("  >>> "+query)
        update_main()
        x=query[1:].split(" ")
        print("\n")
        if x[0].lower()=="open" and "app" not in query and"file" not in x:
            webbrowser.open("www."+x[1]+".com")
            break
        elif "open" in query and "app" in query:
            if "music" in query:
                os.system("rhythmbox")
            if "excel" in query:
                os.system("libreoffice --calc")
            if "word" in query:
                os.system("libreoffice --writer")
            if "paint" in query:
                os.system("libreoffice --draw")
            if "ppt" in query:
                os.system("libreoffice --impress")
            break
        elif "game" in query:
            games(query)
        elif "recommend" in query:
            recs(query)
            break
        elif "calender" in query or "schedule" in query:
            calender(query)
            break
        elif "search" in query:
            sgoogle(query)
            break
        elif "time" in query:
            tellTime()
            break
        elif "clean" in query or "autoremove" in query:
            os.system("sudo apt autoremove")
            break
        elif "email" in query or "send mail" in query:
            mail()
            break
        elif "joke" in query or "make me laugh" in query:
            joke()
            break
        elif "news" in query or "headlines" in query:
            news()
            break
        elif "volume" in query:
            vol()
            break
        elif "ip address" in query:
            ip()
            update_main()
            break
        elif "file" in query:
            #syntax open file xyz
            y=x.index("file")
            openfile(x[y+1])
            break
        elif "system info" in query:
            if "complete" in query:
                compsi()
                time.sleep(3)
                update_main()
                break
            else:
                sysinf()
                update_main()
                break
        elif "bye" in query:
            print("Bye.\n")
            speak("bye bye")
            exit()
        elif "weather" in query:
            weather(query)
            break
        elif "music" in query:
            music()
            break
        elif "day" in query:
            tellDay()
            break
        elif "date" in query:
            speak(tellDate(0,0))
            break
        elif "to do" in query or "todo"in query or "tasks" in query:
            todo()
            break
        elif "pomodoro" in query:
            if "-e" in query:
                global POMO_FLAG
                POMO_FLAG=True
                list_main.append("Enter new timings in hours seperated by space [format: work shortbreak longbreak]")
                update_main()
                inp.delete("1.0",END)
                inp.focus()
                break
            PomodoroTimer()
            break
        else:
            '''llm=OpenAI(temperature=0.5)
            answ=llm(query)
            print(answ)
            speak(answ)'''
            list_main.append("Command not found")
            update_main()
            speak("unable to answer that")
            break

def enterkey(event):
    global POMO_FLAG
    if POMO_FLAG==True:
        
        q=inp.get("1.0",'end-1c')
        changepd(q[1:])
        inp.focus()
        list_main.append(f'timings changes to {q[1:]}')
        print(WORK_TIME,SHORT_BREAK_TIME,LONG_BREAK_TIME)
        update_main()
        POMO_FLAG=False
        inp.delete("1.0",END)

    else:
        Take_query()

def check():
    print(inp.get("1.0",END))

def update_main():
    bx.delete(0,bx.size())
    bx.insert('end'," ")
    for task in list_main:
        bx.insert('end',"  "+task)

def help_update():
    with open("/home/monisha/Lily/help.txt","r") as f:
        c=f.readlines()
        hx.insert('end'," ")
        for i in c:
            hx.insert('end',"  "+i.replace("\n"," "))

def inl(event):
    event.widget.insert("insert","\n ")
    return "break"

def valid(event):
    x=event.widget.get(1.0,"end-1c")
    if x=="///":
        #ddm=OptionMenu(tab2,width=120,)
        print("okkkk")
    else: pass

def onseltab(event):
    if tabControl.index('current')==0:
        inp.focus()

if __name__ == '__main__':
    Hello()
    root=tk.Tk()
    root.title("Personal Assistant")
    w=root.winfo_screenwidth()
    h=root.winfo_screenheight()
    root.geometry(f'{w}x{h}')
    root.config(bg='#2B2E37')
    tabControl = ttk.Notebook(root)
    tab2 = ttk.Frame(tabControl)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab2, text ='Terminal')
    tabControl.add(tab1, text ='Help') 
    tabControl.bind("<<NotebookTabChanged>>",onseltab)
    s = tb.Style("darkly")
    s.configure('TNotebook', font='Arial Bold',foreground="#fff",padding=5)
    #s.configure('TNotebook.Tab', font='Arial Bold',foreground="#fff",background="purple")

    #s2.configure('TNotebook', font='Arial Bold', foreground='salmon',background='#000000')
    #s1=ThemedStyle()
    #s1.theme_use('black')
    
    tabControl.pack(expand = 1, fill ="both") 
    bx=Listbox(tab2,width=145,font=("monospace", 16),height=32,bg='#2B2E37',fg='#fff')
    bx.place(x=8,y=12)
    hx=Listbox(tab1,width=145,font=("monospace", 16),height=35,bg='#2B2E37',fg='#fff')
    hx.place(x=8,y=12)
    help_update()
    inp=Text(master=tab2)
    #print(tabControl.index('current'))
    
    inp.bind('<Return>',enterkey)
    inp.bind("<Control-Return>",inl)
    inp.bind("<KeyRelease>",valid)
    scr=Scrollbar(tab2, orient=VERTICAL, command=inp.yview)
    scr.place(x=1650,y=915)
    inp.config(height=1,font=("monospace", 16),width=120,bg='#2B2E37',fg='#fff',yscrollcommand=scr.set)
    inp.place(x=100,y=910)
    update_main()
    inpenter=Button(tab2,width=15,height=2,text="enter command",bg='lightblue',command=lambda:Take_query())
    inpenter.place(x=1700,y=905)
    '''logo = ImageTk.PhotoImage(Image.open("icon_deactivated.png"))
    logo1 = ImageTk.PhotoImage(Image.open("icon_activated.png"))
    l = Label(image=logo, borderwidth=0, width=1000, anchor="center", bg="pink")
    l.pack()'''
    i=PIL.Image.open("/home/monisha/Lily/MicOn.png").resize((35, 45), PIL.Image.ANTIALIAS)
    button_on = ImageTk.PhotoImage(i)
    mic=Button(tab2,image=button_on,border=0,bg='#2B2E37',width=45,height=55,highlightcolor='#2B2E37',activebackground='#000000')
    mic.place(x=25,y=900)
    pressed = True
    inp.focus()
    root.mainloop()
    


#sk-proj-B0428qiR5IOAnknz0wpQT3BlbkFJ4DH8Tn834H29HyBZfXhX

'''elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am xxx. Your desktop Assistant")'''

# set alarm
# play song on youtube
# next shuffle back for song queue pause continue
# sample note saved in file + ask to read notes
# learn interests and adapt
# learn music preferences
# confirms interest and data learned about user by giving summary every week
# develop itenary/ tell best flights/hotels
# modify/sort datasheets
# password manager? -security????

'''
    4401 2827
    5101 7211
    4459 5287
    9094 2749
    2989 0994
    4726 9842
    8161 2256
    2827 5099
    2672 8560
    8712 4608
'''
#jnel wpcu jlxn zpny 
#  Created calendar: 595b76a9646224cc7b156787e2ffb0efc7f52e473582dea1deb63a44e13fe5fe@group.calendar.google.com -> 2024-07-29-14-00