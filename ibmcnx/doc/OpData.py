######
# Dump a few interesting numbers about the Connections instance
#
# Author: Martin Leyrer
# Mail: leyrer@gmail.com
# Documentation: tbd
#
#
# Version: 10.0
# Date: 2015-03-07
#
# License: Apache 2.0
#
# History:
# 20150307      Martin Leyrer           Initial implementation
# 

import sys
import time
import os
import sys
import ibmcnx.functions
import java.util.ArrayList as ArrayList

batchSize = 250

try:
    execfile( "filesAdmin.py" )
    execfile("communitiesAdmin.py") 
except:
    print "\nDumpData could not connect to the 'IBM Websphere Deployment Manager'. Please make sure the 'dmgr' is running."
    sys.exit()

try:
    numOfPersonalLibraries = FilesLibraryService.getPersonalCount()
    numOfCommunityLibraries = FilesLibraryService.getCommunityCount()

    keys = ArrayList()
    # FilesMetricsService.__fetchMetrics('personal', keys, None, None)
    persMetrics = FilesMetricsService.browsePersonal()

except:
    print "\nDumpData was not able to communicate with the 'IBM Connections Files' application. Please make sure 'Files' is running."
    print sys.exc_info()[0]
    sys.exit()

try:
    allComm = CommunitiesService.fetchBatchComm(batchSize, None)
    numOfCommunities = len(allComm)
except:
    print "\nDumpData was not able to communicate with the 'IBM Connections Communities' application. Please make sure 'Communities' is running."
    sys.exit()

print "\nIBM Connections data as of " + time.strftime("%Y-%m-%d")
print ("Number of Communities: %u" % numOfCommunities )
print "Number of Personal Libraries:  %u" % numOfPersonalLibraries
print "Number of Community Libraries: %u" % numOfCommunityLibraries

#print "Size: " + len(persMetrics)

##for map in metricsList:
#map = persMetrics(-1)
#keyList = ArrayList(map.keySet())
#Collections.sort(keyList)
#for key in keyList:
#    print (key + '=' + str(map.get(key)))

