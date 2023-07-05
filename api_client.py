'''
Requests the server to generate text based on the input text, structured 
in a sort of chatbot format. The server is simply generating text, so you can feel free to modify
the client to be whatever you want, it doesn't have to be a chatbot. 
'''

import requests
import json
import colorama


SERVER_IP = "10.0.0.10" # replace with local or public IP of your server.
URL = f"http://{SERVER_IP}:5000/generate"

USERTOKEN = "USER:\n"
ENDTOKEN = "<|endoftext|>"
ASSISTANTTOKEN = "\nASSISTANT:\n"

def prompt(inp):
    data = {"text": inp}
    headers = {'Content-type': 'application/json'}

    response = requests.post(URL, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()["generated_text"]
    else:
        return "Error:", response.status_code
    

history = ""
while True:
    inp = input(">>> ")
    context = history + USERTOKEN + inp + ASSISTANTTOKEN
    output = prompt(context)
    history = output+'\n'
    # print yellow history if debugging
    #print(colorama.Fore.YELLOW + history + colorama.Style.RESET_ALL)
    just_latest_asst_output = output.split(context)[1].split(USERTOKEN)[0]
    # color just_latest_asst_output green in print:
    print(colorama.Fore.GREEN + just_latest_asst_output + colorama.Style.RESET_ALL)
