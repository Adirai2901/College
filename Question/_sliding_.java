public class _sliding_ {
    public static int[] findMaxInSlidingWindow(int[] arr, int k) {
        if (arr == null || arr.length == 0 || k <= 0 || k > arr.length) {
            throw new IllegalArgumentException("Invalid input");
        }

        int[] result = new int[arr.length - k + 1];
        int max = Integer.MIN_VALUE;

        // Find the maximum for the first window
        for (int i = 0; i < k; i++) {
            max = Math.max(max, arr[i]);
        }
        result[0] = max;

        // Slide the window
        for (int i = k; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            } else if (arr[i - k] == max) {
                // Recalculate max if the outgoing element was the maximum
                max = Integer.MIN_VALUE;
                for (int j = i - k + 1; j <= i; j++) {
                    max = Math.max(max, arr[j]);
                }
            }
            result[i - k + 1] = max;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;
        int[] result = findMaxInSlidingWindow(arr, k);

        System.out.print("Maximum values in each sliding window: ");
        for (int val : result) {
            System.out.print(val + " ");
        }
    }
}