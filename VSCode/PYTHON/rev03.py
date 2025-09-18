#Email

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

remetente_email = ""
remetente_senha = ""
destinatario_email = ""

servidor_smtp = "smtp.gmail.com"
porta_smtp = 587

assunto = ""
corpo_email = ""

msg = MIMEMultipart()
msg['Subject']= assunto
msg['From'] = remetente_email
msg['To'] = destinatario_email

try:
    server = smtplib.SMTP(servidor_smtp, porta_smtp)
    server.starttls()
    server.login(remetente_email, remetente_senha)

    server.sendmail(remetente_email, destinatario_email, msg.as_string())
    print("Email enviado com sucesso!")

except Exception as erro:
    print("Erro ao enviar email: ", erro)
finally:
    server.quit()