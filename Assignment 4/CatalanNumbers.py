def can_transform_to_target(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    if c < a or d < b:
        return "No"

    if (c - a) % gcd(a, b) == 0 and (d - b) % gcd(a, b) == 0 and (c - a) // gcd(a, b) == (d - b) // gcd(a, b):
        return "Yes"
    else:
        return "No"

# Example usage:
a, b = 1, 2
c, d = 3, 6
result = can_transform_to_target(a, b, c, d)
print(result)  # Output will be "No" for this example.
