# SmartShark - An IDS with some Machine Learning

The SmartShark project is the fruit of the work of Valentin De Matos and Quentin Fringhian, two Epitech studients managed by the Poc assosiation. The project started in April 2020 and is still in progress.

## What is SmartShark (SmSh) ?

SmartShark is an IDS (Intrusion Detection Systeme) coupled with some machine learning. The main goal of SmSh is to prevent a network from being attacked by a DDOS (Distributed Denial-of-Service) or a MITM (Man In The Midle). A DDOS can shut down a whole network and avoiding it could avoid some shutdowns of your website, while a MITM will spy your conection and steal some important data. It uses the machine learning to learn how does a DDOS looks like and learns to be more efficient when facing one, and has an algoritme to detect MITM attack.

## What tool are we using

We are using the `Wireshark` technology to catch all the trafic that happens on the network to, hopefully, try to detect some suspicious traffic and stopping it from harming the network. For the machine learning we are using the `TensorFlow` (2.0) tool, it is a powerfull add for our project because it manage to create a neuronal network easily and thanks to that we can detect a DDOS more efficiently.

Also, to make SmSh easy to use, we are using `Flask` to create a graphical interface for the user, making our project more accessible to other. We are using `Docker` as well, making the installation of SmSh very easy for the user, because then the user doesn't need to download all of SmSh's dependencies yourself.

## How did we get here ?

Soon there will be a time line of our work. [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## How to use it ?

To use SmSh on your computer:

1. You will need to have `Docker` installed
2. Clone our repository
3. Go to the `project` folder
4. Execute the following command `sudo docker build -t smsh:latest .`
5. Execute the following command `sudo docker run --net=host --cap-add=NET_ADMIN -e PUID=1000 -e PGID=1000 -d -p 5000:5000 smsh:latest`

And here you go ! SmSh is ready to be used on your computer !

You will be able to setup SmSh with a graphical interface on [this page](http://localhost:5000/). From here you will have the access to a graph showing your data according to your network, and SmSh will show you how many bad flows it has detected on your network. You will also have access to a list of button that will be send task to SmSh; here is a list of all commands that you can use:

- `start` -> will make SmSh look into your network and report every bad flow
- `stop` -> will stop SmSh from looking into your network
- `ddos` -> will only check for ddos atack
- `mitm` -> will only check for mitm atack
- `ddos&mitm` -> will check on both

## Authors

[Valentin De Matos](https://github.com/Thytu)

[Quentin Fringhian](https://github.com/QuentinFringhian)
