# Requires Python 3.0+

# import abstract base class functionality
from abc import ABCMeta, abstractmethod

#
# Defines the methods for a Double-ended Queue that handles characters
#


class CharDoubleEndedQueue(metaclass=ABCMeta):

    #
    # @return true if the queue is empty
    #
    @abstractmethod
    def isEmpty(self):
        pass

    #
    # insert a character at the front of the queue
    #
    @abstractmethod
    def addFirst(self, item):
        pass

    #
    # remove and return a character from the front of the queue
    #
    @abstractmethod
    def removeFirst(self):
        pass

    #
    # insert a character at the end of the queue
    #
    @abstractmethod
    def addLast(self, item):
        pass

    #
    # remove and return a character from the end of the queue
    #
    @abstractmethod
    def removeLast(self):
        pass

    #
    # return without removing the first item in the queue
    #
    @abstractmethod
    def getFirst(self):
        pass

    #
    # return without removing the last item in the queue
    #
    @abstractmethod
    def getLast(self):
        pass

    #
    # print the elements of the queue, starting from the oldest
    # item, to the print stream given as argument. For example, to
    # print the elements to the
    # standard output, pass System.out as parameter. E.g.,
    # printQueue(System.out);
    #
    @abstractmethod
    def printQueue(self, stream):
        pass

    #
    # return the size of the queue, 0 if it is empty
    # @return number of elements in the queue
    #
    @abstractmethod
    def size(self):
        pass
