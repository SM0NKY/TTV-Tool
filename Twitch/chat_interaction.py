import asyncio as asy
from twitchio.ext import commands as ttc
from typing import List, Dict, Optional, Any
import json, os
from pathlib import Path

TTV_CHANNEL:str = "" # <- Here you write your twitch channel, you can copy and paste it Ex. "SM0NKY_"
Token:str = "" # <- You can check your token on this page https://twitchtokengenerator.com/ Ex. "dhj28hih1218y89dui29d29y3jkdf9" (30 digits)

class Viewer_Counter(ttc.Bot):
    def __init__(self) -> object:
        super().__init__(token= Token, prefix='!', initial_channels=[TTV_CHANNEL.lower()])
    
    async def event_ready(self) -> None:
        """ This method checks if the bot is ready

        Parameters
        ----------
        `None`

        Return
        ----------
        `None`
        """
        
        print(f"The bot is ready, connected as {self.nick}")

    async def event_join(self, channel, user) -> None:
        """ Checks if there is new people on the chatstream 
        Parameters
        ----------
        `None`

        Return 
        ----------
        `None`
        """

        
        print(f"There is a new user,{user.name}")
        await self.check_for_names(channel, user.name)

    async def event_message(self, message) -> None:
        """ This method, checks for any messages in the chat, and it does something specific (not defined yet)
        Parameters
        ----------
        `None`

        Return 
        ----------
        `None`

        """
        if message.echo:
            return
            #await self.handle_commands(message)
        else:
            #print(f"{message.author.name}:",message.content)
            return

    async def check_for_names(self,channel, username:str) -> Optional[bool]:
        """ This method checks for any new user in the chat and sends a welcome message
        Parameters
        ----------
        `None`

        Return
        ---------
        `Optional[bool]`
        
        """



        dir = os.path.join(Path(__file__).parent,"users.json")
        
        try:
            with open(dir,'r') as file:
                usuarios:json.load|List[str] = json.load(file)
                
                if username in usuarios:
                    print("There is an old viewer")
                    return False
                
                elif not(username in usuarios):
                    print("There is a new viewer")
                    usuarios.append(username)
                    with open(dir,'w') as file_output:
                        json.dump(usuarios,file_output,indent=4)
                    print(f"Hello, {username}")  
                    
                    await channel.send(f"Willkommen @{username}! 😎🥳 ")
                    return True
                
        except FileNotFoundError:
            with open(dir,'w') as file:
                json.dump([username],file,indent=4)   
            print(f"The file was not found, it was created a correspondent file, it was added {username}")
            await channel.send(f"Willkommen @{username}! 😎🥳")
            return True
        
async def main_func():
    bot:object|Viewer_Counter = Viewer_Counter()
    await bot.start()

def prueba() -> None:
    print("Si")
    
if __name__ == "__main__":
    asy.run(main_func())