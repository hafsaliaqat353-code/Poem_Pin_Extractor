import pyfiglet
import sys
import time

from colorama import init, Fore, Style
init()

 # for typewriter effect
def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    print()

 # for fake progress bar
def fake_progress():
    print(Fore.GREEN + "Decrypting secret code...", end="")
    for i in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()

 # for pin extraction logic
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes        


header = pyfiglet.figlet_format("CLASSIFIED", font="doom")
print(Fore.RED + header)    
typewriter(Fore.BLUE +"Every poem hides a secret.")
typewriter(Fore.BLUE +"Most people just don't know how to read them...")
typewriter("")
typewriter(Fore.BLUE +"Leave your poem below")
typewriter(Fore.BLUE +"I will reveal what is hidden inside...")
typewriter("")  
typewriter(Fore.BLUE + "Share your poem. One line at a time. Write 'seal' when finished.")
typewriter("")
print(Fore.WHITE, end="")
lines = []
while True:
    line = input()
    if line.lower() == "seal":
        typewriter("")
        typewriter(Fore.RED + '[SEALED]')
        typewriter("")
        break
    lines.append(line)
poem = "\n".join(lines)
pins = pin_extractor([poem])
fake_progress()
typewriter("")
typewriter(Fore.GREEN +"Access Granted!")
typewriter("")

typewriter(Fore.YELLOW +"The secret code is: "  + str(pins[0]))
print(Style.RESET_ALL)  # reset back to normal color
