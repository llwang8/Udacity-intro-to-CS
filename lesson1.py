# Udacity - Intro to Computer Science
#
# Lesson 1:

page = 'Search Engines And <a href="https://www.w3.org/1999/xhtml/">The Web</a><br><br>Sample Web Page<br><br>Udacity<br><br>Udacity is a private institution of <a href="ttps://en.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="https://en.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".<br><br>It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Udacity was announced at the 2012 <a href="https://en.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a>conference.'

end_link = -1

start_link = page.find('<a href=', end_link)
end_link = page.find('>', start_link)
link_w3 = page[start_link + 9:end_link]
print link_w3
start_link = end_link

start_link = page.find('<a href=', end_link)
end_link = page.find('>', start_link)
link_higherEdu = page[start_link + 9:end_link]
print link_higherEdu
start_link = end_link

start_link = page.find('<a href=', end_link)
end_link = page.find('>', start_link)
link_Sebastian = page[start_link + 9:end_link]
print link_Sebastian
start_link = end_link

start_link = page.find('"', end_link)
end_link = page.find('"', start_link + 1)
link_highQualityLowCost = page[start_link + 9:end_link]
print link_highQualityLowCost
start_link = end_link

start_link = page.find('<a href=', end_link)
end_link = page.find('>', start_link)
link_digitalLife = page[start_link + 9:end_link]
print link_digitalLife
start_link = end_link


