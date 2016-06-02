# -*- coding:utf-8 -*-  
def align(text, space, align='left'):
	try:
		length = len(text.encode('gb2312'))						# python 3.x
	except UnicodeDecodeError:
		try:
			text = text.decode('utf-8').encode('gb2312')		# Python 2.x
		except UnicodeDecodeError:
			text = text.decode('gb2312').encode('gb2312')
		length = len(text)
	
	space = space - length if space >= length else 0
	
	if align == 'right':
		text = ' ' * space + text
	elif align == 'center':
		text = ' ' * (space//2) + text + ' ' * (space-space//2)
	else:
		text = text + ' ' * space
	
	return text