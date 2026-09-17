class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        suppliesSet = set(supplies)
        recipesMap = {recipes[i]: ingredients[i] for i in range(0, len(recipes))}
        ans = []
        
        for recipe in recipesMap:
            if self.canMake(recipe, suppliesSet, recipesMap, set()):
                ans.append(recipe)
                
        return ans
    
    def canMake(self, target, suppliesSet, recipesMap, seen):
        if target in suppliesSet:
            return True
        if target in seen:
            return False
        if target not in recipesMap:
            return False
        
        seen.add(target)
        
        for ingredient in recipesMap[target]:
            if not self.canMake(ingredient, suppliesSet, recipesMap, seen):
                return False
        
        suppliesSet.add(target)
        return True
        
        
    
        