class Solution {
    public int lengthOfLongestSubstring(String s) {
        ArrayList<Character> subString = new ArrayList<>();
        int highLen = 0;
        int subLen = 0;
        if(s.length() != 1) {
            for(int i = 0; i < s.length(); i++){
                subString.add(s.charAt(i));
                if(subString.size()>1&&subString.indexOf(subString.get(subLen)) != subLen){
                    if(subLen>highLen){
                        highLen=subLen;
                    }
                    int dupeIndex = subString.indexOf(subString.get(subLen));
                    for(int k = 0; k<=dupeIndex; k++){
                        subString.remove(0);
                        subLen--;
                    }
                }
                subLen++;
            }
            if(subLen>highLen){
                highLen=subLen;
            }
            return highLen;
        }
        else{
            return 1;
        }
    }
}
