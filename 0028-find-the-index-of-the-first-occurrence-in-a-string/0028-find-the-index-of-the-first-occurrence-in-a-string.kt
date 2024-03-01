class Solution {
    fun strStr(haystack: String, needle: String): Int {
        var ptr1 = 0
        var i = 0
        while(i < haystack.length) {
            if(needle[ptr1] == haystack[i]) {
                ptr1++
                if(ptr1 == needle.length) return i - needle.length + 1
            } else {
                // reset
                i = i - ptr1
                ptr1 = 0
            }
            i++
        }
        return - 1
    }
}