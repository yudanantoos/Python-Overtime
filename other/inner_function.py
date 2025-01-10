# Examples

def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power

"""
Here’s what’s happening in this function:

Line 3 creates generate_power(), which is a closure factory function. This means that it creates a new closure each time it’s called and then returns it to the caller.
Line 4 defines power(), which is an inner function that takes a single argument, base, and returns the result of the expression base ** exponent.
Line 6 returns power as a function object, without calling it.
"""

raise_two = generate_power(2)
raise_three = generate_power(3)

print(raise_two(4))
# 16
print(raise_two(5))
# 25
print(raise_three(4))
# 64
print(raise_three(5))
# 125