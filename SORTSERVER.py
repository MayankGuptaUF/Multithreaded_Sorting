from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import multiprocessing
import time




server=SimpleXMLRPCServer(("127.0.0.1", 8080))


def sleep_sort(seconds,out):

	time.sleep(0.2*seconds)
	#print(seconds)
	out.put(seconds)
	return seconds

def parralel(N,R,array):
	
	processes = []
	q=multiprocessing.Queue()
	for i in range(0, len(array)):
		p = multiprocessing.Process(target=sleep_sort, args=(array[i], q))
		p.start()
		processes.append(p)
	for process in processes:
		process.join()
		out=[]
	while q.empty() is False:
		out.append(q.get())
	return out
	
server.register_function(parralel, 'para')

server.serve_forever()
