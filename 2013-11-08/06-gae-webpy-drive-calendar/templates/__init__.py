from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def cals (cl):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'<h1>Calendars</h1>\n'])
    extend_([u'<ul>\n'])
    for ccc in loop.setup(sorted(cl, key=(lambda x: x['summary']))):
        extend_([u'<li>', escape_((ccc['summary']), True), u'</li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

cals = CompiledTemplate(cals, './templates/cals.html')
join_ = cals._join; escape_ = cals._escape

# coding: utf-8
def spread (cells):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'<h1>spreadsheets</h1>\n'])
    extend_([u'<ul>\n'])
    for cell in loop.setup(cells):
        extend_([u'<li>', escape_((int(cell.cell.row)), True), u', ', escape_((int(cell.cell.col)), True), u' : ', escape_((cell.content.text), True), u'</li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

spread = CompiledTemplate(spread, './templates/spread.html')
join_ = spread._join; escape_ = spread._escape

# coding: utf-8
def index (tree):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'<h1>Drive</h1>\n'])
    extend_([u'<ul>\n'])
    ffunc = lambda x: x['mimeType'] == 'application/vnd.google-apps.spreadsheet'
    for name, node in loop.setup(tree.flatten_names(filter=ffunc)):
        ssid = node['id']
        extend_([u"<li><a href='/spreadsheets?ssid=", escape_(ssid, True), u"'>", escape_(name, True), u'</a></li>\n'])
    extend_([u'</ul>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

index = CompiledTemplate(index, './templates/index.html')
join_ = index._join; escape_ = index._escape

