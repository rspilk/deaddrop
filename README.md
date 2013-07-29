deaddrop
========

Digital Dead Drop

You are free to use this however you want. I wrote this a few years ago after reading the Ender's series of books by 
Orson Scott Card. I was inspired to create a method of transmitting text in a one-way fashion for later retrieval.

With the springing up of concern over the NSA, I thought this was relevant, although not that practical.


My usage of this was as follows.

I ran the site on a Raspberry Pi connected to my home private network. Remote machines which wanted to talk to the
dead drop must be connected to my OpenVPN in order to speak to the 10.0.0.0/24 subnet. This eliminated some of the
issues I saw from injection attacks and whatnot (since you are effectively allowing a user to dump text directly
to your python session).

It goes without saying that this code is considered *UNSAFE* to run. It requires generating your own keys and to
trust the keys made. It also requires allowing the users of the site to insert *RAW* and *UNCHECKED* text into your
site.

I made this for fun, and a way to dump my thoughts and musings to a text file when I rode the bus. And feel like
Bean and the other battle school bratts in their dealings durring the league war!


I hope this inspires you to make something that works better and is much cooler.

Thanks

Tyler Spilker
 

