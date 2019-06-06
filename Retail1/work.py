

res = 0

ligne= 'czkhhji'

liste = ['h', 'i']
s = [1,1]

i = 0

for k in len(ligne):
    if ligne[k] == liste[i] and ligne[k+1] == liste[i]:
        i+=1
        s[i]+=1
    elif ligne[k] == liste[i] and ligne[k+1] != liste[i]:
        i+=1
    
    if ( i > len(L) ):
        res += s[0] * s[1]
        
        i= 0
        
        s[0] = 1
        s[1] = 1

print( res )
        




