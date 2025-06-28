import java.util.*;
public class Sum {

  public static int findMaxSubarraySum(int[] nums) {

    int n = nums.length;

    if (n == 0) {

      return 0;

    } else if (n == 1) {

      return nums[0];

    }



    int prevMax = nums[0];

    int currMax = Math.max(nums[0], nums[1]);



    for (int i = 2; i < n; i++) {

      int temp = currMax;

      currMax = Math.max(currMax, prevMax + nums[i]);

      prevMax = temp;

    }



    return currMax;

  }



  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);

    int n = scanner.nextInt();

    int[] arr = new int[n];

    for (int i = 0; i < n; i++) {

      arr[i] = scanner.nextInt();

    }

    int maxSubarraySum = findMaxSubarraySum(arr);

    System.out.println("Maximum Subarray Sum: " + maxSubarraySum);

  }

}