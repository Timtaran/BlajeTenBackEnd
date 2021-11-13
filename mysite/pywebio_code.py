from pywebio import input
from pywebio import output
import random
from pywebio.session import download
import time

def bmi():
  output.toast('Пожалуйста подождите 5 секунд...', duration=5, color='green')
  time.sleep(5)
  try: 
    with open ('__foo.ob', 'rb') as fp:
      content = fp.read()
  except IOError:
    with open('__foo.ob', 'w', encoding="UTF-8") as fp:
      content = 'Привет, это тестовый файл для скачивания.'
      fp.write(content)
  except Exception as ex:
    output.put_text(ex)
  output.put_button('Скачать файл', lambda: download(f'{random.randint(0, 9999999999)}.txt', content))