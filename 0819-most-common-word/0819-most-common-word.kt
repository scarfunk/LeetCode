class Solution {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        val words = paragraph.split(Regex("[^a-zA-Z]")).filter { it.isNotEmpty() }.map { it.lowercase() }
        val bannedSet = banned.toSet()
        val wordCount = mutableMapOf<String, Int>()
        for (word in words) {
            if (!bannedSet.contains(word)) {
                wordCount[word] = wordCount.getOrDefault(word, 0) + 1
            }
        }
        return wordCount.maxByOrNull { it.value }!!.key
    }
}