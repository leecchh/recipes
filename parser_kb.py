


methods = ['cook', 'simmer','heat','roast','barbecue', 'barbeque','grill', 'broil', 'sear','bake','fry','boil','poach','steam','saute','smoke']
meat = ['beef','liver','tongue','bone','buffalo','bison','calf', 'caribou', 'goat', 'ham', 'horse','lamb', 'marrow', 'moose', 'mutton', 'pork', 'bacon', 'rabbit', 'snake','alligator', 'ostrich', 'tripe', 'turtle', 'veal', 'tripe','ground beef','prosciutto','sausage']
fish = ['fish', 'salmon', 'tilapia', 'trout', 'yellow tail', 'flounder', 'sea bass', 'halibut','octopus', 'scallop', 'shrimp', 'oyster', 'clam', 'mussle', 'lobster', 'crab', 'crawfish' ]
cheese = ['cheese','cheddar','brie','goat cheese', 'parmesan', 'american cheese','provolone','swiss chese','manchego', 'cream cheese', 'colby cheese', 'string cheese']
dairy = ['butter','milk', 'curd', 'custard', 'ice cream', 'creme fraiche', 'yogurt']
vegetables = ['tomato', 'spinach','basil','celery','yam','pickle','cucumber','artichoke','arugula','asparagus','avocado','gourd','beet','green beans','bok choy', 'broccoli', 'chard','kale','chive','corn','mushroom', 'coriander','fennel','garlic','heart of palm', 'lettuce','olive','onion', 'pepper','potato','pumpkin','radish','nori','seaweed', 'sprout','squash','cabbage','shoots','zucchini']
meat_subs = ['tofu','mushroom', 'jackfruit','eggplant','beets']
tools = ['saucepan', 'pan', 'baking sheet', 'sheet', 'dish', 'toaster', 'fork','knife','plate','steamer','cooker','roaster','frier','kettle','grill','pan','wok','blender','bowl', 'masher','peeler','grater','knife','whisk','spoon','spatula','tongs','ladle', 'measuring cup', 'funnel', 'thermometer','blow torch']
measurements = ['cup','tablespoon','quart','gallon','pinch','handful', 'pound', 'ounce','gram','stick','teaspoon']






ingredients = ['1/2 cup butter', '1 tablespoon dried parsely', '3 tablespoons minced garlic', '6 boneless chicken thighs, with skin', 'dried parsley, to taste', '3 tablespoons soy sauce', '1/4 teaspoon black pepper']

directions = ['Preheat the oven broiler. Lightly grease a baking pan.', 'In a microwave safe bowl, mix the butter, garlic, soy sauce, pepper, and parsley. Cook 2 minutes on High in the microwave, or until butter is melted.', 'Arrange chicken on the baking pan, and coat with the butter mixture, reserving some of the mixture for basting.','Broil chicken 20 minutes in the preheated oven, until juices run clear, turning occasionally and basting with remaining butter mixture. Sprinkle with parsley to serve.']



recipe = [['ingredients',[]], ['tools',[]], ['methods', []]]


def isin(word, wordlist):
    for werd in wordlist:
        if werd in word:
            return True
    return False



def parse_recipe(ingredientl, directionl, recipel):
    for direc in directionl:
        for method in methods:
            if method in direc:
                recipe[2][1].append(method)
    return recipe

#print(parse_recipe(ingredients, directions, recipe))


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

def ing_and_amount(ingredientl):
    amounts = []
    for ing in ingredientl:
        if is_number(ing[0]):
            x = ing.split(' ',2)
            if isin(x[1], measurements):
                amounts.append([x[2], x[0]+ ' ' +x[1]])
            else:
                amounts.append([x[2], x[0]])
    return amounts

print(ing_and_amount(ingredients))
            


