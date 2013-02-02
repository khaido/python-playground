from gearman import GearmanClient
import simplejson
import uuid
import time

# create a client that will connect to the Gearman server running on
# localhost. The array allows you to specify a set of job servers.
client = GearmanClient(['localhost:4730'])

# Submit a synchronous job request to the job server and store the
print 'Sending job...'
build_id = uuid.uuid4().hex
print build_id
jenkins_build_params = {'uuid':build_id,'param2':"true",'param3':'bingo'}
request = client.submit_job('build:lemon:linux&&gcc', simplejson.dumps(jenkins_build_params), poll_timeout=60, unique=build_id)

print request.result
print 'Work complete with state %s' % request.state
