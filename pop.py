stack = [10, 20, 30, 40, 50, 60, 70, 80]

if len(stack) == 0:
    print("stack underflow")
else:
    removed = stack.pop()
    print("popped element:", removed)

print("stack after pop:", stack)

