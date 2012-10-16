#
from messaging import messagebus, messagetransforms
from modules import movement

print "yo bro, starting my engines!"

bus = messagebus.MessageBus()
movementManager = movement.MovementManager()

bus.registerListener( movementManager.acceptedMessageTypes, movementManager.processMessage)
#bus.registerListener( movementManager.acceptedMessageTypes, movementManager.processMessage)
bus.registerListener( ["*"], messagetransforms.messagePrinter )

aheadMessage = messagebus.Message("move_ahead")
aheadMessage.speed = 10



bus.publishMessage(aheadMessage)
