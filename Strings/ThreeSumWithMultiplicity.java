
import java.util.HashMap;
import java.util.LinkedHashMap;

public class ThreeSumWithMultiplicity {

    public static void main(String[] args) {
            int arr[]={1,1,2,2,3,3,4,4,5,5};
            int target=8;
            System.out.println(new ThreeSumWithMultiplicity().threeSumMulti(arr,target));
    }

    // Brute Force Approach 

    // public int threeSumMulti(int[] arr, int target) {
    //     // HashMap<Integer,Integer> map = new LinkedHashMap<>();
    //     int count=0;
    //     for(int i=0 ;i<arr.length;i++){
    //         for(int j=i+1;j<arr.length;j++){
    //               for(int k=j+1;k<arr.length;k++){
    //                   if(arr[i]+arr[j]+arr[k]==target){
    //                       count++;
    //                   }
    //               }
    //         }
    //     }
    //     return count;
    // }

    public int threeSumMulti(int[] arr, int target){
        int count=0;
        HashMap<Integer,Integer> map = new LinkedHashMap<>();

        for(int i=0;i<arr.length;i++){
            for(int j=0; j<i-1 ;j++){
                map.put(arr[j]+arr[i-1], map.getOrDefault(arr[j]+arr[i-1], 0)+1);
            }

            count+=map.getOrDefault(target-arr[i], 0);
            
        }
        return (int)(count % ( Math.pow(10,9)+7));
    }
}