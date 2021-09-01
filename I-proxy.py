import requests , sys , os

if len(sys.argv) != 7:
	print('''Usage : python3 I-proxy.py -f [file.txt] -t [type of proxies] -o [output folder] 

		help:
		-f the PATH of file contain the proxies you want to check
		-t http,https,socks4,socks5 or ALL to check all types
		-o name of folder to save the output in

		EX:

		python3 I-proxy.py -f proxies.txt -t ALL -o out1
		python3 I-proxy.py -f proxies.txt -t socks5 -o out2''')
	exit()

argv = sys.argv
args = {argv[1]:argv[2] , argv[3]:argv[4] , argv[5]:argv[6]}


######FILE##############

with open(args['-f']) as f:
	lista = list(dict.fromkeys(f.read().split('\n')))

########OUTPUT##########

pwd = os.getcwd()
if not os.path.exists(os.path.join(pwd,args['-o'])):
	os.mkdir(os.path.join(pwd,args['-o']))
os.chdir(os.path.join(pwd,args['-o']))
#########TYPE############

if args['-t'].lower() == 'all' :
	typee = ['http' , 'socks5' , 'socks4' , 'https']
else:
	typee = []
	typee.append(args['-t']) 

print('====================')
print('[!] RUNNING ....')
print('====================')


class Proxy:
	def __init__(self , proxy):
		self.proxy = proxy
		self.valid_for = []


	@staticmethod
	def chk(typee , prox):
		try:
			res = requests.get('http://httpbin.org/ip' , proxies={'http':f'{typee}://{prox}'} , timeout=5)
			return True
		except:
			return False

	def prox_type(self , typee):
		if self.chk(typee , self.proxy):
			self.valid_for.append(typee)
			with open(f'{typee}.txt' , 'a') as f:
				f.write(self.proxy + '\n')



for prox in lista:

	proxy = Proxy(prox)

	for typex in typee:
		proxy.prox_type(typex)
	if proxy.valid_for:
		print(f'[-] PROXY : {proxy.proxy} === [ {" | ".join(proxy.valid_for)} ]')


print('Finished!!')
print('CODER : https://github.com/ph-root/')
