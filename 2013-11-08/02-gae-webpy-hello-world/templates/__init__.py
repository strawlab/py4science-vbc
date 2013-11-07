from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def templateexample (data):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'    <head>\n'])
    extend_([u'    </head>\n'])
    extend_([u'    <body>\n'])
    extend_([u'        <h1>EXAMPLE</h1>\n'])
    extend_([u'        <ul>\n'])
    for d in loop.setup(data):
        output = str(d)
        extend_(['            ', u'<li>', escape_((output), True), u'</li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'    </body>\n'])
    extend_([u'</html>\n'])

    return self

templateexample = CompiledTemplate(templateexample, './templates/templateexample.html')
join_ = templateexample._join; escape_ = templateexample._escape

