from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import requests
import ssl
import os
import pyautogui
import smtplib

PATH = "D:\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com")
cevap = input("kimi takip etmek istersiniz")
cevap1 = str(cevap)
time.sleep(10)
simple_email_contex = ssl.create_default_context()
def mail(mesage):
    sahip = ''
    gonderilecek = ''
    giris=''
    sifre=''
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls(context=simple_email_contex)
    server.login(giris,sifre)
    server.sendmail(sahip,gonderilecek,mesage)
    server.quit()
if bool(cevap1)==True:
    arama = driver.find_element("css selector", "body.web.dark:nth-child(2) div._1Fm4m._1h2dM.app-wrapper-web.font-fix.os-win div.two.aHGmo._1jJ70:nth-child(6) div._2Ts6i._3RGKj:nth-child(4) div.k8VZe div._3gYev div._1s7Pa._3wQ5i.o7fBL div._1EUay div._2vDPL:nth-child(4) div.g0rxnol2.ln8gz9je.lexical-rich-text-input div.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt.qh0vvdkp > p.selectable-text.copyable-text.iq0m558w").click()
    arama1 = driver.find_element("css selector", "body.web.dark:nth-child(2) div._1Fm4m._1h2dM.app-wrapper-web.font-fix.os-win div.two.aHGmo._1jJ70:nth-child(6) div._2Ts6i._3RGKj:nth-child(4) div.k8VZe div._3gYev div._1s7Pa._3wQ5i.o7fBL div._1EUay div._2vDPL:nth-child(4) div.g0rxnol2.ln8gz9je.lexical-rich-text-input div.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt.qh0vvdkp > p.selectable-text.copyable-text.iq0m558w").send_keys(cevap1)
    arama2 = driver.find_element("css selector", "body.web.dark:nth-child(2) div._1Fm4m._1h2dM.app-wrapper-web.font-fix.os-win div.two.aHGmo._1jJ70:nth-child(6) div._2Ts6i._3RGKj:nth-child(4) div.k8VZe div._3gYev div._1s7Pa._3wQ5i.o7fBL div._1EUay div._2vDPL:nth-child(4) div.g0rxnol2.ln8gz9je.lexical-rich-text-input div.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt.qh0vvdkp > p.selectable-text.copyable-text.iq0m558w").send_keys(Keys.ENTER)

    time.sleep(10)

    kontrol = True
    kontrol2 = True
    kontrol3 = False
    while True:
        try:
            cevrim = driver.find_element("css selector", "body.web.dark:nth-child(2) div._1Fm4m._1h2dM.app-wrapper-web.font-fix.os-win div.two.aHGmo._1jJ70:nth-child(6) div._2Ts6i._2xAQV:nth-child(5) div._2Ex_b header._23P3O:nth-child(2) div._24-Ff div.p357zi0d.r15c9g6i.g4oj0cdv.ovllcyds.l0vqccxk.pm5hny62 > span.ggj6brxn.gfz4du6o.r7fjleex.lhj4utae.le5p0ye3._11JPr.selectable-text.copyable-text")
            if kontrol == True :
                print(time.asctime(time.localtime()))
                print("çevrimiçi\n")
                kontrol = False
                kontrol2 = True
                kontrol3 = True
                baslangıc = time.time()
        except:
            kontrol = True
            if kontrol2 == True:
                zaman = time.asctime(time.localtime())
                zaman2= str(zaman)
                print(zaman)
                print("cevrimiçi değil\n")
                if kontrol3 == True:
                    bitis =time.time() - baslangıc
                    print("şu kadar süre çevrim içi kalındı=")
                    msg = "şu kadar süre çevrimiçi kalındı ="
                    son = zaman2+msg+str(bitis)
                    mail(son)
                    print(bitis)

                kontrol2 = False

