import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "selcukakarin@gmail.com"

mesaj["To"] = "sampiyon20162017besiktas@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"


yazi = """

Smtp ile mail gönderiyorum.

Selçuk akarın


"""


mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)


mail = smtplib.SMTP("smtp.gmail.com",587)

# smtp server'ına bağlanmamız gerekli. bu şekilde smtp server'ına kendimizi tanıtıyoruz.
mail.ehlo()
# verilerin encrypt edilmesi için bu fonksiyonu kullanıyoruz.
mail.starttls()

mail.login("selcukakarin@gmail.com", "vpcx znlf nokb kjuf")

# MIMEMultipart yapısından string yapısına çevirmek için
mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

print("Mail Başarıyla Gönderildi....")

mail.close()









