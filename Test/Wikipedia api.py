import wikipedia
print(wikipedia.summary("Wikipedia", sentences=5))

print(wikipedia.search("dhaka"))
# [u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']

ny = wikipedia.page("New York city")
ny.title
# u'New York'
ny.url
# u'http://en.wikipedia.org/wiki/New_York'
ny.content
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
ny.links[0]
# u'1790 United States Census'
#wikipedia.set_lang("fr")
print(wikipedia.summary("facebook", sentences=5))
# Facebook est un service de réseautage
