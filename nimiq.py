from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyrogram import Client,filters,idle
import time
import os
import asyncio
from threading import Thread
token = "5223306497:AAGeQqzgRnCgBb0wRA_io4_wn2ENmFQ4stk"

bot = Client("Bot", 3479778, "e61d50b4ab56775b5589a079ebf86522", bot_token = token)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
url = "https://nimiq.watch/"
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options = chrome_options)
r = driver.get(url)
time.sleep(3)
lastest = "2050137"

with bot:
  bot.send_message("coinmadeni", "__Bot Aktif!!__")
while True:
  try:
    lastess = driver.find_element_by_xpath('//*[@id="blocklist"]/div[1]')
    if str(lastess.text.split("#")[1].split(" ")[0]) != lastest:
      if lastess.text.split("found by ")[1].split(" ")[0] == "ACEMINING":
        ids = str(lastess.text.split("#")[1].split(" ")[0])
        times = str(lastess.text.split(ids + " ")[1].split(" min")[0])
        transactions = str(lastess.text.split("min ")[1].split(" transactions")[0])
        size = str(lastess.text.split(" KB")[0].split(" ")[1])
        with bot:
          msg = f"""
**Blok Bulundu!!**
  **ACEMINING.CO**
      **ID:** #{ids}
      **Time:** {times} Dakika Önce.
      **Transactions:** {transactions} Transaction
      **Size:** {size} KB
"""
          bot.send_message("coinmadeni", msg)
        lastest = lastess.text.split("#")[1].split(" ")[0]
  except:
    pass

