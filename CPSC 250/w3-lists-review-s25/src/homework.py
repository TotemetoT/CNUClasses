"""
Week 3 homework

@author Ryan Schatzberg
@version 1/31/2025
"""

# Write one function to "Intermingle Lists" given two lists.
#
# So given [1, 2, 3] and [A, B, C], you generate a *new* list that contains [1, A, 2, B, 3, C].
#
# You code should be able to handle the case where either list is shorter than the other,
# but is a list
#
# If either list is defined as `None`, then just return a (shallow) copy of the other list.
#
# Code incrementally
#   1) Solve case for two lists the same size (this is 50 % points)
#   2) Solve for different size lists (25% of points)
#   3) Solve for not valid lists  (25% of points)
#
#  Commit and push after each increment is working

def intermingle_lists(list1,list2):
    if not list1 or list1 == []:
        if not list2 or list2 == []:
            return None
        else:
            return list2
    elif not list2 or list2 == []:
        return list1
    list3 = list1.copy()
    list4 = list2.copy()
    if len(list1) >= len(list2):
        short = list4
        long = list3
    else:
        short = list3
        long = list4
    mingled = []

    for i in range(len(list1)+len(list2)):
        if short:
            if i % 2 == 0:
                mingled.append(list3[0])
                list3.pop(0)
            else:
                mingled.append(list4[0])
                list4.pop(0)
        else:
            mingled.append(long[0])
            long.pop(0)
    return mingled

if __name__ == "__main__":
    # Demonstration code - no need to modify this
    #  And yes, following PEP8 this is how you should name your function
    first = [1, 2, 3]
    second = ['A', 'B', 'C']
    intermingled = intermingle_lists(first, second)

    print("Same list lengths should work: ")
    print(f" first = {first} - should be unchanged!")
    print(f"second = {second} - should be unchanged!")
    print(f"mingled= {intermingled} - should be [1, A, 2, B, 3, C]")

    print("Different lengths should work as well:")
    third = ['A', 'B', 'C', 'D', 'E']
    mingled2 = intermingle_lists(first, third)

    print(f" first = {first} - should be unchanged!")
    print(f" third = {third} - should be unchanged!")
    print(f"mingled= {mingled2} - should be [1, A, 2, B, 3, C, D, E]")
    print(intermingle_lists([1,2,3],None))
    print(intermingle_lists([1,2,3], []))
    print(intermingle_lists([], [1,2,3]))
    print(intermingle_lists(None, [1,2,3]))
