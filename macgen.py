import os
import random
import argparse
  
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MACgen= changes your device\'s MAC-address')
    parser.add_argument('-d','--device', help='Device name')
    args = parser.parse_args()
    addr = ("%02x:%02x:%02x:%02x:%02x:%02x:"%(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))).upper()
    try:
        os.system(f"sudo ifconfig {args.device} down")
        os.system(f"sudo ifconfig {args.device} hw ether {addr}")
        os.system(f"sudo ifconfig {args.device} up")
        print(f"Now your MAC is: {addr}")
    except:
    	print("Something went wrong :(")
