######
#  Set all Roles to Restricted
#  no anonymous access possible
#
#  Author: Klaus Bild
#  Blog: http://www.kbild.ch
#  E-Mail:
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.1
#  Date:          2014-09-04
#
#  License:       Apache 2.0
#
#  Description:
#  Script is tested with IBM Connections 5.0
#  You have to edit the variables and set them to your administrative Accounts

#  History:

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
    connmobile = configParser.get( 'Generic','j2ee.connmobile' )
    cnxmail = configParser.get( 'Generic','j2ee.cnxmail' )
    cnxreader = configParser.get( 'Generic','j2ee.cnxreader' )
    cnxcommunitycreator = configParser.get( 'Generic','j2ee.communitycreator' )
    cnxwikicreator = configParser.get( 'Generic','j2ee.wikicreator' )
    cnxfilesyncuser = configParser.get( 'Generic','j2ee.filesyncuser' )
    # Variables for Groupmapping
    connadmingroup = configParser.get( 'Generic','j2ee.cnxadmingroup' )
    connmoderatorgroup = configParser.get( 'Generic','j2ee.cnxmoderatorgroup' )
    connmetricsgroup = configParser.get( 'Generic','j2ee.cnxmetricsgroup' )
    connmobilegroup = configParser.get( 'Generic','j2ee.cnxmobilegroup' )
    cnxmailgroup = configParser.get( 'Generic' , 'j2ee.cnxmailgroup' )
    cnxreadergroup = configParser.get( 'Generic','j2ee.cnxreadergroup' )
    cnxcommunitycreatorgroup = configParser.get( 'Generic','j2ee.communitycreatorgroup' )
    cnxwikicreatorgroup = configParser.get( 'Generic','j2ee.wikicreatorgroup' )
    cnxfilesyncusergroup = configParser.get( 'Generic','j2ee.filesyncusergroup' )
else:
    # Variables for Usermapping
    connwasadmin = str( ibmcnx.functions.getAdmin( 'connwasadmin' ) )
    connadmin = str( ibmcnx.functions.getAdmin( 'connadmin' ) )
    connmoderators = str( ibmcnx.functions.getAdmin( 'connmoderators' ) )
    connmetrics = str( ibmcnx.functions.getAdmin( 'connmetrics' ) )
    connmobile = str( ibmcnx.functions.getAdmin( 'connmobile' ) )
    cnxmail = str( ibmcnx.functions.getAdmin( 'cnxmail' ) )
    # Variables for Groupmapping
    connadmingroup = str( ibmcnx.functions.getAdmin( 'connadmingroup' ) )
    connmoderatorgroup = str( ibmcnx.functions.getAdmin( 'connmoderatorgroup' ) )
    connmetricsgroup = str( ibmcnx.functions.getAdmin( 'connmetricsgroup' ) )
    connmobilegroup = str( ibmcnx.functions.getAdmin( 'connmobilegroup' ) )
    cnxmailgroup = str( ibmcnx.functions.getAdmin( 'cnxmailgroup' ) )

def setRoleCmd( appName, roleName, everyone, authenticated, users, groups ):
    # function to set the j2ee role of a Connections Application
    # Values needed appName = Application Name, roleName = Name of the role
    # everyone yes|no, authenticated yes|no, users single uid or uid1|uid2, groups like users
    # 
    AdminApp.edit( appName, '[-MapRolesToUsers [[ "' + roleName + '" ' + everyone + ' ' + authenticated + ' ' + '"' + users + '"' + ' ' + '"' + groups + '"' + ' ]] ]' )
    # example: AdminApp.edit( "Blogs", '[-MapRolesToUsers [["person" No Yes "" ""] ]]' )
    
def setRole( appName, roleName, connwasadmin,connadmin,connmoderators,connmetrics,connmobile,cnxmail,cnxreader,cnxcommunitycreator,cnxwikicreator,cnxfilesyncuser,connadmingroup,connmoderatorgroup,connmetricsgroup,connmobilegroup,cnxmailgroup,cnxreadergroup,cnxcommunitycreatorgroup,cnxwikicreatorgroup,cnxfilesyncusergroup):
    if roleName == "admin" or "search-admin" or "widget-admin" or "dsx-admin":
        # Administration Roles
        setRoleCmd( appName, roleName, "No", "No", connwasadmin + '|' + connadmin, connadmingroup )
    elif roleName == "administrator":
        # Mobile Administration
        setRoleCmd( appName, roleName, "No", "No", connmobile, connmobilegroup )
    elif roleName == "global-moderator":
        # Moderators
        setRoleCmd( appName, roleName, "No", "No", conmoderators, conmoderatorgroup )
    elif roleName == "metrics-reader" or "metrics-report-run" or "community-metrics-run":
        # Metrics
        setRoleCmd( appName, roleName, "No", "No", connmetrics, connmetricsgroup )
    elif roleName == "reader" or "person" or "allAuthenticated" or "everyone-authenticated" or "files-owner":
        # Default Access reader, person, authenticated
        if cnxreader == "allauthenticated":
            setRoleCmd( appName, roleName, "No", "Yes", "", "" )
        else:
            setRoleCmd( appName, roleName, "No", "No", "cnxreader", "cnxreadergroup" )
    elif roleName == "mail-user":
        # Mail User
        if cnxmail == "allauthenticated":
            setRoleCmd( appName, roleName, "No", "Yes", "", "" )
        else:
            setRoleCmd( appName, roleName, "No", "No", "cnxmail", "cnxmailgroup" )
    elif roleName == "everyone":
        # Public to yes
        setRoleCmd( appName, roleName, "Yes", "No", "", "" )
    elif roleName == "discussthis-user":
        # Public to yes
        setRoleCmd( appName, roleName, "Yes", "No", "", "" )
    elif roleName == "community-creator":
        # Community Creator
        if cnxmail == "allauthenticated":
            setRoleCmd( appName, roleName, "No", "Yes", "", "" )
        else:
            setRoleCmd( appName, roleName, "No", "No", "cnxcommunitycreator", "cnxcommunitycreatorgroup" )
    elif roleName == 'wiki-creator':
        # Wiki Creator
        if cnxmail == "allauthenticated":
            setRoleCmd( appName, roleName, "No", "Yes", "", "" )
        else:
            setRoleCmd( appName, roleName, "No", "No", "cnxwikicreator", "cnxwikicreatorgroup" )
    elif roleName == 'filesync-user':
        # Wiki Creator
        if cnxfilesyncuser == "allauthenticated":
            setRoleCmd( appName, roleName, "No", "Yes", "", "" )
        else:
            setRoleCmd( appName, roleName, "No", "No", "cnxfilesyncuser", "cnxfilesyncusergroup" )

def convertRoles2Dict( appname, list ):
    # function to convert backup txt files of Security Role Backup to a dictionary
    # print '\tPATH: ' + path 
    count = 0
    dict = {}

    for line in list.splitlines():
        # for loop through file to read it line by line
        if ( ':' in line ) and ( count > 12 ):
            value = line.split( ':' )[0]
            # cred = line.split(':')[1].strip('\n')
            cred = line.split( ':' )[1]
            # cred = cred.strip(' ')
            cred = cred.strip()
            if value == "Role":
                role = cred
                dict[role] = {}
            dict[role][value] = cred
        count += 1
    return dict

apps = AdminApp.list()
appsList = apps.splitlines()

for app in appsList:
    dictionary = convertRoles2Dict( app, AdminApp.view( app, "-MapRolesToUsers" ) ) 
    # app, role
    for role in dictionary.keys():
        # Loop through Roles
        try:
            print "Setting role: " + role + " \t in " + app
            setRole( app, role, connwasadmin,connadmin,connmoderators,connmetrics,connmobile,cnxmail,cnxreader,cnxcommunitycreator,cnxwikicreator,cnxfilesyncuser,connadmingroup,connmoderatorgroup,connmetricsgroup,connmobilegroup,cnxmailgroup,cnxreadergroup,cnxcommunitycreatorgroup,cnxwikicreatorgroup,cnxfilesyncusergroup )
        except:
            print "Error setting role: " + role + " in App: " + app
    AdminConfig.save()
        