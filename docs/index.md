<!-- ---
hide:
  - toc
--- -->

# Dashboard

<!-- ![LeetCode](images/wordmark.png) -->

<p align="center">
  <img src="images/wordmark.png" alt="LeetCode" width="85%">
</p>

---

**GitHub Pages**: <https://xjasonlyu.github.io/leetcode>

**Source Code**: <https://github.com/xjasonlyu/leetcode>

---

<!-- ![LeetCode Stats](https://leetcard.jacoblin.cool/xjasonlyu?theme=light&font=Play&ext=heatmap) -->

<img
  id="stats"
  align="right"
  src="https://leetcard.jacoblin.cool/xjasonlyu?theme=light&font=Play&ext=heatmap"
  alt="LeetCode Stats"
  width="400px">

<script>
  var stats = document.getElementById("stats")

  let light = "https://leetcard.jacoblin.cool/xjasonlyu?theme=light&font=Play&ext=heatmap";
  let dark = "https://leetcard.jacoblin.cool/xjasonlyu?theme=nord&font=Play&ext=heatmap";

  var palette = __md_get("__palette")
  if (palette && typeof palette.color === "object") {
    var theme = palette.color.scheme === "slate" ? dark : light;
    stats.setAttribute("src", theme)
  }

  document.addEventListener("DOMContentLoaded", function() {
    var ref = document.querySelector("[data-md-component=palette]")
    ref.addEventListener("change", function() {
      var palette = __md_get("__palette")
      if (palette && typeof palette.color === "object") {
        var theme = palette.color.scheme === "slate" ? dark : light;
        stats.setAttribute("src", theme)
      }
    })
  })
</script>

**Some Basic Algorithms**:

- [Binary Search Algorithm](https://www.techiedelight.com/binary-search/)
- [Merge Sort Algorithm](https://www.techiedelight.com/merge-sort/)
- [Quicksort Algorithm](https://www.techiedelight.com/quicksort/)
- [Kruskal’s Algorithm](https://www.techiedelight.com/kruskals-algorithm-for-finding-minimum-spanning-tree/)
- [Breadth First Search (BFS) Algorithm](https://www.techiedelight.com/breadth-first-search/)
- [Depth First Search (DFS) Algorithm](https://www.techiedelight.com/depth-first-search/)
<!-- - [Floyd Warshall Algorithm](https://www.techiedelight.com/pairs-shortest-paths-floyd-warshall-algorithm/)
- [Dijkstra’s Algorithm](https://www.techiedelight.com/single-source-shortest-paths-dijkstras-algorithm/)
- [Bellman Ford Algorithm](https://www.techiedelight.com/single-source-shortest-paths-bellman-ford-algorithm/)
- [Kadane’s Algorithm](https://www.techiedelight.com/maximum-subarray-problem-kadanes-algorithm/)
- [Lee Algorithm](https://www.techiedelight.com/lee-algorithm-shortest-path-in-a-maze/)
- [Flood Fill Algorithm](https://www.techiedelight.com/flood-fill-algorithm/)
- [Floyd’s Cycle Detection Algorithm](https://www.techiedelight.com/detect-cycle-linked-list-floyds-cycle-detection-algorithm/)
- [Union Find Algorithm](https://www.techiedelight.com/disjoint-set-structure-union-find-algorithm/)
- [Topological Sort Algorithm](https://www.techiedelight.com/kahn-topological-sort-algorithm/)
- [KMP Algorithm](https://www.techiedelight.com/implementation-kmp-algorithm-c-cpp-java/)
- [Insertion Sort Algorithm](https://www.techiedelight.com/insertion-sort-iterative-recursive/)
- [Selection Sort Algorithm](https://www.techiedelight.com/selection-sort-iterative-recursive/)
- [Counting Sort Algorithm](https://www.techiedelight.com/counting-sort-algorithm-implementation/)
- [Heap Sort Algorithm](https://www.techiedelight.com/heap-sort-place-place-implementation-c-c/)
- [Kahn’s Topological Sort Algorithm](https://www.techiedelight.com/kahn-topological-sort-algorithm/)
- [Huffman Coding Compression Algorithm](https://www.techiedelight.com/huffman-coding/)
- [Quickselect Algorithm](https://www.techiedelight.com/quickselect-algorithm/)
- [Boyer–Moore Majority Vote Algorithm](https://www.techiedelight.com/find-majority-element-in-an-array-boyer-moore-majority-vote-algorithm/)
- [Euclid’s Algorithm](https://www.techiedelight.com/euclids-algorithm-to-find-gcd-of-two-numbers/) -->

---

_This site is powered by [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and [GitHub Pages](https://pages.github.com/)._
