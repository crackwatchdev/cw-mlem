import json
import requests
import configparser as cp

class Config:
    CONFIG = cp.ConfigParser()
    def __int__(self, path=None):
        self.bot = self.CONFIG['DEFAULT']
        self.bot.read(path | './config.ini')

    def authorization_token(self):
        return self.bot.get('AuthorizationToken')

    def token_type(self):
        return self.bot.get('TokenType')

    def guild_id(self):
        return self.bot.get('GuildId')


class AuditlogsApi(Config):
    def __init__(self):
        super().__init__()
        self.base_api = "https://discordapp.com/api"
        self.api_version = "/v/6"
        self.guild_auditlog = "/guilds/" + self.guild_id()
        self.header = {'Authorization': '+'.join([self.token_type(), self.authorization_token()])}