#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from Axel import Krazy

__CHANNEL_USERNAME__ = "AxelToolChannel"
__GROUP_USERNAME__   = "AxelToolChat"

def signal_handler(sig, frame):
    print("\n Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ɢᴏᴏᴅʙʏᴇᴇ.")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')    
    
    brand_name =  " _____               _   _____               _   \n"
    brand_name += "(  _  )             (_ )(_   _)            ( _ ) \n"
    brand_name += "| (_) |         __   | |  | |   _      _    | | \n"
    brand_name += "|  _  |(`\/') /'__`\ | |  | | /'_`\  /'_`\  | | \n"
    brand_name += "| | | | >  < (  ___/ | |  | |( (_) )( (_) ) | | \n"
    brand_name += "(_) (_)(_/\_)`\____)(___) (_)`\___/'`\___/'(___)\n"
    brand_name += "\n"
    brand_name += "- [ Powered By CyloPlays ]\n"
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         Kɪɴᴅʟʏ ʟᴏɢᴏᴜᴛ ʏᴏᴜʀ ᴄᴘᴍ ғɪʀsᴛ ʙᴇғᴏʀᴇ ᴜsɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ'))
    print(Colorate.Horizontal(Colors.rainbow, '    Sʜᴀʀɪɴɢ ʏᴏᴜʀ ᴀᴄᴄᴇss ᴋᴇʏ ɪs ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴀɴᴅ ᴍᴀʏ ʙᴇ ʙʟᴏᴄᴋᴇᴅ.'))
    print(Colorate.Horizontal(Colors.rainbow, f' ‌           Tᴇʟᴇɢʀᴀᴍ: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.rainbow, '==========[ Pʟᴀʏᴇʀ Dᴇᴛᴀɪʟs ]=========='))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Nᴀᴍᴇ     : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.rainbow, f'Lᴏᴄᴀʟ ID : {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Mᴏɴᴇʏ    : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.rainbow, f'Cᴏɪɴs    : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'Eʀʀᴏʀ: ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛs ᴍᴜsᴛ ʙᴇ sɪɢɴᴇᴅ-ɪɴ ᴛᴏ ᴛʜᴇ ɢᴀᴍᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴄᴇ.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, 'Eʀʀᴏʀ: sᴇᴇᴍs ʟɪᴋᴇ ʏᴏᴜʀ ʟᴏɢɪɴ ɪs ɴᴏᴛ ᴘʀᴏᴘᴇʀʟʏ sᴇᴛ.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.rainbow, '========[ Aᴄᴄᴇss Kᴇʏ Dᴇᴛᴀɪʟs ]========'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Aᴄᴄᴇss Kᴇʏ : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Tᴇʟᴇɢʀᴀᴍ ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.rainbow, f'Bᴀʟᴀɴᴄᴇ $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} Cᴀɴɴᴏᴛ ʙᴇ ᴇᴍᴘᴛʏ ᴏʀ ᴊᴜsᴛ sᴘᴀᴄᴇs, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.rainbow, '=============[ Lᴏᴄᴀᴛɪᴏɴ Dᴇᴛᴀɪʟs ]============='))
    print(Colorate.Horizontal(Colors.rainbow, f'IP Aᴅᴅʀᴇss : {data.get("query")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Lᴏᴄᴀᴛɪᴏɴ   : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
    print(Colorate.Horizontal(Colors.rainbow, f'Cᴏᴜɴᴛʀʏ    : {data.get("country")} {data.get("zip")}.'))
    print(Colorate.Horizontal(Colors.rainbow, '===============[ Axᴇʟ Tᴏᴏʟ Mᴇɴᴜ ]==============='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Aᴄᴄᴏᴜɴᴛ Eᴍᴀɪʟ: [/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Aᴄᴄᴏᴜɴᴛ Pᴀssᴡᴏʀᴅ: [/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Aᴄᴄᴇss Kᴇʏ:[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Tʀʏɪɴɢ ᴛᴏ ʟᴏɢ ɪɴ ᴛᴏ ᴛʜᴇ ɢɪᴠᴇɴ ᴀᴄᴄᴏᴜɴᴛ.[/bold cyan]: ", end=None)
        cpm = Krazy(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'Eʀʀᴏʀ: Aᴄᴄᴏᴜɴᴛ Nᴏᴛ Fᴏᴜɴᴅ.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'Eʀʀᴏʀ: Wʀᴏɴɢ Pᴀssᴡᴏʀᴅ.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'Eʀʀᴏʀ: Iɴᴠᴀʟɪᴅ Aᴄᴄᴇss Kᴇʏ.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ Tʀʏ Aɢᴀɪɴ.'))
                print(Colorate.Horizontal(Colors.rainbow, 'Nᴏᴛᴇ: ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ғɪʟʟᴇᴅ ᴏᴜᴛ ᴛʜᴇ ғɪᴇʟᴅ.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'Sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴏɢɪɴ.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40"]
            print(Colorate.Horizontal(Colors.rainbow, '{01}: Iɴᴄʀᴇᴀsᴇ Mᴏɴᴇʏ           1.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{02}: Iɴᴄʀᴇᴀsᴇ Cᴏɪɴs           4.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{03}: Kɪɴɢ Rᴀɴᴋ                8K'))
            print(Colorate.Horizontal(Colors.rainbow, '{04}: Cʜᴀɴɢᴇ ID                4.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{05}: Cʜᴀɴɢᴇ Nᴀᴍᴇ              100'))
            print(Colorate.Horizontal(Colors.rainbow, '{06}: Cʜᴀɴɢᴇ Nᴀᴍᴇ (Rᴀɪɴʙᴏᴡ)    100'))
            print(Colorate.Horizontal(Colors.rainbow, '{07}: Nᴜᴍʙᴇʀ Pʟᴀᴛᴇs            2K'))
            print(Colorate.Horizontal(Colors.rainbow, '{08}: Aᴄᴄᴏᴜɴᴛ Dᴇʟᴇᴛᴇ           FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{09}: Aᴄᴄᴏᴜɴᴛ Rᴇɢɪsᴛᴇʀ         FREE'))
            print(Colorate.Horizontal(Colors.rainbow, '{10}: Dᴇʟᴇᴛᴇ Fʀɪᴇɴᴅs           500'))
            print(Colorate.Horizontal(Colors.rainbow, '{11}: Uɴʟᴏᴄᴋ Pᴀɪᴅ Cᴀʀs         5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{12}: Uɴʟᴏᴄᴋ ᴀʟʟ Cᴀʀs          6K'))
            print(Colorate.Horizontal(Colors.rainbow, '{13}: Uɴʟᴏᴄᴋ ᴀʟʟ Cᴀʀs Sɪʀᴇɴ    3.5K'))
            print(Colorate.Horizontal(Colors.rainbow, '{14}: Uɴʟᴏᴄᴋ ᴡ16 Eɴɢɪɴᴇ        4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{15}: Uɴʟᴏᴄᴋ Aʟʟ Hᴏʀɴs         3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{16}: Uɴʟᴏᴄᴋ Dɪsᴀʙʟᴇ Dᴀᴍᴀɢᴇ    3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{17}: Uɴʟᴏᴄᴋ Uɴʟɪᴍɪᴛᴇᴅ Fᴜᴇʟ    3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{18}: Uɴʟᴏᴄᴋ Hᴏᴜsᴇ 3           4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{19}: Uɴʟᴏᴄᴋ Sᴍᴏᴋᴇ             4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{20}: Uɴʟᴏᴄᴋ Wʜᴇᴇʟs            4K'))
            print(Colorate.Horizontal(Colors.rainbow, '{21}: Uɴʟᴏᴄᴋ Aɴɪᴍᴀᴛɪᴏɴs        2K'))
            print(Colorate.Horizontal(Colors.rainbow, '{22}: Uɴʟᴏᴄᴋ Eᴏ̨ᴜɪᴘᴀᴍᴇɴᴛs M     3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{23}: Uɴʟᴏᴄᴋ Eᴏ̨ᴜɪᴘᴀᴍᴇɴᴛs F     3K'))
            print(Colorate.Horizontal(Colors.rainbow, '{24}: Cʜᴀɴɢᴇ Rᴀᴄᴇ Wɪɴs         1K'))
            print(Colorate.Horizontal(Colors.rainbow, '{25}: Cʜᴀɴɢᴇ Rᴀᴄᴇ Lᴏsᴇs        1K'))
            print(Colorate.Horizontal(Colors.rainbow, '{26}: Cʟᴏɴᴇ Aᴄᴄᴏᴜɴᴛ            7K'))
            print(Colorate.Horizontal(Colors.rainbow, '{27}: Aᴜᴛᴏ Iɴɴᴇʀ 414ʜᴘ         2.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{28}: Cᴜsᴛᴏᴍ Aɴɢʟᴇ             1.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{29}: Cᴜsᴛᴏᴍ ᴛɪʀᴇ ʙᴜʀɴᴇʀ       1.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{30}: Cᴜsᴛᴏᴍ ᴄᴀʀ ᴍɪʟʟᴀɢᴇ       1.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{31}: Cᴜsᴛᴏᴍ ᴄᴀʀ ʙʀᴀᴋᴇ         2k'))
            print(Colorate.Horizontal(Colors.rainbow, '{32}: Rᴇᴍᴏᴠᴇ ʀᴇᴀʀ ʙᴜᴍᴘᴇʀ       2k'))
            print(Colorate.Horizontal(Colors.rainbow, '{33}: Rᴇᴍᴏᴠᴇ ғʀᴏɴᴛ ʙᴜᴍᴘᴇʀ      2k'))
            print(Colorate.Horizontal(Colors.rainbow, '{34}: Cʜᴀɴɢᴇ ᴀᴄᴄᴏᴜɴᴛ ᴘᴀssᴡᴏʀᴅ  2k'))
            print(Colorate.Horizontal(Colors.rainbow, '{35}: Cʜᴀɴɢᴇ ᴀᴄᴄᴏᴜɴᴛ ᴇᴍᴀɪʟ     2k'))
            print(Colorate.Horizontal(Colors.rainbow, '{36}: Cᴜsᴛᴏᴍ sᴘᴏɪʟᴇʀ           10k'))
            print(Colorate.Horizontal(Colors.rainbow, '{37}: Cᴜsᴛᴏᴍ ʙᴏᴅʏᴋɪᴛ           10k'))
            print(Colorate.Horizontal(Colors.rainbow, '{38}: Uɴʟᴏᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴡʜᴇᴇʟs    4.5k'))
            print(Colorate.Horizontal(Colors.rainbow, '{39}: Uɴʟᴏᴄᴋ ᴛᴏʏᴏᴛᴀ ᴄʀᴏᴡɴ      2k'))
            print(Colorate.Horizontal(Colors.rainbow, '{40}: Cᴏᴘʏ ᴘʟᴀᴛᴇs              2k'))
            print(Colorate.Horizontal(Colors.rainbow, '{0} : Exɪᴛ'))
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] Sᴇʟᴇᴄᴛ ᴀ sᴇʀᴠɪᴄᴇ [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] Iɴsᴇʀᴛ ʜᴏᴡ ᴍᴜᴄʜ ᴍᴏɴᴇʏ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ.'))
                amount = IntPrompt.ask("[?] Aᴍᴏᴜɴᴛ")
                console.print("[%] Sᴀᴠɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much coins do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Sᴀᴠɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ: ", end=None)
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: ɪғ ᴛʜᴇ ᴋɪɴɢ ʀᴀɴᴋ ᴅᴏᴇsɴ'ᴛ ᴀᴘᴘᴇᴀʀ ɪɴ ɢᴀᴍᴇ, ᴄʟᴏsᴇ ɪᴛ ᴀɴᴅ ᴏᴘᴇɴ ғᴇᴡ ᴛɪᴍᴇs.", end=None)
                console.print("[bold red][!] Note:[/bold red]: ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ᴅᴏ Kɪɴɢ Rᴀɴᴋ ᴏɴ sᴀᴍᴇ ᴀᴄᴄᴏᴜɴᴛ ᴛᴡɪᴄᴇ.", end=None)
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] Eɴᴛᴇʀ ʏᴏᴜʀ ɴᴇᴡ ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Sᴀᴠɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] Eɴᴛᴇʀ ʏᴏᴜʀ ɴᴇᴡ Nᴀᴍᴇ.'))
                new_name = Prompt.ask("[?] Nᴀᴍᴇ")
                console.print("[%] Sᴀᴠɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] Eɴᴛᴇʀ ʏᴏᴜʀ ɴᴇᴡ Rᴀɪɴʙᴏᴡ Nᴀᴍᴇ.'))
                new_name = Prompt.ask("[?] Nᴀᴍᴇ")
                console.print("[%] Sᴀᴠɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Gɪᴠɪɴɢ ʏᴏᴜ ᴀ Nᴜᴍʙᴇʀ Pʟᴀᴛᴇs: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] Aғᴛᴇʀ ᴅᴇʟᴇᴛɪɴɢ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ, ᴛʜᴇʀᴇ ɪs ɴᴏ ᴡᴀʏ ᴛᴏ ʀᴇsᴛᴏʀᴇ ɪᴛ.'))
                answ = Prompt.ask("[?] Aʀᴇ ʏᴏᴜ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴀᴄᴄᴏᴜɴᴛ ?", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] Rᴇɢɪsᴛʀɪɴɢ ɴᴇᴡ Aᴄᴄᴏᴜɴᴛ.'))
                acc2_email = prompt_valid_value("[?] Aᴄᴄᴏᴜɴᴛ Eᴍᴀɪʟ: ", "Email", password=False)
                acc2_password = prompt_valid_value("[?] Aᴄᴄᴏᴜɴᴛ Pᴀssᴡᴏʀᴅ: ", "Password", password=False)
                console.print("[%] Cʀᴇᴀᴛɪɴɢ ɴᴇᴡ Aᴄᴄᴏᴜɴᴛ: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'INFO: Iɴ ᴏʀᴅᴇʀ ᴛᴏ ᴛᴡᴇᴀᴋ ᴛʜɪs ᴀᴄᴄᴏᴜɴᴛ ᴡɪᴛʜ Axᴇʟ'))
                    print(Colorate.Horizontal(Colors.rainbow, 'ʏᴏᴜ ᴍᴜsᴛ sɪɢɴ-ɪɴ ғɪʀsᴛ ᴛᴏ ᴛʜᴇ ɢᴀᴍᴇ ᴜsɪɴɢ ᴛʜɪs ᴀᴄᴄᴏᴜɴᴛ.'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Tʜɪs ᴇᴍᴀɪʟ ɪs ᴀʟʀᴇᴀᴅʏ ᴇxɪsᴛs.'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Dᴇʟᴇᴛɪɴɢ ʏᴏᴜʀ Fʀɪᴇɴᴅs: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Nᴏᴛᴇ: ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ ᴛᴀᴋᴇs ᴀ ᴡʜɪʟᴇ ᴛᴏ ᴄᴏᴍᴘʟᴇᴛᴇ, ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ᴄᴀɴᴄᴇʟ.", end=None)
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Aʟʟ Pᴀɪᴅ Cᴀʀs: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Aʟʟ Cᴀʀs: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Aʟʟ Cᴀʀs Sɪʀᴇɴ: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ ᴡ16 Eɴɢɪɴᴇ: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Aʟʟ Hᴏʀɴs: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Dɪsᴀʙʟᴇ Dᴀᴍᴀɢᴇ: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Uɴʟɪᴍɪᴛᴇᴅ Fᴜᴇʟ: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Hᴏᴜsᴇ 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Sᴍᴏᴋᴇ: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 20: # Unlock Wheels
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Wʜᴇᴇʟs: ", end=None)
                if cpm.unlock_wheels():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 21: # Unlock Animations
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Aɴɪᴍᴀᴛɪᴏɴs: ", end=None)
                if cpm.unlock_animations():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 22: # Unlock Equipments
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Eᴏ̨ᴜɪᴘᴀᴍᴇɴᴛs Mᴀʟᴇ: ", end=None)
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] Uɴʟᴏᴄᴋɪɴɢ Eᴏ̨ᴜɪᴘᴀᴍᴇɴᴛs Fᴇᴍᴀʟᴇ: ", end=None)
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Iɴsᴇʀᴛ ʜᴏᴡ ᴍᴜᴄʜ ʀᴀᴄᴇs ʏᴏᴜ ᴡɪɴ.'))
                amount = IntPrompt.ask("[?] Aᴍᴏᴜɴᴛ")
                console.print("[%] Cʜᴀɴɢɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] Iɴsᴇʀᴛ ʜᴏᴡ ᴍᴜᴄʜ ʀᴀᴄᴇs ʏᴏᴜ ʟᴏsᴇ.'))
                amount = IntPrompt.ask("[?] Aᴍᴏᴜɴᴛ")
                console.print("[%] Cʜᴀɴɢɪɴɢ ʏᴏᴜʀ ᴅᴀᴛᴀ: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] Pʟᴇᴀsᴇ Eɴᴛᴇʀ Aᴄᴄᴏᴜɴᴛ Dᴇᴛᴀʟɪs.'))
                to_email = prompt_valid_value("[?] Aᴄᴄᴏᴜɴᴛ Eᴍᴀɪʟ: ", "Email", password=False)
                to_password = prompt_valid_value("[?] Aᴄᴄᴏᴜɴᴛ Pᴀssᴡᴏʀᴅ: ", "Password", password=False)
                console.print("[%] Cʟᴏɴɪɴɢ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                        
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 27:
                console.print("[bold yellow][!] Nᴏᴛᴇ[/bold yellow]: ᴏʀɪɢɪɴᴀʟ sᴘᴇᴇᴅ ᴄᴀɴ ɴᴏᴛ ʙᴇ ʀᴇsᴛᴏʀᴇᴅ!.")
                console.print("[bold cyan][!] Eɴᴛᴇʀ Cᴀʀ Dᴇᴛᴀɪʟs.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] Cᴀʀ ID: [/bold]")
                console.print("[bold cyan][%] Mᴀᴋɪɴɢ ʏᴏᴜʀ ᴄᴀʀ 414ʜᴘ ( ɪɴɴᴇʀ )[/bold cyan]:",end=None)
                if cpm.hack_car_speed(car_id):
                    console.print("[bold green]Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.[/bold green]")
                    console.print("================================")
                    answ = Prompt.ask("[?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ ᴀɴᴅ ᴛʀᴜsᴛɪɴɢ ᴏᴜʀ ᴛᴏᴏʟ, ᴋɪɴᴅʟʏ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Pʟᴇᴀsᴇ ᴜsᴇ ᴠᴀʟɪᴅ ᴠᴀʟᴜᴇs.'))
                    sleep(2)
                    continue
            elif service == 28: # ANGLE
                print(Colorate.Horizontal(Colors.rainbow, '[!] Eɴᴛᴇʀ Cᴀʀ Dᴇᴛᴀɪʟs.'))
                car_id = IntPrompt.ask("[red][?] Cᴀʀ ID: [/red]")
                print(Colorate.Horizontal(Colors.rainbow, '[!] Eɴᴛᴇʀ sᴛᴇᴇʀɪɴɢ ᴀɴɢʟᴇ'))
                custom = IntPrompt.ask("[red][?] Eɴᴛᴇʀ ᴀᴍᴏᴜɴᴛ ᴏғ ᴀɴɢʟᴇ ʏᴏᴜ ᴡᴀɴᴛ.[/red]")                
                console.print("[red][%] Cʜᴀɴɢɪɴɢ ʏᴏᴜʀ ᴄᴀʀ ᴀɴɢʟᴇ.[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    print(Colorate.Horizontal(Colors.rainbow, 'Dᴏɴᴇ, Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.'))
                    answ = Prompt.ask("[red][?] Dᴏ Yᴏᴜ ᴡᴀɴᴛ ᴛᴏ Exɪᴛ[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("Tʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴜsɪɴɢ Axᴇʟ Tᴇʀᴍᴜx Tᴏᴏʟ.")
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Fᴀɪʟᴇᴅ'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Pʟᴇᴀsᴇ Tʀʏ Aɢᴀɪɴ.'))
                    sleep(2)
                    continue  
            elif service == 29: # tire
                console.print("[bold yellow] '[!] ENTER CAR DETALIS[/bold yellow]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold yellow] '[!] ENTER PERCENTAGE[/bold yellow]")
                custom = IntPrompt.ask("[pink][?]﻿ENTER PERCENTAGE TIRES U WANT[/pink]")                
                console.print("[red][%] Setting Percentage [/red]: ", end=None)
                if cpm.max_max2(car_id, custom):
                    console.print("[bold yellow] 'SUCCESSFUL[/bold yellow]")
                    answ = Prompt.ask("[bold green][?] DO YOU WANT TO EXIT[/bold green] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 30: # Millage
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW MILLAGE![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTER MILLAGE U WANT[/bold blue]")                
                console.print("[bold red][%] Setting Percentage [/bold red]: ", end=None)
                if cpm.millage_car(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 31: # Brake
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER NEW BRAKE![/bold]")
                custom = IntPrompt.ask("[bold blue][?]﻿ENTER BRAKE U WANT[/bold blue]")                
                console.print("[bold red][%] Setting BRAKE [/bold red]: ", end=None)
                if cpm.brake_car(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 32: # Bumper rear
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")                
                console.print("[bold red][%] Removing Rear Bumper [/bold red]: ", end=None)
                if cpm.rear_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 33: # Bumper front
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")                
                console.print("[bold red][%] Removing Front Bumper [/bold red]: ", end=None)
                if cpm.front_bumper(car_id):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 75:  # /testin endpoint
                console.print("[bold]ENTER CUSTOM FLOAT DATA[/bold]")
                custom = IntPrompt.ask("[bold][?] VALUE (e.g. 1 or 0)[/bold]")     # This is the value
                console.print(f"[bold red][%] Setting float key... [/bold red]", end=None)
                if cpm.testin(custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold yellow]FAILED[/bold yellow]")
                    console.print("[bold yellow]PLEASE TRY AGAIN[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 34:
                console.print("[bold]Enter New Password![/bold]")
                new_password = prompt_valid_value("[bold][?] Account New Password[/bold]", "Password", password=False)
                console.print("[bold red][%] Changing Password [/bold red]: ", end=None)
                if cpm.change_password(new_password):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white]Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold yellow]FAILED[/bold yellow]")
                    console.print("[bold yellow]PLEASE TRY AGAIN[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 36: # telmunnongodz
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER SPOILER ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]ENTER NEW SPOILER ID[/bold blue]")                
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end=None)
                if cpm.telmunnongodz(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 37: # telmunnongonz
                console.print("[bold]ENTER CAR DETAILS![/bold]")
                car_id = IntPrompt.ask("[bold][?] CAR ID[/bold]")
                console.print("[bold]ENTER BODYKIT ID![/bold]")
                custom = IntPrompt.ask("[bold blue][?]INSERT BODYKIT ID[/bold blue]")                
                console.print("[bold red][%] SAVING YOUR DATA [/bold red]: ", end=None)
                if cpm.telmunnongonz(car_id, custom):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 35:
                console.print("[bold]Enter New Email![/bold]")
                new_email = prompt_valid_value("[bold][?] Account New Email[/bold]", "Email")
                console.print("[bold red][%] Changing Email [/bold red]: ", end=None)
                if cpm.change_email(new_email):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    answ = Prompt.ask("[bold][?] DO YOU WANT TO EXIT[/bold] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white]Thank You for using my tool[/bold white]")
                    else: break
                else:
                    console.print("[bold red]FAILED[/bold yellow]")
                    console.print("[bold red]EMAIL IS ALREADY REGISTERED [/bold red]")
                    sleep(4)
            elif service == 38: # SHITTIN
                console.print("[%] Unlocking Premium Wheels..: ", end=None)
                if cpm.shittin():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 39: # Unlock toyota crown
                console.print("[!] Note: this function takes a while to complete, please don't cancel.", end=None)
                console.print("[%] Unlocking Toyota Crown: ", end=None)
                if cpm.unlock_crown():
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("[bold white] Thank You for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please Try Again[/bold red]")
                    sleep(2)
                    continue
            elif service == 40:  # Clone only license plates between accounts
                console.print("[bold cyan]License Plate Cloner Activated[/bold cyan]")
                to_email = Prompt.ask("[bold][?] Target account email[/bold]")
                to_password = Prompt.ask("[bold][?] Target account password[/bold]", password=True)
                console.print("[bold red][%] Cloning license plates...[/bold red]")

                result = cpm.clone_plates_only(to_email, to_password)

                if result:
                    print(Colorate.Horizontal(Colors.rainbow, "✔ License plates successfully cloned"))
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                    console.print("[bold green]======================================[/bold green]")
                    answ = Prompt.ask("[?] Do you want to exit?", choices=["y", "n"], default="n")
                    if answ == "y":
                        console.print("[bold white]Thank you for using my tool[/bold white]")
                    else: continue
                else:
                    console.print("[bold red]FAILED[/bold red]")
                    console.print("[bold red]Please try again[/bold red]")
                    sleep(2)
            else: continue
            break
        break
            
        
            
              
