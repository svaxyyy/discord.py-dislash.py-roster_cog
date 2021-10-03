import discord
from discord.ext import commands
from dislash import *





class roster(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @slash_command(name = "roster", description = "shows a roster of all roles")
    async def roster(self, inter):

        roles = []
        for role in list(inter.guild.roles):
            roles.append(
                int(role.id)
            )
        embed = discord.Embed(name="Roster", description="** **")

        for r in roles:
            role = inter.guild.get_role(int(r))
            if role.name == "@everyone":
                pass
            elif not role.name == "@everyone":
                usrrlcnt = 0
                role = inter.guild.get_role(int(r))
                members = []
                for m in list(inter.guild.members):
                    for mr in list(m.roles):
                        if (int(role.id) == int(mr.id)):
                            members.append(f"<@{m.id}>")
                            usrrlcnt += 1
                if (int(usrrlcnt) == 0):
                    embed.add_field(name=str(role.name), value="No one has this role", inline=False)
                elif not (int(usrrlcnt) == 0):
                    string = ""
                    for mention in members:
                        string += f"{mention} "
                    string + ""
                    embed.add_field(name=str(role.name), value= f"** ** {string}", inline=False)

        embed.set_footer(text="🔼highest role")
        embed.set_author(name="⬇️lowest role")
        await inter.send(embed=embed)
            
    


def setup(client):
    client.add_cog(roster(client))
