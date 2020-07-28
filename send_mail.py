import smtplib
from email.mime.text import MIMEText

def send_mail(customer,fooditem,rating,comments):
	port = 2525
	smtp_server = 'smtp.mailtrap.io'
	login = 'c3553e0518c7fe'
	password = '98608ac835ae69'
	message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>fooditem: {fooditem}</li><li>Ratings: {rating}</li><li>Comments: {comments}</li></ul>"

	sender_email = 'crazyankurcool@gmail.com'
	receiver_email = 'email2@gmail.com'
	msg = MIMEText(message,'html')
	msg['Subject'] = 'Feedback'
	msg['From'] = sender_email
	msg['To'] = receiver_email

	with smtplib.SMTP(smtp_server,port) as server:
		server.login(login,password)
		server.sendmail(sender_email,receiver_email,msg.as_string()) 
