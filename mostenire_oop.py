# inheritance - mostenire

# clasa parinte
class Chef:
    def make_salad(self):
        print('salad')

    def make_fries(self):
        print('fries')

    def make_eggs(self):
        print('eggs')

# clase copil - mostenesc ce face clasa parinte
class Italian_chef(Chef):
    def make_pizza(self):
        print('pizza')

class Japanese_chef(Chef):
    def make_sushi(self):
        print('sushi')

andrea = Italian_chef()
andrea.make_pizza()
andrea.make_fries() # asta e de la parinti
andrea.make_eggs() # si asta la fel