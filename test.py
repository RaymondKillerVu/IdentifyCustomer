import json
import requests
import base64
from datetime import datetime
from ftplib import FTP
import time
import os

import threading
from MqttClient import MQTTClient
ftp = FTP()
ftp.set_debuglevel(2)
ftpHost = "new-thd.dddns.net"
ftpUser = "ltkftp"
ftpPass = "aNdIcKerbanDeNUmBEtIcYoFUraTHe"
ftpPath = "/files/save/in"

def saveImageFtp(_host,_user,_pass,_path,_image):
    FtpImage = "Image_" + datetime.now().strftime("%b-%d-%Y_%H_%M_%S")+".jpg"
    if not os.path.isfile(_image):
        print "Image path from Mqtt is not exist"
        return False
    fp = open(_image, 'rb')
    ftp.connect(_host)
    ftp.login(_user,_pass)
    ftp.cwd(_path)
    ftp.storbinary('STOR %s' % FtpImage, fp)
    fp.close()
    ftp.quit()
    return (_path + "/" + FtpImage)

t= {"ddd":1,"dfg":"fgag"}
_ImageBase64 = "/home/killer/Desktop/1.jpg"
try:
	k = json.dumps(t)
	print json.loads(k)
	if t["ddd"] == 1:
		k = json.loads(k)
		if k["dddda"] == 3:
			print k
	print t
	#FtpImage = saveImageFtp(ftpHost,ftpUser,ftpPass,ftpPath,_ImageBase64)
except Exception as e:
	print e
	print "error"

print "killer"
