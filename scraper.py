from lxml import html
import requests
import sys

file = open("test.txt", mode='w')
page = requests.get('http://kwoc.kossiitkgp.in/leaderboard')
tree = html.fromstring(page.content)

#gHandle = tree.xpath('//*[@id="mainTable"]/tr/td[1]/text()')
#name = tree.xpath('//*[@id="mainTable"]/tr/td[2]/text()')

gHandle = tree.xpath('//*[@id="mainTable"]/tr/td[1]')
name = tree.xpath('//*[@id="mainTable"]/tr/td[2]')

file.write("{0:<30s} {1:<50s}\n\n".format('GitHub Handle', 'Name'))

for i in range(len(gHandle)):
	file.write("{0:<30s} {1:<50s}\n".format(gHandle[i].text_content(), name[i].text_content()))