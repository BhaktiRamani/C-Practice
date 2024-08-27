import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('bhakti.ramani2020@gmail.com','Bhakti@2002')
server.sendmail('bhakti.ramani2020@gmail.com','parthishere1234@gmail.com','heyyyya pada sending email through pythom...hope this works okay bbyeeee')
print('mail sent')