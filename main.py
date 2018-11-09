import urwid

txt = urwid.Text(u"Bye Bye World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill)
loop.run()

#This is a test addition
