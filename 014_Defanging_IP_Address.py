# Defanging an IP address
# https://leetcode.com/problems/defanging-an-ip-address/

"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]"."""

def defangIPaddr(address: str) -> str:
  return ('[.]'.join(address.split('.')))
      
address = "1.1.1.1"
print (defangIPaddr(address))


"""# Explanation:
Some may be quick to write a quick replace call on the string for a one line solution, but it's important to examine how this will work. In python, strings are immutable objects, meaning if we are searching for '.', we will have as many stack calls underneath the surface when we replace as the number of occurences of '.' in the string.

Thus, since we cannot modify a string in place like we can an array, and since for a general replace call we could have k instances of '.', where k<=n, the worst-case time complexity for a replace call is actually O(n*k)=O(n*n) where n is the length of the string.

A better approach would be to merely split the string up into an array each time we see a . , then join these elements with the proper '[.]' string. With the split and join functions, we parse the input twice, once as the original string, and once as the split array, however, this equates to a time complexity of O(2*n)=O(n)."""