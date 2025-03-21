class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        recipes_list=dict()
        adjacency_list=dict()
        for i in recipes:
            recipes_list[i]=0
        for i in range(len(recipes)):

            for j in ingredients[i]:
                if j in recipes:
                    recipes_list[recipes[i]]+=1
                    if j in adjacency_list:
                        adjacency_list[j].append(recipes[i]) 
                    else:
                        adjacency_list[j]=[recipes[i]]
                elif j not in supplies:
                    recipes_list.pop(recipes[i])

        queue=[]
        result=[]

        while 0 in list(recipes_list.values()):
            idx=list(recipes_list.values()).index(0)
            element=list(recipes_list.keys())[idx]
            queue.append(element)
            if element in adjacency_list:
                for i in adjacency_list[element]:
                    recipes_list[i]-=1

            recipes_list[element]=-1

        return queue