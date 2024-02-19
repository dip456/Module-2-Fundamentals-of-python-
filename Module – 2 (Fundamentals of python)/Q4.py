"""How memory is managed in Python ? """
"""ans :
Python is an interpreted, high-level programming language that is widely used for a variety of applications.
 One of the key features of Python is its automatic memory management, which handles the allocation and deallocation
   of memory for your program. Understanding how Python manages memory is crucial for writing efficient and 
   bug-free code.

In Python, memory management is handled by a private heap space. The heap is a region of memory where objects are 
stored and managed. Python’s memory manager takes care of allocating memory for new objects and freeing memory for 
objects that are no longer in use. This automatic memory management relieves the programmer from the burden of
 manually managing memory, as in other languages like C or C++.

Python uses a technique called reference counting to keep track of objects in memory. Each object in Python has a 
reference count associated with it, which is incremented whenever a new reference to the object is created, and
 decremented whenever a reference to the object is deleted or goes out of scope. When an object’s reference count
   reaches zero, it means that there are no more references to the object, and the memory occupied by the object 
   can be freed.


"""