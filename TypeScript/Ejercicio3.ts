function lengthOfLongestSubstring(s: string): number {
  let subString: string[] = [];
  var highLen = 0;
  var subLen = 0;

  if (s.length != 1) {
    for (var i = 0; i < s.length; i++) {
      subString.push(s.charAt(i));
      var j = subString.lastIndexOf(s.charAt(i)) - 1;
      while (j != -1 && subString.length > 1) {
        if (subString[j] == s.charAt(i)) {
            if (subLen > highLen) {
                highLen = subLen;
            }
            var dupeIndex = subString.indexOf(subString[subLen]);
            if (j < 1) {
                subString.shift();
                subLen--;
            } else {
            for (var k = 0; k <= dupeIndex; k++) {
              subString.shift();
              subLen--;
            }
            break;
          }
        }
        j=j-1;
      }
      subLen++;
    }
    if (subLen > highLen) {
      highLen = subLen;
    }
    return highLen;
  } else {
    return 1;
  }
}
