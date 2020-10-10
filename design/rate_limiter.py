'''
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

Approach 1: Queue + Set
Intuition
Before we tackle the problem, it is imperative to clarify the conditions of the problem, since it was not explicit in the problem description.
Here is one important note:
It is possible that several messages arrive roughly at the same time.
We keep the incoming messages in a queue. In addition, to accelerate the check of duplicates, we use a set data structure to index the messages.

Approach 2: Hashtable / Dictionary
Intuition
One could combine the queue and set data structure into a hashtable or dictionary,
which gives us the capacity of keeping all unique messages as of queue as well as the capacity to quickly evaluate the duplication of messages as of set.
The idea is that we keep a hashtable/dictionary with the message as key, and its timestamp as the value.
The hashtable keeps all the unique messages along with the latest timestamp that the message was printed.
'''
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        if message not in self._msg_dict:
            # case 1). add the message to print
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10:
            # case 2). update the timestamp of the message
            self._msg_dict[message] = timestamp
            return True
        else:
            return False
            
 '''
 Complexity Analysis

Time Complexity:O(1). The lookup and update of the hashtable takes a constant time.
Space Complexity:O(M) where M is the size of all incoming messages. Over the time,
the hashtable would have an entry for each unique message that has appeared.
