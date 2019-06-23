# Init Variables
theMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""
profession = ["", "", "", ""]
adj = ["", ""]

# Get Input from Users
print("Welcome User")
print("Let's Playa a Game!")
neo = input("Whats Your Name: ")

# Getting the Matrix variable from user
print(f"Hello {neo}! Are you Ready?")
theMatrix = input("What is something you want to know more about?\n")

# Getting system variable from user
print(f"Oooh! You want to know more abour the {theMatrix} huh?")
print(f"Okay well first, tell me what you already know about {theMatrix}\n")
system = input(f"What Noun would you Categorize {theMatrix} as:")

# geting enemy variable from user
enemy = input(f"Give me an opposing noun to {system}: ")

# geting inside varible from user
inside = input(f"Now give me any relaxing noun (present tense): ")

# getting all profession varible from user
print(f"Okay, now I need 4 professions relating to {system}: ")

# loop
for i in range(len(profession)):
    profession[i] = input(f"Profession {i+1} / {len(profession)}:")

# getting the save variable from user
save = input(f"Give me a helo-related verb (present tense):")

# getting the unplugged variable from user
unplugged = input(f"Now give me a verb that makes you think abour relif (past tense): ")

# getting the adjectives
print(f"Lastly, I need 2 dystopian adjectives: ")

# loop
for i in range (len(adj)):
    adj[i] = input(f"Adjective {i+1} / {len(adj)}: ")

fight = input(f"and a verb:")

# init Story
story = (f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. " +
         f"But when you're {inside}, you look around, what do you see? " +
         f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}.The very minds " +
         f"of the people we are trying to {save}. But until we do, " +
         f"these people are still a part of that {system} and that makes " +
         f"them our {enemy}. You have to understand, most of these people " +
         f"are not ready to be {unplugged}. And many of them are so {adj[0]}, " +
         f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

# Print Story
print(story)

