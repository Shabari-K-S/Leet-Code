class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        String strChk = "";

        for (char c : s.toCharArray()) {
            int index = strChk.indexOf(c);
            if (index != -1) {
                strChk = strChk.substring(index + 1);
            }
            strChk += c;
            maxLen = Math.max(maxLen, strChk.length());
        }

        return maxLen;
    }
}
