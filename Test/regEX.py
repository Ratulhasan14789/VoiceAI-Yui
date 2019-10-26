import re

str = "hello s:@world::wind@:f dfg :@world::wind@:"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall(r":@.*::.*@:", str)
print(x)
