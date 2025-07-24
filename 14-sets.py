# Sets is like a list of unique items
# note that the repeated words are inserted only once
print(set("my name is Eric and Eric is my name".split()))

# You can also use set(["item1", "item2", "item3"]) notation
seta = { "William", "Eric", "John" }
setb = { "Eric", "Anna", "Jane" }

# intersection of two sets (common items between two sets)
# Or you can use seta.intersection(setb)
print(f"Intersection between a and b: {seta & setb}")

# Symmetric difference (items that are in either set, but not both)
# Or you can use seta.symmetric_difference(setb)
print(f"Symmetric diff from a to b: {seta ^ setb}")
print(f"Symmetric diff from b to a: {setb ^ seta}")

# Difference (items that are in seta but not in setb)
# Or you can use seta.difference(setb)
print(f"Difference from a to b: {seta - setb}")
print(f"Difference from b to a: {setb - seta}")

# Union (all items from both sets)
# Or you can use seta.union(setb)
print(f"Union of a and b: {seta | setb}")