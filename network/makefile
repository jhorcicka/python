
PORT=12345

all: clear client

client: client.py
	./client.py

server: killport server.py
	./server.py

killport: 
	killport $(PORT)

clear: 
	clear

