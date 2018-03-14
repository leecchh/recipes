import urllib

#URL for recipes
#url = "https://www.allrecipes.com/recipe/8562/chicken-noodle-soup/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202"
url="https://www.allrecipes.com/recipe/25759/steves-chicken-noodle-soup/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%205"
file = urllib.urlopen(url)
htmlString=file.read()

measurements = ['cup','tablespoon','quart','gallon','pinch','handful', 'pound', 'ounce','gram','stick','teaspoon','cube']
methods = ['cook', 'simmer','heat','roast','barbecue', 'barbeque','grill', 'broil', 'sear','bake','fry','boil','poach','steam','saute','smoke']
tools = ['saucepan', 'pan', 'baking sheet', 'sheet', 'dish', 'toaster', 'fork','knife','plate','steamer','cooker','roaster','frier','kettle','grill','pan','wok','blender','bowl', 'masher','peeler','grater','knife','whisk','spoon','spatula','tongs','ladle', 'measuring cup', 'funnel', 'thermometer','blow torch', 'broiler', 'pot', 'skillet', 'whisk']

def find(inputs, terms):
	result_set = set()
	for inp in inputs:
		for term in terms:
			if term.lower() in inp.lower():
				result_set.add(term)
	return result_set

def isin(word, wordlist):
    for werd in wordlist:
        if werd.lower() in word.lower():
            return True
    return False

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def parse_ingredient(ingredientl):
    amounts = []
    for ing in ingredientl:
        if is_number(ing[0]):
            if is_number(ing[1]):
                x = ing.split(' ',3)
                if isin(x[2], measurements):
                    amounts.append([x[3], x[0]+ ' ' +x[1]+ ' '+x[2]])
                else:
                    if len(x) == 4:
                        amounts.append([x[2]+ ' '+ x[3], x[0]+ ' ' +x[1]])
                    else:
                        amounts.append([x[2], x[0]+ ' ' +x[1]])
            else:
                x = ing.split(' ',2)
                if isin(x[1], measurements):
                    amounts.append([x[2], x[0]+ ' ' +x[1]])
                else:
                    if len(x) == 3:
                        amounts.append([x[1]+ ' '+ x[2], x[0]])
                    else:
                        amounts.append([x[1], x[0]])
    return amounts

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


#Let user select what transformation they want
transformSelection = ""
while transformSelection not in ["V","NV","H","UH","HA","NT"]:
	transformSelection = raw_input("What transformation do you want? V for vegetarian, NV for non-vegetarian, H for healthy, UH for unhealthy, HA for Hawaiian, NT for no transformation\n")
	if transformSelection not in ["V","NV","H","UH","HA","NT"]:
		print "Please enter a valid transformation"

#print directionsList

###################################
#Part 2, Transformation
healthy=["celery", "carrot", "fresh rosemary"]




notHealthy=["butter", "marjoram", "fresh rosemary"]
healthyReplace=[['celery', '1 cup'], ['carrots', '1/4 cup'], ['carrots', '1/4 cup']]



notHealthyReplace=[['butter', '1/4 cup'], ['bacon', '4 strips'], ['carrots', '1/4 cup']]
meat = ['beef','liver','tongue','bone','buffalo','bison','calf', 'caribou', 'goat', 'ham', 'horse','lamb', 'marrow', 'moose', 'mutton', 'pork', 'bacon', 'rabbit', 'snake','alligator', 'ostrich', 'tripe', 'turtle', 'veal', 'tripe','ground beef','prosciutto','sausage','chicken']
meatReplace=[]
for m in meat:
	meatReplace.append("vegetarian "+m)

parsedIngredients=parse_ingredient(finalIngredients)
addHawaiianIng=[['pineapples', '5 slices'],['macadamia nuts', '1 cup']]
addHawaiianDir=['Sprinkle macadamia nuts on top, decorate with pineapple slices.']
addMeatIng=[['bacon bits', '1 cup']]
addMeatDir=['Sprinkle bacon bits on top of dish.']

#print parsedIngredients
ingredientChange=[]
################Remove healthy ingredients
if transformSelection=='UH':
	for i in range(0,len(parsedIngredients)):
		for j in range(0,len(healthy)):
			if healthy[j] in parsedIngredients[i][0]:
				parsedIngredients[i]=notHealthyReplace[j]
				ingredientChange.append([healthy[j], notHealthyReplace[j][0]])

###############Remove unhealthy ingredients
if transformSelection=='H':
	for i in range(0,len(parsedIngredients)):
		for j in range(0,len(notHealthy)):
			if notHealthy[j] in parsedIngredients[i][0]:
				parsedIngredients[i]=healthyReplace[j]
				ingredientChange.append([notHealthy[j], healthyReplace[j][0]])

###############Remove meats
if transformSelection=='V':
	for i in range(0,len(parsedIngredients)):
		words=parsedIngredients[i][0].split()
		for k in range(0,len(words)):
			for j in range(0,len(meat)):
				if words[k]==meat[j]:
					ingredientChange.append([words[k], meatReplace[j]])
					words[k]=meatReplace[j]
					parsedIngredients[i][0]=' '.join(words)

################Change healthy-unhealthy, vegetarian-nonvegetarian

if transformSelection!='HA' and transformSelection!='NV':
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

################Hawaii
if transformSelection=='HA':
	for newIng in addHawaiianIng:
		parsedIngredients.append(newIng)
	for newDir in addHawaiianDir:
		directionsList.append(newDir)

if transformSelection=='NV':
	for newIng in addMeatIng:
		parsedIngredients.append(newIng)
	for newDir in addMeatDir:
		directionsList.append(newDir)

print ingredientChange
print "Ingredients: "
print parsedIngredients
print ""
print "Tools: "
print find(directionsList, tools)
print ""
print "Methods: "
print find(directionsList, methods)
print ""

#printing direction list
for i in range(0,len(directionsList)):
	numStr=str(i+1)
	print numStr+") "+directionsList[i]


