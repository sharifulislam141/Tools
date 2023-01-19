import os
from colorama import Fore,init

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

init(convert=True)

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE
	c = Fore.CYAN
	g = Fore.GREEN
	w = Fore.WHITE

def clean():
	lines_seen = set()
	outfile = open('dorks.txt', "a")
	infile = open('dorkstest.txt', "r")
	for line in infile:
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	infile.close()
	if os.name == "nt":
		os.system("del dorkstest.txt")
	else:
		os.system("rm -rf dorkstest.txt")
	print(("[{}+{}] Duplicate dorks removed successfully!".format(settings.r,settings.y)))
	print(("\n[{}+{}] Dorks saved as {}dorks.txt{}!".format(settings.r,settings.y,settings.b,settings.y)))


print(("""{}
______           _   ___  ___      _             
|  _  \         | |  |  \/  |     | |              [{}+{}]{} Coded by NullS0UL1337{}
| | | |___  _ __| | _| .  . | __ _| | _____ _ __   [{}+{}]{} Get many sites in minutes!{}
| | | / _ \| '__| |/ / |\/| |/ _` | |/ / _ \ '__|  [{}+{}]{} Facebook : facebook.com/nulls0ul.ofc{}
| |/ / (_) | |  |   <| |  | | (_| |   <  __/ |     [{}+{}]{} Telegran : t.me/NullS0UL{}
|___/ \___/|_|  |_|\_\_|  |_/\__,_|_|\_\___|_|     [{}+{}]{} Github   : github.com/NullS0UL{}
                                                 
""".format(settings.c,settings.r,settings.c,settings.g,settings.c,settings.r,settings.c,settings.g,settings.c,settings.r,settings.c,settings.g,settings.c,settings.r,settings.c,settings.g,settings.c,settings.r,settings.c,settings.g,settings.c,settings.r,settings.c,settings.g,settings.c)))

print(("="*80))
text = input("\n{}[{}~{}] Please input any text : {}".format(settings.g,settings.r,settings.g,settings.w))
words = text.split(" ")
print(("{}[{}!{}] ".format(settings.g,settings.r,settings.g) + str(len(words)) + "{} text verified! Now let's make some dorks!\n".format(settings.g)))
print(("="*80))
print(("\n{}[{}1{}] WordPress".format(settings.c,settings.r,settings.c)))
print(("{}[{}2{}] Joomla".format(settings.c,settings.r,settings.c)))
print(("{}[{}3{}] OpenCart".format(settings.c,settings.r,settings.c)))
cms = input("\n{}[{}?{}] Which CMS dorks do you want to make? : ".format(settings.g,settings.r,settings.g))
if cms == "1":
	print(("{}[{}+{}] Prepared dorks:".format(settings.c,settings.r,settings.c) + "\n"))
	wpdorks = {'("Comment on Hello world!")',
			   '("Comentarios en Hello world!")',
			   '("author/admin")',
			   '("uncategorized/hello-world")',
			   '("category/sin-categoria")',
			   '("uncategorized")',
			   '("Proudly powered by WordPress")',
			   '("Welcome to WordPress. This is your first post.")',
			   '("Just another WordPress site")',
			   '("Mr WordPress on Hello world!")',
			   '("/wp/hello-world/")'}
	for wpdork in wpdorks:
		for word in words:
			print((wpdork + word))
			try:
				with open("dorkstest.txt","a") as f:
					f.write(wpdork + word + "\n")
			except:
				pass

elif cms == "2":
	print(("[{}+{}] Prepared dorks:".format(settings.r,settings.y) + "\n"))
	jmdorks = {'index.php?option=com_users ',
			   'index.php?option=com_jce ',
			   '("com_user")'}
	for jmdork in jmdorks:
		for word in words:
			print((jmdork + word))
			try:
				with open("dorkstest.txt","a") as f:
					f.write(jmdork + word + "\n")
			except:
				pass
	eval(input("\n[{}*{}] Please enter to remove duplicate dorks...".format(settings.r,settings.y)))
	clean()

elif cms == "3":
	print(("[{}+{}] Prepared dorks:".format(settings.r,settings.y) + "\n"))
	ocdorks = {'index.php?route=product ',
			   'index.php?route='}
	for ocdork in ocdorks:
		for word in words:
			print((ocdork + word))
			try:
				with open("dorkstest.txt","a") as f:
					f.write(ocdork + word + "\n")
			except:
				pass
	eval(input("\n[{}*{}] Please hit enter to remove duplicate dorks...".format(settings.r,settings.y)))
	clean()

else:
	print(("[{}-{}] Invalid Optionn! Tool closed!".format(settings.r,settings.y)))