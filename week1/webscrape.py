import urllib2
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(
          urllib2.urlopen('http://seminars.viennabiocenter.org/seminars.php').read(),
          convertEntities='html')
for seminar in soup('table',{'width':'700'}):
    title, body = seminar('td')
    title = ":".join( title.text.split(':')[1:] )
    date = body('b')[0].text

    print "%s \n\t - %s" % (title, date)

