import random


quotes = [
    "The best way to predict the future is to invent it." - Alan Kay",
    "I have not failed. I've just found 10,000 ways that won't work." - Thomas Edison",
    "If you don't stand for something, you will fall for anything." - Malcolm X",
    "Believe you can and you're halfway there." - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill",
    "Education is the most powerful weapon which you can use to change the world." - Nelson Mandela",
    "Life is 10% what happens to us and 90% how we react to it." - Charles R. Swindoll",
    "The only way to do great work is to love what you do." - Steve Jobs",
    "In the end, we will remember not the words of our enemies, but the silence of our friends." - Martin Luther King Jr.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall." - Nelson Mandela",
    "Be the change that you wish to see in the world." - Mahatma Gandhi",
    "It does not matter how slowly you go as long as you do not stop." - Confucius",
    "It is not the strongest of the species that survives, nor the most intelligent, but the one most responsive to change." - Charles Darwin",
    "The only true wisdom is in knowing you know nothing." - Socrates",
    "The only thing necessary for the triumph of evil is for good men to do nothing." - Edmund Burke",
    "Success is stumbling from failure to failure with no loss of enthusiasm." - Winston Churchill",
    "I would rather die of passion than of boredom." - Vincent van Gogh",
    "In three words I can sum up everything I've learned about life: it goes on." - Robert Frost",
    "The only source of knowledge is experience." - Albert Einstein",
    "Life is like riding a bicycle. To keep your balance, you must keep moving." - Albert Einstein",
    "Everything you can imagine is real." - Pablo Picasso",
    "A room without books is like a body without a soul." - Marcus Tullius Cicero",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment." - Ralph Waldo Emerson",
    "We must let go of the life we have planned, so as to accept the one that is waiting for us." - Joseph Campbell",
    "The difference between genius and stupidity is: genius has its limits." - Albert Einstein",
    "You miss 100% of the shots you don't take." - Wayne Gretzky",
    "The best revenge is massive success." - Frank Sinatra",
    "Happiness is not something ready made. It comes from your own actions." - Dalai Lama",
    "The greatest glory in living lies not in never falling, but in rising every time we fall." - Nelson Mandela",
    "It always seems impossible until it's done." - Nelson Mandela",
    "The greatest wealth is to live content with little." - Plato",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle." - Christian D. Larson",
    "Life is a journey, and if you fall in love with the journey, you will be in love forever." - Peter Hagerty",
    "There is only one way to avoid criticism: do nothing, say nothing, and be nothing." - Aristotle ]


while True:
    random_quote = random.choice(quotes)
    print(random_quote)
    repeat = input("Would you like to see another quote? (y/n) ")
    if repeat.lower() != "y":
        break
