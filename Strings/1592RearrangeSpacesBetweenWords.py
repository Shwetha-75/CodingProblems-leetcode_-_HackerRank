class Solution:
    def reorderSpaces(self, text: str) -> str:
        count_words=text.split(" ")
        count_spaces=len(text)-len(text.replace(" ",""))
        # corner case when there is only one word 
        # Add the spaces at the end of the word and return it   
        count_words=[word for word in count_words if word]
        if len(count_words)==1:
           return  count_words[0]+' '.join(count_spaces)
        else:
            quotient=count_spaces//(len(count_words)-1)
            remainder=count_spaces%(len(count_words)-1)
            return (' '*quotient).join(count_words)+' '*remainder 
class TestApp:
       def testing_case_one(self):
           assert Solution().reorderSpaces("  this   is  a sentence ")=="this   is   a   sentence"
       def testing_case_two(self):
           assert Solution().reorderSpaces(" practice   makes   perfect")=="practice   makes   perfect "  
           
           
                          