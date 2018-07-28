import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import time

def gmail(): #Gmail hesabınızdan e-posta göndermek istiyorsanız, ayarlara gidip
             #"Güvenliği düşük uygulamaların hesaplara erişmesine izin ver" seçeneğini aktif hale getirmeniz gereklidir.

    mesaj = MIMEMultipart()
    mesaj["From"] = seçim
    mesaj["To"] = input("Mesaj Göndermek İstediğiniz E-Posta Adresiniz Giriniz :")
    mesaj["Subject"] = input("Konu Başlığı Giriniz :")
    yazi = input("Göndermek istediğiniz Mesajı Giriniz :")
    parola = input("Parolanızı giriniz :")
    m = MIMEText(yazi, "plain")
    mesaj.attach(m)
    while True:
        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(mesaj["From"],parola)
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
            print("E-Posta Başarıyla Gönderildi.")
            time.sleep(1)
            continue

        except:
            sys.stderr.write("Gönderme İşlemi Başarısız! Lütfen Bilgilerinizi Kontrol Edip Tekrar Deneyiniz.\n")
            sys.stderr.flush()

def hotmail():

    mesaj = MIMEMultipart()
    mesaj["From"] = seçim
    mesaj["To"] = input("Mesaj Göndermek İstediğiniz E-Posta Adresiniz Giriniz :")
    mesaj["Subject"] = input("Konu Başlığı Giriniz :")
    yazi = input("Göndermek istediğiniz Mesajı Giriniz :")
    parola = input("Parolanızı giriniz :")
    m = MIMEText(yazi, "plain")
    mesaj.attach(m)
    while True:
        try:
            mail = smtplib.SMTP("smtp-mail.outlook.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(mesaj["From"], parola)
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("E-Posta Başarıyla Gönderildi.")
            time.sleep(1)
            continue

        except:
            sys.stderr.write("Gönderme İşlemi Başarısız! Lütfen Bilgilerinizi Kontrol Edip Tekrar Deneyiniz.\n")
            sys.stderr.flush()

liste = ["@gmail.com"]
liste1 = ["@hotmail.com"]

seçim = input("Lütfen E-Posta Adresinizi Giriniz :")
for x in liste:
    if x in seçim:
        gmail()

for q in liste1:
    if q in seçim:
        hotmail()
