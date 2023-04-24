import smtplib

# Sender and receiver email addresses
sender_email = "adhirat23@gmail.com"
receiver_email = "22bce506@nirmauni.ac.in"

# Gmail account login credentials
username = "adhirat23@gmail.com"
password = "vubembrysiraudxh"

# Email message to be sent
subject = "Test email"
body = "This is a test email sent using Python!"
message = f"Subject: {subject}\n\n{body}"

# Create a SMTP session
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login to your Gmail account
server.login(username, password)

# Send email
server.sendmail(sender_email, receiver_email, message)

# Close the SMTP session
server.quit()
