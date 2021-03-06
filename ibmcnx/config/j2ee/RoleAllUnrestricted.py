######
#  Set all Roles to Unrestricted
#  anonymous access possible
#
#  Author: Klaus Bild
#  Blog: http://www.kbild.ch
#  E-Mail:
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2014-06-04
#
#  License:       Apache 2.0
#
#
# cfgJ2EERolesRestricted
#
# Description:
# Script is tested with IBM Connections 4.5 CR2
# You have to edit the variables and set them to your administrative Accounts

# History:
# 20131124  Christoph Stoettner    Update with loop and try/except to handle errors, added group support
# 20131201  Christoph Stoettner    Add menu to ask for parameters

import ibmcnx.functions
import ConfigParser

configParser = ConfigParser.ConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read( configFilePath )

answer = raw_input( 'Do you want to set the j2ee roles with Users and Groups from ibmcnx.properties? (Yes|No) ' )
allowed_answer = ['yes', 'y', 'ja', 'j']

if answer.lower() in allowed_answer:
    # Get Admin Accounts and Groups for J2EE Roles
    connwasadmin = configParser.get( 'Generic','j2ee.cnxwasadmin' )
    connadmin = configParser.get( 'Generic','j2ee.cnxadmin' )
    connmoderators = configParser.get( 'Generic','j2ee.cnxmoderators' )
    connmetrics = configParser.get( 'Generic','j2ee.cnxmetrics' )
    connmobile = configParser.get( 'Generic','j2eeconnmobile' )
    # Variables for Groupmapping
    connadmingroup = configParser.get( 'Generic','j2ee.cnxadmingroup' )
    connmoderatorgroup = configParser.get( 'Generic','j2ee.cnxmoderatorgroup' )
    connmetricsgroup = configParser.get( 'Generic','j2ee.cnxmetricsgroup' )
    connmobilegroup = configParser.get( 'Generic','j2ee.cnxmobilegroup' )
else:
    # Variables for Usermapping
    connwasadmin = str( ibmcnx.functions.getAdmin( 'connwasadmin' ) )
    connadmin = str( ibmcnx.functions.getAdmin( 'connadmin' ) )
    connmoderators = str( ibmcnx.functions.getAdmin( 'connmoderators' ) )
    connmetrics = str( ibmcnx.functions.getAdmin( 'connmetrics' ) )
    connmobile = str( ibmcnx.functions.getAdmin( 'connmobile' ) )

    # Variables for Groupmapping
    connadmingroup = str( ibmcnx.functions.getAdmin( 'connadmingroup' ) )
    connmoderatorgroup = str( ibmcnx.functions.getAdmin( 'connmoderatorgroup' ) )
    connmetricsgroup = str( ibmcnx.functions.getAdmin( 'connmetricsgroup' ) )
    connmobilegroup = str( ibmcnx.functions.getAdmin( 'connmobilegroup' ) )

def j2eeRolesCmdUnrestricted( appName, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup ):
    if( appName == 'Activities' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""] ]]' )
    elif( appName == 'Blogs' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["reader" Yes No "" ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Common' ):
         AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["metrics-report-run" No No ' + connmetrics + ' ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["reader" Yes No "" ""]  ]]' )
    elif( appName == 'Communities' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""] ["metrics-reader" Yes No "" ""] ["community-creator" Yes No "" ""] ["community-metrics-run" No Yes ' + connmetrics + ' ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Dogear' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'FNCS' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["Authenticated" Yes No "" ""] ["Anonymous" Yes No "" ""] ]]' )
    elif( appName == 'Files' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["files-owner" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["app-connector" No No "" ""] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["org-admin" No No "" ""] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Forums' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["metrics-reader" Yes No "" ""] ["reader" Yes No "" ""] ["everyone" Yes No "" ""] ["discussThis-user" Yes No "" ""] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["global-moderator" No No "' + connwasadmin + '|' + connmoderators + '" ""] ["bss-provisioning-admin" No No "" ""] ["search-public-admin" No No "" ""]  ]]' )
    elif( appName == 'Homepage' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Metrics' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["community-metrics-run" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["metrics-report-run" No No ' + connmetrics + ' ""]  ]]' )
    elif( appName == 'Mobile' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""]  ]]' )
    elif( appName == 'Mobile Administration' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["administrator" No No "' + connmobile + '" "' + connmobilegroup + '"] ["everyone" No Yes "" ""]  ]]' )
    elif( appName == 'Moderation' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["person" No Yes "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"]  ]]' )
    elif( appName == 'News' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["sharebox-reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["allAuthenticated" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Profiles' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["dsx-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["org-admin" No No "' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'Search' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone-authenticated" No Yes "" ""]  ]]' )
    elif( appName == 'WebSphereOauth20SP' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["authenticated" No Yes "" ""] ["client manager" No No "" ""]  ]]' )
    elif( appName == 'WidgetContainer' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["everyone" Yes No "" ""] ["reader" Yes No "" ""] ["metrics-reader" No No "" ""] ["global-moderator" No No "' + connmoderators + '" "' + connmoderatorgroup + '"] ["mail-user" No Yes "" ""] ["trustedExternalApplication" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"]  ]]' )
    elif( appName == 'Wikis' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["everyone" Yes No "" ""] ["person" No Yes "" ""] ["reader" Yes No "" ""] ["metrics-reader" Yes No "" ""] ["everyone-authenticated" No Yes "" ""] ["wiki-creator" No Yes "" ""] ["admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["search-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["widget-admin" No No "' + connwasadmin + '|' + connadmin + '" "' + connadmingroup + '"] ["bss-provisioning-admin" No No "" ""]  ]]' )
    elif( appName == 'connectionsProxy' ):
        AdminApp.edit( appName, '[-MapRolesToUsers [["person" No Yes "" ""] ["allAuthenticated" No Yes "" ""] ["reader" Yes No "" ""] ["everyone" Yes No "" ""]  ]]' )
    else:
        print "Unknown Application: %s" % appName


apps = AdminApp.list()
appsList = apps.splitlines()
for app in appsList:
    print "Setting Security Roles for %s" % app.upper()
    try:
        j2eeRolesCmdUnrestricted( app, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup )
    except:
        print "Error occured on setting security roles for %s" % app.upper()

ibmcnx.functions.saveChanges()
