import random
from random import seed
import string

# Genererar ett random stor bokstav (Baserat på ASCII kod)
# uppercaseLetter = chr(random.randint(65, 90))

# Detta är en function som shufflar alla karaktärer i en sträng
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)


uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
uppercaseLetter3 = chr(random.randint(65, 90))
uppercaseLetter4 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(65, 90))
lowercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter3 = chr(random.randint(65, 90))
lowercaseLetter4 = chr(random.randint(65, 90))

number = random.randint(1, 9)
punc = random.choice(string.punctuation)

# Skapar lösenordet
password = (
    uppercaseLetter1
    + uppercaseLetter2
    + uppercaseLetter3
    + uppercaseLetter4
    + str.lower(lowercaseLetter1)
    + str.lower(lowercaseLetter2)
    + str.lower(lowercaseLetter3)
    + str.lower(lowercaseLetter4)
    + str(number)
    + punc
)
# Shufflar om det så att det blir "random"
password = shuffle(password)


# Sista som händer, här är appen slut
# str() gör om vårat nummer som är en int till en sträng så att man kan plussa ihop dessa två
print("Your password is " + password)
