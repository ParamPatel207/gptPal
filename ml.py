import os
import openai
from newspaper import Article
from urlextract import URLExtract
# Load your API key from an environment variable or secret management service
openai.api_key = os.environ["OPEN_AI"]

def generateTLDR(prompt):
  response = openai.Completion.create(
  engine="davinci",
  prompt= prompt + '\ntl;dr:',
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)
  return response.choices[0].text

def urlToText(url = "https://www.google.com"):
  article = Article(url)
  article.download()
  article.parse()
  return article.text

def getURLS(message): # Returns all URLs in a string as a list
  extractor = URLExtract()
  urls = extractor.find_urls(message)
  return urls

def FinalOutput(message):
  urls = getURLS(message)
  temp = ""
  if not urls:
      return generateTLDR(message)
  else:
      for i, siteStr in enumerate([urlToText(URL) for URL in urls]):
          temp = temp + 'Summarizing ' + urls[i] + ': \n' + generateTLDR(siteStr) + '\n'
      return temp