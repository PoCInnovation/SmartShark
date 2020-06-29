# SmartShark - An IDS with some Machine Learning

The SmartShark project is the fruit of the work of Valentin De Matos and Quentin Fringhian, tow Epitech studient managed by the Poc assosiation. The project started in April 2020 and is steel in progress.

## What is SmartShark (SmSh) ?

SmartShark is an IDS (Intrusion Detection Systeme) coupled with some machine learning. The main goal of SmSh is to prevent a network from being attacked by a DDOS (Distributed Denial-of-Service), a DDOS can shut down an entier network and avoiding it could avoid some shutdown of your website. It use the machine learning to learn what does a DDOS looks like and learn to be more eficient when facing one.

## What tool are we using

We are using the `Wireshark` technologie to catch all the trafic that happen on the network to, hopefully, try detect some suspisius trafic and stoping it from harming the network. For the machine learning we are using the `TensorFlow` (2.0) tool, it is a powerfull add for our project because it manage to create a neronal network easly and thanks to that we can detect a DDOS more efficiently.

Also, to make SmSh easy to use, we are using `Flask` to creat a graphical interface for the user, making our project more accecible to other. We are using `Docker` as well, making the installation of SmSh very easy for you, because you don't need to download all of SmSh's dependenses yourself.

## How did we get here ?

Soon there will be a time line of our work.

## How to use it ?

To use SmSh on your computer, you have tow option:

1) You will need to have installed `Docker`
2) Clone our repository
3) Go to `project/app`
4) Execute the following commande `sudo docker build -t smsh:latest .`
5) Execute the following commande `sudo docker run --net=host --cap-add=NET_ADMIN -e PUID=1000 -e PGID=1000 -d -p 5000:5000 smsh:latest`

And here you go ! SmSh is reday to go on your computer !

You will be abble to setup SmSh with a graphical interface on [this page](http://localhost:5000/). From here you have the acces to a graph chowing you data according to your network, and SmSh will show you how many bad flow it has detected on your network. You have acces to a commande interpreter where you can insert instruction that will be send to SmSh, here is a list of all commande that you can use:
- `start` -> will make SmSh look into your network and report every bad flow
- `stop` -> will stop SmSh from looking into your network
- `time` + `sec` (int > 0) -> will set the frequence of observasion on your network to sec (ex: `time 10` -> this will set the frequence to 10 secondes)
- `detect` + `%` (int > 0) -> will set the alert systeme to alert you when % of observation has been detect has bad (ex: `detect 10 `-> this will alert you when you have more than 10% of bad observation on your network)
- `save` + `bool` (True or False) -> this will set the saving system to bool (ex: `save True` -> this will save every observation on your network)


## External link

