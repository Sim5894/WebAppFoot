import smtplib


carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@page.nextel.com'
}


def send(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    #to_number = '0470037469{}'.format(carriers['att'])
    to_number = '0470037469@txt.att.net'
    auth = ('simontestsms5@gmail.com', 'testingsms')

    # Establish a secure session with gmail's outgoing SMTP server using your gmail account

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail( auth[0], to_number, message)