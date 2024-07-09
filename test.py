# encoding=utf8
 
'''
Python批量识别图片中的文字并保存到txt文档中
'''
 
# 导入包
from PIL import Image
import string,re,os
import pytesseract
 
 
# 定义方法
def imgtostr(imgpath):
	'''识别图片中的所有文字'''
	image = Image.open(imgpath)
	text = pytesseract.image_to_string(image, 
	lang = 'chi_sim') # 使用简体中文解析图片
	return text
	#return text.replace("\n", "") # 去掉换行
 
 
def writefile(txtpath,strstr):
	'''将文字累加并写入txt文档'''
	with open(txtpath, "a", encoding= "utf-8") as f:
		f.write(strstr) # 写入文件
		f.write("\n\n")
 
 
if __name__ == '__main__':
 
	# 存放待识别图片的目录,支持所有图片格式
	imgpath = r'C:\Program Files\Tesseract-OCR\img'
 
	# 识别结果保存的txt文件路径
	txtpath = r'C:\Program Files\Tesseract-OCR\word\word.txt'
 
	# 开始执行
	for a, b, filenames in os.walk(imgpath):
		toltal = 0
		for fe in filenames:
			grpaimg = imgpath + '/' + fe
			print(grpaimg)
			textddd = imgtostr(grpaimg)
			writefile(txtpath, grpaimg+":\n"+textddd)
			#print(grpaimg, textddd, end="\n\n")
 
