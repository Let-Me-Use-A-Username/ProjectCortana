# Packages

import discord
from discord.ext import commands
import random

# Games class
# Contains all the games and all the fun stuff


class Games(commands.Cog):
    ''' Games module, contains games such as magic 8 ball and dice roll. '''

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loading Cog: Games')
        print('========================')
        print('Game cog loaded successfully.\n')

    # Commands for 8ball game
    @commands.command(name='Cortana')
    async def eightball(self, ctx, *, question):
        ''' :Magic 8ball. You ask a question and Cortana answers based on 15 answers.
            Answers contain: 10 positive ones | 5 hazy ones | 5 negative ones.
            All of the answers are choses randomly using random module. '''
    # ===============================================
    
        answers = ['It is certain.', 'It is decidedly so.',
                   'Without a doupt.', 'Yes - definetely.',
                   'You may rely on it.', 'As I see it,yes.',
                   'Most likely.', 'Outlook good.',
                   'Yes.', 'Signs point to yes.','Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.', 'Cannot predict now.',
                    'Concentrate and ask again.',"Don't count on it.",
                    'My reply is no.',
                   'My sources say no.', 'Outlook not so good.',
                   'Very douptful.']
                   
    # ===============================================
    
        answer = random.choice(answers)
        await ctx.send(f'Question: {question}\nAnswer: {answer}')

    ''' Roll the dice '''
    @commands.command()
    async def dice(self, ctx, member1, member2):
        ''' :Rolls 2, 6-sided dice, for 2 member and displays victory.
            Member arguments can be tags of members or just member nicknames. '''
        dice_member1 = []
        dice_member2 = []
        dice_roll = ['1', '2', '3', '4', '5', '6']
        for index in range(2):
            dice_member1.extend(random.choice(dice_roll))
            dice_member2.extend(random.choice(dice_roll))
        await ctx.send(f'{member1} is rolling...\n {member1} rolled: {dice_member1[0]} and {dice_member1[1]}.')
        await ctx.send(f'{member2} is rolling...\n {member2} rolled: {dice_member2[0]} and {dice_member2[1]}.')
        sum1 = int(dice_member1[0]) + int(dice_member1[1])
        sum2 = int(dice_member2[0]) + int(dice_member2[1])
        if sum1 > sum2:
            await ctx.send(f'{member1} WON!.')
        elif sum1 < sum2:
            await ctx.send(f'{member2} WON!.')
        elif sum1 == sum2:
            await ctx.send("That's a draw.")

    @commands.command(pass_content=True)
    async def coin_flip(self, ctx, member1, member2):
        quotes = {'geos#5334': 'ΕΕ ΚΑΛΑ ΡΕ ΜΑΛΑΚΕΣ ΠΑΛΙ 3 MID ΕΛΑ ΕΝΤΑΞΕΙ FF 15 OOOOOOOOOOPEN',
                 'kavleas#5425': 'Το Conqueror ειναι σπασμενο μαλακες', 'Fizzmain#1155': 'ΓΙΑΤΙ ΤΡΩΩ DC', 'pipisxiv#9107': 'κατσε καλα κοντε θα σε γαμησω',
                  'BøatS#1805': 'ΕΕ ΜΑΛΑΚΕΣ ΜΟΥ ΠΗΡΕ ΤΟ BLUE ΓΑΜΩ ΤΟ ΧΡΙΣΤΟ', 'TTsKO#0583': 'ΕΕ ΝΤΑΞΕΙ ΡΕ ΜΑΛΑΚΑ ΟΚ ΓΑΜΙΕΣΑΙ ΡΕ ΦΙΛΕ ΚΑΙ ΓΑΜΙΕΤΑΙ ΚΙ Η ΜΑΝΑ ΣΟΥ',
                  'Jags#1501': 'ΕΠΑΘΑ ΑΝΕΥΡΙΣΜΑ', '_Amen_#3904': 'E εισαι πολυ αρχιδι ρε φιλε'}
        await ctx.send('Coin flip games, winner says his catch phrase\n')
        coin = random.randint(1, 2)
        if coin == 1:
            await ctx.send('The winner is ' + member1)
            if member1 in quotes.keys():
                await ctx.send('He says: ' + quotes[member1])
        else:
            await ctx.send('The winner is ' + member2)
            if member2 in quotes.keys():
                await ctx.send('He says: ' + quotes[member2])


def setup(client):
    client.add_cog(Games(client))

