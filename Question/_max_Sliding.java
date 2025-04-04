public class _max_Sliding {

    public static int maxnum(int[] arr){
       
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++) {
            max = Math.max(max, arr[i]);
        }
        return max;
    }
    public static int minnum(int arr[]){
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            min = Math.min(min, arr[i]);
        }
        return min;
    }
    public static void main(String[] args) {
        int[] nums = {2,4,6,8,10};
        int result = maxnum(nums);
        System.out.println("The maximum number in the array is: " + result);
        System.out.println("The minumun number in the array is: " + minnum(nums));
        
    }
}
