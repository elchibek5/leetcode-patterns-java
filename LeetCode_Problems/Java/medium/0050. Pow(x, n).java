class Solution {
    public double myPow(double x, int n) {
        long exponent = (long) n;

        if (exponent < 0) {
            exponent = -exponent;
            x = 1 / x;
        }
        return myPow_(x, exponent);
    }

    private double myPow_(double x, long exponent) {
        if (exponent == 0) return 1;

        return (exponent % 2 == 0) ? myPow_(x * x, exponent / 2)
                                   : myPow_(x * x, exponent / 2) * x;
    }
}
