# Polymorphism is the ability of different objects to respond to
# the same method in different ways.
# It occurs in two main forms:
# 1. Method Overriding (Runtime Polymorphism): Achieved via inheritance when one class 
# overrides the method of other.
# 2. Duck Typing (Informal Polymorphism): Based on object behavior, not type. It happens
# when different objects implement the same method in different ways,
# without requiring inheritance.

# Method Overriding or Runtime Polymorphism: 
class Notification:
    def send(self):
        print('Sending Notification...')
class EmailNotification(Notification):
    def send(self):
        print('Sending Email Notification...')
class SMSNotification(Notification):
    def send(self):
        print('Sending SMS Notification...')
class PushNotification(Notification):
    def send(self):
        print('Sending Push Notification...')    
for item in (EmailNotification(), SMSNotification(), PushNotification()):
    item.send()
# The send() method of the child classes overrides the one of parent class.

# Duck Typing or Informal Polymorphism:
class PDFDocument:
    def render(self):
        print('Rendering PDF file...')
class WordDocument:
    def render(self):
        print('Rendering Word document...')
class ImageFile:
    def render(self):
        print('Rendering image preview...')
for doc in (PDFDocument(), WordDocument(), ImageFile()):
    doc.render()
# The render() method produces different results for different classes. 


