import smtplib
from email.mime.multipart import MIMEMultipart

mesaj = MIMEMultipart()

mesaj["From"] = "selcukakarin@gmail.com"
mesaj["To"] = "@gmail.com"
mesaj["Subject"] = "SMTP MAIL GONDERME"

yazi = """
Şirketimize yaptığıınız başvauru gdeğerlendirlimiş olup"""

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.startls()
mail.login("selcukakarin.gmail.com","(şifre girilecek)")

#MIMEMultipart -----> str 
mail.sendmail(mesaj["From"],mesaj["To"], mesaj.as_string())

print("mail başarıyla gönderildi......")
mail.close()