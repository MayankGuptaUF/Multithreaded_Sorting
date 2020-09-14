# Multithreaded_Sorting
README:

python version 3.5+
OS - Ubuntu 16.04

The port to communicate is 8080 and the Local host address is kept as 127.0.0.1

There are 4 files in this Assignment, SORTPARALLEL.py, SORTCLIENT.py , SORTSERVER.py and SORTSERVER_BONUS.py

The only difference between SORTSERVER.py and SORTSERVER_BONUS.py is that in SORTSERVER the address is declared at a local host, whereas in SORTSERVER_BONUS, it serves all the ports and thus we can communicate between 2 machines on the IP address.



SORTPARALLEL.py has 3 functions-
1) sleep_sort- this is the function which puts the process in sleep mode for n seconds which is the number.
2) generate- this is used to generate the random list
3) parallel-this is the function in which the processes are created the main functions only needs to call this process.

SORTCLIENT has only generate and SORTSERVER has parallel and sleep_sort

Libraries used-time, sys, multiprocessing, random, xmlrpc.client,xmlrpc.server
