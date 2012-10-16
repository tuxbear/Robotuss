# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:36:37 2012

@author: tuxbear

"""
from sys import inspect


class MessageBus:
    def __init__(self):
        self.transforms = []
        self.listeners = {"*": set()}
    
    def publishMessage(self, message):
        receivers = self.listeners[message.messageType]
        for receiver in receivers:
            receiver(message)
        
        genericReceivers = self.listeners["*"]
        for genericReceiver in genericReceivers:
            genericReceiver(message)
        
    def registerListener(self, acceptedMessages,  receiverFunction):
        for messageType in acceptedMessages:
            if self.listeners.has_key(messageType):
                self.listeners[messageType].add(receiverFunction)
            else:
                self.listeners[messageType] = set([ receiverFunction ])
                
        
        
class Message(object):
    def __init__(self, messageType):
        self.messageType = messageType
       