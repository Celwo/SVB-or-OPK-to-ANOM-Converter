import os
import re

def main():
    folder = "configs"
    for count, filename in enumerate(os.listdir(folder)):
        string = f"{filename}"
        string = re.sub("\.svb|\.opk",".anom",string)
        dst = f"{string}"
        src =f"{folder}/{filename}"
        dst =f"{folder}/{dst}"
        
        os.rename(src, dst)
print(f"""
 ▄████▄   ▒█████   ███▄    █ ██▒   █▓▓█████  ██▀███  ▄▄▄█████▓▓█████ ▓█████▄     ▐██▌ 
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌    ▐██▌ 
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▓██  █▒░▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░▒███   ░██   █▌    ▐██▌ 
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒ ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌    ▓██▒ 
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░  ▒▀█░  ░▒████▒░██▓ ▒██▒  ▒██▒ ░ ░▒████▒░▒████▓     ▒▄▄  
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒     ░▀▀▒ 
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░    ░     ░ ░  ░ ░ ▒  ▒     ░  ░ 
░        ░ ░ ░ ▒     ░   ░ ░     ░░     ░     ░░   ░   ░         ░    ░ ░  ░        ░ 
░ ░          ░ ░           ░      ░     ░  ░   ░                 ░  ░   ░        ░    
░                                ░                                    ░               
              by Celwo
             flip-gen.fr  
""")

if __name__ == '__main__':
     
    # Calling main() function
    main()