class Solution:
     def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        if len(words)==1:
            return "".join(words+[" "]*(maxWidth-len(words[0])))
        stack=[words[0]]
        result=[]
        word_length=len(words[0])
        for i in range(1,len(words)):
            if word_length+len(words[i])+len(stack)==maxWidth:
               stack.append(words[i])
               for j in range(1,len(stack)):
                   stack[j]=' '+stack[j]
               result.append("".join(stack))
               stack=[]
               word_length=0 
            elif word_length+len(words[i])+len(stack)>maxWidth:
                diff=maxWidth-(word_length+len(stack)-1)     
                #  evenly assign the spaces 
                # check the length of the stack 
                if len(stack)==1:
                   result.append("".join(stack+[' ']*(maxWidth-len(stack[0]))))
                else:
                    for j in range(1,len(stack)):
                        stack[j]=' '+stack[j]
                    while diff:
                          for j in range(1,len(stack)):
                              if diff:
                                  stack[j]=' '+stack[j]
                                  diff-=1
                              else:
                                  break 
                    result.append("".join(stack))
                stack=[words[i]] 
                word_length=len(words[i])
            else:
                stack.append(words[i])
                word_length+=len(words[i])
        if stack:
            if len(stack)==1:
               result.append("".join(stack+[' ']*(maxWidth-len(stack[0]))))
            else:
                diff=maxWidth-(word_length+len(stack)-1)
                for i in range(1,len(stack)):
                    stack[i]=' '+stack[i]
                result.append("".join(stack+[' ']*diff))
      
        return result   
class TestApp:
      def testing_case_one(self):
            assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)==["This    is    an","example  of text","justification.  "]
      def testing_case_two(self):
          assert Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20)==["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
      def testing_case_three(self):
          assert Solution().fullJustify(["What","must","be","acknowledgment","shall","be"],16)==["What   must   be","acknowledgment  ","shall be        "]
