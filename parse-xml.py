import xml.etree.ElementTree as etree
class Dataset:
    def __init__(self,url,prefix):
        self.url=url
        self.prefix=prefix
        self.pageTag = prefix+"page"
        self.titleTag = prefix+"title"
        self.nsTag = prefix+"ns"
        self.textTag = prefix+"text"
ls_data = Dataset('data/lightsaber.xml','')
dump = Dataset('data/starwars_pages_current.xml','{http://www.mediawiki.org/xml/export-0.10/}')


dataset = dump
context = etree.iterparse(dataset.url, events=('end',))

known = dict()
elem = dict()
pages = []
for event, element in context:
    if element.tag == dataset.pageTag:
        pages.append(elem)
        if not elem['ns'] in known:
            print elem['ns'],elem['title']
            known[elem['ns']] = elem
        elem=dict()
        if len(pages)%10000 == 0:
            print len(pages)
        
    if element.tag == dataset.titleTag:
        elem['title'] = element.text
    elif element.tag == dataset.nsTag:
        elem['ns'] = element.text
    elif element.tag == dataset.textTag:
        elem['text']= element.text
    element.clear()
pages = filter(lambda page:page['ns'] == '0' or page['ns'] == '14',pages)
