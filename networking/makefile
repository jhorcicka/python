
PORT=12345

all: clear client

client: http_client.py
	./http_client.py

server: killport server.py
	./server.py

killport: 
	killport $(PORT)

clear: 
	clear

