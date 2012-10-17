# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:56:34 2012

@author: tuxbear
"""

import unittest
if __name__ == '__main__':
    if __package__ == None:
        __package__ = "Robotuss.messaging.tests"
    unittest.main()

from .. import messagebus

class MessageBus_Tests(unittest.TestCase):
    def SetUp(self):
        self.messageHandlerCallCount = 0
        self.messageBus = messagebus.MessageBus()
        
    def test_registering_same_handler_multiple_times_is_ignored(self):
        self.messageBus.registerListener(["test topic"], self.messageHandlerFunction)
        self.messageBus.registerListener(["test topic"], self.messageHandlerFunction)
        
        self.messageBus.publishMessage("test topic", messagebus.Message())        
        
        assert self.messageHandlerCallCount == 1
        
    def messageHandlerFunction(self, message):
        self.lastMessage = message;
        self.messageHandlerCallCount += 1
    