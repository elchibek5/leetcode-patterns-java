class Solution {
    public String largestOddNumber(String num) {
        int last_digit = num.charAt(num.length() - 1) - '0';

        if (last_digit % 2 != 0) return num;

        for (int i = num.length() - 1; i > -1; i--) {
            int digit = num.charAt(i) - '0';
            if (digit % 2 == 1) {
                return num.substring(0, i + 1);
            }
        }

        return "";

    }
}
