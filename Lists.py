"""
13-FEB-2018

author: Alejandro Guevara
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [11, 12]

print('Origininal Lists')
print(list)

list.append(10) # Add an item to the end of the list. Equivalent to a[len(a):] = [x]
print(list)
list.extend(l2) # Extend the list by appending all the items from the iterable. It could
                # another list ie. Equivalent to a[len(a):] = iterable.
print(list)
list.insert(0, 0)   # Insert an item at a given position. The first argument is
                    # the index of the element before which to insert, so
                    # a.insert(0, x) inserts at the front of the list, and
                    # a.insert(len(a), x) is equivalent to a.append(x).
print(list)
list.remove(12) # Remove the first item from the list whose value is 12. It is
                # an error if there is no such item.
print(list)
list.pop(0)     # Remove the item at the given position in the list, and return
                # it. If no index is specified, a.pop() removes and returns the
                # last item in the list.
print(list)
print(list.index(9))# Return zero-based index in the list of the first item
                    # whose value is 9. Raises a ValueError if there is no such
                    # item.
                    # list.index(x[, start[, end]])
                    # The optional arguments start and end are interpreted as in
                    # the slice notation and are used to limit the search to a
                    # particular subsequence of the list. The returned index is
                    #computed relative to the beginning of the full sequence
                    # rather than the start argument.
print(list.count(1))# Return the number of times x appears in the list.
list.sort() # Sort the items of the list in place (the arguments can be used for
            # sort customization, see sorted() for their explanation).
print(list)
list.reverse()  # Reverse the elements of the list in place.
print(list)
b = list.copy()     # Return a shallow copy of the list. Equivalent to a[:].
print(b)
list.clear()    # Remove all items from the list. Equivalent to del a[:].
print(list)
