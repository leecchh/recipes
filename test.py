import urllib

#URL for recipes
url = "https://www.allrecipes.com/recipe/8562/chicken-noodle-soup/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202"
file = urllib.urlopen(url)
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

###################################
#Part 2, Transformation
healthy=["celery", "carrots"]
notHealthy=["butter", "marjoram"]
healthyReplace=[['celery', '1 cup'], ['carrots', '1/4 cup']]
notHealthyReplace=[['butter', '1/4 cup'], ['bacon', '4 strips']]
parsedIngredients=[['chopped, cooked chicken meat', '4 cups'], ['chopped celery', '1 cup'], ['chopped carrots', '1/4 cup'], ['chopped onion', '1/4 cup'], ['butter', '1/4 cup'], ['egg noodles', '8 ounces'], ['water', '12 cups'], ['chicken bouillon', '9'], ['dried marjoram', '1/2 teaspoon'], ['ground black pepper', '1/2 teaspoon'], ['leaf', '1'], ['dried parsley', '1 tablespoon']]

#print parsedIngredients
ingredientChange=[]
#################Remove healthy ingredients
# for i in range(0,len(parsedIngredients)):
# 	words=parsedIngredients[i][0].split()
# 	for word in words:
# 		for j in range(0,len(healthy)):
# 			if word==healthy[j]:
# 				parsedIngredients[i]=notHealthyReplace[j]
# 				ingredientChange.append([word, notHealthyReplace[j][0]])

################Remove unhealthy ingredients
for i in range(0,len(parsedIngredients)):
	words=parsedIngredients[i][0].split()
	for word in words:
		for j in range(0,len(notHealthy)):
			if word==notHealthy[j]:
				parsedIngredients[i]=healthyReplace[j]
				ingredientChange.append([word, healthyReplace[j][0]])

print ingredientChange
for i in range(0,len(directionsList)):
	words=directionsList[i].split()
	for j in range(0, len(words)):
		for pairs in ingredientChange:
			if pairs[0]==words[j]:
				words[j]=pairs[1]
			if pairs[0]==(words[j])[0:len(words[j])-1]:
				separate=(words[j])[len(words[j])-1:len(words[j])]
				words[j]=pairs[1]
				words[j]=words[j]+separate
	newDirections=' '.join(words)
	directionsList[i]=newDirections

print directionsList



#print refinedHtml

