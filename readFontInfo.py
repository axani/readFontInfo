import os
from fontTools.ttLib import TTFont

class FontInfo:
	def __init__(self, fontfile):
		self.font = TTFont(fontfile)
		self.fontinfo = {}
		self.fontinfo['copyright'] =  self.font['name'].names[0].string
		self.fontinfo['font_family'] =  self.font['name'].names[1].string
		self.fontinfo['font_subfamily'] =  self.font['name'].names[2].string
		self.fontinfo['fullfontname'] =  self.font['name'].names[4].string
		self.fontinfo['trademark'] =  self.font['name'].names[7].string
		self.fontinfo['manufacturer'] =  self.font['name'].names[8].string
		self.fontinfo['designer'] =  self.font['name'].names[10].string
		self.fontinfo['vendor_url'] =  self.font['name'].names[11].string
		self.fontinfo['designer_url'] =  self.font['name'].names[12].string
		self.fontinfo['license_descr'] =  self.font['name'].names[13].string
		self.fontinfo['license_url'] =  self.font['name'].names[14].string
		print self.fontinfo

fontfolder = 'fonts2read'
fontlist = ['SourceCodePro-Regular.otf']

for font in fontlist:
	path = os.path.join(fontfolder, font)
	fontinfo = FontInfo(path)