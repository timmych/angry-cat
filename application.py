from flask import Flask, Request
import random

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some cute pictures
def cute_hello(username = "World"):
    squirrels = [
        "https://media.npr.org/assets/img/2017/04/25/istock-115796521-fcf434f36d3d0865301cdcb9c996cfd80578ca99-s800-c85.jpg",
        "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2019/07/931/524/creepy-cat.jpg",
        "https://i.pinimg.com/originals/e7/25/de/e725dea7d28c0519f75b4399b971fcaa.jpg",
        "http://www.thetimes.co.uk/imageserver/image/methode%2Ftimes%2Fprod%2Fweb%2Fbin%2F11fb3572-7380-11e7-8eac-856e9b33761e.jpg?crop=3000%2C1687%2C0%2C156&resize=685",
    ]

    # some bits of text for the page.
    header_text = '''
        <html>\n<head> <title>Duoduo's Home Page</title> </head>\n<body>'''
    instructions = '''
        <p><em>Hint</em>: This is a page to show Christopher's cute animals.</p>\n<img src="{}"/>'''.format(squirrels[random.randint(0,len(squirrels) - 1)])
    home_link = '<p><a href="/">Back</a></p>\n'
    footer_text = '</body>\n</html>'
    return header_text + say_hello(username) + instructions + home_link + footer_text

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    cute_hello(username)))

@application.route('/')
def index():
    return cute_hello()

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()