# SmartShark

>## <b>Project</b>
> The <b>SmartShark</b> an IDS (intrusion detection systeme) with machine learning. It will notify as soon as an anormal conection is made on the network.

>## <b>Logbook</b>
> This is a small presentation on what progress we made trough time. Each point will represent the outcome of a meeting (wich happen every week).
>* <b>WEEK 00 (27/03/2020)</b>
>   <pre>A global presentaion where made about the project in this session, our referant told us what <b>SmartShark</b> was all about, and what tools we could use.</pre>
>* <b>WEEK 01 (01/04/2020)</b>
>   <pre>At this time point, we where abble to understand how WireShark and TShark worked (in the big line), and we worked out that TenserFlow 2.0 would be the best framework to use as a tool for machin lurning</pre>
>* <b>WEEK 02 (08/04/2020)</b>
>   <pre>Since the last week we worked with TShark and managed to get live info in a pcap file to use in a possible futur programme. Also we lurned more from TenserFlow trough some tutorial to abble to use it later.</pre>
>* <b>WEEK 03 (15/04/2020)</b>
>   <pre>We trained ourselves with TensorFlow thanks to some task given to us by our referents, and thanks to those task we lurned that the use of an non supervise mnist algorithm would be hard to use in our cases. Also we made some research to have a better understanding of DDOS attack in a network</pre>
>* <b>WEEK 04 (22/04/2020)</b>
>   <pre>We manange to think that an anomaly detector algorithm would be a good choice of algorithme. Also, our surch for dataset to use for our machin lurning programme were unconcluant, we needed more time to find a good dataset to use.</pre>
>* <b>WEEK 05 (29/04/2020)</b>
>   <pre>We finally found a good dataset and we are abble to extract information from it throug some code that Valentin wrote. Furthemore, instead of using an unsupervised machin lurning algorithme, we would use a supervised algorithme (we conclude that it would be a better thing in our case scenario).</pre>
>* <b>WEEK 06 (06/05/2020)</b>
>   <pre>Thanks to some code and TanserFlow (and all we lurned since the beginng) we finally arrive at a point where our AI is abble to reconize a DDOS attack (in some case scenario) with a good accuracy.</pre>
>* <b>WEEK 07 (13/05/2020)</b>
>   <pre></pre>

>## <b>Dataset</b>
> The dataset is a main part of this project, in deed, it will be thanks to it that our machine leanring will learn. We first used a dataset given by the <a href=https://www.unb.ca/cic/datasets/ddos-2019.html>Univesity Of New Brunswick</a>, this dataset is veryusefull beaceause it has labbeled the network traffic so we can easely make our AI work on it and make a nice model of what an intrusion would look like. This dataset has many information, but we only use some of theme:
> * SourceIP: to know the source of the IP
> * SourcePort: to know the source of the Port
> * DestinationIP: to know the destination of the IP
> * DestinationPort: to know the destination of the Port
> * Protocol: to know wich protocol is used
> * TotalLengthofFwdPackets:
> * TotalLengthofBwdPackets:
>
> Also, we don't watch all of the traffic (it would be a waste of ressources), so we make our own data trough this data, in deed, we take 10 packets from the traffic and extract some data from it.