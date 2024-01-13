
from import_everything import *

smtp_server = 'outlook.office365.com'  # Outlook SMTP server address
smtp_port = 587  # The default port for TLS
smtp_username = 'unichem_sender_automated@outlook.com'  # Your Outlook email address
smtp_password = 'UnichemSender'  # Your Outlook password
from_email = 'unichem_sender_automated@outlook.com'
to_email = 'unichem_sender_automated@outlook.com'


server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Use TLS
server.login(smtp_username, smtp_password)