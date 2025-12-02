[[TCP-IP Protocol Architecture]]

# Application Architectures
## Client-Server
- Server
	- Always-on host
	- Permanent IP
- Client
	- Communicate with server
	- No client-client connections
	- May be intermittently connected
	- May have dynamic IPs
## Peer-To-Peer P2P
- No always-on server
- Arbitrary end systems directly communicate
- Peers are intermittently connected and change IPs
- **Highly scalable but difficult to manage**
## Hybrid Architecture
### Napster
- File transfer is P2P
- File search is centralized
	- Peers query central server to locate content
### Instant Messaging
- Chatting between two users is P2P
- Presence detection/location is centralized
	- User registers IP with central server upon coming online
	- User contacts central server to find IP addresses of buddies
- WhatsApp
	- Client-server: core messaging functions
	- P2P: File transfers
# Electronic Mail
![[Pasted image 20251106144714.png]]
- Three major components:
## User Agent
- Aka "mail reader"
- Tasked with composing, editing, and reading mail
- Eg: Eudora, outlook, elm. netscape manager
- Outgoing, incoming messages stored on server
## Mail Servers
- Mailbox contains incoming messages for user
- Message queue of outgoing (to be sent) mail messages
- SMTP Protocol between mail servers to send mail
	- Client: sending mail server
	- "Server": receiving mail server
## Simple Mail Transfer Protocol SMTP
- Uses TCP to reliably transfer email from client to server
	- Dedicated port 25
- Direct transfer: sending server to receiving server
- Three phases of transfer
	- Handshaking (greeting)
	- Transfer of messages
	- Closure
- Messages must in ASCII or Unicode (eg UTF-8)
## Example Scenario: Alice Emails Bob
![[Pasted image 20251106145801.png]]
1. Alice uses User Agent to compose message and send to `bob@school.edu`
2. Alice's UA sends message to her mail server; message placed in message queue
3. Client side of SMTP opens TCP connection with Bob's mail server
4. SMTP client sends Alice's message over the TCP connection
5. Bob's mail server places the message in Bob's mailbox
## Mail Message Format
- SMTP for exchange between servers
- RFC 822: standard for text message format
- ![[Pasted image 20251106150011.png]]
### MIME: Multipurpose Internet Mail Extension
- Additional lines in message header declare MIME content type
- ![[Pasted image 20251106145930.png]]
## User Mail Access Protocols
### POP: Post Office Protocol \[RFC 1939\]
- After authorization, user can download and usually delete emails from the server
- For single-device access or offline storage of emails
- When you go to post office, they just give you the mail and it's your responsibility now
![[Pasted image 20251106150250.png]]
- Auth phase
	- Client commands:
		- User: declare username
		- Pass: password
	- Server responses:
		- +OK
		- -ERR
- Transaction phase, client:
	- list: list message numbers
	- retr: retrieve message by number
	- dele: delete
	- quit
### IMAP: Internet Mail Access Protocol
- Keep all emails on the server
	- Manipulation of stored messages are done on the server
	- For multi-device users
### HTTP: Hotmail, Yahoo!, Gmail etc
# Web and HTTP
## Jargon
- A web page consists of objects
- Objects can be HTML files, JPEG images, Java applets, audio files, etc
- Web page consists of a base HTML file which includes several referenced objects
- Each object is addressable by a URL
	- Uniform Resource Locator
## HTTP Overview
- Web's application layer protocol
- Operates on a client/server model
	- Client: browser that requests, receives, and presents Web objects to the user
	- Server: Web server sends objects in response to requests
- RFCs:
	- HTTP 1.0: RFC 1945
	- HTTP 1.1: RFC 2068
- HTTP is stateless:
	- Server maintains no information about past requests
- HTTP uses TCP
	- Client initiates TCP connection (creates socket) to server on dedicated port 80
	- Server accepts TCP connection from client
	- HTTP messages exchanged between server and client
	- TCP connection closed
## User-server State: Cookies
- Cookies are a file kept on user's host, managed by user's browser
- Used to access functionality from back-end database at website
- A cookie is a value that the server uses to differentiate users and address their unique states
- Cookies can bring:
	- Authorization
	- Shopping carts
	- Recommendations
	- User session state (Web e-mail)
- ![[Pasted image 20251106150948.png]]
## Web Caches (Proxy Server)
![[Pasted image 20251106151620.png]]
- Goal is to satisfy client requests without involving the origin server
- A cache or proxy server is typically closer to the end user than the origin server
- Brows sends all HTTP requests to cache
	- If cache hit: return object
	- If cache miss: Send request to origin server, then send object to client
- Cache acts as both client and server
- Typically, cache is installed by ISP
### Why Web Caching?
- Reduce response time
- Reduce traffic on an institution's access link
### Caching Example
![[Pasted image 20251106151814.png]]
#### Assumptions
- Average object size = 100Kb
- Avg request rate from institution's browsers to origin servers = 15 sec
- Delay from institutional router to any origin server and back to router = 2 sec
- The access link is the bottleneck, it is slow and fully utilized
##### Consequences
- Utilization on LAN = 15%
- Utilization on access link = 100%
- Total delay = Internet delay + access delay + LAN delay
- = 2 sec + minutes + milliseconds
### Possible Solution
- Increase bandwidth of access link to 10 Mbps
#### Consequences
- Utilization on LAN = 15%
- Utilization on access link = 15%
- Total delay = 2 sec + msecs + msecs
- Often a costly upgrade
#### Install Cache
- Suppose hit rate is 0.4
#### Consequences
- 40% of requests will be satisfied almost immediately
- 60% of requests will be satisfied by the origin server
- Utilization of access link reduced to 60%, resulting in negligible delays
