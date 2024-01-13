from import_everything import *
import smtp_server
# Email configuration for Outlook

def send_mail(to_email, subject, message):

    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = smtp_server.from_email
    msg['To'] = smtp_server.to_email
    msg['Subject'] = subject

    # Add plain text body to the email
    
    msg.attach(MIMEText(message, 'plain'))

    try:
        smtp_server.server.sendmail(smtp_server.from_email, to_email, msg.as_string())
        
        print('Email sent successfully.')
    except Exception as e:
        print('Email could not be sent. Error:', str(e))

# Attach a file (optional)
##attachment_path = 'path/to/attachment.pdf'
##attachment = open(attachment_path, 'rb')
##part = MIMEBase('application', 'octet-stream')
##part.set_payload((attachment).read())
##encoders.encode_base64(part)
##part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
##msg.attach(part)

def quit_everything():
    smtp_server.server.quit()