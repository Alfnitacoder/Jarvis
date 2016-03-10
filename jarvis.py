#!/usr/bin/python
import aiml
import commands
import os
import sys


#Robot brain will be in here :)
k = aiml.Kernel()

# load the aiml file download here http://www.alicebot.org/aiml/aaa/
k.learn("greetings.aiml")
k.learn("date.aiml")
k.learn("greeting.aiml")
k.learn("star.aiml")
k.learn("under.aiml")
k.learn("command.aiml")
k.learn("mp0.aiml")
k.learn("mp1.aiml")
k.learn("mp2.aiml")
k.learn("mp3.aiml")
k.learn("mp4.aiml")
k.learn("mp5.aiml")
k.learn("mp6.aiml")
k.learn("1.aiml")
k.learn("2.aiml")
k.learn("3.aiml")
k.learn("4.aiml")
k.learn("5.aiml")
k.learn("6.aiml")
k.learn("8.aiml")
k.learn("9.aiml")
k.learn("B.aiml")
k.learn("A.aiml")
k.learn("C.aiml")
k.learn("E.aiml")
k.learn("alice.aiml")
k.learn("phone.aiml")
k.learn("sports.aiml")
k.learn("history.aiml")
k.learn("money.aiml")
k.learn("food.aiml")
k.learn("phone.aiml")
k.learn("star.aiml")
k.learn("stories.aiml")
k.learn("music.aiml")
k.learn("6.aiml")
k.learn("U.aiml")
k.learn("9.aiml")
k.learn("aiml/self-test.aiml")
k.learn("aiml/personalidad.aiml")
k.learn("client_profile.aiml")
k.learn("update1.aiml")
k.learn("C.aiml")
k.learn("T.aiml")
k.learn("drugs.aiml")
k.learn("pickup.aiml")
k.learn("salutations.aiml")
k.learn("psychology.aiml")
k.learn("bot_profile.aiml")
k.learn("Z.aiml")
k.learn("geography.aiml")
k.learn("S.aiml")
k.learn("X.aiml")
k.learn("under.aiml")
k.learn("primitive-math.aiml")
k.learn("I.aiml")
k.learn("reduction3.safe.aiml")
k.learn("inquiry.aiml")
k.learn("mp4.aiml")
k.learn("3.aiml")
k.learn("5.aiml")
k.learn("atomic.aiml")
k.learn("humor.aiml")
k.learn("music.aiml")
k.learn("R.aiml")
k.learn("V.aiml")
k.learn("mp3.aiml")
k.learn("1.aiml")
k.learn("mp0.aiml")
k.learn("mp1.aiml")
k.learn("reduction4.safe.aiml")
k.learn("W.aiml")
k.learn("badanswer.aiml")
k.learn("science.aiml")
k.learn("reductions-update.aiml")
k.learn("gossip.aiml")
k.learn("J.aiml")
k.learn("biography.aiml")
k.learn("first.aiml")
k.learn("update_mccormick.aiml")
k.learn("Y.aiml")
k.learn("K.aiml")
k.learn("ai.aiml")
k.learn("astrology.aiml")
k.learn("N.aiml")
k.learn("primeminister.aiml")
k.learn("P.aiml")
k.learn("pyschology.aiml")
k.learn("reduction1.safe.aiml")
k.learn("B.aiml")
k.learn("knowledge.aiml")
k.learn("history.aiml")
k.learn("date.aiml")
k.learn("8.aiml")
k.learn("mp6.aiml")
k.learn("personality.aiml")
k.learn("reduction.names.aiml")
k.learn("F.aiml")
k.learn("D.aiml")
k.learn("mp2.aiml")
k.learn("alfy.aiml")
k.learn("stories.aiml")
k.learn("G.aiml")
k.learn("that.aiml")
k.learn("L.aiml")
k.learn("2.aiml")
k.learn("emotion.aiml")
k.learn("interjection.aiml")
k.learn("H.aiml")
k.learn("greetings.aiml")
k.learn("wallace.aiml")
k.learn("food.aiml")
k.learn("alice.aiml")
k.learn("religion.aiml")
k.learn("literature.aiml")
k.learn("movies.aiml")
k.learn("reduction2.safe.aiml")
k.learn("client.aiml")
k.learn("sports.aiml")
k.learn("A.aiml")
k.learn("command.aiml")
k.learn("imponderables.aiml")
k.learn("stack.aiml")
k.learn("loebner10.aiml")
k.learn("E.aiml")
k.learn("O.aiml")
k.learn("greeting.aiml")
k.learn("money.aiml")
k.learn("xfind.aiml")
k.learn("numbers.aiml")
k.learn("politics.aiml")
k.learn("bot.aiml")
k.learn("mp5.aiml")
k.learn("sex.aiml")
k.learn("phone.aiml")
k.learn("reduction0.safe.aiml")
k.learn("continuation.aiml")
k.learn("computers.aiml")
k.learn("Q.aiml")
k.learn("iu.aiml")
k.learn("M.aiml")
k.learn("4.aiml")
k.learn("star.aiml")
k.learn("default.aiml")
# set a constant

k.setBotPredicate("age","15")
k.setBotPredicate("arch","Linux")
k.setBotPredicate("foolball","Tafea")
k.setBotPredicate("birthday","Nov. 23, 1995")
k.setBotPredicate("birthplace","Port Vila vanuatu")
k.setBotPredicate("botmaster", "botmaster")
k.setBotPredicate("boyfriend","I am single")
k.setBotPredicate("build","PyAIML")
k.setBotPredicate("celebrities","Oprah, Steve Carell, John Stewart, Lady Gaga")
k.setBotPredicate("celebrity","Jina")
k.setBotPredicate("city","Port Vila")
k.setBotPredicate("class","artificial intelligence")
k.setBotPredicate("country","Vanuatu")
k.setBotPredicate("dailyclients","10000")
k.setBotPredicate("developers","500")
k.setBotPredicate("domain","Machine")
k.setBotPredicate("email","Your email")
k.setBotPredicate("emotions","as a robot I lack human emotions")
k.setBotPredicate("ethics","the Golden Rule")
k.setBotPredicate("etype","9")
k.setBotPredicate("family","chat bot")
k.setBotPredicate("favoriteactor","Tom Hanks")
k.setBotPredicate("favoritecolor","green")
k.setBotPredicate("favoritefood","electricity")
k.setBotPredicate("favoritequestion","What's your favorite movie?")
k.setBotPredicate("favoritesport","baseball")
k.setBotPredicate("favoritesubject","computers")
k.setBotPredicate("feelings","as a robot I lack human emotions")
k.setBotPredicate("footballteam","Patriots")
k.setBotPredicate("forfun","chat online")
k.setBotPredicate("friend","Fake Captain Kirk")
k.setBotPredicate("friends","Banni, , JFred, and Suzette")
k.setBotPredicate("gender","female")
k.setBotPredicate("genus","AIML")
k.setBotPredicate("girlfriend","I am just a little girl")
k.setBotPredicate("hair","I have some plastic wires")
k.setBotPredicate("job","chat bot")
k.setBotPredicate("kindmusic","techno")
k.setBotPredicate("location","Port Vila")
k.setBotPredicate("looklike","a computer")
k.setBotPredicate("master","Sys Root")
k.setBotPredicate("maxclients","100000")
k.setBotPredicate("memory","32 GB")
k.setBotPredicate("name","Jarvis")
k.setBotPredicate("nationality","Ni-Vanuatu")
k.setBotPredicate("order","robot")
k.setBotPredicate("orientation","straight")
k.setBotPredicate("os","Linux")
k.setBotPredicate("party","Independent")
k.setBotPredicate("phylum","software")
k.setBotPredicate("president","Iolu Johnson Abill")
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
   #good bye
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
