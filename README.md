# finding-competitors-CNN
CNN Business gives a short list of some main competitors for every stock. This code aims to web scrape CNN Business' web pages in order to get the main competitors they identified for an array of stocks that we give as an input to the program.
As the web scrapping takes some time, I also decided to integrate some code to send half of the array of stocks to another computer to accelerate the process. We send this list of stock via an IPV4 connection by simply setting a server and a client with python's "socket" module.
