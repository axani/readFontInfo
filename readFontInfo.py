import os
from fontTools.ttLib import TTFont

def getFontInfo(fontfile):
	font = TTFont(fontfile)

	fontinfo_dict = {}
	try:
		fontinfo_dict['fullfontname']	= font['name'].getName(4,1,0).string
	except:
		fontinfo_dict['fullfontname']	= ''
	try:
		fontinfo_dict['font_family']	= font['name'].getName(1,1,0).string
	except:
		fontinfo_dict['font_family']	= ''
	try:
		fontinfo_dict['font_subfamily']	= font['name'].getName(2,1,0).string
	except:
		fontinfo_dict['font_subfamily']	= ''
	try:
		fontinfo_dict['postscript_name']= font['name'].getName(6,1,0).string
	except:
		fontinfo_dict['postscript_name']= ''
	try:
		fontinfo_dict['designer']		= font['name'].getName(9,1,0).string
	except:
		fontinfo_dict['designer']		= ''
	try:
		fontinfo_dict['designer_url']	= font['name'].getName(12,1,0).string
	except:
		fontinfo_dict['designer_url']	= ''
	try:
		fontinfo_dict['manufacturer']	= font['name'].getName(8,1,0).string
	except:
		fontinfo_dict['manufacturer']	= ''
	try:
		fontinfo_dict['vendor_url']		= font['name'].getName(11,1,0).string
	except:
		fontinfo_dict['vendor_url']		= ''
	try:
		fontinfo_dict['trademark']		= font['name'].getName(7,1,0).string
	except:
		fontinfo_dict['trademark']		= ''
	try:
		fontinfo_dict['copyright']		= font['name'].getName(14,1,0).string
	except:
		fontinfo_dict['copyright']		= ''
	try:
		fontinfo_dict['license_descr']	= font['name'].getName(13,1,0).string
	except:
		fontinfo_dict['license_descr']	= ''
	try:
		fontinfo_dict['license_url']	= font['name'].getName(14,1,0).string
	except:
		fontinfo_dict['license_url']	= ''
	return fontinfo_dict

class Export:
	def __init__(self, all_fontinfos):
		self.all_fontinfos = all_fontinfos
		print 'Exporting to', export_filename, '...'


	def CSV(self):
		self.csv_separator = ','
		self.csv_head_list = self.createCSVHead()
		self.csv_head_string = self.csv_separator.join(self.csv_head_list)
		self.csv_content_list = self.createCSVContent()
		self.csv_content_string = '\n'.join(self.csv_content_list)
		self.writeCSV()

	def createCSVHead(self):
		head_list = [
			'fullfontname',
			'font_family',
			'font_subfamily',
			'postscript_name',
			'designer',
			'designer_url',
			'manufacturer',
			'vendor_url',
			'trademark',
			'copyright',
			'license_descr',
			'license_url'
		]
		return head_list

	def createCSVContent(self):
		content_list = []
		for this_dict in self.all_fontinfos:
			row_string = ''
			for head_column in self.csv_head_list:
				escaped_string = this_dict[head_column].replace('"', '\'').replace('\r','').replace('\n', '')
				row_string += '"' + escaped_string + '",'

			# Append without trailing comma
			print row_string
			content_list.append(row_string.rstrip(','))

		return content_list



	def writeCSV(self):
		export_file = open(export_filename, 'w')
		export_file.write(self.csv_head_string + '\n')
		export_file.write(self.csv_content_string)
		export_file.close()



export_filename = 'fontinfos.csv'
fontfolder = 'fonts2read'
fontlist = []

for f in os.listdir(fontfolder):
	if f.endswith('.otf') or f.endswith('.ttf'):
		fontlist.append(f)

all_fontinfos = []

for font in fontlist:
	path = os.path.join(fontfolder, font)
	all_fontinfos.append(getFontInfo(path))

exportdata = Export(all_fontinfos)
exportdata.CSV()