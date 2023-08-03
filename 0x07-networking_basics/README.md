## Tasks

### 0. OSI model


OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

-   The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
-   The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230803T145746Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a67dc520aa2b3efe1b8903d6a91694f96d7acdd03a8050dd5b1a411b54ca8c4c)

In this project we will mainly focus on:

-   The Transport layer and especially TCP/UDP
-   On the Network layer with IP and ICMP

The image bellow describes more concretely how you can relate to every level.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230803T145746Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1331267143c849c903048b39677f32801892ac7b4271948e302444c661e8812f)


What is the OSI model?

1.  Set of specifications that network hardware manufacturers must respect
2.  The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3.  The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

1.  Alphabetically
2.  From the lowest to the highest level
3.  Randomly



### 1. Types of network


LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

What type of network a computer in local is connected to?

1.  Internet
2.  WAN
3.  LAN

What type of network could connect an office in one building to another office in a building a few streets away?

1.  Internet
2.  WAN
3.  LAN

What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

1.  Internet
2.  WAN
3.  LAN


### 2. MAC and IP address


What is a MAC address?

1.  The name of a network interface
2.  The unique identifier of a network interface
3.  A network interface

What is an IP address?

1.  Is to devices connected to a network what postal address is to houses
2.  The unique identifier of a network interface
3.  Is a number that network devices use to connect to networks


### 3. UDP and TCP

-   Which statement is correct for the TCP box:
    1.  `It is a protocol that is transferring data in a slow way but surely`
    2.  `It is a protocol that is transferring data in a fast way and might loss data along in the process`
-   Which statement is correct for the UDP box:
    1.  `It is a protocol that is transferring data in a slow way but surely`
    2.  `It is a protocol that is transferring data in a fast way and might loss data along in the process`
-   Which statement is correct for the TCP worker:
    1.  `Have you received boxes x, y, z?`
    2.  `May I increase the rate at which I am sending you boxes?`


### 4. TCP and UDP ports

Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

-   **22** for SSH
-   **80** for HTTP
-   **443** for HTTPS

Note that a specific IP + port = socket

Write a Bash script that displays listening ports:

-   That only shows listening sockets
-   That shows the PID and name of the program to which each socket belongs

### 5. Is the host on the network


The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command `ping` uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

