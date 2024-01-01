What is a server?
                 server is a computer program or process that provides 
                 functionality for other programs or devices, called “clients”
                 . This architecture is called the client-server model. 
                 Servers can provide various functionalities, often called
                 “services”, such as sharing data or resources among multiple
                  clients or performing computations for a client.
What is the role of the domain name?
             To provide a human-friendly alias for an IP Address. For example,
             the domain name www.wikipedia.org is easier to recognize and 
             remember than 91.198.174.192. The IP address and domain name
             alias is mapped in the Domain Name System (DNS)
The type of DNS record www is in www.foobar.com.
             www.foobar.com uses an A record. This can be checked by running
             dig www.foobar.com.Note: the results might be different but for 
              the infrastructure in this design, an A record is used. Address
              Mapping record (A Record)—also known as a DNS host record,
              stores a hostname and its corresponding IPv4 address.
what is the role of web server?
             It is responsible for storing and broadcasting web pages over
             the internet to users who request them. When a user loads a 
             website, the web server retrieves the relevant files and sends
             them to the user’s browser so that the user can interact with 
             them.
What is the role of the application server?
              An application server is a type of server that provides a 
              platform for running applications. It is designed to install, 
              operate, and host applications and associated services for 
              end-users, IT services, and organizations.
What is the role of the database?
             A database is a collection of data that is organized and stored 
             in a computer system. It can be accessed or stored in a computer
             system. It can be managed through a Database Management System 
            (DBMS), a software used to manage data. The primary goal of a 
            database system is to facilitate data retrieval and provide a 
            dependable storage platform for essential data.
What is the server using to communicate with the computer of the user requesting the website?
            When a user requests a website, the web browser sends an HTTP 
            request to the web server through its IP address, as published 
            in DNS. The web server then completes the acknowledgment of its 
            side of the TCP connection and sends HTTP responses to the browser
             to retrieve the content. The browser retrieves the content from 
             the HTTP packets and displays it accordingly.

There are multiple SPOF (Single Point Of Failure) in this infrastructure.
For example, if the MySQL database server is down, the entire site would be down.

Downtime when maintenance needed.
When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.

Cannot scale if there's too much incoming traffic.
It would be hard to scale this infrastructure becauses one server contains the required components. The server can quickly run out of resources or slow down when it starts receiving a lot of requests.



