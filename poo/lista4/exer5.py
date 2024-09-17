#5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa 
#classe deve ter funcionalidades para adicionar amigos, publicar mensagens, 
#comentar em posts e buscar por usuários.
class SocialNetwork:
    users = {}
    
    @classmethod
    def add_user(cls, username):
        cls.users[username] = {'friends': [], 'posts': []}
    
    @classmethod
    def add_friend(cls, username, friend):
        if friend in cls.users:
            cls.users[username]['friends'].append(friend)
    
    def __init__(self, username):
        self.username = username
    
    def post_message(self, message):
        SocialNetwork.users[self.username]['posts'].append(message)
    
    def view_posts(self):
        for post in SocialNetwork.users[self.username]['posts']:
            print(post)

# Teste
SocialNetwork.add_user('Rafael')
SocialNetwork.add_user('Ana')
SocialNetwork.add_friend('Rafael', 'Ana')

rafael_profile = SocialNetwork('Rafael')
rafael_profile.post_message('Hello, world!')
rafael_profile.view_posts()
