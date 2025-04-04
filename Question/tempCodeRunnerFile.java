public class _sliding_ {
    public static int findMaxInSlidingWindow(int[] arr, int k) {
        

        int max = Integer.MIN_VALUE;
        for (int i = 0; i < k; i++) {
            max = Math.max(max, arr[i]);
        }

        int[] result = new int[arr.length - k + 1];
        result[0] = max;

        for (int i = k; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            } else if (arr[i - k] == max) {
                max = Integer.MIN_VALUE;
                for (int j = i - k + 1; j <= i; j++) {
                    max = Math.max(max, arr[j]);
                }
            }
            result[i - k + 1] = max;
        }

        return result[result.length - 1];
    }
}
