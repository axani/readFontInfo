import os
import pprint
from fontTools.ttLib import TTFont

class GetFontInfo:
	def __init__(self, fontpath):
		self.fontinfo_dict = {}
		self.font = TTFont(fontpath)

		# Add data
		#self.getNameInfo()
		self.getOtherInfo()

	def getNameInfo(self):
		self.addInfo('fullfontname', self.font['name'].getName(4,1,0))
		self.addInfo('font_family', self.font['name'].getName(1,1,0))
		self.addInfo('font_subfamily', self.font['name'].getName(2,1,0))
		self.addInfo('postscript_name', self.font['name'].getName(6,1,0))
		self.addInfo('designer', self.font['name'].getName(9,1,0))
		self.addInfo('designer_url', self.font['name'].getName(12,1,0))
		self.addInfo('manufacturer', self.font['name'].getName(8,1,0))
		self.addInfo('vendor_url', self.font['name'].getName(11,1,0))
		self.addInfo('trademark', self.font['name'].getName(7,1,0))
		self.addInfo('copyright', self.font['name'].getName(14,1,0))
		self.addInfo('license_descr', self.font['name'].getName(13,1,0))
		self.addInfo('license_url', self.font['name'].getName(14,1,0))

	def getOtherInfo(self):
		#self.fontinfo_dict['glyphCount'] = len(self.font.getGlyphOrder())
		self.fontinfo_dict['maxp'] = {'numGlyphs': self.font['maxp'].numGlyphs}
		
		self.fontinfo_dict['featuretags'] = []
		for feat in self.font['GSUB'].table.FeatureList.FeatureRecord:
			if feat.FeatureTag not in self.fontinfo_dict['featuretags']:
				self.fontinfo_dict['featuretags'].append(feat.FeatureTag)

		self.fontinfo_dict['head'] = {
			'unitsPerEm': self.font['head'].unitsPerEm,
			'created': self.font['head'].created,
			'modified': self.font['head'].modified,
			'xMin': self.font['head'].xMin,
			'yMin': self.font['head'].yMin,
			'xMax': self.font['head'].xMax,
			'yMax': self.font['head'].yMax,
			'macStyle': self.font['head'].macStyle,
			'lowestRecPPEM': self.font['head'].lowestRecPPEM
		}

		self.fontinfo_dict['hhea'] = {
			'ascent': self.font['hhea'].ascent,
			'descent': self.font['hhea'].descent,
			'lineGap': self.font['hhea'].lineGap,
			'advanceWidthMax': self.font['hhea'].advanceWidthMax,
			'minLeftSideBearing': self.font['hhea'].minLeftSideBearing,
			'minRightSideBearing': self.font['hhea'].minRightSideBearing,
			'xMaxExtent': self.font['hhea'].xMaxExtent,
			'caretSlopeRise': self.font['hhea'].caretSlopeRise,
			'caretSlopeRun': self.font['hhea'].caretSlopeRun,
			'caretOffset': self.font['hhea'].caretOffset,
			'numberOfHMetrics': self.font['hhea'].numberOfHMetrics
		}

		self.fontinfo_dict['os2'] = {
			'xAvgCharWidth': self.font['OS/2'].xAvgCharWidth,
			'usWeightClass': self.font['OS/2'].usWeightClass,
			'usWidthClass': self.font['OS/2'].usWidthClass,
			'fsType': self.font['OS/2'].fsType,
			'ySubscriptXSize': self.font['OS/2'].ySubscriptXSize,
			'ySubscriptYSize': self.font['OS/2'].ySubscriptYSize,
			'ySubscriptXOffset': self.font['OS/2'].ySubscriptXOffset,
			'ySubscriptYOffset': self.font['OS/2'].ySubscriptYOffset,
			'ySuperscriptXSize': self.font['OS/2'].ySuperscriptXSize,
			'ySuperscriptYSize': self.font['OS/2'].ySuperscriptYSize,
			'ySuperscriptXOffset': self.font['OS/2'].ySuperscriptXOffset,
			'ySuperscriptYOffset': self.font['OS/2'].ySuperscriptYOffset,
			'yStrikeoutSize': self.font['OS/2'].yStrikeoutSize,
			'yStrikeoutPosition': self.font['OS/2'].yStrikeoutPosition,
			'sFamilyClass': self.font['OS/2'].sFamilyClass,
			'ulUnicodeRange1': self.font['OS/2'].ulUnicodeRange1,
			'ulUnicodeRange2': self.font['OS/2'].ulUnicodeRange2,
			'ulUnicodeRange3': self.font['OS/2'].ulUnicodeRange3,
			'ulUnicodeRange4': self.font['OS/2'].ulUnicodeRange4,
			'achVendID': self.font['OS/2'].achVendID,
			#'usFirstCharIndex': self.font['OS/2'].usFirstCharIndex,
			#'usLastCharIndex': self.font['OS/2'].usLastCharIndex,
			'sTypoAscender': self.font['OS/2'].sTypoAscender,
			'sTypoDescender': self.font['OS/2'].sTypoDescender,
			'sTypoLineGap': self.font['OS/2'].sTypoLineGap,
			#'usWinAscent': self.font['OS/2'].usWinAscent,
			#'usWinDescent': self.font['OS/2'].usWinDescent,
			'ulCodePageRange1': self.font['OS/2'].ulCodePageRange1,
			'ulCodePageRange2': self.font['OS/2'].ulCodePageRange2,
			'sxHeight': self.font['OS/2'].sxHeight,
			'sCapHeight': self.font['OS/2'].sCapHeight,
			#'usDefaultChar': self.font['OS/2'].usDefaultChar,
			#'usBreakChar': self.font['OS/2'].usBreakChar,
			#'usMaxContext': self.font['OS/2'].usMaxContext
		}

		self.fontinfo_dict['os2_panose'] = {
			'bFamilyType': self.font['OS/2'].panose.bFamilyType,
			'bSerifStyle': self.font['OS/2'].panose.bSerifStyle,
			'bWeight': self.font['OS/2'].panose.bWeight,
			'bProportion': self.font['OS/2'].panose.bProportion,
			'bContrast': self.font['OS/2'].panose.bContrast,
			'bStrokeVariation': self.font['OS/2'].panose.bStrokeVariation,
			'bArmStyle': self.font['OS/2'].panose.bArmStyle,
			#'bLetterform': self.font['OS/2'].panose.bLetterform,
			'bMidline': self.font['OS/2'].panose.bMidline,
			'bXHeight': self.font['OS/2'].panose.bXHeight
		}

		self.fontinfo_dict['post'] = {
			'formatType': self.font['post'].formatType,
			'italicAngle': self.font['post'].italicAngle,
			'underlinePosition': self.font['post'].underlinePosition,
			'underlineThickness': self.font['post'].underlineThickness,
			'isFixedPitch': self.font['post'].isFixedPitch,
			'minMemType42': self.font['post'].minMemType42,
			'maxMemType42': self.font['post'].maxMemType42,
			'minMemType1': self.font['post'].minMemType1,
			'maxMemType1': self.font['post'].maxMemType1
		}

		#self.fontinfo_dict['glyphnames'] = self.font.getGlyphOrder()


	def addInfo(self, dictionary_key, font_object):
		try:
			self.fontinfo_dict[dictionary_key]	= font_object.string
		except:
			self.fontinfo_dict[dictionary_key]	= ''

class Export:
	def __init__(self, all_fontinfos):
		self.all_fontinfos = all_fontinfos
		print 'Exporting to', export_filename, '...'

	def console(self):
		pprint.pprint(all_fontinfos)


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
	f = GetFontInfo(path)
	all_fontinfos.append(f.fontinfo_dict)

exportdata = Export(all_fontinfos)
exportdata.console()
#exportdata.CSV()