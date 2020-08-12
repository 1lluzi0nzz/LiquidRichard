import discord
import random
import BJ
import DND
import Scenario
from Player import Player
import sys
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(["League of Legends", "Factorio", "Joe Mama", "Stronghold Crusader HD", "Appearing Offline"])

@client.event
async def on_ready():
    change_status.start()
    print("Bot Started...")   

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def wor(ctx, amount=1):
    quotes = ['WEBBY FUCKING LEAVE DUDE!','Look at how shit that guy in the corner is..','Man fuck you WingsMemes all you do is spend your time like photoshopping me standing next to pepsi machines.  Thats what you do with your life.  Get banned.','I was so happy 3 years ago. 3 years ago I didnt have the whole world against me.','Just because youre overweight doesnt mean youre in bad health. I was in perfect health at 500 pounds...other than being massively overweight.','Like, I had a guy that would pretend to be Willy Wonka and tell every girl on my Facebook that I called them fat on stream. Trolls fuck with me HARD.','How the flying fuck does a submachine gun beat the BAR?!','Would I suck Bernie Sanders nipple for free healthcare? Yes. Yes I would.','My day is shit, its gonna be shit tomorrow, its gonna be shit after that, its gonna be shit after that.','COME ON!!! FUCK YOU LION!','Why would you wish me a happy Thanksgiving? as far as i know youre not even american..\nso why would you say that? \nmatter of fact, im just gonna ban you.', 'Dont come in here asking me how my day is, I dont care about that.','Id beat you with a fucking pistol grip until your teeth fell out your head.','Uhm...Im banning anyone trying to give me advice. Real talk.','Im not camping. Im holding an angle.','I handle people in real life much better than I handle with people on the internet. Because people in real life dont sit here and make fun of you all day for 6 or 7 months in a row. And if they DO sit there and make fun of you, guess what? You can slap them in the mouth. I aint got no bitch in my blood. I got zero bitch in my blood. Zero.','I dont give a FUCK if I finish one game or not, please just leave me alone! Just leave me alone.','Yeah whatever, I hope your family dies in an automobile wreck.','Im pretty much worthless sexually at this point.','Man, itd be fucking awesome to have a big ass thick burger with fucking bacon on it. Mothafucka. Big old melted pieces of cheese, two patties, fucking some lettuce, get some fucking fries, season that right, dip that shit in ketchup.','How many times a day do I masturbate? Does a half a time a day count?','I currently have 7 or 8000 thousand people banned.','WHERE THE FUCK IS MY HELP? WHERES ASH?','Yeah keep fuckin laughing you fuckin faggot.','The way my body is shaped, I dont have trouble having doggy style sex, what I do is I pick my stomach up and put it on their lower back.','My grandma stuck her finger up my butt and mashed the turd up.','No, Ive ever drunk milk so fresh it felt like someone jizzed in my mouth.','FatTitsofLardation, thank you for the dollar sixty-nine donation.','Appearing offline doesnt work Im fucking offline.','LOOK HERE! LOOK LISTEN! Appearing offline does not fucking stop it. So stop giving advice you know nothing about.','Use the LMG class kill yoself.','Dude shut the fuck up dude youre a little kid.','Jokes on them, if they join one more time, Im going back online...and Im stacking a team up.','Liquid Richard is like the generic knock off of a Rolex watch.','Im literally miserable, I cant sleep. I vomited twice yesterday just from fuckin up my subcount.','Oh dude Im delet - nooo dude, noo - you, nah Im out, you gone dude. Fuck that nigga. Oh mah lord, I hate him, I HATE HIM!','Walmart currently has Diet Pepsi on sale.', 'This is the last hoorah. If I fail this, I die...I die in a bed alone.', 'Dont pick him up, DONT PICK HIM UP! Thats it, youve just lost your friend slot.']
    await ctx.channel.purge(limit=amount)
    await ctx.send(random.choice(quotes))

@client.command()
async def gold(ctx, amount=1):
    quotes = ['God it must be a burden for any woman to want to have sex with you. I can see you at work now just sitting there trying to help some old mexican lady like "DURH I WORK AT A BANK" with a tie tied with a fuckin bobby pin.  Then the thing just fuckin unravvels and hits the tip of your dick.  Then the lady asks if everythings alright and your like "HOLD ON IM ABOUT TO CUM."', 'Yeah Ill get you some shoes but first you gotta help me out here dude', 'Im guessing the guy didnt expect Sony to come over and rush him. Then when they figured out the game wasnt fucking ready, just leave him to foot the bill.']
    await ctx.channel.purge(limit=amount)
    await ctx.send(random.choice(quotes))

@client.command()
async def shen(ctx, amount=1):
    quotes = ['Man Im so drunk right now', 'PLEASE!', 'I MISSED THE FUCKING CANNON', 'MY INTERNET I LITERALLY CANT PLAY LIKE THIS', 'Im like not that great but I still got to gold off macro.', 'Those stats cant be right', 'Fuck man im playin like shit']
    await ctx.channel.purge(limit=amount)
    await ctx.send(random.choice(quotes))

@client.command()
async def coinflip(ctx):
    out = ['HEADS', 'TAILS']
    await ctx.send(f'{ctx.author.name} flipped {random.choice(out)}')

@client.command()
async def diceroll(ctx):
    out = ['1','2','3','4','5','6']
    await ctx.send(f'{ctx.author.name} rolled a {random.choice(out)}')

@client.command()
async def bjack(ctx, command=""):
    if sum(BJ.player_cards) > 21:
        await ctx.send(f'{ctx.author.name} BUSTED! Liquid Richard wins.')
        BJ.player_cards = []
        BJ.dealer_cards = []
    elif sum(BJ.player_cards) == 21:
        await ctx.send(f'{ctx.author.name} has BLACKJACK!')
        BJ.player_cards = []
        BJ.dealer_cards = []
    elif(command == "start"):
        BJ.dealCards()
        await ctx.send(f'Starting a Game of BlackJack for: {ctx.author.name}\nLiquid Richard has __ & {BJ.dealer_cards[1]} \n{ctx.author.name} you have {BJ.player_cards}\n{ctx.author.name} do you want to stay or hit?')
    elif(command == "hit"):
        if sum(BJ.player_cards) > 21:
            await ctx.send(f'{ctx.author.name} BUSTED! Liquid Richard wins.')
            BJ.player_cards = []
            BJ.dealer_cards = []
        else:
            BJ.hit()
            await ctx.send(f'{ctx.author.name} you have {BJ.player_cards}')
            if sum(BJ.player_cards) > 21:
                await ctx.send(f'{ctx.author.name} BUSTED! Liquid Richard wins.')
                BJ.player_cards = []
                BJ.dealer_cards = []
            else:
                await ctx.send(f'You now have a total of {str(sum(BJ.player_cards))} from these cards {BJ.player_cards}\n{ctx.author.name} do you want to stay or hit?')
    elif(command == "stay"):
        BJ.stay()
        await ctx.send(f'Liquid Richard has a total of {str(sum(BJ.dealer_cards))} with {BJ.dealer_cards}\n{ctx.author.name}, you have a total of {str(sum(BJ.player_cards))} with, {BJ.player_cards}')
        if (sum(BJ.dealer_cards) > sum(BJ.player_cards)) and ((sum(BJ.dealer_cards) < 22)):
            await ctx.send("Liquid Richard wins!")
            BJ.player_cards = []
            BJ.dealer_cards = []
        else:
            await ctx.send(f'{ctx.author.name} wins!')
            BJ.player_cards = []
            BJ.dealer_cards = []

@client.command()
async def dnddebugchar(ctx, index=0):
    await ctx.send(f'Name: {DND.players[index].name}:\nStrength: {DND.players[index].strength}\nDexterity: {DND.players[index].dexterity}\nConstitution: {DND.players[index].constitution}\nIntelligence: {DND.players[index].intelligence}\nCharisma: {DND.players[index].charisma}\nRace: {DND.players[index].race}\nClass: {DND.players[index].charClass}\nStarting Item: {DND.players[index].item}\nHealth: {DND.players[index].health}\nGold: {DND.players[index].gold}\nInventory: {DND.players[index].inventory}')

@client.command()
async def dndrm(ctx, index=0):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Removed {DND.players[int(index)]}\n')
    DND.players.pop(index)
    await ctx.send(f'Current Players: {DND.players}')

@client.command()
async def dndadd(ctx, name, strength, dexterity, constitution, intelligence, charisma, race, charClass, item):
    newPlayer = Player(name, strength, dexterity, constitution, intelligence, charisma, race, charClass, item)
    if(Player.isValid(newPlayer)):
        DND.players.append(newPlayer)
    await ctx.send(f'CHARACTER CREATED - {newPlayer.name}:\nStrength: {newPlayer.strength}\nDexterity: {newPlayer.dexterity}\nConstitution: {newPlayer.constitution}\nIntelligence: {newPlayer.intelligence}\nCharisma: {newPlayer.charisma}\nRace: {newPlayer.race}\nClass: {newPlayer.charClass}\nItem: {newPlayer.item}\n\nCurrent Players: {DND.players}')

#Handles Speech Event
@client.command()
async def dndspeech(ctx, option=0):
    Scenario.response = option
    await ctx.send(Scenario.loadEvent1(Scenario.currentStatus, option))
    await ctx.send(f'{DND.players[DND.cycleCurrentPlayer(DND.currentPlayer)].name} Turn:')
    

#Start an Event or start next event
@client.command()
async def dndstart(ctx, scenario=1, event=Scenario.currentEvent):
    partyString = ""
    for p in DND.players:
        partyString += f'{p.name} is a {p.race} {p.charClass} starting with {p.health} health and an inventory of {p.inventory}\n'
    await ctx.send(f'Current Party | Current Event: {Scenario.currentEvent}\n\n{partyString}\n\n\n')
    if(scenario == 1):
        if(Scenario.currentEvent == 1):
            await ctx.send(f'SPEECH EVENT\n {Scenario.event1Intro}\n{DND.players[DND.currentPlayer].name} Turn:')
        elif(Scenario.currentEvent == 2):
            await ctx.send(f'SPEECH EVENT\n {Scenario.event2Intro}\n{DND.players[DND.currentPlayer].name} Turn:')

#Makes a random combat scenario
@client.command()        
async def dndrand(ctx):
    DND.enemyParty = []
    DND.generateEnemyParty()
    ePartyString = ""
    for e in DND.enemyParty:
        ePartyString += f'{e.name} is a {e.type} with {e.HP} health and holding {e.weapon}\n'
    await ctx.send(f'Enemy Party:\n\n{ePartyString}\n\n\n')
    # Party Enters the Event
    # Player picks weapon AND target[index]
    # Chance to hit = d20 + weapon modifier
    # If chance to hit >= Enemy AC then HIT
    # Damage is a d6 roll
    # Subtract d6 from enemy 

@client.command()
async def dndreset(ctx):
    DND.players = []
    DND.currentPlayer = 0
    DND.downedPlayers = []
    DND.turn = 0
    Scenario.currentStatus = 0
    Scenario.currentEvent = 1
    Scenario.response = 0
    Scenario.message = ""
    Scenario.result = ""
    await ctx.send("Game has been reset, ready for new round.")

@client.command()
async def byenigga(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f'{ctx.author} task killed Richard')
    sys.exit()

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear5(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#AUDIO PLAYER
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command(pass_context=True)
async def leave(ctx):
  await ctx.voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await ctx.channel.purge(limit=1)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

client.run("NDQ1MzQ2Mzc1NzkwNzU1ODQx.XxfMhw.RYU3j0Vp2cYkzo8mLgFlbMR2gRM")