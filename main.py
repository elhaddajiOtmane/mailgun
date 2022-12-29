
import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
		auth=("api", "afa16b86ca9dc16346b835ffc0c6b984-d117dd33-936d9246"),
		data={"from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
			"to": ["otmanhaddaji17@gmail.com", "sandboxbba88e5955e44c82babe88f73f3fab31.mailgun.org"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
send_simple_message()