import webbrowser
import time
socialMedia =["www.youtube.com", "www.facebook.com"]

def open_urls(Urls):
	for i in Urls:
		webbrowser.open_new_tab(i)
		
def main():
	open_urls(socialMedia)
	
main()
