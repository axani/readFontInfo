import os
from fontTools.ttLib import TTFont

def getFontInfo(fontfile):
	font = TTFont(fontfile)

	fontinfo_dict = {}
	fontinfo_dict['fullfontname']	= font['name'].names[4].string
	fontinfo_dict['font_family']	= font['name'].names[1].string
	fontinfo_dict['font_subfamily']	= font['name'].names[2].string
	fontinfo_dict['designer']		= font['name'].names[10].string
	fontinfo_dict['designer_url']	= font['name'].names[12].string
	fontinfo_dict['manufacturer']	= font['name'].names[8].string
	fontinfo_dict['vendor_url']		= font['name'].names[11].string
	fontinfo_dict['trademark']		= font['name'].names[7].string
	fontinfo_dict['copyright']		= font['name'].names[0].string
	fontinfo_dict['license_descr']	= font['name'].names[13].string
	fontinfo_dict['license_url']	= font['name'].names[14].string
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
				escaped_string = this_dict[head_column].replace('"', '""').replace('\n\n', '\n')
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



fontfolder = 'fonts2read'
fontlist = ['SourceCodePro-Regular.otf']
export_filename = 'fontinfos.csv'
all_fontinfos = []

for font in fontlist:
	path = os.path.join(fontfolder, font)
	all_fontinfos.append(getFontInfo(path))

exportdata = Export(all_fontinfos)
exportdata.CSV()