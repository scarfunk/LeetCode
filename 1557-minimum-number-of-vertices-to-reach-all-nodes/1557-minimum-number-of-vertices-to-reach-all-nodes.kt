class Solution {
    fun findSmallestSetOfVertices(n: Int, edges: List<List<Int>>): List<Int> {
        val set = edges.map { it[0] }.toSet() - edges.map { it[1] }.toSet()
        return set.toList()
    }
}