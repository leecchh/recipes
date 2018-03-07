file = open("chicken.txt","r")
htmlString=file.read()

refinedHtml=""
rerefinedHtml=""
webText=True

for c in htmlString:
	if c=="<" and webText==True:
		webText=False
	if c==">" and webText==False:
		webText=True
	elif webText:
		refinedHtml=refinedHtml+c

webText=True
for c in refinedHtml:
	if c=="{" and webText==True:
		webText=False
	if c=="}" and webText==False:
		webText=True
	elif webText:
		rerefinedHtml=rerefinedHtml+c

refinedHtml=rerefinedHtml

splitHtml=refinedHtml.split()

ingStrLst=["Find", "the", "closest", "stores", "(uses", "your", "location)"]
ingredientList=[]
index=0
ingStart=False

for w in splitHtml:
	if ingStart:
		ingredientList.append(w)
	if not ingStart:
		if w==ingStrLst[index]:
			index+=1
		else:
			index=0
		if index==len(ingStrLst):
			ingStart=True

print ingredientList

# ingStr="Find the closest stores(uses your location)"
# startIng=False
# currIndex=0
# for c in refinedHtml:
# 	if c!=" ":
# 		if startIng==False:
# 			if c==ingStr[currIndex]:
# 				currIndex+=1
# 			else:
# 				currIndex=0
# 			if currIndex==len(ingStr):
# 				startIng=True
# 	if startIng==True:
# 		ingredientString=ingredientString+c

#print rerefinedHtml