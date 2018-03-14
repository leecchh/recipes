
import random


methods = ['cook', 'simmer','heat','roast','barbecue', 'barbeque','grill', 'broil', 'sear','bake','fry','boil','poach','steam','saute','smoke']
meat = ['beef','liver','tongue','bone','buffalo','bison','calf', 'caribou', 'goat', 'ham', 'horse','lamb', 'marrow', 'moose', 'mutton', 'pork', 'bacon', 'rabbit', 'snake','alligator', 'ostrich', 'tripe', 'turtle', 'veal', 'tripe','ground beef','prosciutto','sausage','chicken']
fish = ['fish', 'salmon', 'tilapia', 'trout', 'yellow tail', 'flounder', 'sea bass', 'halibut','octopus', 'scallop', 'shrimp', 'oyster', 'clam', 'mussle', 'lobster', 'crab', 'crawfish' ]
cheese = ['cheese','cheddar','brie','goat cheese', 'parmesan', 'american cheese','provolone','swiss chese','manchego', 'cream cheese', 'colby cheese', 'string cheese']
dairy = ['butter','milk', 'curd', 'custard', 'ice cream', 'creme fraiche', 'yogurt']
non_vegan = ['egg']
vegetables = ['tomato', 'spinach','basil','celery','yam','pickle','cucumber','artichoke','arugula','asparagus','avocado','gourd','beet','green beans','bok choy', 'broccoli', 'chard','kale','chive','corn','mushroom', 'coriander','fennel','garlic','heart of palm', 'lettuce','olive','onion', 'pepper','potato','pumpkin','radish','nori','seaweed', 'sprout','squash','cabbage','shoots','zucchini']
meat_subs = ['tofu','mushroom', 'jackfruit','eggplant','beets']
tools = ['saucepan', 'pan', 'baking sheet', 'sheet', 'dish', 'toaster', 'fork','knife','plate','steamer','cooker','roaster','frier','kettle','grill','pan','wok','blender','bowl', 'masher','peeler','grater','knife','whisk','spoon','spatula','tongs','ladle', 'measuring cup', 'funnel', 'thermometer','blow torch', 'broiler', 'pot']
measurements = ['cup','tablespoon','quart','gallon','pinch','handful', 'pound', 'ounce','gram','stick','teaspoon','cube']
sauce = ['sauce']





ingredients = ['1/2 cup butter', '1 tablespoon dried parsely', '3 tablespoons minced garlic', '6 boneless chicken thighs, with skin', 'dried parsley, to taste', '3 tablespoons soy sauce', '1/4 teaspoon black pepper']

directions = ['Preheat the oven broiler. Lightly grease a baking pan.', 'In a microwave safe bowl, mix the butter, garlic, soy sauce, pepper, and parsley. Cook 2 minutes on High in the microwave, or until butter is melted.', 'Arrange chicken on the baking pan, and coat with the butter mixture, reserving some of the mixture for basting.','Broil chicken 20 minutes in the preheated oven, until juices run clear, turning occasionally and basting with remaining butter mixture. Sprinkle with parsley to serve.']



recipe = [['ingredients',[]], ['tools',[]], ['methods', []]]


def isin(word, wordlist):
    for werd in wordlist:
        if werd.lower() in word.lower():
            return True
    return False



def find(inputs, terms):
    result_set = set()
    for inp in inputs:
        for term in terms:
            if term.lower() in inp:
                result_set.add(term)
    return result_set



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


def has_category(ingredientl, categoryl):
    matching_ents = set()
    for ingredient in ingredientl:
        for ent in categoryl:
            if ent.lower() in ingredient[0].lower():
                matching_ents.add(ent)
    return matching_ents






def isveg(ingredientl):
    a = has_category(ingredientl, meat)
    b = has_category(ingredientl, fish)
    if (a == [] and b == []):
        return True
    elif a == []:
        return b
    elif b == []:
        return a
    else:
        return a.union(b)


def makenonveg(ingredientl, directionsl):
    ingredientl.append(['bacon bits','to taste'])
    directionsl.append(['Sprinkle bacon bits on top of dish'])


def makeveg(ingredientl, directionsl):
    a = isveg(ingredientl)
    new_directions = []
    if a != True:
        for word in a:
            xyz = random.choice(meat_subs)
            for ingredient in ingredientl:
                ingredient[0] = ingredient[0].replace(word, xyz)
            for direction in directionsl:
                new_directions.append(direction.replace(word, xyz))
        return ingredientl, new_directions
    else:
        return "ingredients already vegetarian"
        



import urllib

#URL for recipes
url = "https://www.allrecipes.com/recipe/188957/drunken-shrimp/?internalSource=streams&referringId=1237&referringContentType=recipe%20hub&clickId=st_trending_s"
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
        x = parse_ingredient(finalIngredients)


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


#print directionsList


#print find(directionsList, methods)
#print find(directionsList,tools)
#print directionsList
print makeveg(x, directionsList)
 
