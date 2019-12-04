import time
def strftime():
    a = time.strftime('%A , %B %d %Y', time.localtime())
    print(a)
    b = time.strftime('%I:%M %p %Z on %b/%d/%Y', time.localtime())
    print(b)
    c = time.strftime('I will meet you on %a %B %d at %I:%M %p', time.localtime())
    print(c)
strftime()
