# AMAZON CLOUD ARCHITECT 

### What is NAT?

NAT: Network Address Translation (NAT) is the process where a network device, usually a firewall, assigns a public address to a computer (or group of computers) inside a private network
In AWS world:
We can use a NAT instance in a public subnet in a VPC to enable instances in the private subnet to initiate outbound IPv4 traffic to the Internet or other AWS services but prevent the instances from receiving inbound traffic initiated by someone on the Internet.

### Explain the difference between TCP and UDP?

TCP Transmission Control Protocol - more reliable as it expects acknowledgement of packets sent; connection bound

UDP User Datagram Protocol - less reliable but good for speed, eg. video conferencing, broadcast services, etc. ; connection-less


### How do you build a web application which can handle 100 million active session?

### How do you migrate 5000 servers from on-premise to cloud?

### How do you move 2billion files from on-premise to cloud?

It depends on the size of the files. On an average if the file size is about 1MB, then we are talking about transferring nearly a Petabyte(PB) of data. Then use AWS Snowball, they will send a drive to which you copy the files and ship it to them to upload it.

https://www.youtube.com/watch?v=vg5onp8TU6Q&list=PLhr1KZpdzukdRxs_pGJm-qSy5LayL6W_Y&index=2

### Differences between SQL and No Relational DDBB?

### CAP theorem

https://www.naukri.com/learning/articles/top-aws-interview-questions-answers/
