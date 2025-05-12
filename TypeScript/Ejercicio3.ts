function lengthOfLongestSubstring(s: string): number {
  let subString: string[] = [];
  var highLen = 0;
  var subLen = 0;

  if (s.length != 1) {
    for (var i = 0; i < s.length; i++) {
      subString.push(s.charAt(i));
      if(subString.length > 1 && subString.indexOf(subString[subLen]) != subLen) {
        if (subLen > highLen) {
            highLen = subLen;
        }
        var dupeIndex = subString.indexOf(subString[subLen]);
        for (var k = 0; k <= dupeIndex; k++) {
            subString.shift();
            subLen--;
        }
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
