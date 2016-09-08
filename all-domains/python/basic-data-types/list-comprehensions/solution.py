#https://www.hackerrank.com/challenges/list-comprehensions
#!/us/bin/env python

# x_coordinates = 1
# y_coordinates = 1
# z_coordinates = 1
# n = 2

x_coordinates = int(raw_input())
y_coordinates = int(raw_input())
z_coordinates = int(raw_input())
n = int(raw_input())

result = [[x, y, z]
          for x in xrange(x_coordinates + 1)
          for y in xrange(y_coordinates + 1)
          for z in xrange(z_coordinates + 1)
          if x + y + z != n]
print(result)
