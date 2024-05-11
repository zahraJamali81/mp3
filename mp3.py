import newspaper
from gtts import gTTS

url = input("enter your url :")

# url = 'https://www.geeksforgeeks.org/top-5-open-source-online-machine-learning-environments/' #for testing

url_in = newspaper.Article(url="%s" % (url), language='en')
url_in.download()
url_in.parse()

print(url_in.text)
text = url_in.text
tts = gTTS(text , lang='en')
tts.save('output.mp3')










