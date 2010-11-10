import urllib

def generate_define_url(arg):
    return 'http://www.google.com/search?q=define%%3A%s&ie=utf-8&oe=utf-8' % (arg)

class Google:

    def getCommands(self):
        return ['define']

    def getType(self):
        return 'command'

    def define(self, args):
	args['output'].write('oieeeemm')
	key = args['message']
	x = urllib.urlopen(generate_define_url(key))
	bigstring = ''.join(x.readlines())
	a = bigstring.find('<ul')
	b = bigstring.find('</ul')
	print a, b
	bigstring = bigstring[a:b]

	args['output'].write(bigstring)


