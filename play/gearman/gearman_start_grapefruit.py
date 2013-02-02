from gearman import GearmanClient
import simplejson
import uuid
import time

# create a client that will connect to the Gearman server running on
# localhost. The array allows you to specify a set of job servers.
#client = GearmanClient(['localhost:4730'])
client = GearmanClient(['15.185.117.66:4730'])

# Submit a synchronous job request to the job server and store the
print 'Sending job...'
build_id = uuid.uuid4().hex
#build_id = uuid.UUID('{0ab10215-0405-0607-0809-0a0b0c0d0e0f}').hex
print build_id
jenkins_build_params = {'uuid':build_id,'param2':"true",'param3':'bingo'}
request = client.submit_job('build:grapefruit:master', simplejson.dumps(jenkins_build_params), poll_timeout=60, unique=build_id)

print request.result
print 'Work complete with state %s' % request.state
