class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result=[] 
        stack=[]
        for i in range(len(words)):
          
            if len("".join(stack))+len(words[i])+1>=maxWidth:
                
                if len("".join(stack))==maxWidth:
                    result.append("".join(stack))
                    stack=[words[i]]
                    print(result)
                elif len("".join(stack))+len(words[i])+1==maxWidth:
                    if not stack:
                       result.append(words[i]+" ") 
                    else:
                        result.append("".join(stack)+" "+words[i])
                    stack=[]
                else:
                    if i==len(words)-1 and len("".join(stack))+len(words[i])+1==maxWidth:
                       stack.append(" ")
                       stack.append(words[i])
                       r=maxWidth-len(stack)
                       
                       result.append("".join(stack)+" "*r) 
                       stack=[]
                    else:
                        temp=[word for word in stack if word!=' ' and word]
                        
                        num_words=len(temp)
                        if len(temp)==1:
                            result.append(temp[0]+" "*(maxWidth-len(temp[0])))
                        
                        elif temp:
                             
                             count=len(''.join(temp))
                             q=(maxWidth-count)//(num_words-1)
                             r=(maxWidth-count)%(num_words-1)
                             temp_index=0
                             if r!=0 and temp_index<len(temp):
                                 while r:
                                       temp[temp_index]+=' '
                                       r-=1
                                       temp_index+=1
                                 result.append((" "*q).join(temp))
                             else:
                                 result.append((" "*q).join(temp)+' '*r)
                       
                    stack=[words[i]]
            else:
                if stack:
                    stack.append(" ")
                    stack.append(words[i])
                else:
                    stack.append(words[i])
        if stack:
           r=maxWidth-len("".join(stack))
           result.append("".join(stack)+" "*r)
        print(result)
        return result        
class TestApp:
      def testing_case_one(self):
          assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)==["This    is    an","example  of text","justification.  "]
      def testing_case_two(self):
          assert Solution().fullJustify(["What","must","be","acknowledgment","shall","be"],16)==["What   must   be","acknowledgment  ","shall be        "]
      def testing_case_three(self):
          assert Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20)==["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]     
      def testing_case_four(self):
          assert Solution().fullJustify(["","Listen","to    ","many, ","speak ","to   a","few.  "],6)==["Listen","to    ","many, ","speak ","to   a","few.  "]     
 
      def testing_case_five(self):
          assert Solution().fullJustify(["What","must","be","shall","be."],5)==["What ","must ","be   ","shall","be.  "]