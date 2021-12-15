"""The 'break' statement can be used to terminate the 'while' loop."""

# Which of the following does not produce the same output?

'''
 cnt = 0
           while True:
                 print cnt
                 cnt+=1
                 if cnt>5:
                      break
   cnt = 0
           while cnt<6:
                 while cnt<6:
                       print cnt
                       cnt+=1

   cnt = 0
           while cnt<6:
                 print cnt
                 cnt+=1

   cnt = 0
           while cnt<6:
                 print cnt
                 if cnt==6:
                      continue
                 cnt+=1
'''