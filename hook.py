import os
from os import environ
from bs4 import BeautifulSoup
import requests
import time
from dhooks import Webhook
hook = Webhook(environ['kluczyk'])



def get_price(waluta):
  url = 'https://www.google.com/search?q='+waluta+'+to+pln'
  HTML = requests.get(url)


  soup = BeautifulSoup(HTML.text, 'html.parser')
  #<div class="BNeawe iBp4i AP7Wnd">

  text = soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
  return text



def main():
  last_price = -1
  while True:
    kurs = 'bitcoin'
    price = get_price(kurs)
    wzrost = int(price[1])
    
    if price != last_price:
      print(kurs +' price: ',price)
      
      last_price = price
      if wzrost == int(environ['wzrost']):
        print("kupuje wariacie")
        hook.send('WZROST !!!', price)
    elif wzrost == int(environ['spadek']):
        print("Cenka spada")
        hook.send("Spadek !!", price)
    
    time.sleep(3) 
    
main()