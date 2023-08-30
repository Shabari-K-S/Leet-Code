class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> symbolToValue = new HashMap<>();
        symbolToValue.put("M", 1000);
        symbolToValue.put("CM", 900);
        symbolToValue.put("D", 500);
        symbolToValue.put("CD", 400);
        symbolToValue.put("C", 100);
        symbolToValue.put("XC", 90);
        symbolToValue.put("L", 50);
        symbolToValue.put("XL", 40);
        symbolToValue.put("X", 10);
        symbolToValue.put("IX", 9);
        symbolToValue.put("V", 5);
        symbolToValue.put("IV", 4);
        symbolToValue.put("I", 1);

        int result = 0;
        int i = 0;

        while (i < s.length()) {
            if (i + 1 < s.length() && symbolToValue.containsKey(s.substring(i, i + 2))) {
                result += symbolToValue.get(s.substring(i, i + 2));
                i += 2;
            } else {
                result += symbolToValue.get(s.substring(i, i + 1));
                i++;
            }
        }

        return result;
    }
}