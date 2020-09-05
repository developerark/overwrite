import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="Number of times to overwrite")

args = parser.parse_args()

try:
    for i in range(0, args.n):
        SIZE = 3 * 1024 * 1024 * 1024 # GB
        print("[+] Starting to write...")
        print("[+] Iteration: {}".format(i + 1))
        if os.path.exists(".temp"):
            os.remove(".temp")
            pass

        while SIZE > 0:
            print("[+] Writing {} B".format(SIZE))
            content = "a" * SIZE
            try:
                with open(".temp", 'a') as file:
                    file.write(content)
            except Exception as error:
                print("[-] {}".format(str(error)))
                SIZE = int(SIZE / 2)
except KeyboardInterrupt as error:
    print("Terminating...")