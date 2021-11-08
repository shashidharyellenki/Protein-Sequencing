    res=dna[startIndex:]
    list_=[]
    string=""
    ignore=["UAG", "UAA","UGA"]
    for letter in range(len(res)):
        if len(string)!=3:
            string+=res[letter]
        if len(string)==3:
            x= string.replace("T","U")
            if x in ignore:
                list_.append(x)
                return list_
            else:
                list_.append(x)
                string=""