class ValidParenthesis
{
    public static void main(String[] args) {
        String str=")))))))))))(())()";
        char array[]=str.toCharArray();
        int left=0;
        int right=array.length-1;
        int count=0;
        while(left<right)
        {
            if(array[left]=='(' && array[right]==')')
            {
                count+=2;
                left+=1;
                right-=1;
            }
            left+=1;
            
        }
        System.out.println(count);
    }
}