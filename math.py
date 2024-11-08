a = [1,2,3,5,6,7,8,10,11,12,13,14,15,17,18,19,20]
m=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range (len(a)):
    for j in range (len(a)):
        if (a[i]==a[j]):
            continue
        if (a[i]%a[j]==0 or a[j]%a[i]==0):
            continue
        
        
        for k in range(len(m)):
            for l in range(len(n)):
                # print(a[i]*(m[k]**2))
                # print(a[j]*(n[l]**2))
                # print("\n")
                if (a[i]*(m[k]**2)==a[j]*(n[l]**2)):
                    print("Found")
                    print (a[i])
                    print(a[j])
                    print(m[k])
                    print(n[l])
