# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:13:59 2012

@author: tuxbear
"""

def messagePrinter(message): 
    print "Message type:", message.messageType
    print "Message origin: ", message.origin
    for property, value in vars(message).iteritems():
        print property, ": ", value