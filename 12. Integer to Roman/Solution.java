class Solution {
    public String intToRoman(int num) {
        int[] val = {
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        };
        String[] syms = {
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        };
        
        StringBuilder romanNumeral = new StringBuilder();
        int i = 0;
        
        while (num > 0) {
            int div = num / val[i];
            num %= val[i];
            
            while (div > 0) {
                romanNumeral.append(syms[i]);
                div--;
            }
            
            i++;
        }
        
        return romanNumeral.toString();
    }
}