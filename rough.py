    # res=dna[startIndex:]
    # list_=[]
    # string=""
    # ignore=["UAG", "UAA","UGA"]
    # for letter in range(len(res)):
    #     if len(string)!=3:
    #         string+=res[letter]
    #     if len(string)==3:
    #         x= string.replace("T","U")
    #         if x in ignore:
    #             list_.append(x)
    #             return list_
    #         else:
    #             list_.append(x)
    #             string=""

# import json
# def makecodondict(filename):
#     f = open(filename)
#     read = json.load(f)
#     # print(read)
#     d={}
#     for x,y in read.items():
#         # print(y)
#         for i in y:
#             d[i.replace('T','U')]=x
#     print(d)
            


# print(makecodondict("data/codon_table.json"))
# '''
# {
#     "phe":"TTA",
#     "phe":"TTC"
# }
# '''

# def dnaToRna(dna, startIndex):
#     res=dna[startIndex:]
#     list_=[]
#     string=""#atgaug
#     ignore=["UAG", "UAA","UGA"]
#     for letter in range(len(res)):
#         if len(string)!=3:
#             string+=res[letter]
#         if len(string)==3:
#             x= string.replace("T","U")
#             if x in ignore:
#                 list_.append(x)
#                 return list_
#             else:
#                 list_.append(x)
#                 string=""
#     return list_

# dna = "ATGGATGGACTCTAACTCATGCCCTTTTAG"
# print(dnaToRna(dna,0))

from itertools import zip_longest
dict1, dict2=[1,2,3],[4,5]
d={}
for x,y in zip_longest(dict1, dict2, fillvalue=None):
    # if x ==None or y==None:
    #     pass
    # else:
        print(x)
        print(y)