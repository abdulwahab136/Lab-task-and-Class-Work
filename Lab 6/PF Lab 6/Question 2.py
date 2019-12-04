def forcast():
    a = 'It will be sunny day today'
    print("Number of time day occurred :",a.count('day'),'times')
    print("Index of word Sunny : ", a.find('sunny'))
    b = a.replace('sunny','cloudy')
    print(b)
forcast()