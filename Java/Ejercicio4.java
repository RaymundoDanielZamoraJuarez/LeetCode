class Solution {
    public boolean isMatch(String s, String p) {
        HashMap<List<Integer>,Boolean> cache = new HashMap<List<Integer>,Boolean>();
        return dfs(0, 0, s, p, cache);
    }
    private boolean dfs(int sI, int pI, String s, String p, HashMap cache) {
        List<Integer> indexesKey = new ArrayList<Integer>();
        indexesKey.add(sI);
        indexesKey.add(pI);
        if(cache.containsKey(indexesKey)==true){
            return (Boolean) cache.get(indexesKey);
        }
        if (sI == s.length() && pI == p.length()) {
            return true;
        }
        if (pI == p.length()) {
            return false;
        }

        boolean match = sI < s.length() && (p.charAt(pI) == '.' || p.charAt(pI) == s.charAt(sI));
        if(pI+1<p.length()&&p.charAt(pI+1)=='*'){
            cache.put(indexesKey,(dfs(sI,pI+2,s,p,cache) || (match && dfs(sI+1,pI,s,p,cache))));
            return (Boolean) cache.get(indexesKey);
        }
        if(match==true){
            cache.put(indexesKey,dfs(sI+1,pI+1,s,p,cache));
            return (Boolean) cache.get(indexesKey);
        }
        cache.put(indexesKey,false);
        return false;
    }
}
