from gearman import GearmanClient
import simplejson
import uuid

# create a client that will connect to the Gearman server running on
# localhost. The array allows you to specify a set of job servers.
#client = GearmanClient(['impinj-pc-0461'])
client = GearmanClient(['localhost:4730'])

# Submit a synchronous job request to the job server and store the
print 'Sending job...'
# This runs the "echo" job on the argument "foo"
#request = client.submit_job('reverse', 'hello')

#jenkins_data = {'url':"http://localhost:8080",'jobId':'burnit'}
#jenkins_burnit_status = {'url':"http://localhost:8080",'jobId':'burnit'}

#info_json = "{'url':'baba','job_id':'didi'}"
#request = client.submit_job('jenkins_invoke_job', simplejson.dumps(jenkins_data))
#request = client.submit_job('org.gearman.example.ReverseFunction', "burnit", unique="id3456", poll_timeout=5)
#request = client.submit_job('reverse', "burnit", unique="id3456", poll_timeout=5)
#request = client.submit_job('reverse', "burnit", poll_timeout=5)
#request = client.submit_job('echo', "mama")
#request = client.submit_job('bravo', "mama")
#print request.result

#request = client.submit_job('reverse', "baba", unique="id1234", poll_timeout=5)
#print request.result
#request = client.submit_job('JenkinsJobStatus', "burnit", poll_timeout=5)
#client.shutdown()
#request = client.submit_job('org.gearman.example.JenkinsInvokeJob', "wet", poll_timeout=5)
#request = client.submit_job('org.gearman.example.JenkinsJobStatus', "burnit", poll_timeout=5)
#request = client.submit_job('JenkinsJobStatus', simplejson.dumps(jenkins_burnit_status), poll_timeout=5)
#request = client.submit_job('JenkinsInvokeJob', "build:wet:vs2005", poll_timeout=5)
#request = client.submit_job('build:dog:python-2.7', "", poll_timeout=5)
#request = client.submit_job('build:lemon:centos', "", poll_timeout=5)

# do a build job
build_id = uuid.uuid4().hex
print build_id

#job_params = {'param1':"12321",'param2':"true",'param3':"validate"}
#jenkins_data = {'uuid':'id2021', 'params':unicode(job_params)}
jenkins_build_params = {'param1':"12321",'param2':"true",'param3':"validate"}
#request = client.submit_job('build:lemon:oneiric-642067', simplejson.dumps(jenkins_data), poll_timeout=5)
request = client.submit_job('stop:localhost', simplejson.dumps(jenkins_build_params), poll_timeout=5, unique=build_id)

#request = client.submit_job('build:guava', simplejson.dumps(jenkins_build_params), poll_timeout=5, unique=build_id)
#request = client.submit_job('build:mango:torrent', simplejson.dumps(jenkins_build_params), unique="2012", poll_timeout=5)

# do a stop job
#request = client.submit_job('stop:jenkins_master.hp.com',"")

#request = client.submit_job('echo', simplejson.dumps(jenkins_build_params), poll_timeout=5, unique=build_id)

print request.result
print 'Work complete with state %s' % request.state
#request = client.submit_job('echo', 'foo')
#print request.result
#print 'Work complete with state %s' % request.state