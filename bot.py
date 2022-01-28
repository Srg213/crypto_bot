# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time


file = open('symbols.json', 'r')
symbols = json.load(file)
print(symbols)

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        msg = turn_context.activity.text
        print(type(msg),msg,msg[0],msg.split())
        if msg[0] == 'S' or msg[0] == 'R':
            msg= msg.split()    
            print(msg)
            trigger = msg[2]
            symbol = msg[1]
            state = msg[0]
            print(type(symbol))
            print(trigger)

            if symbol not in symbols.values():
                await turn_context.send_activity(f"The symbol is not correct. Please type the correct symbol.")

            times = 1
            while(1):
                if times > 1: 
                    time.sleep(10)
                else:
                    await turn_context.send_activity(f"The trigger price is {trigger}. You have created a {state} request.")
                    if state == 'SET':
                        await turn_context.send_activity(f"You will be notified when price is below the trigger.")
                    elif state == 'REM':
                        await turn_context.send_activity(f"You will be notified when price is above the trigger.")

                url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
                parameters = {
                'symbol': symbol,
                'convert':'INR'
                }
                headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': 'af2d5d3d-89a1-43c9-815e-d6b66a07fc0f',
                }

               
                session = Session()
                session.headers.update(headers)

                try:
                    response = session.get(url, params=parameters)
                    data = json.loads(response.text)
                    a = data['data'][symbol]['quote']['INR']['price']
                    print(a)
                except:
                    await turn_context.send_activity(f"The symbol is not correct. Please type the correct symbol.")
                    break 

                times +=1
                if state == 'SET':
                    if float(trigger) > a: 
                        continue
                    else:
                        await turn_context.send_activity(f"Price of {symbol} is now {a}. The trigger price was {trigger}.")
                        break
                elif state == 'REM' :
                    if float(trigger) < a:
                        continue
                    else:
                        await turn_context.send_activity(f"Price of {symbol} is now {a}. The trigger price was {trigger}. ")
                        break

        elif msg in symbols.values(): 
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            parameters = {
            'symbol': turn_context.activity.text,
            'convert':'INR'
            }
            headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'af2d5d3d-89a1-43c9-815e-d6b66a07fc0f',
            }

            session = Session()
            session.headers.update(headers)

            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
                a = data['data'][turn_context.activity.text]['quote']['INR']['price']
                print(data)
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)
            
            await turn_context.send_activity(f"Price of {turn_context.activity.text} is {a} ")

        else:
            await turn_context.send_activity(f"The symbol is not correct. Please type the correct symbol.")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("""
                Hello and welcome!.
                This is a crytocurrency notification bot. 
                You can check the current price and also use it to set a target price for an alert.
                This bot will notify the user when the current price is
                1. more than the alert price(use 'SET 'keyword) or 
                2. when the price is lower than the trigger price(use 'REM' keyword)  """)

                await turn_context.send_activity("Please type a symbol to get started like BTC or ETH.")