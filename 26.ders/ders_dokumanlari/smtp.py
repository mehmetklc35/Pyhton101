import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mesaj = MIMEMultipart()

mesaj["From"] = "selcukakarin@gmail.com"
mesaj["To"] = "sampiyon20162017besiktas@gmail.com"
mesaj["Subject"] = "SMTP MAIL GONDERME"

yazi = """
Şirketimize yaptığınız başvuru değerlendirilmiş olup, salı günkü
mülakatımıza katılmanızı talep ediyoruz.

Aşağıdaki linkten katılım sağlayabilirsiniz.
"""

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login("selcukakarin@gmail.com","jbid ohoh onua vfxy")

# MIMEMultipart -> str
mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

print("Mail başarıyla gönderildi.....")
mail.close()
