# SmartShark - An IDS with some Machine Learning

The SmartShark project is the fruit of the work of Valentin De Matos and Quentin Fringhian, two Epitech studients managed by the Poc assosiation. The project started in April 2020 and is still in progress.

## What is SmartShark (SmSh) ?

SmartShark is an IDS (Intrusion Detection Systeme) coupled with some machine learning. The main goal of SmSh is to prevent a network from being attacked by a DDOS (Distributed Denial-of-Service). A DDOS can shut down a whole network and avoiding it could avoid some shutdowns of your website. It uses the machine learning to learn how does a DDOS looks like and learns to be more efficient when facing one.

## What tool are we using

We are using the `Wireshark` technology to catch all the trafic that happens on the network to, hopefully, try to detect some suspicious traffic and stopping it from harming the network. For the machine learning we are using the `TensorFlow` (2.0) tool, it is a powerfull add for our project because it manage to create a neuronal network easily and thanks to that we can detect a DDOS more efficiently.

Also, to make SmSh easy to use, we are using `Flask` to create a graphical interface for the user, making our project more accessible to other. We are using `Docker` as well, making the installation of SmSh very easy for the user, because then the user doesn't need to download all of SmSh's dependencies yourself.

## How did we get here ?

Soon there will be a time line of our work.

## How to use it ?

To use SmSh on your computer:

1) You will need to have `Docker` installed
2) Clone our repository
3) Go to the `project` folder
4) Execute the following command `sudo docker build -t smsh:latest .`
5) Execute the following command `sudo docker run --net=host --cap-add=NET_ADMIN -e PUID=1000 -e PGID=1000 -d -p 5000:5000 smsh:latest`

And here you go ! SmSh is ready to be used on your computer !

You will be able to setup SmSh with a graphical interface on [this page](http://localhost:5000/). From here you will have the access to a graph showing your data according to your network, and SmSh will show you how many bad flows it has detected on your network. You will also have access to a command interpreter where you can insert instructions that will be send to SmSh; here is a list of all commands that you can use:
- `start` -> will make SmSh look into your network and report every bad flow
- `stop` -> will stop SmSh from looking into your network
- `time` + `sec` (int > 0) -> will set the frequency of observation on your network to `sec` (ex: `time 10` -> this will set the frequency to 10 seconds)
- `detect` + `%` (int > 0) -> will set the alert system to alert you when `%` of observations have been detected as bad (ex: `detect 10 `-> this will alert you when you have more than 10% of bad observations on your network)
- `save` + `bool` (True or False) -> this will set the saving system to `bool` (ex: `save True` -> this will save every observation on your network)

## Authors

[Valentin De Matos](https://github.com/Thytu)

[Quentin Fringhian](https://github.com/QuentinFringhian)