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
ingStrEndLst=["Add", "all", "ingredients", "to", "list"]
ingredientList=[]
index=0
ingStart=False

for w in splitHtml:
	if ingStart:
		ingredientList.append(w)
		if w==ingStrEndLst[index]:
			index+=1
		else:
			index=0
		if index==len(ingStrEndLst):
			break
	if not ingStart:
		if w==ingStrLst[index]:
			index+=1
		else:
			index=0
		if index==len(ingStrLst):
			ingStart=True
			index=0

currentIng=""
finalIngredients=[]
for w in ingredientList:
	if w=="ADVERTISEMENT":
		finalIngredients.append(currentIng)
		currentIng=""
	else:
		if currentIng=="":
			currentIng+=w
		else:
			currentIng=currentIng+" "+w
#print finalIngredients

dirStartStr="<span class=\"recipe-directions__list--item\">"
dirEndStr="</span></li>"
finalEndStr="</ol>"
currIndex=0
endIndex=0
finalIndex=0
dirStartBool=False
currDirections=""
directionsList=[]

for c in htmlString:
	if dirStartBool:
		currDirections+=c
		if c==dirEndStr[endIndex]:
			endIndex+=1
		else:
			endIndex=0
		if endIndex==len(dirEndStr):
			directionsList.append(currDirections[0:len(currDirections)-len(dirEndStr)])
			currDirections=""
			currIndex=0
			endIndex=0
			finalIndex=0
			dirStartBool=False

		if c==finalEndStr[finalIndex]:
			finalIndex+=1
		else:
			finalIndex=0
		if finalIndex==len(finalEndStr):
			break
	if not dirStartBool:
		if c==dirStartStr[currIndex]:
			currIndex+=1
		else:
			currIndex=0
		if currIndex==len(dirStartStr):
			dirStartBool=True


print directionsList

#print refinedHtml

