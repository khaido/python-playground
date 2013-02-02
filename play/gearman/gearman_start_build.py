from gearman import GearmanClient
import simplejson
import uuid
import time
import optparse






if __name__ == "__main__":
    usage = "usage: %prog [options] [status|on|off|cycle|get_outlet_name|set_outlet_name] [range|arg]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--hostname',dest='hostname',default=None,help="gearman server host (default %default)")
    parser.add_option('--port',dest='port',default=None,type=int,help="gearman server port (default %default)")
    parser.add_option('--timeout',dest='timeout',default=None,type=int,help="Timeout for value for power switch communication (default %default)")
    parser.add_option('--function',dest='function',default=None,help="the gearman function to run (default %default)")
    (options, args) = parser.parse_args()


    print 'Sending job...'
    
    server_conn = "%s:%d"%(options.hostname,options.port);
    print server_conn

    client = GearmanClient([server_conn])

    build_id = uuid.uuid4().hex
    print build_id
    jenkins_build_params = {'uuid':build_id,'param2':"true",'param3':'bingo'}
    request = client.submit_job(options.function, 
                                simplejson.dumps(jenkins_build_params), 
                                poll_timeout=options.timeout, 
                                unique=build_id)


    print request.result
