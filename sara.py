from tkinter import *
from tkinter import ttk
import pyttsx3
import speech_recognition as sr
import datetime
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import sys
import smtplib
from webdriver_manager.chrome import ChromeDriverManager
import wikipedia
import requests
from threading import Thread
global run
global linkdin_u,linkdin_p,gmail_u,gmail_p
def shutdown():
    global run
    run=False
    Thread(target=sara).start()
    root.destroy()

def begin():
 global run
 run=True
 Thread(target=sara).start()

#function named sara is heart of this program it may contain many things like it can speak,listen do all work which you assign.
def sara():
    #Below given variables are assigned for startup page for app
    global linkdin_u,linkdin_p,gmail_u,gmail_p
    #This function is used to create a browser for searching 
    def browser_making():
        global browser 
        browser=webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://google.com")

    #This Function will provide program speaking skills

    def speak(audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 120)
        engine.setProperty('volume', 1) 
        engine.say(audio)
        engine.runAndWait()

    #This Function will leads program for speech Recoginition
    def speech():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening")
            r.energy_threshold=1500
            r.pause_threshold = 1
            audio = r.record(source,duration=5)
            try:
                print("initialising")
                query = r.recognize_google(audio, language='en-in')
                print(query)
                
            except Exception:
                print("i can't recognise your sound can you please,speak again")  
                return "None"
            return query
    # This function will greet properly as per the current time 
    def wish():
        time=datetime.datetime.now().hour
        if time>4 and time<11:
            speak("good morning sir!!!")   
        elif time>11 and time<17:
            speak("good afternoon sir!!!")   
        elif time>17 and time<21:
            speak("good evening sir!!!")    
        else:
            speak("good night sir!!!")
    # This fucntion will handle browsing capabilities
    def website():
        g_url="https://google.com/search?q="
        speak("on google what do you like to search") 
        s_url= speech().lower()
        print()
        "%20".join(s_url.split(" "))
        url=g_url+s_url
        browser.get(url)

        if 'youtube' in url:
            youtube()
                
        
        elif 'song'  in url:
            play_song()
        
        else:
            browser.get(url)
            time.sleep(3)
            site_name=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a/h3')
            time.sleep(2)
            speak("i found here"+site_name.text)
            speak("would you like to go to this website")
            response=speech().lower()
            if 'yes' in response:
                time.sleep(1)
                site_name.click()
            elif 'no' in response:
                pass
            elif 'exit' in response:

                browser.quit()
            else:
                pass

    # This function will provide current time,date ,and day
    def time_date():
        time_status=datetime.datetime.now().ctime()
        speak(time_status)
#   This function will provide you Top headlines of current time
    def news():
        key='8b06f5edb25e4f65b02bac8cfd552cf7'
        url='https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=8b06f5edb25e4f65b02bac8cfd552cf7'
        parameter={'q':'bigdata','pagesize':20,'country':'in','apikey':key}
        response=requests.get(url,params=parameter)
        response_json=response.json()
        speak("hear i found some current news")
        j=1
        results_n=[]
        for i in response_json['articles']:
            results_n.append(i['title'])
        for i in range(len(results_n)):
            speak(str(j)+ results_n[i])
            j=j+1

        # This function will provide you and list of videos of youtube which will you search in youtube:
    def youtube_list():
        time.sleep(1)
        choice_1=browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
        time.sleep(1)
        choice_2=browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a[1]')
        time.sleep(1)
        choice_3=browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]/div[1]/div/div[1]/div/h3/a[1][1]')
        time.sleep(1)
        choice_4=browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[4]/div[1]/div/div[1]/div/h3/a[1][1][1]')
        time.sleep(1)
        choice_5=browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[5]/div[1]/div/div[1]/div/h3/a[1][1][1][1]')
        speak("hear is your list of videos")
        speak("one"+choice_1.text)
        speak("two"+choice_2.text)
        speak("three"+choice_3.text)
        speak("four"+choice_4.text)
        speak("five"+choice_5.text)
        speak("speak your choice")
        selector=speech().lower()
        if '1' or 'one' in selector:
            time.sleep(1)
            choice_1.click()
        elif '2' or 'two'in selector:
            time.sleep(1)
            choice_2.click()
        elif '3' or 'three' in selector:
            time.sleep(1)
            choice_3.click()
        elif '4' or 'four' in selector:
            time.sleep(1)
            choice_4.click()    
        elif '5' or 'five' in selector:
            time.sleep(1)
            choice_5.click()
        else:
            pass

        # This function will perform a duty of handling a task to search on youtube as per the user command
    def youtube():
        browser.get("https://youtube.com")
        y_url="https://www.youtube.com/results?search_query="
        speak("in youtube what do you like to search")
        s_url=speech().lower()
        "%20".join(s_url.split(" "))
        url=y_url+s_url
        browser.get(url)
        youtube_list()
     #This function will lead you to open your linkdin account and it is also auto matically sign up for your accouunt   
    def linkdin():
        browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')             
        u_linkdin=browser.find_element_by_name('session_key')
        u_linkdin.send_keys(linkdin_u) 
        p_linkdin=browser.find_element_by_name('session_password')
        p_linkdin.send_keys(linkdin_p)
        sign_in=browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button')
        time.sleep(0.1)
        sign_in.click()
    #This function will play a song online as per your choice 
    def play_song():
        m_url="https://soundcloud.com/search?q="
        browser.get(m_url)
        speak("which song do you like to here")
        s_url=speech().lower()
        "%20".join(s_url.split(" "))
        url=m_url+s_url
        browser.get(url)
        r=requests.get(url)
        soup=BeautifulSoup(r.text,'html.parser')
        t=soup.select("h2")[3:]
        track_links=[]
        track_name=[]
        speak("here is your list of songs")
        for index,track in enumerate(t):
            track_links.append(track.a.get('href'))
            track_name.append(track.text)
            print(str(index+1)+":"+track.text)
            
            speak(str(index+1)+":"+track.text)
            print()
        speak("speak your choice")     
        selector=speech().lower()
        if '1'or 'one' in selector:
            r=0
        elif '2' or 'two' in selector:
            r=1
        elif '3' or 'three' in selector:
            r=2
        elif '4' or 'four' in selector:
            r=3    
        elif '5' or 'five' in selector:
            r=4
        elif '6' or 'six' in selector:
            r=5
        elif '7' or 'seven' in selector:
            r=6
        elif 'exit' in selector:
            browser.quit()
        else:
            browser.quit()   
        
        browser.get("https://soundcloud.com"+track_links[int(r)])
        time.sleep(2)
        play_button=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a')
        time.sleep(1)
        play_button.click()
    #This function will use to open your pc like word,excel,acess and other
    def open_f():
        speak("which file do you want to open in pc")
        a=speech().lower()
        if 'excel' in a:
         open_file=os.startfile('C:\Program Files\Microsoft Office\Office15\EXCEL.EXE')
            
        elif 'access' in a:
         open_file=os.startfile('C:\Program Files\Microsoft Office\Office15\MSACCESS.EXE')
        
        elif 'word' in a:
         open_file=os.startfile('C:\Program Files\Microsoft Office\Office15\WINWORD.EXE')
        
        elif 'powerpoint'in a:
         open_file=os.startfile('C:\Program Files\Microsoft Office\Office15\POWERPNT.EXE')
        
        elif 'images' in a:
         open_file=os.startfile('C:\\Users\\anura\\Pictures\\photo')
        else:
         pass
    #this function Will lead you to acess you gmail with auto sign up feature
    def g_mail():
        browser.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        speak("loading your username and password")
        u=browser.find_element_by_name('identifier')
        u.send_keys(gmail_u)
        n=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        time.sleep(0.1)
        n.click()
        time.sleep(3)
        p=browser.find_element_by_name("password")
        p.send_keys(gmail_p)
        signin=browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        time.sleep(0.1)
        signin.click()
        time.sleep(2)
        browser.get("https://mail.google.com/mail/u/0/#inbox")
    #This function will use to handle task which will give you weather report of perticuler city as per users choice
    def weather():
        speak("speak a name of city you want weather report")
        city=speech().lower()
        url="https://api.openweathermap.org/data/2.5/weather?appid=6965f746c3cbee3ddb78c208a5c51f26&q="
        f_url=url+city
        response=requests.get(f_url).json()
        t=( response['main'])
        z=t['temp']
        x=response['weather']
        y=x[0]['description']
        p=(int(int(z)-273.15))
        speak ("today's tempreture "+str(p)+ " degree celcius "+ "and it is having chances of "+str(y))

    def message():
        print("what you like to msg enter below:")
        msg=sys.stdin.read()
        return msg
#This function is acctually not assign in main program but this function may use for Sending an email to anyone 
    def send_mail(): 
        r_mail=input("whom do you want to send a mail enter his email-ID:")
        masg=message()
        session=smtplib.SMTP('smtp.gmail.com',587)
        session.starttls()
        session.login(gmail_u,gmail_p)
        session.sendmail(gmail_u,r_mail,masg)
        session.quit()


    if __name__ == "__main__":
        while run:
            speak("hi, i am sara,i run at hundred tera bytes speed, i would like to do work which you will assign to me")
            speak("Before proceeding toward any action or work i would like to get your information so i can give better results of your command")
            time.sleep(1)
            speak("initialising all my duties it will take several seconds")
            time.sleep(1)
            speak("now my all setup is ready i will accept all your command")
            while run:
                wish()
                while run:
                    command=speech().lower()
                    if 'time' in command:
                        time_date()
                    elif 'google' in command:
                        browser_making()
                        website()
                        while run:
                            command=speech().lower()
                            if 'exit' in command:
                                browser.quit()
                                break
                            else:
                                pass
                    elif 'youtube' in command:
                        browser_making()
                        youtube()
                        while run:
                            command=speech().lower()
                            if 'exit' in command:
                                browser.quit()
                                break
                            else:
                                pass
                    elif 'song' in command:
                        browser_making()
                        play_song()
                        while run:
                            command=speech().lower()
                            if 'exit' in command:
                                browser.quit()
                                break
                            else:
                                pass
                    elif 'news' in command:
                        news()
                    elif 'weather' in command:
                        weather()
                    elif 'open' in command:
                        open_f()
                        while run:
                            command=speech().lower()
                            if 'exit' in command:
                                break
                            else:
                                pass
                    elif 'linkedin' in command:
                        browser_making()
                        linkdin()
                        while run:
                            command=speech().lower()
                            if 'exit' in command:
                                browser.quit()
                                break
                            else:
                                pass
                    elif 'gmail' in command:
                        browser_making()
                        g_mail()
                        while run:
                            command=speech().lower()
                            if 'exit' in command:
                                browser.quit()
                                break
                            else:
                                pass
                    elif 'exit' in command:
                        browser.quit()
                        break
                    else:
                        pass
                    
if __name__ == "__main__":
    root=Tk()
    root.geometry('300x550+0+0')
    root.title('sara your companion')
    root.config(bg='black')
    root.iconbitmap("C:\\Users\\anura\\Downloads\\robot.ico")
    photo=PhotoImage(file=r"C:\Users\anura\Downloads\ai.png")
    photo1=PhotoImage(file=r"C:\Users\anura\Desktop\robo.png")
    
    global linkdin_u,linkdin_p,gmail_u,gmail_p
    linkdin_u_var=StringVar()
    linkdin_p_var=StringVar()
    gmail_u_var=StringVar()
    gmail_p_var=StringVar()
    
    def new():
        global linkdin_u,linkdin_p,gmail_u,gmail_p
        linkdin_u=linkdin_u_var.get()
        linkdin_p=linkdin_p_var.get()
        gmail_u=gmail_u_var.get()
        gmail_p=gmail_p_var.get()
        n_win=Toplevel(root)
        n_win.geometry('300x570+0+0')
        n_win.iconbitmap("C:\\Users\\anura\\Downloads\\robot.ico")
        n_win.title('Sara a Companion')
        n_win.config(bg="black")
        start=Button(n_win,text='start',bd=8,width=38,height=3,command=begin,background='Skyblue')
        start.pack(side=TOP,padx=5,pady=5)
        
        Label(n_win,image=photo1).pack(padx=5,pady=5)
        close=Button(n_win,text='close',bd=8,width=38,height=3,command=shutdown,background='Skyblue')
        close.pack(side=TOP,padx=5,pady=5)
       
    Label(root,text="Insert your basic info",bd=8,font=("harrington",10,"bold"),background="skyblue",width=38).pack(padx=5,pady=3)
    Label(root,text="Linkdin Username:",font=("harrington",10,"bold"),bd=8,background="skyblue",width=35).pack(padx=5,pady=3)
    e1=Entry(root,width=35,textvariable=linkdin_u_var)
    e1.pack(padx=5,pady=3)
    Label(root,text="Linkdin Password:",font=("harrington",10,"bold"),bd=8,background="skyblue",width=35).pack(padx=5,pady=3)
    e2=Entry(root,width=35,textvariable=linkdin_p_var)
    e2.pack(padx=5,pady=3)
    Label(root,text="Gmail Username:",font=("harrington",10,"bold"),background="skyblue",bd=8,width=35).pack(padx=5,pady=3)
    e3=Entry(root,width=35,textvariable=gmail_u_var)
    e3.pack(padx=5,pady=3)
    Label(root,text="Gmail Password:",font=("harrington",10,"bold"),background="skyblue",bd=8,width=35).pack(padx=5,pady=3)
    e4=Entry(root,width=35,textvariable=gmail_p_var)
    e4.pack(padx=5,pady=3)
    Label(root,image=photo,compound=TOP,).pack(padx=5,pady=5)
    Button(root,text="next",command=new,background="skyblue",width=38,height=3,bd=8).pack(side=TOP,padx=5,pady=5)
   
    root.mainloop()




