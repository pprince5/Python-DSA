# Copy over your a1_partc.py file here
#    Main Author(s): kexian Guo
#    Main Reviewer(s): Kiran Dhillon, Prince



class Stack:
    # It is passed a value representing it's capacity, with a default capacity of 10 if no capacity is passed in.
    def __init__(self, cap=10):
        self.cap = cap
        self.buf = [None] * cap
        self.top = -1
 # This function returns capacity.
    def capacity(self):
        return self.cap
# This function adds data to the "top" of the Stack.
    def push(self, data):
         # add 1 to the top position of the stack
        self.top += 1
        # determine whether expansion is necessary
        if self.top >= self.cap:
             # Resizing always doubles the current capacity of the array.
            self.cap *= 2
             # create a buffer of specified capacity
            buffer = [None] * self.cap
            i = 0
            while i < self.top:
                buffer[i] = self.buf[i]
                i += 1
            self.buf = buffer
        self.buf[self.top] = data
 # This function removes the newest value from the Stack (the value at the "top" of the Stack).
    def pop(self):
        # If the function is called on an empty Stack, raise the IndexError with this statement.
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        value = self.buf[self.top]
        self.top -= 1
        return value
 # This function returns the newest value (value at "top") from the Stack without removing it.
    def get_top(self):
         # Function returns None if stack is empty
        if self.is_empty():
            return None
        return self.buf[self.top]

    def is_empty(self):
        return self.top == -1

    def __len__(self):
        return self.top + 1


class Queue:
    # This function initializes the Queue class data members.
    def __init__(self, cap=10):
        self.cap = cap
        self.buf = [None] * cap
        self.front = 0
        self.rear = -1

    def capacity(self):
        return self.cap

    def enqueue(self, data):
        self.rear += 1
         # Check if there is any space left at the front of the queue
        if self.front != 0:
            i = self.front
            j = 0
            while j + i < self.rear:
                self.buf[j] = self.buf[j + i]
                j += 1
                # Update the position of the front and rear
            self.front = 0
            self.rear -= i
        elif self.rear >= self.cap:
              # Resizing always doubles the current capacity of the array.
            self.cap *= 2
            buffer = [None] * self.cap
            i = 0
            while i < self.rear:
                buffer[i] = self.buf[i]
                i += 1
            self.buf = buffer
        self.buf[self.rear] = data
# This function removes the oldest value from the Queue (the value at the "front" of the Queue).
    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        value = self.buf[self.front]
        self.front += 1
        return value
# This function returns the the oldest value (value at "front") from the Queue without removing it.
    def get_front(self):
        if self.is_empty():
            return None
        return self.buf[self.front]
 # This function returns True if Queue is empty, False otherwise.
    def is_empty(self):
        return self.front > self.rear

    def __len__(self):
        return self.rear - self.front + 1


class Deque:
     # This function initializes the Deque class data members.
    def __init__(self, cap=10):
        self.capacity_value = cap
          # Generate an array that can hold cap elements
        self.deque_list = [None] * self.capacity_value
        self.rear = cap // 2
        self.front = self.rear - 1

    def capacity(self):
        return self.capacity_value
# This function adds data to the "front" of the Deque.
    def push_front(self, data):
        if self.rear - self.front <= self.capacity_value:
            if self.front == -1:
                i = self.rear - 1
                while i >= 0:
                    self.deque_list[i + 1] = self.deque_list[i]
                    i -= 1
                     # Moving data blocks
                self.front = 0
                self.rear += 1
        else:
              # Resize doubles the current capacity of the array
            self.capacity_value *= 2
            temp = [None] * self.capacity_value
            j = self.capacity_value // 2
            w = j // 2
             # Use the while loop to copy the data from the old array to the new array
            i = 0
            while i < j:
                temp[w + i] = self.deque_list[i]
                i += 1
            self.deque_list = temp
            self.front = w - 1
            self.rear = w + j
        self.deque_list[self.front] = data
        self.front -= 1
 # This function removes the value from the "front" of the Deque.
    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        self.front += 1
        return self.deque_list[self.front]
# This function adds data to the "back" of the Deque.
    def push_back(self, data):
        if self.rear - self.front <= self.capacity_value:
            if self.rear == self.capacity_value:
                i = self.front + 1
                while i < self.rear:
                    self.deque_list[i - 1] = self.deque_list[i]
                    i += 1
                self.front -= 1
                self.rear -= 1
        else:
            self.capacity_value *= 2
            temp = [None] * self.capacity_value
            j = self.capacity_value // 2
            w = j // 2
            i = 0
            while i < j:
                temp[w + i] = self.deque_list[i]
                i += 1
            self.deque_list = temp
            self.front = w - 1
            self.rear = w + j
        self.deque_list[self.rear] = data
        self.rear += 1
 # This function removes the value from the "back" of the Deque.
    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        self.rear -= 1
        return self.deque_list[self.rear]
# This function returns the value from the "front" of the Deque without removing it.
    def get_front(self):
        if self.is_empty():
            return None
        return self.deque_list[self.front + 1]
 # This function returns the value from the "back" of the Deque without removing it.
    def get_back(self):
        if self.is_empty():
            return None
        return self.deque_list[self.rear - 1]
 # This function returns True if Deque is empty, False otherwise.
    def is_empty(self):
        return self.rear - self.front == 1

    def __len__(self):
        return self.rear - self.front - 1
# This function returns the k'th value from the "front" of the Deque without removing it.
    def __getitem__(self, k):
        if k < 0 or k >= len(self):
            raise IndexError('Index out of range')
        return self.deque_list[self.front + 1 + k]
