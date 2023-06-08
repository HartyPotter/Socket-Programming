# Socket-Programming

The client code uses TCP connection, it sends a request to the TCP socket to initiate a 
connection, then the server code listens for a connection from the client. The user in the client 
end then enters a number from 1 to 100. If the number is more than 100 or less than 1, the server 
prints an error message and ends the connection.
The client socket then sends a formatted message to the server. The server receives the message 
and print the client name, the server name, client number, and the server number then it 
computes the sum and prints it.
The server sends a message to the client containing the name of the server, and its number.
The client reads the message sent by the server and display its name, the server’s
name, its integer value, and the server’s integer value, and then computes the sum. The
client then terminates after releasing any created sockets.

# Threading
The code is modified to enable threading on the server. The server is to be a concurrent server - that is a server that waits on the welcoming socket and then creates a new thread or process to handle the incoming request.
