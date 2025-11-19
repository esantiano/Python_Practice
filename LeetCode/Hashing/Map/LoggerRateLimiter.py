# Time O(1) - look up and update within hashmap is constant
# Space O(M) - M is size of incoming messages 
# Design:
# Logger needs to remember message and timestamp
# use a hashmap to store message:timestamp relationship
# shouldPrintMessage: will first check message to see if its in messages 
# if it is then check if the associated time stamp is within the acceptable range
# if it is then we update the timestamp in messages and return True
# if it isn't then we return False
# if the message is not inside messages we create a new relationship inside messages and return True
# in this approach we keep all the messages even when they are expired - which is problematic for memory. we need to implement a garbage collection function but its outside of the scope 
class Logger:

    def __init__(self):
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # The logic here can be cleaned up 
        if message in self.messages: 
            if timestamp < self.messages[message]+10:
                return False
            else:
                self.messages[message]=timestamp
                return True
        else:
            self.messages[message]=timestamp
            return True       
    def shouldPrintMessage2(self, timestamp: int, message: str) -> bool:
        if message not in self.messages or self.messages[message]+10<=timestamp:
            self.messages[message]=timestamp
            return True
        else:
            return False
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)