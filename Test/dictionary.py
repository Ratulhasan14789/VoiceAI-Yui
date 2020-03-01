import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='beautifulsoup4')

from PyDictionary import PyDictionary



dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")

'There can be any number of words in the Instance'



print(dictionary.printMeanings())
print(dictionary.getMeanings())
print (dictionary.getSynonyms())
