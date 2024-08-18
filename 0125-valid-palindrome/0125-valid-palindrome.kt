class Solution {
    fun isPalindrome(s: String): Boolean {
        var start = 0
        var end = s.length - 1
        while(start < end) {
            when {
                !isChar(s[start]) -> start++
                !isChar(s[end]) -> end--
                else -> {
                    if(toLow(s[start]) != toLow(s[end])) {
                        return false
                    }
                    start++
                    end--
                }
            }
        }
        return true
    }
    
    fun isChar(c: Char): Boolean {
        return Character.isLetterOrDigit(c)
    }
    
    fun toLow(c: Char): Char {
        return Character.toLowerCase(c)
    }
}