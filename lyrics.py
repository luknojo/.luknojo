import time

lyrics = [
    "Baby you're my sweetest deja vu",
    "I like your pretty face and your tattoos",
    "When we're together I know what to do",
    "You know it too you like it too",
    "Your touch is electric",
    "Sending shivers down my spine",
    "And I'm falling deeper",
    "Can barely control my mind",
    "You're my guilty pleasure",
    "My secret vice",
    "I know I shouldn't",
    "But it feels so right",
    "I'm caught up in your web",
    "Like a fly in a trap",
    "I know it's wrong",
    "But I can't turn it back"
]

timing = [5, 4, 4, 10, 5, 5.8, 4.5, 3, 3, 2, 3, 3, 3, 2, 2, 3]

for i, line in enumerate(lyrics):
    print(line)
    time.sleep(timing[i])