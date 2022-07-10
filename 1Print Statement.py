print("Harshit",end=" ")    #Implicite lineJoining:- Single line
print("Singh\nHello")       #Explicit line Joining:- Divide the line


# Format Fundamental Concept

# Syntax
# format(value, specifier)


# Digit Format

v=format(8/9, '.3f')
print(v)

# String Format

# 1) Right Justification
q = format("Hello","<40")           # 40 is the maximum limit of string
print(q)

# 2) Left justification
w = format("Harshit",">30")         # 30 is the maximum limit of string
print(w)

# 3)Center Justification
E=format("Renu", "^30")
print(E)