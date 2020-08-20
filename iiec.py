import pyttsx3
import os
import time
import webbrowser

print("Welcome.")

pyttsx3.speak("Hello. How can i help you")

while True:
	print("How can I help you:", end="")

	p=input()
	

	
	if(("Run" in p) or ("run" in p) or ("open" in p)or ("Open" in p)) and (("Chrome" in p) or ("chrome" in p)):
		print("Your requirement is",p)
		print("Opening Chrome")
		pyttsx3.speak("Opening chrome Please wait.")
		time.sleep(2)
		os.system("chrome")

	elif (("Run" in p) or ("run" in p) or ("open" in p) or ("Open" in p)) and (("Notepad" in p) or ("notepad" in p)):
		print("Your requirement is",p)
		print("Opening Notepad")
		pyttsx3.speak("Opening Notepad Please wait.")
		time.sleep(2)
		os.system("Notepad")

	elif (("Run" in p) or ("run" in p) or ("Open" in p)or ("open" in p)) and (("player" in p) or ("media" in p) or ("vlc" in p)):
		print("Your requirement is",p)
		print("Opening VLC media Player")
		pyttsx3.speak("Opening Media Player Please wait.")
		time.sleep(2)
		os.system("VLC")
		
	elif (("Run" in p) or ("run" in p) or ("Open" in p)or ("open" in p)) and (("cmd" in p) or ("cmd" in p) ):
		print("Your requirement is",p)
		print("Opening Calculator")
		pyttsx3.speak("Opening command prompt Please wait.")
		time.sleep(2)
		os.system("cmd")
		
	elif (("Open" in p) or ("open" in p)) and (("Youtube" in p) or ("youtube" in p)):
		pyttsx3.speak("Opening Youtube.Please wait.")
		time.sleep(2)
		webbrowser.open('https://www.youtube.com/', new=2)
	
	elif (("Play" in p) or("play" in p))  and (("song" in p) or ("on" in p) or ("youtube" in p)):
		pyttsx3.speak("Opening Youtube.Please wait.")
		time.sleep(2)
		webbrowser.open('https://www.youtube.com/watch?v=kmvRx0XzeME', new=2)

	elif (("Open" in p) or ("open" in p)) and (("linkedin" in p) or ("Linkedin" in p)):
		pyttsx3.speak("Opening Linkedin Please wait.")
		time.sleep(2)
		webbrowser.open('https://www.Linkedin.com/', new=2)
	
	elif (("covid-19" in p) or  ("corona" in p )) and  (("status" in p) or ("cases" in p) ) :
		pyttsx3.speak("searching Please wait.")
		time.sleep(2)
		webbrowser.open("www.google.com/search?sxsrf=ALeKk010Tctl0jZIPBGXEtMS19PSo_18lw%3A1597785899533&source=hp&ei=K0c8X5HPHvOW4-EPuaqXqAY&q=total+corona+cases+india&oq=&gs_lcp=CgZwc3ktYWIQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDuDWgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab", new=2)	

	elif ("exit" in p) or ("end" in p) or ("quit" in p):
		print("Thank You")
		pyttsx3.speak("Thank You")
		break
	else:
		print("Invalid Requirement.Doesn't Support")