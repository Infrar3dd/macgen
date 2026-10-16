import os
import random
import argparse
  
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MACgen= changes your device\'s MAC-address')
    parser.add_argument('-d','--device', help='wifi device name')
    args = parser.parse_args()
    addr = ("%02x:%02x:%02x:%02x:%02x:%02x:"%(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))).upper()
    try:
        if (';' in args.device) or ('|' in args.device) or ('&' in args.device):
            print("Something went wrong :(")
        else:
            os.system(f"sudo ifconfig {args.device} down")
            os.system(f"sudo ifconfig {args.device} hw ether {addr}")
            os.system(f"sudo ifconfig {args.device} up")
            print(f"Now your MAC is: {addr}")
    except:
    	print("Something went wrong :(")
