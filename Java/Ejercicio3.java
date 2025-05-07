class Solution {
    public int lengthOfLongestSubstring(String s) {
        ArrayList<Character> subString = new ArrayList<>();
        int highLen = 0;
        int subLen = 0;
        if(s.length() != 1) {
            for(int i = 0; i < s.length(); i++){
                subString.add(s.charAt(i));
                int j=subString.lastIndexOf(s.charAt(i))-1;
                while(j != -1){
                    if(subString.get(j) == s.charAt(i)){
                        if(subLen>highLen){
                            highLen=subLen;
                        }
                        var dupeIndex = subString.indexOf(subString.get(subLen));
                        if(j<1){
                            subString.remove(0);
                            subLen--;
                        }
                        else{
                            for(int k = 0; k<=dupeIndex; k++){
                                subString.remove(0);
                                subLen--;
                            }
                            break;
                        }
                    }
                    j--;
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
