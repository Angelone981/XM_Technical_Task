
import logging

def extract_incoming_logs(logname):
    
    logging.basicConfig(filename = logname, filemode = 'a',
                        format='%(asctime)s - %(message)s!!!',
                        level = logging.DEBUG)
    
     
