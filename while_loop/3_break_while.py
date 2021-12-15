"""The 'break' statement can be used to terminate the 'while' loop."""

# What will be the maximum value of 'cnt'?
cnt = 0
while True:
    while cnt<10:
        cnt+=1
        if cnt>10:
                break
# Infinity, because it goes into endless loop.
