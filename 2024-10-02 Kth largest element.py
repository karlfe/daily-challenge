# Kth Largest Element Finder  --  10-02-2024
# ⏱️ 25 min | [Arrays] | 🌟🌟🌟 Medium
# Your mission: Write a function to find the Kth largest element in an unsorted array.
# Input: An array of integers and an integer k
# Output: The Kth largest element in the array

def kth_largest_sorted(lst, k):
    """kth_largest: function to find the kth largest or kth smallest value in a sorted  array
       inputs:  list -- the list of sorted values to examine
                k    -- the priority value to find
                        * positive numbers find the kth largest, 
                        * negative numbers find the abs(k)th smallest
                        * k == zero, or abs(k) greater than the size of the list, returns None"""
    if abs(k) > len(lst) or k == 0:
        return None
    
    return lst[-(k+1) if k < 0 else -k]

def kth_largest(lst, k):
    """kth_largest: function to find the kth largest or kth smallest value in an array
       inputs:  list -- the list of values to examine
                k    -- the priority value to find
                        * positive numbers find the kth largest 
                        * negative numbers find the abs(k)th smallest
                        * k == zero, or k greater than the size of the list, returns None"""
    lst.sort()
    return kth_largest_sorted(lst, k)


if __name__ == "__main__":
    list1 = [ 10, 4, 1, 27, 100, -3, 97, 94, 61 ]
    tail = { 1 : "st", 2 : 'nd', 3 : 'rd'}

    print(f"list1 = {str(list1)}\n")

    print(f"{len(list1)+1}{tail.get(len(list1) % 10, 'th')} largest = {kth_largest(list1, len(list1)+1)}")
    print(f"(list1 = {str(list1)})\n")

    for k in range(len(list1), 0, -1):
        print(f"{k}{tail.get(abs(k) % 10, 'th')} largest = {kth_largest_sorted(list1, k)}")

    print(f"\n0th largest = {kth_largest_sorted(list1, 0)}\n")
          
    for k in range(1, len(list1)+2):
        print(f"{k}{tail.get(abs(k) % 10, 'th')} smallest = {kth_largest_sorted(list1, -k)}")


# result:

# ...\daily challenge> python3 '.\2024-10-02 Kth largest element.py'
# list1 = [-3, 10, 4, 1, 27, 100, 97, 94, 61]

# 10th largest = None
# (list1 = [-3, 1, 4, 10, 27, 61, 94, 97, 100])

# 9th largest = -3
# 8th largest = 1
# 7th largest = 4
# 6th largest = 10
# 5th largest = 27
# 4th largest = 61
# 3rd largest = 94
# 2nd largest = 97
# 1st largest = 100

# 0th largest = None

# 1st smallest = -3
# 2nd smallest = 1
# 3rd smallest = 4
# 4th smallest = 10
# 5th smallest = 27
# 6th smallest = 61
# 7th smallest = 94
# 8th smallest = 97
# 9th smallest = 100
# 10th smallest = None