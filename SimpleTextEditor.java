import java.util.*;
class SimpleTextEditor
{
    public static void main(String[] args) 
    {
        Scanner s=new Scanner(System.in);
        int test=s.nextInt();
        List list=new LinkedList();
        s.nextLine();
        String str="";
        while(test!=0)
        {
            String input=s.nextLine();
            String array[]=input.split(" ");
            switch (Integer.parseInt(array[0])) 
            {
                //append operation 
                case 1: 
                      list.add(str);
                      str+=array[1];
                    break;
                //delete
                case 2:
                     list.add(str);
                     str=str.substring(0,str.length()-Integer.parseInt((array[1])));
                     break;
                //print:
                case 3:
                System.out.println(str.charAt(Integer.parseInt(array[1])-1));
                break;
                case 4:
                     str=(String)list.remove(list.size()-1);
                    break;
            }
            test--;
        }
    }
}