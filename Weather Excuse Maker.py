import random
import tkinter as tk

def generate_excuse(location):
    excuses = [
        "I'm sorry, but the weather machine got stuck in a loop while trying to check the temperature in {0}.",
        "Oh no, the weather forecast for {0} got eaten by a mischievous squirrel.",
        "The weather report for {0} is trapped in a parallel dimension. I can't retrieve it right now.",
        "Unfortunately, a flock of flying turtles disrupted the weather sensors in {0}.",
        "I regret to inform you that the weather conditions in {0} are currently being recalculated by a group of confused mathematicians.",
        "The weather data in {0} mysteriously transformed into a collection of puns. I'm working on decoding them.",
        "Apologies, but the weather forecast for {0} is hidden in a secret treasure chest. I can't reveal it just yet.",
        "Oops! The weather information for {0} is being held hostage by a band of mischievous gnomes. They demanded more chocolate chips as ransom.",
        "I'm afraid the weather gods in {0} are on vacation, and they took the forecast with them.",
        "My apologies, but the weather report for {0} has been temporarily transformed into a haiku. I'm deciphering it as we speak.",
        "The weather in {0} is currently tangled up in a game of Twister. I'm waiting for them to sort it out.",
        "I'm sorry, but the weather data for {0} was intercepted by a group of prankster aliens. They're having too much fun with it.",
        "The weather in {0} is experiencing an existential crisis. It's questioning its purpose in the universe.",
        "Unfortunately, the weather in {0} went on strike, demanding better working conditions and more frequent coffee breaks.",
        "Apologies, but the weather report for {0} is currently touring as the opening act for a famous rock band.",
        "I'm afraid the weather forecast for {0} is written in a language known only to a secret society of meteorologists.",
        "Oops! The weather conditions in {0} are being used as a training ground for amateur skydivers. They keep messing with the instruments.",
        "My sincerest apologies, but the weather in {0} is attending a mandatory yoga retreat. It will be back to work shortly.",
        "The weather forecast for {0} accidentally got mixed up with a recipe for blueberry muffins. I'm trying to unscramble the ingredients.",
        "I'm sorry, but the weather conditions in {0} are engaged in an intense game of hide-and-seek. They're doing a great job at hiding.",
        "The weather in {0} is currently on a quest to find the lost city of Atlantis. It might take a while.",
        "Apologies, but the weather report for {0} got stuck in a time loop. I'm trying to break the cycle.",
        "I regret to inform you that the weather data in {0} was abducted by aliens for their intergalactic weather studies.",
        "I'm afraid the weather forecast for {0} got caught in a wormhole. It's experiencing some temporal turbulence.",
        "Oops! The weather conditions in {0} have decided to take a spontaneous vacation in the Bahamas. Can't blame them, really.",
        "My sincerest apologies, but the weather in {0} got tangled in a knitting project. I'm trying to untangle the yarn.",
        "The weather report for {0} got caught in traffic. It will arrive fashionably late.",
        "Apologies, but the weather forecast for {0} accidentally got sent to a parallel universe. I'm working on retrieving it.",
        "I'm sorry, but the weather conditions in {0} are locked in a heated debate over whether clouds should be fluffy or puffy.",
        "Oh no! The weather in {0} got trapped in a time capsule. It won't be available until the future arrives.",
        "The weather data for {0} is currently on a top-secret mission. It's classified information.",
        "I regret to inform you that the weather report for {0} was transformed into a catchy song. I'm deciphering the lyrics.",
        "I'm afraid the weather in {0} got mixed up with the inventory of a clown supplies store. I'm sorting through the red noses and oversized shoes.",
        "Apologies, but the weather forecast for {0} accidentally got turned into a game of Sudoku. I'm solving it as fast as I can.",
        "Oops! The weather conditions in {0} were borrowed by a wizard for a magical experiment. It might take a while to return them.",
        "My sincerest apologies, but the weather in {0} got entangled in a string of holiday lights. I'm untangling them one bulb at a time.",
        "The weather report for {0} decided to join a circus. It's practicing tightrope walking as we speak.",
        "I'm sorry, but the weather conditions in {0} are taking a nap. They will wake up when they feel like it.",
        "Oh no! The weather in {0} accidentally fell into a plot hole. I'm trying to rewrite the story to bring it back.",
        "The weather data for {0} has been converted into binary code. I'm translating it back to English.",
        "Apologies, but the weather forecast for {0} is currently trapped in a Rubik's Cube. I'm solving it to set it free.",
        "I'm afraid the weather in {0} decided to go on an adventure. It's exploring uncharted territories.",
        "Oops! The weather conditions in {0} have become self-aware. They're contemplating their existence.",
        "My sincerest apologies, but the weather in {0} accidentally joined a mariachi band. It's playing the trumpet.",
        "The weather report for {0} is on a coffee break. It will be back with fresh updates soon.",
        "I'm sorry, but the weather conditions in {0} are attending a costume party. They're currently disguised as tropical fruit.",
        "Oh no! The weather in {0} got distracted by a squirrel wearing sunglasses. It's trying to have a conversation with it.",
        "The weather data in {0} is learning to play the piano. It's practicing scales and arpeggios.",
        "Apologies, but the weather forecast for {0} has been transformed into a jigsaw puzzle. I'm putting the pieces back together.",
        "I'm afraid the weather in {0} is taking a detour to visit all the world wonders. It won't be back for a while.",
        "Oops! The weather conditions in {0} are caught up in a heated debate over the best flavor of ice cream. Things got messy.",
        "My sincerest apologies, but the weather in {0} accidentally joined a synchronized swimming team. It's perfecting its backstroke.",
        "The weather report for {0} is on a coffee break. It will be back with fresh updates soon.",
        "I'm sorry, but the weather conditions in {0} are attending a costume party. They're currently disguised as tropical fruit.",
        "Oh no! The weather in {0} got distracted by a squirrel wearing sunglasses. It's trying to have a conversation with it.",
        "The weather data in {0} is learning to play the piano. It's practicing scales and arpeggios.",
        "Apologies, but the weather forecast for {0} has been transformed into a jigsaw puzzle. I'm putting the pieces back together.",
        "I'm afraid the weather in {0} is taking a detour to visit all the world wonders. It won't be back for a while.",
        "Oops! The weather conditions in {0} are caught up in a heated debate over the best flavor of ice cream. Things got messy.",
        "My sincerest apologies, but the weather in {0} accidentally joined a synchronized swimming team. It's perfecting its backstroke.",
        "The weather report for {0} decided to take a spontaneous nap. It will wake up feeling refreshed.",
        "I'm sorry, but the weather conditions in {0} are attending a secret meteorology conference. They're sharing their best cloud jokes.",
        "Oh no! The weather in {0} went on a quest to find the mythical land of eternal sunshine. It might take a while.",
        "The weather data for {0} accidentally fell into a pile of autumn leaves. I'm brushing them off one by one.",
        "Apologies, but the weather forecast for {0} is practicing its dance moves for an upcoming talent show.",
        "I'm afraid the weather in {0} got carried away by a group of enthusiastic kites. They're having a soaring adventure together.",
        "Oops! The weather conditions in {0} took a wrong turn at Albuquerque. I'm redirecting them back on track.",
        "My sincerest apologies, but the weather in {0} is writing a love letter to the moon. It's feeling poetic.",
        "The weather report for {0} got caught up in a game of hide-and-seek with the clouds. I'm searching for them.",
        "I'm sorry, but the weather conditions in {0} decided to learn to juggle. They're tossing raindrops in the air.",
        "Oh no! The weather in {0} joined a book club. It's currently discussing the latest bestseller.",
        "The weather data in {0} accidentally got turned into a flock of origami birds. I'm unfolding them to retrieve the information.",
        "Apologies, but the weather forecast for {0} is practicing its stand-up comedy routine. It's trying to make rain jokes.",
        "I'm afraid the weather in {0} is on a quest to find the pot of gold at the end of the rainbow. It might take a while.",
        "Oops! The weather conditions in {0} have decided to start a band. They're currently jamming with thunder and lightning.",
        "My sincerest apologies, but the weather in {0} got trapped in a maze. I'm guiding it through the twists and turns.",
        "The weather report for {0} is attending a self-improvement seminar. It's learning to be more sunny and less cloudy.",
        "I'm sorry, but the weather conditions in {0} are trying to solve a complex Sudoku puzzle. I'm helping them find the missing numbers.",
        "Oh no! The weather in {0} was invited to a tea party with the unicorns. It's sipping tea and having delightful conversations.",
        "The weather data in {0} accidentally got mixed up with a recipe for strawberry jam. I'm trying to separate the ingredients.",
        "Apologies, but the weather forecast for {0} is taking a nap. It will wake up with refreshed predictions.",
        "I'm afraid the weather in {0} got caught up in a game of hopscotch. It's hopping from one square to another.",
        "Oops! The weather conditions in {0} are currently on a treasure hunt. They're searching for the golden sunshine.",
        "My sincerest apologies, but the weather in {0} got wrapped up in a giant ball of yarn. I'm untangling it.",
        "The weather report for {0} decided to join a marching band. It's practicing its drumming skills.",
        "I'm sorry, but the weather conditions in {0} are busy playing hide-and-seek with the rainbows. They're excellent hiders.",
        "Oh no! The weather in {0} fell into a time warp. I'm trying to bring it back to the present.",
        "The weather data for {0} is currently on a mission to count all the stars in the universe. It's quite a task.",
        "Apologies, but the weather forecast for {0} accidentally got transformed into a crossword puzzle. I'm filling in the blanks.",
        "I'm afraid the weather in {0} is taking a break to chase fireflies. It's having a magical time.",
        "Oops! The weather conditions in {0} are performing in a Broadway musical. They're singing and dancing their hearts out.",
        "My sincerest apologies, but the weather in {0} accidentally joined a choir. It's practicing harmonizing with the wind.",
        "The weather report for {0} is writing a love letter to the ocean. It's feeling a deep connection.",
        "I'm sorry, but the weather conditions in {0} decided to take up gardening. They're watering the plants and talking to the flowers.",
        "Oh no! The weather in {0} went on a quest to find the lost city of El Dorado. It's searching for hidden treasures.",
        "The weather data in {0} accidentally got turned into a collection of origami animals. I'm unfolding them to retrieve the information.",
        "Apologies, but the weather forecast for {0} is taking a break to practice yoga. It's finding its inner balance.",
        "I'm afraid the weather in {0} is attending a class on cloud sculpting. It's learning to create masterpieces in the sky.",
        "Oops! The weather conditions in {0} got tangled in a game of jump rope. I'm untangling the ropes.",
        "My sincerest apologies, but the weather in {0} accidentally joined a bird choir. It's tweeting along with the melodies.",
        "The weather report for {0} is on a quest to find the pot of gold at the end of the rainbow. It's following the colors.",
        "I'm sorry, but the weather conditions in {0} are practicing their acrobatic skills. They're somersaulting through the sky.",
        "Oh no! The weather in {0} got caught up in a bubble-blowing contest. It's creating a sky full of bubbles.",
        "The weather data in {0} accidentally got mixed up with a recipe for rainbow cake. I'm trying to separate the layers.",
        "Apologies, but the weather forecast for {0} is learning to write poetry. It's composing weather-themed sonnets.",
        "I'm afraid the weather in {0} is on a mission to find the end of the rainbow. It's searching for a pot of gold.",
        "Oops! The weather conditions in {0} got invited to a tea party with the fairies. They're sipping tea and having enchanting conversations.",
        "My sincerest apologies, but the weather in {0} accidentally joined a cloud sculpting competition. It's shaping clouds into amazing forms.",
        "The weather report for {0} is on a coffee break. It will be back with fresh updates soon.",
        "I'm sorry, but the weather conditions in {0} are attending a costume party. They're currently disguised as tropical fruit.",
        "Oh no! The weather in {0} got distracted by a squirrel wearing sunglasses. It's trying to have a conversation with it.",
        "The weather data in {0} is learning to play the piano. It's practicing scales and arpeggios.",
        "Apologies, but the weather forecast for {0} has been transformed into a jigsaw puzzle. I'm putting the pieces back together.",
        "I'm afraid the weather in {0} is taking a detour to visit all the world wonders. It won't be back for a while.",
        "Oops! The weather conditions in {0} are caught up in a heated debate over the best flavor of ice cream. Things got messy.",
        "My sincerest apologies, but the weather in {0} accidentally joined a synchronized swimming team. It's perfecting its backstroke.",
        "The weather report for {0} is on a coffee break. It will be back with fresh updates soon.",
        "I'm sorry, but the weather conditions in {0} are attending a costume party. They're currently disguised as tropical fruit.",
        "Oh no! The weather in {0} got distracted by a squirrel wearing sunglasses. It's trying to have a conversation with it.",
        "The weather data in {0} is learning to play the piano. It's practicing scales and arpeggios.",
        "Apologies, but the weather forecast for {0} has been transformed into a jigsaw puzzle. I'm putting the pieces back together.",
        "I'm afraid the weather in {0} is taking a detour to visit all the world wonders. It won't be back for a while.",
        "Oops! The weather conditions in {0} are caught up in a heated debate over the best flavor of ice cream. Things got messy.",
        "My sincerest apologies, but the weather in {0} accidentally joined a synchronized swimming team. It's perfecting its backstroke.",
        "The weather report for {0} is on a coffee break. It will be back with fresh updates soon.",
        "I'm sorry, but the weather conditions in {0} are attending a costume party. They're currently disguised as tropical fruit.",
        "Oh no! The weather in {0} got distracted by a squirrel wearing sunglasses. It's trying to have a conversation with it.",
        "The weather data in {0} is learning to play the piano. It's practicing scales and arpeggios.",
        "Apologies, but the weather forecast for {0} has been transformed into a jigsaw puzzle. I'm putting the pieces back together.",
        "I'm afraid the weather in {0} is taking a detour to visit all the world wonders. It won't be back for a while.",
        "Oops! The weather conditions in {0} are caught up in a heated debate over the best flavor of ice cream. Things got messy.",
        "My sincerest apologies, but the weather in {0} accidentally joined a synchronized swimming team. It's perfecting its backstroke.",
        "The weather report for {0} is on a coffee break. It will be back with fresh updates soon.",
        "I'm sorry, but the weather conditions in {0} are attending a costume party. They're currently disguised as tropical fruit.",
        "Oh no! The weather in {0} got distracted by a squirrel wearing sunglasses. It's trying to have a conversation with it.",
        "The weather data in {0} is learning to play the piano. It's practicing scales and arpeggios.",
        "Apologies, but the weather forecast for {0} has been transformed into a jigsaw puzzle. I'm putting the pieces back together.",
        "I'm afraid the weather in {0} is taking a detour to visit all the world wonders. It won't be back for a while.",
        "Oops! The weather conditions in {0} are caught up in a heated debate over the best flavor of ice cream. Things got messy.",
        "My sincerest apologies, but the weather in {0} accidentally joined a synchronized swimming team. It's perfecting its backstroke.",
        "The weather report for {0} is on a coffee break. It will be back with fresh updates soon.",
        "I'm sorry, but the weather conditions in {0} are attending a costume party. They're currently disguised as tropical fruit.",
        "Oh no! The weather in {0} got distracted by a squirrel wearing sunglasses. It's trying to have a conversation with it.",
        "The weather data in {0} is learning to play the piano. It's practicing scales and arpeggios.",
        "Apologies, but the weather forecast for {0} has been transformed into a jigsaw puzzle. I'm putting the pieces back together.",
        "I'm afraid the weather in {0} is taking a detour to visit all the world wonders. It won't be back for a while.",
        "Oops! The weather conditions in {0} are caught up in a heated debate over the best flavor of ice cream. Things got messy.",
        "My sincerest apologies, but the weather in {0} accidentally joined a synchronized swimming team. It's perfecting its backstroke."
    ]
    excuse = random.choice(excuses)
    return excuse.format(location)

def generate_button_clicked():
    location = location_entry.get()
    excuse = generate_excuse(location)
    excuse_label.config(text=excuse)

# Create the main window
window = tk.Tk()
window.title("Weather Excuse Maker")

# Make the window fullscreen
window.attributes('-fullscreen', True)

# Configure the window to center the elements
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Create and place the UI elements
location_label = tk.Label(window, text="Enter your location:", font=("Helvetica", 15))
location_label.pack(anchor=tk.CENTER, pady=50)

location_entry = tk.Entry(window)
location_entry.pack(anchor=tk.CENTER, pady=50)

generate_button = tk.Button(window, text="Generate Excuse", command=generate_button_clicked)
generate_button.pack(anchor=tk.CENTER, pady=50)

excuse_label = tk.Label(window, text="", font=("Helvetica", 15))
excuse_label.pack(anchor=tk.CENTER, pady=50)

# Start the main event loop
window.mainloop()
