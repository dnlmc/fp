import re

# extract all <p> tags
posts17 = friendsoup17.find_all('p')

# remove html tags
friend17clean = []   

for i in range(len(friend17)):
    friend17clean.append(re.sub('<[^>]+>', '', friend17[i]))