## Walrus operator - declares a variable as an expression
```python
n = 5
for i in range(n):
  for j in range(n):
    if i + j == (goal_sum := 4):  # saves a line by not having to declare goal_sum = 4 on another line
      print('i is', i, 'j is', j)
```
## Lambda expressions - an anonymous function
```
sum = lambda a, b: a + b
print(sum(2, 3))

def accepts_function(func, a):
  return func(a, a)

b = accepts_function(sum, 3)

queadratic_equation = lambda x: 3 * x ** 2 + 4 * x - 2
```
## Sum
longer
```
arr = np.array([1, 2, 3])

res = 0
for i in range(arr.size):
  res += arr[i]
```
shorter
```
arr = np.array([1, 2, 3])

res = sum(arr[i] for i in range(arr.size))
```
same also works for `math.prod`
