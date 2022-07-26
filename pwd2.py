import random
import string
# x=input("Press Y to generate a random secure password:")
charvar=string.ascii_letters+string.digits+string.punctuation
# randomcharvar=random.choice(charvar)
randomcharvar=''.join(random.choice(charvar)for i in range(8)) 
numvar=random.randint(10000, 10000000000000)
print(randomcharvar,numvar,sep='')
