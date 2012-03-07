import urllib2
import BeautifulSoup

soup = BeautifulSoup.BeautifulSoup(
          urllib2.urlopen('http://seminars.viennabiocenter.org/seminars.php').read(),
          convertEntities='html')
for seminar in soup('table',{'width':'700'}):
    title, body = seminar('td')
    title = title.text.replace("VBC Regular Seminar:","")
    date = body('b')[0].text

    print "%s \n\t - %s" % (title, date)

