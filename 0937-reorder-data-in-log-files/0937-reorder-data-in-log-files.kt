class Solution {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        val letters = mutableListOf<String>()
        val digits = mutableListOf<String>()

        for(l in logs) {
            if (Character.isDigit(l.split(" ")[1][0])) {
                digits.add(l)
            } else {
                letters.add(l)
            }
        }
        letters.sortWith(Comparator { a, b ->
                val ax = a.split(" ", limit = 2)
                val bx = b.split(" ", limit = 2)
                // 0 은 let1, let2
                // 1 은 abc def xxx
                ax[1].compareTo(bx[1]).let {
                    if (it == 0) ax[0].compareTo(bx[0]) else it
                }
            })
        letters.addAll(digits)
        return letters.toTypedArray()
    }
}