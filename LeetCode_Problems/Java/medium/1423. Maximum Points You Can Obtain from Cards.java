class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int currentScore = 0;

        for (int i = 0; i < k; i++) {
            currentScore += cardPoints[i];
        }

        int maxScore = currentScore;

        int left = k - 1;
        int right = n - 1;

        for (int i = 0; i < k; i++) {
            currentScore -= cardPoints[left];
            currentScore += cardPoints[right];

            maxScore = Math.max(maxScore, currentScore);

            left--;
            right--;
        }

        return maxScore;
    }
}
