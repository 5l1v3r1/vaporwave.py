#!/usr/bin/env python3
# encoding: UTF-8

"""
    
    
    IPGeoLocation - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
    
    
"""




class UserAgentFileEmptyError(Exception):
    pass

class InvalidTargetError(Exception):
    pass

class TargetsFileEmptyError(Exception):
    pass

class TargetsFileNotSpecifiedError(Exception):
    pass

class UserAgentFileNotSpecifiedError(Exception):
    pass

class ProxyServerNotReachableError(Exception):
    pass

class ProxiesFileNotSpecifiedError(Exception):
    pass

class ProxiesFileEmptyError(Exception):
    pass

class InvalidProxyUrlError(Exception):
    pass
