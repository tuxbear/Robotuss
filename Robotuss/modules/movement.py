# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:07:28 2012

@author: tuxbear

Accepts messages:
    move_ahead
        speed (1-100)
    move_backwards
        speed (1-100)
    move_rotate
        angle(-360 - 360)
    move_stop

Publish messages:
    move_moving
        direction ("ahead", "backwards")
        speed (1-100)
    move_rotating
        angle (-360 - 360)
    move_stopped
"""

class MovementManager(object):
    def __init__(self):
        self.acceptedMessageTypes = [ "move_ahead", "move_backwards", "move_rotate", "move_stop" ]    
    
    def processMessage(self, message):
        if message.messageType in self.acceptedMessageTypes:
            print message.messageType, "accepted"
            handler = getattr(self, message.messageType)
            handler(message)
        else:
            print "Unexpected messageType"
            
    def move_ahead(self, message):
        print "Moving ahead with speed of" , message.speed
        
    def move_backwards(self, message):
        print "Moving backwards with speed of" , message.speed
        
    def move_rotate(self, message):
        print "Rotating " , message.angle, " degrees"
        
    def move_stop(self, message):
        print "Stopped"
    