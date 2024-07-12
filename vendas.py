import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("danilokog652@gmail.com", "tydf hpmj opge nqkp")
server.sendmail(
  "danilokog652@gmail.com",
  "natylimas652@gmail.com",
  "menssagem teste")
server.quit()
