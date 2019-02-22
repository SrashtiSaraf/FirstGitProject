import webbrowser
import time
socialMedia =["www.google.com","www.youtube.com", "www.facebook.com",]

f = open("myfile.txt", "a")
f.write("Adding more content")
f.close()

def open_urls(Urls):
	for i in Urls:
		webbrowser.open_new_tab(i)
		
def main():
	open_urls(socialMedia)
	
main()

#Added some comments
