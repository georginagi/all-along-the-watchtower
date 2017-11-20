# Requires Python 3.0+

# import abstract base class functionality
from abc import ABCMeta, abstractmethod

#
# Defines the methods for a FIFO queue that handles characters
#
class CharQueue(metaclass=ABCMeta):

    #
    # @return true if the queue is empty
    #
    @abstractmethod
    def isEmpty(self):
        pass

    #
    # insert a single character to the queue
    #
    @abstractmethod
    def put(self, item):
        pass

    #
    # remove and return the oldest item of the queue
    # @return oldest item of the queue
    # @throws NoSuchElementException if the queue is empty
    #
    @abstractmethod
    def get(self):
        pass

    #
    # return without removing the oldest item of the queue
    # @return oldest item of the queue
    # @throws NoSuchElementException if the queue is empty
    #
    @abstractmethod
    def peek(self):
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
