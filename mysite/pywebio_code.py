from pywebio import input
from pywebio import output
import random
from pywebio.session import download
import time
try: 
    with open ('RPbuilersMODS.zip', 'rb') as fp:
      mods = fp.read()
except Exception as ex:
    pass
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
  output.put_button('Скачать тестовый файл', lambda: download(f'{random.randint(0, 9999999999)}.txt', content))

def MSM():
  output.put_button('Скачать архив с модами', lambda: download(f'MineScaleModsFabric.zip', mods))