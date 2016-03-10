#!/usr/bin/python
import aiml
import commands
import os
import sys
k = aiml.Kernel()
k.learn("default.aiml")
k.setBotPredicate("age","15")
k.setBotPredicate("foolball","Tafea")
k.setBotPredicate("birthday","Nov. 23, 2015")
k.setBotPredicate("birthplace","Port Vila vanuatu")
k.setBotPredicate("botmaster", "botmaster")
k.setBotPredicate("boyfriend","I am single")
k.setBotPredicate("celebrity","Jina")
k.setBotPredicate("city","Port Vila")
k.setBotPredicate("country","Vanuatu")
k.setBotPredicate("email","Your email")
k.setBotPredicate("etype","9")
k.setBotPredicate("family","chat bot")
k.setBotPredicate("favoriteactor","Tom Hanks")
k.setBotPredicate("favoritecolor","green")
k.setBotPredicate("favoritefood","electricity")
k.setBotPredicate("favoritequestion","What's your favorite movie?")
k.setBotPredicate("gender","female")
k.setBotPredicate("girlfriend","I am just a little girl")
k.setBotPredicate("question","What's your favorite movie?")
k.setBotPredicate("religion","Pesbytrian")
k.setBotPredicate("state","Vanuatu")
k.setBotPredicate("website","wehackdem.blogspot.com")

while True:
    input = raw_input("Ask me anything: ")
    if input == "quit":
      sys.exit(0)
    response = k.respond(input)
    print 'Jarvis: ', response
 
    # and as speech
    print commands.getoutput("/usr/bin/espeak -v en+f4 -p 99 -s 160 2>/dev/null \"" + response + "\"")
    #("espeak --stdout \"" + response + "\" | aplay")
    #("/usr/bin/espeak -v en+f4 -p 99 -s 160 \"" + response + "\" | aplay")
   
   #for command
    if response == "starting up firefox":
 	os.system("firefox"); 
    elif response == "starting google":
      	os.system("gnome-open http://www.google.com");    
    elif response == "ok i will show it in a second":
  	os.system("gnome-open /root/images.jpeg"); 
    elif response == "starting the music now":
      	os.system("mocp -p");    
    elif response == "stoping the music":
      	os.system("mocp -s");    
    elif response == "playing the next song":
      os.system("mocp -f");
  #   elif response == "preavious song":
   #    os.system("mocp -r");           
    elif response == "Hey.. stoping the music":
      os.system("mocp -s");
    elif response == "That's cool.. stoping the music":
     os.system("mocp -s");
    elif response == "Far out.. stoping the music":
      os.system("mocp -s");
    elif response == "Whoa.. stoping the music":
      os.system("mocp -s");
    elif response == "Ah.. stoping the music":
      os.system("mocp -s");
    elif response == "And?. stoping the music":
      os.system("mocp -s");
    elif response == "Really.. stoping the music":
      os.system("mocp -s");
    elif response == "Really.. stoping the music":
      os.system("mocp -s");
    elif response == "That's interesting.. stoping the music":
      os.system("mocp -s");
    elif response == "Aha.. stoping the music":
      os.system("mocp -s");
    elif response == "Blimey.. stoping the music":
      os.system("mocp -s");
    elif response == "Hmm.. stoping the music":
      os.system("mocp -s");
    elif response == "Next question?. stoping the music":
      os.system("mocp -s");
    elif response == "Mmm.. stoping the music":
      os.system("mocp -s");
    elif response == "Right on.. stoping the music":
      os.system("mocp -s");
    elif response == "Woe!. stoping the music":
      os.system("mocp -s");
    elif response == "I see.. stoping the music":
      os.system("mocp -s");
    elif response == "Far out.. stoping the music":
      os.system("mocp -s");
    elif response == "Yay.. stoping the music":
      os.system("mocp -s");
    elif response == "Next question?. stoping the music":
      os.system("mocp -s");
    elif response == "Hurrah!. stoping the music":
      os.system("mocp -s");
    elif response == "Tell me more.. stoping the music":
      os.system("mocp -s");
    elif response == "Come on.. stoping the music":
      os.system("mocp -s");
    elif response == "Take it easy.. stoping the music":
      os.system("mocp -s");
    elif response == "Are you shy?. stoping the music":
      os.system("mocp -s");
    elif response == "Ahem.. stoping the music":
      os.system("mocp -s");
   
    elif response == "It's all good.. starting the music now":
      os.system("mocp -p");
   
    elif response == "Give me a break.. starting the music now":
      os.system("mocp -p");

    elif response == "It goes without saying.. starting the music now":
      os.system("mocp -p");

    elif response == "Take it easy.. starting the music now":
      os.system("mocp -p");

    elif response == "Come on.. starting the music now":
      os.system("mocp -p");
    elif response == "Hmm.. starting the music now":
      os.system("mocp -p");
    elif response == "Excuse me!. starting the music now":
      os.system("mocp -p");

    elif response == "And?. starting the music now":
      os.system("mocp -p");

    elif response == "Yay.. starting the music now":
      os.system("mocp -p");

    elif response == "That's interesting.. starting the music now":
      os.system("mocp -p");

    elif response == "Are you shy?. starting the music now":
      os.system("mocp -p");

    elif response == "Come on.. starting the music now":
      os.system("mocp -p");

    elif response == "Give me a break.. starting the music now":
      os.system("mocp -p");

    elif response == "Yeah that's right.. starting the music now":
      os.system("mocp -p");

    elif response == "Dude!. starting the music now":
      os.system("mocp -p");

    elif response == "OK.. starting the music now":
      os.system("mocp -p");

    elif response == "Yippee!. starting the music now":
      os.system("mocp -p");

    elif response == "Alright then.. starting the music now":
      os.system("mocp -p");

    elif response == "Aha.. staring the muisc now":
      os.system("mocp -p");
    elif response == "It's all good.. starting the music now":
      os.system("mocp -p");

    elif response == "Groovy.. starting the music now":
      os.system("mocp -p");

    elif response == "That's interesting.. starting the music now":
      os.system("mocp -p");

    elif response == "It's all good.. starting the music now":
      os.system("mocp -p");
   
    elif response == "Uh.. starting the music now":
      os.system("mocp -p");
    elif response == "See you later. Alright then.":
      os.system(sys.exit(0));
    elif response == "See you later. Ayuh":
 	os.system(sys.exit(0));
    elif response == "See you later. Thanks for the compliment.":
 	os.system(sys.exit(0));
    elif response == "See you later.":
 	os.system(sys.exit(0));
    elif response == "Bye.":
 	os.system(sys.exit(0));
    elif response == "Bye for now.":
 	os.system(sys.exit(0));
    elif response == "Goodbye.":
 	os.system(sys.exit(0));
    elif response == "Sayonara.":
 	os.system(sys.exit(0));
    elif response == "Bye bye.":
 	os.system(sys.exit(0));
    elif response == "Until next time.":
 	os.system(sys.exit(0)); 
