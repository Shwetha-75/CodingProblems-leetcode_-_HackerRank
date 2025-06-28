import java.util.*;
public class Sample2 {
    public static void main(String[] args) 
    {
        List<Integer> list=new ArrayList<Integer>();
        list.add(1);
        list.add(2);
        list.add(3);
        List<Integer> list1=new ArrayList<Integer>();
        list1.add(1);
        list1.add(2);
        list1.add(3);
        list.addAll(list1);
        System.out.println(list);
        Sample2.largestSubSet(list);
    }
    public static void largestSubSet(List<Integer> array)
    {
        List<List<Integer>> list=new ArrayList();
        for(Integer i:array)
        {
            List<Integer> temp=new ArrayList<Integer>();
            temp.add(i);
            list.add(temp);
        }
        for(int i=0;i<array.size();i++)
        {
            for(int j=0;j<i;j++)
            {
                if(array.get(i)%array.get(j)==0 && list.get(i).size()<list.get(j).size()+1)
                {
                    List<Integer> temp1=new ArrayList<Integer>();
                    temp1.add(array.get(i));
                    temp1.addAll(list.get(j));
                    System.out.println(temp1);
                    list.add(i,temp1);
                }
            }
        }
        System.out.println(list);
    }
    
}
