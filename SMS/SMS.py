#https://www.reddit.com/r/Python/comments/8gb88e/free_alternatives_to_twilio_for_sending_text/

import smtplib

email = "projects4ll3n@gmail.com"
authToken = "vtrrlrlawammuusv"
myNumber = '4237736938{}'

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(message):
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = myNumber.format(carriers['tmobile'])
	auth = (email, authToken)

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)

send("sent from python")


"""
    import SMS

    some_text = 'Blah, blah'

    SMS.send(some_text)
    """