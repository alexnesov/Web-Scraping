# Web Scraping
CNN Business gives a short list of some main competitors for every stock. This code aims to web scrape CNN Business' web pages in order to get the main competitors they identified for an array of stocks that we give as an input to the program.
As the web scrapping takes some time, I also decided to integrate some code to send half of the array of stocks to another computer to accelerate the process. We send this list of stocks via an IPV4 connection by simply setting a server and a client with python's "socket" module.

<h5> *Update </h5>

As stated above, the aim was to indeed identify more "direct" competitors - so to speak - than those we could find in the usual sectors and sub-sectors catageroizations.
CNN Business'competitors seemed interesting, eventhough I don't know the criteria on which they based who is a competitor or not.
Todays sector boundaries are very blurry indeed. Who is the main competitor of Tesla? General Motors? Nvidia (they  partnered with Mercedes), or maybe even Apple?

One of the most convincing source is maybe yahoo finance's "People who watch this stock also watch this other..". Their powerful algorithm's (clusterisation) work for us and we scrap.


<h4> Websites targeted: </h4>

* CNN Business
* Stocktwits: to monitor nb of watchers for a set of selected stocks
* Yahoo finance


