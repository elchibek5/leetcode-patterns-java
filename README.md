# LeetCode Patterns in Java

LeetCode solutions in Java, plus a few Codeforces problems in C++, grouped by the technique each one uses, with the key idea and its time and space complexity on one line.

<!-- counts:start -->
**269 LeetCode** (148 Easy · 103 Medium · 18 Hard) and **16 Codeforces** solutions, organized by 21 techniques.
<!-- counts:end -->

<div align="center">
  <img src="./leetcode-stats.svg?v=1" alt="LeetCode Note stats" />
</div>

<div align="center">
  <p><em>"The human whose code is written in this note shall pass the technical interview."</em></p>
</div>

## How to use this repo

- **Study one pattern at a time.** Pick a technique from the table of contents below and work down its table: read the problem, try it, then compare your approach with the key idea and the solution.
- **Find a problem by number.** Search this page for the number with your browser's find (Ctrl+F or Cmd+F).
- **Practise with an AI coding agent.** Install the [coach skill](#practise-with-an-ai-coach) below: it gives hints one step at a time instead of the answer, reviews your attempt, and suggests what to solve next from this index.

Every LeetCode solution is written the way LeetCode expects it (a `class Solution`, or the class a design problem names), so you can paste it into the LeetCode editor unchanged.

## The index

Each row links the problem number to its page on LeetCode or Codeforces and the title to the solution file. Difficulty is the platform's own rating. Time and space describe the code in the file; space is the extra memory it uses, not counting the returned output.

<!-- index:start -->
| Technique | Problems |
|---|---:|
| [Arrays & Hashing](#arrays--hashing) | 30 |
| [Two Pointers](#two-pointers) | 34 |
| [Sliding Window](#sliding-window) | 10 |
| [Prefix Sum](#prefix-sum) | 10 |
| [Binary Search](#binary-search) | 8 |
| [Stack](#stack) | 12 |
| [Linked List](#linked-list) | 11 |
| [Trees](#trees) | 24 |
| [Heap / Priority Queue](#heap--priority-queue) | 19 |
| [Graphs](#graphs) | 5 |
| [Backtracking](#backtracking) | 6 |
| [Dynamic Programming](#dynamic-programming) | 4 |
| [Greedy](#greedy) | 12 |
| [Intervals](#intervals) | 4 |
| [Sorting](#sorting) | 15 |
| [Bit Manipulation](#bit-manipulation) | 7 |
| [Math](#math) | 28 |
| [Strings](#strings) | 14 |
| [Simulation](#simulation) | 7 |
| [Design](#design) | 6 |
| [Union-Find](#union-find) | 3 |
| [Codeforces](#codeforces) | 16 |

### Arrays & Hashing

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [1](https://leetcode.com/problems/two-sum/) | [Two Sum](LeetCode_Problems/Java/easy/0001.%20Two%20Sum.java) | Easy | One pass with a value→index map; look up target − x before inserting x. | O(n) | O(n) |
| [49](https://leetcode.com/problems/group-anagrams/) | [Group Anagrams](LeetCode_Problems/Java/medium/0049.%20Group%20Anagrams.java) | Medium | Sort each word's letters to form a key and group the words by key in a hash map. | O(n·k log k) | O(n·k) |
| [128](https://leetcode.com/problems/longest-consecutive-sequence/) | [Longest Consecutive Sequence](LeetCode_Problems/Java/medium/0128.%20Longest%20Consecutive%20Sequence.java) | Medium | Put every number in a set; from each number with no predecessor, count upward while the next number exists. | O(n) | O(n) |
| [169](https://leetcode.com/problems/majority-element/) | [Majority Element](LeetCode_Problems/Java/easy/0169.%20Majority%20Element.java) | Easy | Boyer-Moore voting: keep a candidate and a counter, +1 on a match and −1 otherwise, replacing the candidate at zero. | O(n) | O(1) |
| [219](https://leetcode.com/problems/contains-duplicate-ii/) | [Contains Duplicate II](LeetCode_Problems/Java/easy/0219.%20Contains%20Duplicate%20II.java) | Easy | Map each value to its last index; seeing it again within k of that index means true. | O(n) | O(n) |
| [229](https://leetcode.com/problems/majority-element-ii/) | [Majority Element II](LeetCode_Problems/Java/medium/0229.%20Majority%20Element%20II.java) | Medium | Boyer-Moore voting with two candidates and counters, then a second pass checks each appears more than n/3 times. | O(n) | O(1) |
| [274](https://leetcode.com/problems/h-index/) | [H-Index](LeetCode_Problems/Java/medium/0274.%20H-Index.java) | Medium | Bucket papers by citation count, capped at n, then scan down from n until the papers counted reach the index. | O(n) | O(n) |
| [383](https://leetcode.com/problems/ransom-note/) | [Ransom Note](LeetCode_Problems/Java/easy/0383.%20Ransom%20Note.java) | Easy | Count magazine letters in a map, then spend one per ransom-note letter, failing when a count runs out. | O(m + n) | O(m + n) |
| [387](https://leetcode.com/problems/first-unique-character-in-a-string/) | [First Unique Character in a String](LeetCode_Problems/Java/easy/0387.%20First%20Unique%20Character%20in%20a%20String.java) | Easy | Count each char in a map, then return the first index whose char has count 1. | O(n) | O(1) |
| [409](https://leetcode.com/problems/longest-palindrome/) | [Longest Palindrome](LeetCode_Problems/Java/easy/0409.%20Longest%20Palindrome.java) | Easy | Toggle chars in a set; each completed pair adds 2, and any unpaired char left adds 1 for the center. | O(n) | O(n) |
| [448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [Find All Numbers Disappeared in an Array](LeetCode_Problems/Java/easy/0448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array.java) | Easy | Mark each seen value by negating nums[value − 1]; indices left positive are the missing numbers. | O(n) | O(1) |
| [485](https://leetcode.com/problems/max-consecutive-ones/) | [Max Consecutive Ones](LeetCode_Problems/Java/easy/0485.%20Max%20Consecutive%20Ones.java) | Easy | Count the current run of 1s, reset it at each 0, and keep the longest run. | O(n) | O(1) |
| [771](https://leetcode.com/problems/jewels-and-stones/) | [Jewels and Stones](LeetCode_Problems/Java/easy/0771.%20Jewels%20and%20Stones.java) | Easy | Count every stone type in a map, then sum the counts of the jewel types. | O(m + n) | O(1) |
| [804](https://leetcode.com/problems/unique-morse-code-words/) | [Unique Morse Code Words](LeetCode_Problems/Java/easy/0804.%20Unique%20Morse%20Code%20Words.java) | Easy | Translate each word letter by letter into Morse code and count the distinct encodings in a set. | O(S) | O(S) |
| [819](https://leetcode.com/problems/most-common-word/) | [Most Common Word](LeetCode_Problems/Java/easy/0819.%20Most%20Common%20Word.java) | Easy | Lowercase and split on non-letters, count non-banned words in a map, and track the most frequent one. | O(n + m) | O(n + m) |
| [867](https://leetcode.com/problems/transpose-matrix/) | [Transpose Matrix](LeetCode_Problems/Java/easy/0867.%20Transpose%20Matrix.java) | Easy | Copy matrix[i][j] into result[j][i] of a new cols × rows matrix. | O(m·n) | O(1) |
| [1207](https://leetcode.com/problems/unique-number-of-occurrences/) | [Unique Number of Occurrences](LeetCode_Problems/Java/easy/1207.%20Unique%20Number%20of%20Occurrences.java) | Easy | Count occurrences in a map; the counts must all be distinct, checked by putting them in a set. | O(n) | O(n) |
| [1470](https://leetcode.com/problems/shuffle-the-array/) | [Shuffle the Array](LeetCode_Problems/Java/easy/1470.%20Shuffle%20the%20Array.java) | Easy | Interleave the halves: ans[2i] = nums[i] and ans[2i + 1] = nums[i + n]. | O(n) | O(1) |
| [1572](https://leetcode.com/problems/matrix-diagonal-sum/) | [Matrix Diagonal Sum](LeetCode_Problems/Java/easy/1572.%20Matrix%20Diagonal%20Sum.java) | Easy | Add mat[i][i] and mat[i][n − 1 − i] for every row, skipping the second when it is the same cell. | O(n) | O(1) |
| [1582](https://leetcode.com/problems/special-positions-in-a-binary-matrix/) | [Special Positions in a Binary Matrix](LeetCode_Problems/Java/easy/1582.%20Special%20Positions%20in%20a%20Binary%20Matrix.java) | Easy | Count the 1s in every row and column, then count cells holding 1 whose row and column counts are both 1. | O(m·n) | O(m + n) |
| [1748](https://leetcode.com/problems/sum-of-unique-elements/) | [Sum of Unique Elements](LeetCode_Problems/Java/easy/1748.%20Sum%20of%20Unique%20Elements.java) | Easy | Count every number in a map, then sum the keys whose count is 1. | O(n) | O(n) |
| [1929](https://leetcode.com/problems/concatenation-of-array/) | [Concatenation of Array](LeetCode_Problems/Java/easy/1929.%20Concatenation%20of%20Array.java) | Easy | Fill an array of length 2n with nums[i mod n]. | O(n) | O(1) |
| [1941](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/) | [Check if All Characters Have Equal Number of Occurrences](LeetCode_Problems/Java/easy/1941.%20Check%20if%20All%20Characters%20Have%20Equal%20Number%20of%20Occurrences.java) | Easy | Count every char in a map and check that every count equals the first char's count. | O(n) | O(n) |
| [2022](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | [Convert 1D Array Into 2D Array](LeetCode_Problems/Java/easy/2022.%20Convert%201D%20Array%20Into%202D%20Array.java) | Easy | If the sizes match, place original[i] at row i / n, column i mod n. | O(m·n) | O(1) |
| [2404](https://leetcode.com/problems/most-frequent-even-element/) | [Most Frequent Even Element](LeetCode_Problems/Java/easy/2404.%20Most%20Frequent%20Even%20Element.java) | Easy | Count even values in a map, then pick the highest count, breaking ties toward the smaller value. | O(n) | O(n) |
| [2657](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) | [Find the Prefix Common Array of Two Arrays](LeetCode_Problems/Java/medium/2657.%20Find%20the%20Prefix%20Common%20Array%20of%20Two%20Arrays.java) | Medium | Walk both permutations, adding each value to a seen set; a value already seen means it has just become common. | O(n) | O(n) |
| [3005](https://leetcode.com/problems/count-elements-with-maximum-frequency/) | [Count Elements With Maximum Frequency](LeetCode_Problems/Java/easy/3005.%20Count%20Elements%20With%20Maximum%20Frequency.java) | Easy | Count frequencies, then add up the frequencies of every element tied for the maximum. | O(n) | O(n) |
| [3065](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/) | [Minimum Operations to Exceed Threshold Value I](LeetCode_Problems/Java/easy/3065.%20Minimum%20Operations%20to%20Exceed%20Threshold%20Value%20I.java) | Easy | Count the elements below k; each one takes one removal. | O(n) | O(1) |
| [3917](https://leetcode.com/problems/count-indices-with-opposite-parity/) | [Count Indices With Opposite Parity](LeetCode_Problems/Java/easy/3917.%20Count%20Indices%20With%20Opposite%20Parity.java) | Easy | Brute force: for each index, count the elements from it onward with the opposite parity. | O(n^2) | O(1) |
| [3925](https://leetcode.com/problems/concatenate-array-with-reverse/) | [Concatenate Array With Reverse](LeetCode_Problems/Java/easy/3925.%20Concatenate%20Array%20With%20Reverse.java) | Easy | Copy nums into the first half, then copy it again in reverse into the second half. | O(n) | O(1) |

### Two Pointers

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [11](https://leetcode.com/problems/container-with-most-water/) | [Container With Most Water](LeetCode_Problems/Java/medium/0011.%20Container%20With%20Most%20Water.java) | Medium | Start at both ends, record the area, then move the shorter wall inward because it caps the height. | O(n) | O(1) |
| [15](https://leetcode.com/problems/3sum/) | [3Sum](LeetCode_Problems/Java/medium/0015.%203Sum.java) | Medium | Sort, fix each distinct anchor, then move two pointers inward toward a zero sum, skipping duplicate values. | O(n^2) | O(log n) |
| [19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [Remove Nth Node From End of List](LeetCode_Problems/Java/easy/0019.%20Remove%20Nth%20Node%20From%20End%20of%20List.java) | Medium | From a dummy node, move a fast pointer n + 1 steps ahead, advance both until fast ends, then unlink slow.next. | O(sz) | O(1) |
| [26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Remove Duplicates from Sorted Array](LeetCode_Problems/Java/easy/0026.%20Remove%20Duplicates%20from%20Sorted%20Array.java) | Easy | A write index keeps one copy of each value, copying nums[i] only when it differs from nums[i − 1]. | O(n) | O(1) |
| [27](https://leetcode.com/problems/remove-element/) | [Remove Element](LeetCode_Problems/Java/easy/0027.%20Remove%20Element.java) | Easy | Copy every element that is not val forward to a write index; the index is the new length. | O(n) | O(1) |
| [42](https://leetcode.com/problems/trapping-rain-water/) | [Trapping Rain Water](LeetCode_Problems/Java/hard/0042.%20Trapping%20Rain%20Water.java) | Hard | Move the lower side inward, tracking its running max; water above a bar is that max minus its height. | O(n) | O(1) |
| [75](https://leetcode.com/problems/sort-colors/) | [Sort Colors](LeetCode_Problems/Java/medium/0075.%20Sort%20Colors.java) | Medium | Dutch national flag: a cursor swaps 0s down to the low pointer and 2s up to the high pointer, skipping 1s. | O(n) | O(1) |
| [80](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | [Remove Duplicates from Sorted Array II](LeetCode_Problems/Java/easy/0080.%20Remove%20Duplicates%20from%20Sorted%20Array%20II.java) | Medium | Write nums[i] only when it differs from the value two slots behind the write index, keeping at most two copies. | O(n) | O(1) |
| [88](https://leetcode.com/problems/merge-sorted-array/) | [Merge Sorted Array](LeetCode_Problems/Java/easy/0088.%20Merge%20Sorted%20Array.java) | Easy | Fill nums1 from the back, taking the larger of the two tails until nums2 is used up. | O(m + n) | O(1) |
| [125](https://leetcode.com/problems/valid-palindrome/) | [Valid Palindrome](LeetCode_Problems/Java/easy/0125.%20Valid%20Palindrome.java) | Easy | Move pointers inward from both ends, skipping non-alphanumerics, and compare chars case-insensitively. | O(n) | O(1) |
| [141](https://leetcode.com/problems/linked-list-cycle/) | [Linked List Cycle](LeetCode_Problems/Java/easy/0141.%20Linked%20List%20Cycle.java) | Easy | Floyd's tortoise and hare: a pointer moving two steps meets the one-step pointer only if there is a cycle. | O(n) | O(1) |
| [142](https://leetcode.com/problems/linked-list-cycle-ii/) | [Linked List Cycle II](LeetCode_Problems/Java/medium/0142.%20Linked%20List%20Cycle%20II.java) | Medium | Once fast and slow meet, restart slow at the head; stepping both singly, they meet at the cycle start. | O(n) | O(1) |
| [160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [Intersection of Two Linked Lists](LeetCode_Problems/Java/easy/0160.%20Intersection%20of%20Two%20Linked%20Lists.java) | Easy | One pointer walks A then B, the other B then A; equal total distance makes them meet at the intersection or null. | O(m + n) | O(1) |
| [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Two Sum II - Input Array Is Sorted](LeetCode_Problems/Java/medium/0167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.java) | Medium | Pointers at both ends: move left up when the sum is too small and right down when it is too large. | O(n) | O(1) |
| [189](https://leetcode.com/problems/rotate-array/) | [Rotate Array](LeetCode_Problems/Java/medium/0189.%20Rotate%20Array.java) | Medium | Reverse the whole array, then reverse the first k elements and the remaining n − k elements. | O(n) | O(1) |
| [202](https://leetcode.com/problems/happy-number/) | [Happy Number](LeetCode_Problems/Java/easy/0202.%20Happy%20Number.java) | Easy | Floyd cycle detection on the digit-square-sum sequence; stop when fast reaches 1 or meets slow. | O(log n) | O(1) |
| [283](https://leetcode.com/problems/move-zeroes/) | [Move Zeroes](LeetCode_Problems/Java/easy/0283.%20Move%20Zeroes.java) | Easy | Copy each non-zero forward to a write index, then fill the rest with zeros. | O(n) | O(1) |
| [287](https://leetcode.com/problems/find-the-duplicate-number/) | [Find the Duplicate Number](LeetCode_Problems/Java/medium/0287.%20Find%20the%20Duplicate%20Number.java) | Medium | Treat each value as a pointer to an index; Floyd's cycle detection finds the cycle entrance, which is the duplicate. | O(n) | O(1) |
| [344](https://leetcode.com/problems/reverse-string/) | [Reverse String](LeetCode_Problems/Java/easy/0344.%20Reverse%20String.java) | Easy | Swap the two ends and move both pointers inward until they meet. | O(n) | O(1) |
| [345](https://leetcode.com/problems/reverse-vowels-of-a-string/) | [Reverse Vowels of a String](LeetCode_Problems/Java/easy/0345.%20Reverse%20Vowels%20of%20a%20String.java) | Easy | Two pointers skip non-vowels from each end, then swap the vowels they stop on. | O(n) | O(n) |
| [350](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | [Intersection of Two Arrays II](LeetCode_Problems/Java/medium/0350.%20Intersection%20of%20Two%20Arrays%20II.java) | Easy | Sort both arrays and walk them with two pointers, collecting values that match. | O(m log m + n log n) | O(min(m, n)) |
| [392](https://leetcode.com/problems/is-subsequence/) | [Is Subsequence](LeetCode_Problems/Java/easy/0392.%20Is%20Subsequence.java) | Easy | Scan t once, advancing a pointer in s on every match; s is a subsequence if it gets fully matched. | O(\|t\|) | O(1) |
| [443](https://leetcode.com/problems/string-compression/) | [String Compression](LeetCode_Problems/Java/medium/0443.%20String%20Compression.java) | Medium | A read pointer measures each run; a write pointer stores the char and, for runs longer than 1, the count's digits. | O(n) | O(1) |
| [541](https://leetcode.com/problems/reverse-string-ii/) | [Reverse String II](LeetCode_Problems/Java/easy/0541.%20Reverse%20String%20II.java) | Easy | Step through the string in chunks of 2k and reverse the first k chars of each chunk in place. | O(n) | O(n) |
| [557](https://leetcode.com/problems/reverse-words-in-a-string-iii/) | [Reverse Words in a String III](LeetCode_Problems/Java/easy/0557.%20Reverse%20Words%20in%20a%20String%20III.java) | Easy | Scan for spaces and reverse each word's chars in place between its start and the next space. | O(n) | O(n) |
| [611](https://leetcode.com/problems/valid-triangle-number/) | [Valid Triangle Number](LeetCode_Problems/Java/medium/0611.%20Valid%20Triangle%20Number.java) | Medium | Sort; for each largest side i, two pointers count pairs summing above nums[i], adding b − a pairs at once. | O(n^2) | O(log n) |
| [680](https://leetcode.com/problems/valid-palindrome-ii/) | [Valid Palindrome II](LeetCode_Problems/Java/easy/0680.%20Valid%20Palindrome%20II.java) | Easy | Move two pointers inward; at the first mismatch, check whether skipping the left or the right char leaves a palindrome. | O(n) | O(1) |
| [905](https://leetcode.com/problems/sort-array-by-parity/) | [Sort Array By Parity](LeetCode_Problems/Java/easy/0905.%20Sort%20Array%20By%20Parity.java) | Easy | Swap each even number forward to a write pointer. | O(n) | O(1) |
| [922](https://leetcode.com/problems/sort-array-by-parity-ii/) | [Sort Array By Parity II](LeetCode_Problems/Java/easy/0922.%20Sort%20Array%20By%20Parity%20II.java) | Easy | One pointer walks even slots past evens, another walks odd slots past odds; swap the misplaced values they find. | O(n) | O(1) |
| [977](https://leetcode.com/problems/squares-of-a-sorted-array/) | [Squares of a Sorted Array](LeetCode_Problems/Java/easy/0977.%20Squares%20of%20a%20Sorted%20Array.java) | Easy | Compare absolute values at both ends and write the larger square into the answer from the back. | O(n) | O(1) |
| [1089](https://leetcode.com/problems/duplicate-zeros/) | [Duplicate Zeros](LeetCode_Problems/Java/easy/1089.%20Duplicate%20Zeros.java) | Easy | Count zeros, then copy from the back with a write index shifted by that count, writing zeros twice when in bounds. | O(n) | O(1) |
| [2161](https://leetcode.com/problems/partition-array-according-to-given-pivot/) | [Partition Array According to Given Pivot](LeetCode_Problems/Java/medium/2161.%20Partition%20Array%20According%20to%20Given%20Pivot.java) | Medium | With a write pointer, place the smaller values in order, then every pivot copy, then a second pass of larger values. | O(n) | O(1) |
| [2465](https://leetcode.com/problems/number-of-distinct-averages/) | [Number of Distinct Averages](LeetCode_Problems/Java/easy/2465.%20Number%20of%20Distinct%20Averages.java) | Easy | Sort, pair the smallest with the largest while moving inward, and count the distinct pair sums in a set. | O(n log n) | O(n) |
| [2540](https://leetcode.com/problems/minimum-common-value/) | [Minimum Common Value](LeetCode_Problems/Java/easy/2540.%20Minimum%20Common%20Value.java) | Easy | Walk both sorted arrays, advancing the side with the smaller value; the first equal pair is the answer. | O(m + n) | O(1) |

### Sliding Window

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Longest Substring Without Repeating Characters](LeetCode_Problems/Java/medium/0003.%20Longest%20Substring%20Without%20Repeating%20Characters.java) | Medium | Grow the window rightward; while the new char is already in the set, drop chars from the left; track the widest window. | O(n) | O(1) |
| [239](https://leetcode.com/problems/sliding-window-maximum/) | [Sliding Window Maximum](LeetCode_Problems/Java/hard/0239.%20Sliding%20Window%20Maximum.java) | Hard | Monotonic deque of indices: drop indices that left the window and smaller values at the back; the front is the max. | O(n) | O(k) |
| 325 | [Maximum Sum of Subarrays of Size K](LeetCode_Problems/Java/easy/0325.%20Maximum%20Sum%20of%20Subarrays%20of%20Size%20K.java) | — | Fixed-size window: add the new element; once the window holds k elements, record its sum and drop the leftmost. | O(n) | O(1) |
| [424](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Longest Repeating Character Replacement](LeetCode_Problems/Java/medium/0424.%20Longest%20Repeating%20Character%20Replacement.java) | Medium | Window with letter counts; shrink while its size minus the top letter frequency exceeds k; track the widest window. | O(n) | O(1) |
| [594](https://leetcode.com/problems/longest-harmonious-subsequence/) | [Longest Harmonious Subsequence](LeetCode_Problems/Java/easy/0594.%20Longest%20Harmonious%20Subsequence.java) | Easy | Sort, then keep a window whose max − min is at most 1, recording its size when the difference is exactly 1. | O(n log n) | O(log n) |
| [904](https://leetcode.com/problems/fruit-into-baskets/) | [Fruit Into Baskets](LeetCode_Problems/Java/medium/0904.%20Fruit%20Into%20Baskets.java) | Medium | A window of fruit counts that never shrinks: whenever it holds more than two types, slide its left edge one step. | O(n) | O(1) |
| [1423](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | [Maximum Points You Can Obtain from Cards](LeetCode_Problems/Java/medium/1423.%20Maximum%20Points%20You%20Can%20Obtain%20from%20Cards.java) | Medium | Start with the first k cards, then trade the prefix's last card for the next card from the end, k times. | O(k) | O(1) |
| [1438](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](LeetCode_Problems/Java/medium/1438.%20Longest%20Continuous%20Subarray%20With%20Absolute%20Diff%20Less%20Than%20or%20Equal%20to%20Limit.java) | Medium | Two monotonic deques track the window's max and min; advance left while max − min exceeds limit. | O(n) | O(n) |
| [1984](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) | [Minimum Difference Between Highest and Lowest of K Scores](LeetCode_Problems/Java/easy/1984.%20Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores.java) | Easy | Sort, then slide a window of k values and minimize its last minus first value. | O(n log n) | O(log n) |
| [2461](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) | [Maximum Sum of Distinct Subarrays With Length K](LeetCode_Problems/Java/medium/2461.%20Maximum%20Sum%20of%20Distinct%20Subarrays%20With%20Length%20K.java) | Medium | Keep a set of the window's values: shrink past any duplicate; at size k, record the sum and drop the leftmost. | O(n) | O(k) |

### Prefix Sum

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [238](https://leetcode.com/problems/product-of-array-except-self/) | [Product of Array Except Self](LeetCode_Problems/Java/medium/0238.%20Product%20of%20Array%20Except%20Self.java) | Medium | Fill ans with prefix products from the left, then multiply in a running suffix product from the right. | O(n) | O(1) |
| [303](https://leetcode.com/problems/range-sum-query-immutable/) | [Range Sum Query - Immutable](LeetCode_Problems/Java/easy/0303.%20Range%20Sum%20Query%20-%20Immutable.java) | Easy | Precompute prefix sums; a range sum is prefix[right + 1] − prefix[left]. | O(n) build, O(1) query | O(n) |
| [304](https://leetcode.com/problems/range-sum-query-2d-immutable/) | [Range Sum Query 2D - Immutable](LeetCode_Problems/Java/medium/0304.%20Range%20Sum%20Query%202D%20-%20Immutable.java) | Medium | Build 2D prefix sums by inclusion-exclusion; a region sum combines four corner values. | O(m·n) build, O(1) query | O(m·n) |
| [370](https://leetcode.com/problems/range-addition/) | [Range Addition](LeetCode_Problems/Java/medium/0370.%20Range%20Addition.java) | Medium | Difference array: add the value at start, subtract it just after end, then prefix-sum the array once. | O(length + k) | O(1) |
| [560](https://leetcode.com/problems/subarray-sum-equals-k/) | [Subarray Sum Equals K](LeetCode_Problems/Java/medium/0560.%20Subarray%20Sum%20Equals%20K.java) | Medium | Keep a running prefix sum and a count map of earlier prefix sums; add the count of prefix − k each step. | O(n) | O(n) |
| [862](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | [Shortest Subarray with Sum at Least K](LeetCode_Problems/Java/hard/0862.%20Shortest%20Subarraywith%20Sumat%20Least%20K.java) | Hard | Prefix sums with a deque of increasing prefixes: pop the front while the sum reaches k, pop larger prefixes off the back. | O(n) | O(n) |
| [1109](https://leetcode.com/problems/corporate-flight-bookings/) | [Corporate Flight Bookings](LeetCode_Problems/Java/medium/1109.%20Corporate%20Flight%20Bookings.java) | Medium | Difference array: add seats at first, subtract them after last, then a running total gives each flight's seats. | O(n + m) | O(n) |
| [1674](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) | [Minimum Moves to Make Array Complementary](LeetCode_Problems/Java/medium/1674.%20Minimum%20Moves%20to%20Make%20Array%20Complementary.java) | Medium | Per pair, mark on a difference array over target sums where it costs 0, 1 or 2 moves; prefix-sum, take the minimum. | O(n + limit) | O(limit) |
| [1854](https://leetcode.com/problems/maximum-population-year/) | [Maximum Population Year](LeetCode_Problems/Java/easy/1854.%20Maximum%20Population%20Year.java) | Easy | Difference array over 1950–2050: +1 at birth, −1 at death; a running total finds the earliest peak year. | O(n) | O(1) |
| [2536](https://leetcode.com/problems/increment-submatrices-by-one/) | [Increment Submatrices by One](LeetCode_Problems/Java/medium/2536.%20Increment%20Submatrices%20by%20One.java) | Medium | 2D difference array: mark four corners per query, then a 2D prefix sum yields every cell's count. | O(n^2 + q) | O(n^2) |

### Binary Search

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [69](https://leetcode.com/problems/sqrtx/) | [Sqrt(x)](LeetCode_Problems/Java/easy/0069.%20Sqrt%28x%29.java) | Easy | Binary search 0..x for the largest mid whose square, computed as a long, is at most x. | O(log x) | O(1) |
| [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Find Minimum in Rotated Sorted Array](LeetCode_Problems/Java/medium/0153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.java) | Medium | If nums[mid] > nums[r] the minimum lies right of mid, otherwise at mid or left of it; shrink until l meets r. | O(log n) | O(1) |
| [154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | [Find Minimum in Rotated Sorted Array II](LeetCode_Problems/Java/hard/0154.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II.java) | Hard | Rotated-array binary search against nums[r]; when nums[mid] equals nums[r], drop r by one because duplicates hide the side. | O(log n), O(n) worst | O(1) |
| [278](https://leetcode.com/problems/first-bad-version/) | [First Bad Version](LeetCode_Problems/Java/easy/0278.%20First%20Bad%20Version.java) | Easy | Binary search for the leftmost bad version, remembering each bad mid and searching left of it. | O(log n) | O(1) |
| [367](https://leetcode.com/problems/valid-perfect-square/) | [Valid Perfect Square](LeetCode_Problems/Java/easy/0367.%20Valid%20Perfect%20Square.java) | Easy | Binary search 0..num with longs; true if some mid squared equals num exactly. | O(log num) | O(1) |
| [374](https://leetcode.com/problems/guess-number-higher-or-lower/) | [Guess Number Higher or Lower](LeetCode_Problems/Java/easy/0374.%20Guess%20Number%20Higher%20or%20Lower.java) | Easy | Binary search 1..n, moving by the sign that guess returns until it returns 0. | O(log n) | O(1) |
| [441](https://leetcode.com/problems/arranging-coins/) | [Arranging Coins](LeetCode_Problems/Java/easy/0441.%20Arranging%20Coins.java) | Easy | Binary search, with longs, for the largest row count k where k(k + 1)/2 ≤ n. | O(log n) | O(1) |
| [1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [Capacity To Ship Packages Within D Days](LeetCode_Problems/Java/medium/1011.%20Capacity%20To%20Ship%20Packages%20Within%20D%20Days.java) | Medium | Binary search the capacity between the heaviest package and the total, greedily counting the days each capacity needs. | O(n log S) | O(1) |

### Stack

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [20](https://leetcode.com/problems/valid-parentheses/) | [Valid Parentheses](LeetCode_Problems/Java/easy/0020.%20Valid%20Parentheses.java) | Easy | Push opening brackets; each closing bracket must match the top; the string is valid if the stack ends empty. | O(n) | O(n) |
| [32](https://leetcode.com/problems/longest-valid-parentheses/) | [Longest Valid Parentheses](LeetCode_Problems/Java/hard/0032.%20Longest%20Valid%20Parentheses.java) | Hard | Stack indices over a -1 base; on ')' pop, then measure from the new top, or make i the base if empty. | O(n) | O(n) |
| [150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Evaluate Reverse Polish Notation](LeetCode_Problems/Java/medium/0150.%20Evaluate%20Reverse%20Polish%20Notation.java) | Medium | Push numbers; on an operator pop two operands, apply it with the earlier operand on the left, and push the result. | O(n) | O(n) |
| [234](https://leetcode.com/problems/palindrome-linked-list/) | [Palindrome Linked List](LeetCode_Problems/Java/easy/0234.%20Palindrome%20Linked%20List.java) | Easy | Push first-half values while a fast pointer runs ahead, skip the middle if odd, then pop to compare with the second half. | O(n) | O(n) |
| [394](https://leetcode.com/problems/decode-string/) | [Decode String](LeetCode_Problems/Java/medium/0394.%20Decode%20String.java) | Medium | Two stacks hold repeat counts and outer builders; on ']' append the inner string count times to the popped outer one. | O(n + L) | O(n + L) |
| [402](https://leetcode.com/problems/remove-k-digits/) | [Remove K Digits](LeetCode_Problems/Java/medium/0402.%20Remove%20K%20Digits.java) | Medium | Monotonic stack: pop larger earlier digits while k remains, cut any leftover k from the end, strip leading zeros. | O(n) | O(n) |
| [496](https://leetcode.com/problems/next-greater-element-i/) | [Next Greater Element I](LeetCode_Problems/Java/easy/0496.%20Next%20Greater%20Element%20I.java) | Easy | A monotonic stack over nums2 maps each value to the first larger value after it; then look up each nums1 value. | O(m + n) | O(n) |
| [503](https://leetcode.com/problems/next-greater-element-ii/) | [Next Greater Element II](LeetCode_Problems/Java/medium/0503.%20Next%20Greater%20Element%20II.java) | Medium | Monotonic stack of indices over two passes of the circular array; a larger value resolves every smaller index it pops. | O(n) | O(n) |
| [739](https://leetcode.com/problems/daily-temperatures/) | [Daily Temperatures](LeetCode_Problems/Java/medium/0739.%20Daily%20Temperatures.java) | Medium | Scan right to left with a monotonic stack of indices, popping days that are not warmer; the top is the answer. | O(n) | O(n) |
| [844](https://leetcode.com/problems/backspace-string-compare/) | [Backspace String Compare](LeetCode_Problems/Java/easy/0844.%20Backspace%20String%20Compare.java) | Easy | Rebuild each string with a StringBuilder used as a stack, deleting the last char on '#', then compare them. | O(m + n) | O(m + n) |
| [901](https://leetcode.com/problems/online-stock-span/) | [Online Stock Span](LeetCode_Problems/Java/medium/0901.%20Online%20Stock%20Span.java) | Medium | Monotonic stack of (price, span); pop every price at most today's and add its span into today's span. | O(1) amortized | O(n) |
| [3660](https://leetcode.com/problems/jump-game-ix/) | [Jump Game IX](LeetCode_Problems/Java/medium/3660.%20Jump%20Game%20IX.java) | Medium | Monotonic stack of blocks: a smaller value merges with larger earlier blocks; every index gets its block's maximum. | O(n) | O(n) |

### Linked List

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [2](https://leetcode.com/problems/add-two-numbers/) | [Add Two Numbers](LeetCode_Problems/Java/medium/0002.%20Add%20Two%20Numbers.java) | Medium | Walk both lists digit by digit with a carry, appending each sum mod 10 to a dummy-headed result list. | O(max(m, n)) | O(1) |
| [21](https://leetcode.com/problems/merge-two-sorted-lists/) | [Merge Two Sorted Lists](LeetCode_Problems/Java/easy/0021.%20Merge%20Two%20Sorted%20Lists.java) | Easy | Splice the smaller head onto a dummy tail until one list runs out, then attach the remainder. | O(m + n) | O(1) |
| [24](https://leetcode.com/problems/swap-nodes-in-pairs/) | [Swap Nodes in Pairs](LeetCode_Problems/Java/medium/0024.%20Swap%20Nodes%20in%20Pairs.java) | Medium | From a dummy node, rewire each pair A→B into B→A→rest, then step past the pair. | O(n) | O(1) |
| [25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Reverse Nodes in k-Group](LeetCode_Problems/Java/hard/0025.%20Reverse%20Nodes%20in%20k%20Group.java) | Hard | Find each group's k-th node; if it exists, reverse the group in place and splice it after the previous group. | O(n) | O(1) |
| [61](https://leetcode.com/problems/rotate-list/) | [Rotate List](LeetCode_Problems/Java/medium/0061.%20Rotate%20List.java) | Medium | Measure the length, close the list into a ring, then cut it after node number length − (k mod length). | O(n) | O(1) |
| [86](https://leetcode.com/problems/partition-list/) | [Partition List](LeetCode_Problems/Java/medium/0086.%20Partition%20List.java) | Medium | Route nodes into two dummy-headed lists, below x and at least x, then join them and cut the tail. | O(n) | O(1) |
| [92](https://leetcode.com/problems/reverse-linked-list-ii/) | [Reverse Linked List II](LeetCode_Problems/Java/medium/0092.%20Reverse%20Linked%20List%20II.java) | Medium | Walk to the node before left, then repeatedly move the node after the sublist's tail to the sublist's front. | O(n) | O(1) |
| [143](https://leetcode.com/problems/reorder-list/) | [Reorder List](LeetCode_Problems/Java/medium/0143.%20Reorder%20List.java) | Medium | Find the middle with slow and fast pointers, reverse the second half, then interleave the two halves. | O(n) | O(1) |
| [203](https://leetcode.com/problems/remove-linked-list-elements/) | [Remove Linked List Elements](LeetCode_Problems/Java/easy/0203.%20Remove%20Linked%20List%20Elements.java) | Easy | Recursively clean the rest of the list first, then skip the current node if it holds val. | O(n) | O(n) |
| [206](https://leetcode.com/problems/reverse-linked-list/) | [Reverse Linked List](LeetCode_Problems/Java/easy/0206.%20Reverse%20Linked%20List.java) | Easy | Recursively point each node back at its predecessor and return the old tail as the new head. | O(n) | O(n) |
| [237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [Delete Node in a Linked List](LeetCode_Problems/Java/medium/0237.%20Delete%20Node%20in%20a%20Linked%20List.java) | Medium | Copy the next node's value into this node, then unlink the next node. | O(1) | O(1) |

### Trees

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [98](https://leetcode.com/problems/validate-binary-search-tree/) | [Validate Binary Search Tree](LeetCode_Problems/Java/medium/0098.%20Validate%20Binary%20Search%20Tree.java) | Medium | Recurse with an open (min, max) range kept as longs; every node must lie strictly inside its range. | O(n) | O(h) |
| [101](https://leetcode.com/problems/symmetric-tree/) | [Symmetric Tree](LeetCode_Problems/Java/easy/0101.%20Symmetric%20Tree.java) | Easy | Compare the two subtrees as mirrors: equal values, outer children mirror each other, inner children mirror each other. | O(n) | O(h) |
| [102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Binary Tree Level Order Traversal](LeetCode_Problems/Java/medium/0102.%20Binary%20Tree%20Level%20Order%20Traversal.java) | Medium | BFS with a queue, draining exactly the current queue size each round to collect one level. | O(n) | O(n) |
| [103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Binary Tree Zigzag Level Order Traversal](LeetCode_Problems/Java/medium/0103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal.java) | Medium | Level-order BFS that inserts values at the front of the level list on every other level. | O(n^2) | O(n) |
| [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Maximum Depth of Binary Tree](LeetCode_Problems/Java/easy/0104.%20Maximum%20Depth%20of%20Binary%20Tree.java) | Easy | Depth is 1 plus the larger depth of the two subtrees; an empty tree has depth 0. | O(n) | O(h) |
| [105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Construct Binary Tree from Preorder and Inorder Traversal](LeetCode_Problems/Java/medium/0105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal.java) | Medium | Preorder's first value is the root; its inorder index, from a value→index map, splits both ranges into subtrees. | O(n) | O(n) |
| [107](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | [Binary Tree Level Order Traversal II](LeetCode_Problems/Java/medium/0107.%20Binary%20Tree%20Level%20Order%20Traversal%20II.java) | Medium | Level-order BFS that inserts each finished level at the front of the result list. | O(n^2) | O(n) |
| [110](https://leetcode.com/problems/balanced-binary-tree/) | [Balanced Binary Tree](LeetCode_Problems/Java/easy/0110.%20Balanced%20Binary%20Tree.java) | Easy | Post-order DFS returns each subtree's height and flags imbalance when child heights differ by more than 1. | O(n) | O(h) |
| [112](https://leetcode.com/problems/path-sum/) | [Path Sum](LeetCode_Problems/Java/easy/0112.%20Path%20Sum.java) | Easy | Subtract each node's value on the way down; a leaf succeeds when the remaining sum is zero. | O(n) | O(h) |
| [113](https://leetcode.com/problems/path-sum-ii/) | [Path Sum II](LeetCode_Problems/Java/medium/0113.%20Path%20Sum%20II.java) | Medium | DFS keeping the root-to-node path; copy it at leaves matching the remaining sum, then remove the node on return. | O(n·h) | O(h) |
| [199](https://leetcode.com/problems/binary-tree-right-side-view/) | [Binary Tree Right Side View](LeetCode_Problems/Java/medium/0199.%20Binary%20Tree%20Right%20Side%20View.java) | Medium | Level-order BFS that keeps the last node of each level. | O(n) | O(n) |
| [226](https://leetcode.com/problems/invert-binary-tree/) | [Invert Binary Tree](LeetCode_Problems/Java/easy/0226.%20Invert%20Binary%20Tree.java) | Easy | Recursively invert both subtrees, then swap them. | O(n) | O(h) |
| [235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [Lowest Common Ancestor of a Binary Search Tree](LeetCode_Problems/Java/medium/0235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.java) | Medium | Walk down from the root: left if both values are smaller, right if both are larger, otherwise this node splits them. | O(h) | O(1) |
| [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Lowest Common Ancestor of a Binary Tree](LeetCode_Problems/Java/medium/0236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree.java) | Medium | Return the node if it is null, p or q; a node whose left and right searches both succeed is the LCA. | O(n) | O(h) |
| [257](https://leetcode.com/problems/binary-tree-paths/) | [Binary Tree Paths](LeetCode_Problems/Java/easy/0257.%20Binary%20Tree%20Paths.java) | Easy | DFS that appends each value to a path string and records the finished path at every leaf. | O(n·h) | O(h^2) |
| [404](https://leetcode.com/problems/sum-of-left-leaves/) | [Sum of Left Leaves](LeetCode_Problems/Java/medium/0404.%20Sum%20of%20Left%20Leaves.java) | Easy | If a node's left child is a leaf add its value, otherwise recurse into it; always recurse into the right child. | O(n) | O(h) |
| [437](https://leetcode.com/problems/path-sum-iii/) | [Path Sum III](LeetCode_Problems/Java/medium/0437.%20Path%20Sum%20III.java) | Medium | DFS holding the root-to-node path; at each node sum backward along the path and count suffixes equal to targetSum. | O(n·h) | O(h) |
| [450](https://leetcode.com/problems/delete-node-in-a-bst/) | [Delete Node in a BST](LeetCode_Problems/Java/medium/0450.%20Delete%20Node%20in%20a%20BST.java) | Medium | Find key by BST order; with two children, copy in the right subtree's minimum and delete that value from the right. | O(h) | O(h) |
| [563](https://leetcode.com/problems/binary-tree-tilt/) | [Binary Tree Tilt](LeetCode_Problems/Java/easy/0563.%20Binary%20Tree%20Tilt.java) | Easy | Post-order DFS returns each subtree's sum and adds \|left sum − right sum\| to a running total. | O(n) | O(h) |
| [700](https://leetcode.com/problems/search-in-a-binary-search-tree/) | [Search in a Binary Search Tree](LeetCode_Problems/Java/easy/0700.%20Search%20in%20a%20Binary%20Search%20Tree.java) | Easy | Follow BST order from the root, left when val is smaller and right when larger, until it matches or runs out. | O(h) | O(h) |
| [783](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) | [Minimum Distance Between BST Nodes](LeetCode_Problems/Java/easy/0783.%20Minimum%20Distance%20Between%20BST%20Nodes.java) | Easy | In-order traversal visits values in sorted order; track the smallest gap between consecutive values. | O(n) | O(h) |
| [987](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | [Vertical Order Traversal of a Binary Tree](LeetCode_Problems/Java/hard/0987.%20Vertical%20Order%20Traversal%20Binary%20Tree.java) | Hard | BFS records (row, value) per column in a TreeMap, then each column is sorted by row and value. | O(n log n) | O(n) |
| [993](https://leetcode.com/problems/cousins-in-binary-tree/) | [Cousins in Binary Tree](LeetCode_Problems/Java/easy/0993.%20Cousins%20in%20Binary%20Tree.java) | Easy | Level-order BFS: fail if x and y are children of one parent, succeed if both appear on the same level. | O(n) | O(n) |
| [2415](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/) | [Reverse Odd Levels of Binary Tree](LeetCode_Problems/Java/medium/2415.%20Reverse%20Odd%20Levels%20of%20Binary%20Tree.java) | Medium | Level-order BFS collects each level's nodes; on odd levels swap values from both ends inward. | O(n) | O(n) |

### Heap / Priority Queue

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [23](https://leetcode.com/problems/merge-k-sorted-lists/) | [Merge k Sorted Lists](LeetCode_Problems/Java/hard/0023.%20Merge%20KSorted%20Lists.java) | Hard | Seed a min-heap with every list head; pop the smallest node, append it, and push its successor. | O(N log k) | O(k) |
| [295](https://leetcode.com/problems/find-median-from-data-stream/) | [Find Median from Data Stream](LeetCode_Problems/Java/hard/0295.%20Find%20Median%20from%20Data%20Stream.java) | Hard | A max-heap holds the lower half and a min-heap the upper; rebalance so the lower has equal or one more. | O(log n) add, O(1) median | O(n) |
| [347](https://leetcode.com/problems/top-k-frequent-elements/) | [Top K Frequent Elements](LeetCode_Problems/Java/medium/0347.%20Top%20K%20Frequent%20Elements.java) | Medium | Count frequencies, keep a size-k min-heap by count, then pop it into the answer from the back. | O(n log k) | O(n) |
| [451](https://leetcode.com/problems/sort-characters-by-frequency/) | [Sort Characters By Frequency](LeetCode_Problems/Java/medium/0451.%20Sort%20Characters%20By%20Frequency.java) | Medium | Count chars, push them into a max-heap ordered by count, then append each char count times as it pops. | O(n + k log k) | O(n) |
| [480](https://leetcode.com/problems/sliding-window-median/) | [Sliding Window Median](LeetCode_Problems/Java/hard/0480.%20Sliding%20Window%20Median.java) | Hard | Two heaps with lazy deletion: a balance counter tracks live sizes, and outgoing values are discarded once they reach a heap top. | O(n log n) | O(n) |
| [506](https://leetcode.com/problems/relative-ranks/) | [Relative Ranks](LeetCode_Problems/Java/easy/0506.%20Relative%20Ranks.java) | Easy | Pop scores from a max-heap to assign medals and ranks in a score→rank map, then read ranks in input order. | O(n log n) | O(n) |
| [621](https://leetcode.com/problems/task-scheduler/) | [Task Scheduler](LeetCode_Problems/Java/medium/0621.%20Task%20Scheduler.java) | Medium | Simulate each time unit: run the most frequent task from a max-heap, then park it in a cooldown queue for n units. | O(m·n) | O(1) |
| [630](https://leetcode.com/problems/course-schedule-iii/) | [Course Schedule III](LeetCode_Problems/Java/hard/0630.%20Course%20Schedule%20III.java) | Hard | Sort by deadline and take each course; if time passes the deadline, drop the longest course taken, kept in a max-heap. | O(n log n) | O(n) |
| [659](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | [Split Array into Consecutive Subsequences](LeetCode_Problems/Java/medium/0659.%20Split%20Array%20into%20Consecutive%20Subsequences.java) | Medium | Min-heap of (chain end, length): extend the shortest chain ending at num − 1; fail on any closed chain shorter than 3. | O(n log n) | O(n) |
| [692](https://leetcode.com/problems/top-k-frequent-words/) | [Top K Frequent Words](LeetCode_Problems/Java/medium/0692.%20Top%20K%20Frequent%20Words.java) | Medium | Count words, keep a size-k min-heap (lower count first, then later word first), then pop and reverse. | O(n log k) | O(n) |
| [703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Kth Largest Element in a Stream](LeetCode_Problems/Java/easy/0703.%20Kth%20Largest%20Element%20in%20a%20Stream.java) | Easy | Keep only the k largest values in a min-heap; its top is the k-th largest after each add. | O(log k) per add | O(k) |
| [857](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | [Minimum Cost to Hire K Workers](LeetCode_Problems/Java/hard/0857.%20Minimum%20Cost%20to%20Hire%20K%20Workers.java) | Hard | Sort workers by wage/quality; keep the k smallest qualities in a max-heap and price each group at the current ratio. | O(n log n) | O(n) |
| [1046](https://leetcode.com/problems/last-stone-weight/) | [Last Stone Weight](LeetCode_Problems/Java/easy/1046.%20Last%20Stone%20Weight.java) | Easy | Max-heap of stones: smash the two heaviest and push back their difference until at most one remains. | O(n log n) | O(n) |
| [1337](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/) | [The K Weakest Rows in a Matrix](LeetCode_Problems/Java/easy/1337.%20The%20K%20Weakest%20Rows%20in%20a%20Matrix.java) | Easy | Count each row's leading soldiers, then poll a min-heap ordered by (count, index) k times. | O(m·n + m log m) | O(m) |
| [1464](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | [Maximum Product of Two Elements in an Array](LeetCode_Problems/Java/easy/1464.%20Maximum%20Product%20of%20Two%20Elements%20in%20an%20Array.java) | Easy | Push every number into a max-heap, pop the two largest, and multiply each minus one. | O(n log n) | O(n) |
| [1792](https://leetcode.com/problems/maximum-average-pass-ratio/) | [Maximum Average Pass Ratio](LeetCode_Problems/Java/medium/1792.%20Maximum%20Average%20Pass%20Ratio.java) | Medium | A max-heap ordered by the ratio gain of one more passing student; give each extra student to the top class. | O((n + k) log n) | O(n) |
| [2099](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/) | [Find Subsequence of Length K With the Largest Sum](LeetCode_Problems/Java/easy/2099.%20Find%20Subsequence%20of%20Length%20K%20With%20the%20Largest%20Sum.java) | Easy | Keep the k largest (value, index) pairs in a min-heap, then sort them by index to restore the original order. | O(n log k) | O(k) |
| [2335](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/) | [Minimum Amount of Time to Fill Cups](LeetCode_Problems/Java/easy/2335.%20Minimum%20Amount%20of%20Time%20to%20Fill%20Cups.java) | Easy | Each second, fill one cup from each of the two largest remaining amounts in a max-heap; a lone amount adds itself. | O(S) | O(1) |
| [2974](https://leetcode.com/problems/minimum-number-game/) | [Minimum Number Game](LeetCode_Problems/Java/easy/2974.%20Minimum%20Number%20Game.java) | Easy | Each round, pop the two smallest from a min-heap and write them back in swapped order. | O(n log n) | O(n) |

### Graphs

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [721](https://leetcode.com/problems/accounts-merge/) | [Accounts Merge](LeetCode_Problems/Java/medium/0721.%20Accounts%20Merge.java) | Medium | Link each account's emails to its first email in an adjacency map, then DFS each unseen component and sort its emails. | O(N log N) | O(N) |
| [994](https://leetcode.com/problems/rotting-oranges/) | [Rotting Oranges](LeetCode_Problems/Java/medium/0994.%20Rotting%20Oranges.java) | Medium | Multi-source BFS from every rotten orange, one minute per level, until no fresh oranges remain. | O(m·n) | O(m·n) |
| [1306](https://leetcode.com/problems/jump-game-iii/) | [Jump Game III](LeetCode_Problems/Java/medium/1306.%20Jump%20Game%20III.java) | Medium | DFS from start, marking visited indices by negating them; succeed on reaching a zero. | O(n) | O(n) |
| [1345](https://leetcode.com/problems/jump-game-iv/) | [Jump Game IV](LeetCode_Problems/Java/hard/1345.%20Jump%20Game%20IV.java) | Hard | BFS over indices using i ± 1 and same-value portals, deleting each value's portal list after its first use. | O(n) | O(n) |
| [3629](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/) | [Minimum Jumps to Reach End via Prime Teleportation](LeetCode_Problems/Java/medium/3629.%20Minimum%20Jumps%20to%20Reach%20End%20via%20Prime%20Teleportation.java) | Medium | BFS over indices: step ±1, and from a prime value jump once to every index whose value it divides. | O(n·√M) | O(n log M) |

### Backtracking

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [22](https://leetcode.com/problems/generate-parentheses/) | [Generate Parentheses](LeetCode_Problems/Java/medium/0022.%20Generate%20Parentheses.java) | Medium | Build strings char by char, adding '(' while fewer than n are open and ')' while it stays balanced. | O(n·4^n / √n) | O(n^2) |
| [37](https://leetcode.com/problems/sudoku-solver/) | [Sudoku Solver](LeetCode_Problems/Java/hard/0037.%20Sudoku%20Solver.java) | Hard | Fill the first empty cell with each digit valid for its row, column and box; recurse and undo on failure. | O(9^m) | O(m) |
| [46](https://leetcode.com/problems/permutations/) | [Permutations](LeetCode_Problems/Java/medium/0046.%20Permutations.java) | Medium | Extend the current list with each number not already in it, recurse, then remove it. | O(n^2·n!) | O(n) |
| [51](https://leetcode.com/problems/n-queens/) | [N-Queens](LeetCode_Problems/Java/hard/0051.%20NQueens.java) | Hard | Place one queen per row, skipping columns and both diagonals already marked in boolean arrays, then unmark. | O(n·n!) | O(n^2) |
| [77](https://leetcode.com/problems/combinations/) | [Combinations](LeetCode_Problems/Java/medium/0077.%20Combinations.java) | Medium | Choose numbers in increasing order from start to n, recurse with k − 1 left, then undo the choice. | O(k·C(n, k)) | O(k) |
| [698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | [Partition to K Equal Sum Subsets](LeetCode_Problems/Java/medium/0698.%20Partition%20to%20K%20Equal%20Sum%20Subsets.java) | Medium | Sort descending, place each number into a bucket with room, undo on failure, and stop trying after an empty bucket. | O(k^n) | O(n + k) |

### Dynamic Programming

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [84](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Largest Rectangle in Histogram](LeetCode_Problems/Java/hard/0084.%20Largest%20Rectanglein%20Histogram.java) | Hard | For each bar, find the nearest shorter bar on each side by jumping through boundaries already computed; area = height × gap. | O(n) | O(n) |
| [118](https://leetcode.com/problems/pascals-triangle/) | [Pascal's Triangle](LeetCode_Problems/Java/easy/0118.%20Pascal%27s%20Triangle.java) | Easy | Each row starts and ends with 1; every inner entry is the sum of the two entries above it. | O(numRows^2) | O(1) |
| [509](https://leetcode.com/problems/fibonacci-number/) | [Fibonacci Number](LeetCode_Problems/Java/easy/0509.%20Fibonacci%20Number.java) | Easy | Top-down memoized recursion: f[n] = fib(n − 1) + fib(n − 2), cached in an array. | O(n) | O(n) |
| [2770](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) | [Maximum Number of Jumps to Reach the Last Index](LeetCode_Problems/Java/medium/2770.%20Maximum%20Number%20of%20Jumps%20to%20Reach%20the%20Last%20Index.java) | Medium | dp[j] = most jumps to reach j: try every earlier reachable i within target of nums[j] and take dp[i] + 1. | O(n^2) | O(n) |

### Greedy

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [45](https://leetcode.com/problems/jump-game-ii/) | [Jump Game II](LeetCode_Problems/Java/medium/0045.%20Jump%20Game%20II.java) | Medium | Treat reach as BFS levels: track the farthest jump, and when i hits the current level's end, jump and extend it. | O(n) | O(1) |
| [55](https://leetcode.com/problems/jump-game/) | [Jump Game](LeetCode_Problems/Java/medium/0055.%20Jump%20Game.java) | Medium | Track the farthest reachable index; fail if i ever passes it, succeed once it covers the last index. | O(n) | O(1) |
| [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Best Time to Buy and Sell Stock](LeetCode_Problems/Java/easy/0121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.java) | Easy | Track the lowest price so far and the best profit from selling at today's price. | O(n) | O(1) |
| [122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [Best Time to Buy and Sell Stock II](LeetCode_Problems/Java/medium/0122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.java) | Medium | Find each local valley and the peak after it, adding every valley-to-peak rise to the profit. | O(n) | O(1) |
| [134](https://leetcode.com/problems/gas-station/) | [Gas Station](LeetCode_Problems/Java/medium/0134.%20Gas%20Station.java) | Medium | When the running tank goes negative, restart after that station; a non-negative total surplus means that start works. | O(n) | O(1) |
| [455](https://leetcode.com/problems/assign-cookies/) | [Assign Cookies](LeetCode_Problems/Java/easy/0455.%20Assign%20Cookies.java) | Easy | Sort both arrays; hand out cookies in increasing size, each to the least greedy child it can satisfy. | O(n log n + m log m) | O(log n + log m) |
| [860](https://leetcode.com/problems/lemonade-change/) | [Lemonade Change](LeetCode_Problems/Java/easy/0860.%20Lemonade%20Change.java) | Easy | Count fives and tens; for a 20, prefer giving a ten and a five over three fives. | O(n) | O(1) |
| [1403](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) | [Minimum Subsequence in Non-Increasing Order](LeetCode_Problems/Java/easy/1403.%20Minimum%20Subsequence%20in%20Non-Increasing%20Order.java) | Easy | Sort, then take the largest values until their sum exceeds the sum of the rest. | O(n log n) | O(log n) |
| [1488](https://leetcode.com/problems/avoid-flood-in-the-city/) | [Avoid Flood in The City](LeetCode_Problems/Java/medium/1488.%20Avoid%20Flood%20in%20The%20City.java) | Medium | Remember each lake's last rain day; when it rains there again, dry it on the first later dry day from a TreeSet. | O(n log n) | O(n) |
| [1665](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/) | [Minimum Initial Energy to Finish Tasks](LeetCode_Problems/Java/hard/1665.%20Minimum%20Initial%20Energy%20to%20Finish%20Tasks.java) | Hard | Sort by minimum − actual descending, then go backward from the last task keeping max(energy + actual, minimum). | O(n log n) | O(n) |
| [1775](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/) | [Equal Sum Arrays With Minimum Number of Operations](LeetCode_Problems/Java/medium/1775.%20Equal%20Sum%20Arrays%20With%20Minimum%20Number%20of%20Operations.java) | Medium | Collect each element's possible gain toward closing the sum gap in a max-heap and apply the largest gains first. | O((m + n) log(m + n)) | O(m + n) |
| [2833](https://leetcode.com/problems/furthest-point-from-origin/) | [Furthest Point From Origin](LeetCode_Problems/Java/easy/2833.%20Furthest%20Point%20From%20Origin.java) | Easy | Send every '\_' in the dominant direction: the answer is \|R count − L count\| plus the '\_' count. | O(n) | O(n) |

### Intervals

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [56](https://leetcode.com/problems/merge-intervals/) | [Merge Intervals](LeetCode_Problems/Java/medium/0056.%20Merge%20Intervals.java) | Medium | Sort by start; extend the last merged interval while the next overlaps it, otherwise start a new one. | O(n log n) | O(n) |
| [57](https://leetcode.com/problems/insert-interval/) | [Insert Interval](LeetCode_Problems/Java/medium/0057.%20Insert%20Interval.java) | Medium | Copy intervals that end before the new one, absorb every overlapping interval into it, then copy the rest. | O(n) | O(1) |
| [435](https://leetcode.com/problems/non-overlapping-intervals/) | [Non-overlapping Intervals](LeetCode_Problems/Java/medium/0435.%20Non-overlapping%20Intervals.java) | Medium | Sort by end; keep each interval starting at or after the last kept end and count the rest as removals. | O(n log n) | O(n) |
| [495](https://leetcode.com/problems/teemo-attacking/) | [Teemo Attacking](LeetCode_Problems/Java/easy/0495.%20Teemo%20Attacking.java) | Easy | Each attack adds the smaller of the gap to the next attack and duration; the last attack adds a full duration. | O(n) | O(1) |

### Sorting

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [147](https://leetcode.com/problems/insertion-sort-list/) | [Insertion Sort List](LeetCode_Problems/Java/medium/0147.%20Insertion%20Sort%20List.java) | Medium | Insert each node into a sorted list behind a dummy, scanning from the front for its position. | O(n^2) | O(1) |
| [215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Kth Largest Element in an Array](LeetCode_Problems/Java/medium/0215.%20Kth%20Largest%20Element%20in%20an%20Array.java) | Medium | Sort the whole array with randomized quicksort that skips runs equal to the pivot, then read index n − k. | O(n log n) expected | O(log n) expected |
| [242](https://leetcode.com/problems/valid-anagram/) | [Valid Anagram](LeetCode_Problems/Java/easy/0242.%20Valid%20Anagram.java) | Easy | Sort the characters of both strings and compare the arrays. | O(n log n) | O(n) |
| [315](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | [Count of Smaller Numbers After Self](LeetCode_Problems/Java/hard/0315.%20Count%20of%20Smaller%20Numbers%20After%20Self.java) | Hard | Merge sort (value, index) pairs; each right element placed before left ones adds to those left elements' counts. | O(n log n) | O(n) |
| [324](https://leetcode.com/problems/wiggle-sort-ii/) | [Wiggle Sort II](LeetCode_Problems/Java/medium/0324.%20Wiggle%20Sort%20II.java) | Medium | Quickselect the median, then put smaller values on even slots from the back, larger on odd slots from the front, median elsewhere. | O(n) expected | O(n) |
| [414](https://leetcode.com/problems/third-maximum-number/) | [Third Maximum Number](LeetCode_Problems/Java/easy/0414.%20Third%20Maximum%20Number.java) | Easy | Sort, then walk down from the largest counting distinct values; return the third, or the maximum if there are fewer. | O(n log n) | O(log n) |
| [561](https://leetcode.com/problems/array-partition/) | [Array Partition](LeetCode_Problems/Java/easy/0561.%20Array%20Partition.java) | Easy | Sort, then pair neighbours; the answer is the sum of the elements at even indices. | O(n log n) | O(log n) |
| [645](https://leetcode.com/problems/set-mismatch/) | [Set Mismatch](LeetCode_Problems/Java/easy/0645.%20Set%20Mismatch.java) | Easy | Sort, then scan with an expected counter: a repeat of the previous value is the duplicate, a jump reveals the missing one. | O(n log n) | O(log n) |
| [912](https://leetcode.com/problems/sort-an-array/) | [Sort an Array](LeetCode_Problems/Java/medium/0912.%20Sort%20an%20Array.java) | Medium | Randomized quicksort that skips runs equal to the pivot on both sides before recursing. | O(n log n) expected | O(log n) expected |
| [973](https://leetcode.com/problems/k-closest-points-to-origin/) | [K Closest Points to Origin](LeetCode_Problems/Java/medium/0973.%20K%20Closest%20Points%20to%20Origin.java) | Medium | Quickselect (squared distance, index) pairs so the k smallest end up first, then copy those points. | O(n) expected | O(n) |
| [1200](https://leetcode.com/problems/minimum-absolute-difference/) | [Minimum Absolute Difference](LeetCode_Problems/Java/easy/1200.%20Minimum%20Absolute%20Difference.java) | Easy | Sort, then scan adjacent pairs, resetting the answer when a smaller gap appears and appending on ties. | O(n log n) | O(log n) |
| [1365](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | [How Many Numbers Are Smaller Than the Current Number](LeetCode_Problems/Java/easy/1365.%20How%20Many%20Numbers%20Are%20Smaller%20Than%20the%20Current%20Number.java) | Easy | Sort a copy; each value's first index in the sorted copy is how many numbers are smaller than it. | O(n log n) | O(n) |
| [1913](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) | [Maximum Product Difference Between Two Pairs](LeetCode_Problems/Java/easy/1913.%20Maximum%20Product%20Difference%20Between%20Two%20Pairs.java) | Easy | Counting sort the values; the answer is the product of the two largest minus the product of the two smallest. | O(n + V) | O(V) |
| [2164](https://leetcode.com/problems/sort-even-and-odd-indices-independently/) | [Sort Even and Odd Indices Independently](LeetCode_Problems/Java/easy/2164.%20Sort%20Even%20and%20Odd%20Indices%20Independently.java) | Easy | Split the values at even and odd indices, sort evens ascending and odds descending, then write them back. | O(n log n) | O(n) |
| [2500](https://leetcode.com/problems/delete-greatest-value-in-each-row/) | [Delete Greatest Value in Each Row](LeetCode_Problems/Java/easy/2500.%20Delete%20Greatest%20Value%20in%20Each%20Row.java) | Easy | Sort each row, then for each column from the right add the maximum across all rows. | O(m·n log n) | O(log n) |

### Bit Manipulation

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [136](https://leetcode.com/problems/single-number/) | [Single Number](LeetCode_Problems/Java/easy/0136.%20Single%20Number.java) | Easy | XOR all numbers; equal pairs cancel to zero, leaving the single one. | O(n) | O(1) |
| [190](https://leetcode.com/problems/reverse-bits/) | [Reverse Bits](LeetCode_Problems/Java/easy/0190.%20Reverse%20Bits.java) | Easy | For every set bit i of n, set bit 31 − i of the result. | O(1) | O(1) |
| [191](https://leetcode.com/problems/number-of-1-bits/) | [Number of 1 Bits](LeetCode_Problems/Java/easy/0191.%20Number%20of%201%20Bits.java) | Easy | Test bits 0 to 30 with a shifting mask and count the set ones. | O(1) | O(1) |
| [461](https://leetcode.com/problems/hamming-distance/) | [Hamming Distance](LeetCode_Problems/Java/easy/0461.%20Hamming%20Distance.java) | Easy | XOR the two numbers so differing bits become 1, then count them with Integer.bitCount. | O(1) | O(1) |
| [476](https://leetcode.com/problems/number-complement/) | [Number Complement](LeetCode_Problems/Java/easy/0476.%20Number%20Complement.java) | Easy | Build a mask of 1s as wide as num's binary form and XOR num with it. | O(1) | O(1) |
| [693](https://leetcode.com/problems/binary-number-with-alternating-bits/) | [Binary Number with Alternating Bits](LeetCode_Problems/Java/easy/0693.%20Binary%20Number%20with%20Alternating%20Bits.java) | Easy | n XOR (n >> 1) is all 1s exactly when bits alternate; x & (x + 1) being zero confirms all 1s. | O(1) | O(1) |
| [1009](https://leetcode.com/problems/complement-of-base-10-integer/) | [Complement of Base 10 Integer](LeetCode_Problems/Java/easy/1009.%20Complement%20of%20Base%2010%20Integer.java) | Easy | Extract n's bits into a list, flip each one, and rebuild the number with powers of two. | O(log n) | O(log n) |

### Math

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [7](https://leetcode.com/problems/reverse-integer/) | [Reverse Integer](LeetCode_Problems/Java/medium/0007.%20Reverse%20Integer.java) | Medium | Pop the last digit and push it onto a long accumulator, returning 0 as soon as it leaves the int range. | O(log x) | O(1) |
| [9](https://leetcode.com/problems/palindrome-number/) | [Palindrome Number](LeetCode_Problems/Java/easy/0009.%20Palindrome%20Number.java) | Easy | Write the digits in reverse order into a string and compare it with the number's own string. | O(log x) | O(log x) |
| [48](https://leetcode.com/problems/rotate-image/) | [Rotate Image](LeetCode_Problems/Java/medium/0048.%20Rotate%20Image.java) | Medium | Transpose across the main diagonal, then reverse each row; together they rotate the matrix 90° clockwise. | O(n^2) | O(1) |
| [50](https://leetcode.com/problems/powx-n/) | [Pow(x, n)](LeetCode_Problems/Java/medium/0050.%20Pow%28x%2C%20n%29.java) | Medium | Fast exponentiation: square x and halve the exponent, multiplying in one extra x when it is odd; negative n uses 1/x. | O(log n) | O(log n) |
| [67](https://leetcode.com/problems/add-binary/) | [Add Binary](LeetCode_Problems/Java/easy/0067.%20Add%20Binary.java) | Easy | Add digits from the right with a carry, appending sum mod 2, then reverse the built string. | O(max(m, n)) | O(1) |
| [231](https://leetcode.com/problems/power-of-two/) | [Power of Two](LeetCode_Problems/Java/easy/0231.%20Power%20of%20Two.java) | Easy | Halve n while it is even; it is a power of two only if it reaches exactly 1. | O(log n) | O(1) |
| [258](https://leetcode.com/problems/add-digits/) | [Add Digits](LeetCode_Problems/Java/easy/0258.%20Add%20Digits.java) | Easy | Digital root: 0 stays 0, multiples of 9 give 9, everything else gives num mod 9. | O(1) | O(1) |
| [263](https://leetcode.com/problems/ugly-number/) | [Ugly Number](LeetCode_Problems/Java/easy/0263.%20Ugly%20Number.java) | Easy | Divide out every factor of 2, 3 and 5; the number is ugly if 1 remains. | O(log n) | O(1) |
| [268](https://leetcode.com/problems/missing-number/) | [Missing Number](LeetCode_Problems/Java/easy/0268.%20Missing%20Number.java) | Easy | Subtract the array's sum from n(n + 1)/2, the sum of 0 to n. | O(n) | O(1) |
| [292](https://leetcode.com/problems/nim-game/) | [Nim Game](LeetCode_Problems/Java/easy/0292.%20Nim%20Game.java) | Easy | You lose exactly when n is a multiple of 4, because the opponent can always restore that. | O(1) | O(1) |
| [326](https://leetcode.com/problems/power-of-three/) | [Power of Three](LeetCode_Problems/Java/easy/0326.%20Power%20of%20Three.java) | Easy | Divide by 3 while divisible; it is a power of three only if it reaches exactly 1. | O(log n) | O(1) |
| [342](https://leetcode.com/problems/power-of-four/) | [Power of Four](LeetCode_Problems/Java/easy/0342.%20Power%20of%20Four.java) | Easy | Divide by 4 while divisible; it is a power of four only if it reaches exactly 1. | O(log n) | O(1) |
| [389](https://leetcode.com/problems/find-the-difference/) | [Find the Difference](LeetCode_Problems/Java/easy/0389.%20Find%20the%20Difference.java) | Easy | Sum t's char codes and subtract s's; what is left is the added character. | O(n) | O(n) |
| [396](https://leetcode.com/problems/rotate-function/) | [Rotate Function](LeetCode_Problems/Java/medium/0396.%20Rotate%20Function.java) | Medium | Compute F(0) and the total sum, then derive each rotation as F(i) = F(i − 1) + sum − n·nums[n − i]. | O(n) | O(1) |
| [788](https://leetcode.com/problems/rotated-digits/) | [Rotated Digits](LeetCode_Problems/Java/medium/0788.%20Rotated%20Digits.java) | Medium | Check each number up to n digit by digit: no 3, 4 or 7, plus some 2, 5, 6 or 9. | O(n log n) | O(1) |
| [1185](https://leetcode.com/problems/day-of-the-week/) | [Day of the Week](LeetCode_Problems/Java/easy/1185.%20Day%20of%20the%20Week.java) | Easy | Count days elapsed since Friday 1971-01-01, including leap days, and pick the weekday by total mod 7. | O(year − 1971) | O(1) |
| [1217](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) | [Minimum Cost to Move Chips to The Same Position](LeetCode_Problems/Java/easy/1217.%20Minimum%20Cost%20to%20Move%20Chips%20to%20The%20Same%20Position.java) | Easy | Moving by 2 is free, so chips gather by parity; the cost is the smaller of the even and odd counts. | O(n) | O(1) |
| [1304](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) | [Find N Unique Integers Sum up to Zero](LeetCode_Problems/Java/easy/1304.%20Find%20N%20Unique%20Integers%20Sum%20up%20to%20Zero.java) | Easy | Write the pairs −i and i for i from 1 to n/2, plus a 0 when n is odd. | O(n) | O(1) |
| [1523](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) | [Count Odd Numbers in an Interval Range](LeetCode_Problems/Java/easy/1523.%20Count%20Odd%20Numbers%20in%20an%20Interval%20Range.java) | Easy | (high − low) / 2 odd numbers fit in the gap; add one more if either end is odd. | O(1) | O(1) |
| [1716](https://leetcode.com/problems/calculate-money-in-leetcode-bank/) | [Calculate Money in Leetcode Bank](LeetCode_Problems/Java/easy/1716.%20Calculate%20Money%20in%20Leetcode%20Bank.java) | Easy | Full weeks form an arithmetic series: recurse on the earlier weeks and add the partial week with a closed formula. | O(n) | O(n) |
| [1952](https://leetcode.com/problems/three-divisors/) | [Three Divisors](LeetCode_Problems/Java/easy/1952.%20Three%20Divisors.java) | Easy | Count the divisors of n below n; n has exactly three divisors when that count is two. | O(n) | O(1) |
| [1979](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) | [Find Greatest Common Divisor of Array](LeetCode_Problems/Java/easy/1979.%20Find%20Greatest%20Common%20Divisor%20of%20Array.java) | Easy | Find the minimum and maximum, then run Euclid's algorithm on the pair. | O(n) | O(1) |
| [2180](https://leetcode.com/problems/count-integers-with-even-digit-sum/) | [Count Integers With Even Digit Sum](LeetCode_Problems/Java/easy/2180.%20Count%20Integers%20With%20Even%20Digit%20Sum.java) | Easy | Brute force: sum the digits of every number up to num and count the even sums. | O(num log num) | O(1) |
| [2553](https://leetcode.com/problems/separate-the-digits-in-an-array/) | [Separate the Digits in an Array](LeetCode_Problems/Java/easy/2553.%20Separate%20the%20Digits%20in%20an%20Array.java) | Easy | Peel each number's digits with mod 10, inserting at the front to keep their order, and flatten them into one array. | O(D) | O(D) |
| [3658](https://leetcode.com/problems/gcd-of-odd-and-even-sums/) | [GCD of Odd and Even Sums](LeetCode_Problems/Java/easy/3658.%20GCD%20of%20Odd%20and%20Even%20Sums.java) | Easy | The odd sum is n² and the even sum is n(n + 1), so their GCD is always n. | O(1) | O(1) |
| [3918](https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/) | [Sum of Primes Between Number and Its Reverse](LeetCode_Problems/Java/medium/3918.%20Sum%20of%20Primes%20Between%20Number%20and%20Its%20Reverse.java) | Medium | Reverse n's digits, then sum every prime between the two numbers using 6k ± 1 trial division. | O(R·√R) | O(1) |
| [3932](https://leetcode.com/problems/count-k-th-roots-in-a-range/) | [Count K-th Roots in a Range](LeetCode_Problems/Java/easy/3932.%20Count%20K-th%20Roots%20in%20a%20Range.java) | Medium | Count powers i^k, for i from 0 upward, that land in [l, r], stopping once past r; k = 1 is special-cased. | O(r^(1/k)) | O(1) |
| [3959](https://leetcode.com/problems/check-good-integer/) | [Check Good Integer](LeetCode_Problems/Java/easy/3959.%20Check%20Good%20Integer.java) | Easy | Sum the digits and the squared digits in two passes; n is good when the difference is at least 50. | O(log n) | O(1) |

### Strings

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [13](https://leetcode.com/problems/roman-to-integer/) | [Roman to Integer](LeetCode_Problems/Java/easy/0013.%20Roman%20to%20Integer.java) | Easy | Add each symbol's value, but subtract it when the next symbol is larger. | O(n) | O(1) |
| [14](https://leetcode.com/problems/longest-common-prefix/) | [Longest Common Prefix](LeetCode_Problems/Java/easy/0014.%20Longest%20Common%20Prefix.java) | Easy | Take the first word as the prefix and trim its last char until every other word starts with it. | O((n + m)·m^2) | O(m) |
| [434](https://leetcode.com/problems/number-of-segments-in-a-string/) | [Number of Segments in a String](LeetCode_Problems/Java/easy/0434.%20Number%20of%20Segments%20in%20a%20String.java) | Easy | Count positions holding a non-space char whose previous char is a space or the string start. | O(n) | O(1) |
| [696](https://leetcode.com/problems/count-binary-substrings/) | [Count Binary Substrings](LeetCode_Problems/Java/easy/0696.%20Count%20Binary%20Substrings.java) | Easy | Track the lengths of the previous and current runs of equal chars; each run boundary adds min(previous, current). | O(n) | O(1) |
| [796](https://leetcode.com/problems/rotate-string/) | [Rotate String](LeetCode_Problems/Java/easy/0796.%20Rotate%20String.java) | Easy | goal is a rotation of s exactly when the lengths match and goal appears inside s + s. | O(n^2) | O(n) |
| [1507](https://leetcode.com/problems/reformat-date/) | [Reformat Date](LeetCode_Problems/Java/easy/1507.%20Reformat%20Date.java) | Easy | Split into day, month and year; map the month name to its number, strip the day's suffix, zero-pad both. | O(1) | O(1) |
| [1592](https://leetcode.com/problems/rearrange-spaces-between-words/) | [Rearrange Spaces Between Words](LeetCode_Problems/Java/easy/1592.%20Rearrange%20Spaces%20Between%20Words.java) | Easy | Split into words and count spaces; put total / (words − 1) spaces between words and the remainder at the end. | O(n) | O(n) |
| [1903](https://leetcode.com/problems/largest-odd-number-in-string/) | [Largest Odd Number in String](LeetCode_Problems/Java/easy/1903.%20Largest%20Odd%20Number%20in%20String.java) | Easy | Return the prefix that ends at the rightmost odd digit, or an empty string if there is none. | O(n) | O(1) |
| [1967](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/) | [Number of Strings That Appear as Substrings in Word](LeetCode_Problems/Java/easy/1967.%20Number%20of%20Strings%20That%20Appear%20as%20Substrings%20in%20Word.java) | Easy | Count the patterns that word.contains finds. | O(n·P) | O(1) |
| [2000](https://leetcode.com/problems/reverse-prefix-of-word/) | [Reverse Prefix of Word](LeetCode_Problems/Java/easy/2000.%20Reverse%20Prefix%20of%20Word.java) | Easy | Find the first ch, reverse the prefix up to and including it, and append the rest. | O(n) | O(n) |
| [3258](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/) | [Count Substrings That Satisfy K-Constraint I](LeetCode_Problems/Java/easy/3258.%20Count%20Substrings%20That%20Satisfy%20KConstraint%20I.java) | Easy | Brute force every substring, counting zeros and ones as it grows, and keep those with either count at most k. | O(n^2) | O(1) |
| [3582](https://leetcode.com/problems/generate-tag-for-video-caption/) | [Generate Tag for Video Caption](LeetCode_Problems/Java/easy/3582.%20Generate%20Tag%20for%20Video%20Caption.java) | Easy | Split into words, lowercase the first, capitalize the rest, prefix '#', and cut the result to 100 chars. | O(n) | O(n) |
| [3926](https://leetcode.com/problems/count-valid-word-occurrences/) | [Count Valid Word Occurrences](LeetCode_Problems/Java/medium/3926.%20Count%20Valid%20Word%20Occurrences.java) | Medium | Join the chunks, split on whitespace, trim edge hyphens, split on double hyphens, and count words in a map. | O(L + q) | O(L) |
| [3931](https://leetcode.com/problems/check-adjacent-digit-differences/) | [Check Adjacent Digit Differences](LeetCode_Problems/Java/easy/3931.%20Check%20Adjacent%20Digit%20Differences.java) | Easy | Check each adjacent digit pair and fail as soon as two neighbours differ by more than 2. | O(n) | O(1) |

### Simulation

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [54](https://leetcode.com/problems/spiral-matrix/) | [Spiral Matrix](LeetCode_Problems/Java/medium/0054.%20Spiral%20Matrix.java) | Medium | Walk the top, right, bottom and left edges, shrinking each bound after its edge and stopping when bounds cross. | O(m·n) | O(1) |
| [806](https://leetcode.com/problems/number-of-lines-to-write-string/) | [Number of Lines To Write String](LeetCode_Problems/Java/easy/0806.%20Number%20of%20Lines%20To%20Write%20String.java) | Easy | Add each letter's width to the current line, starting a new line whenever it would pass 100 pixels. | O(n) | O(1) |
| [1389](https://leetcode.com/problems/create-target-array-in-the-given-order/) | [Create Target Array in the Given Order](LeetCode_Problems/Java/easy/1389.%20Create%20Target%20Array%20in%20the%20Given%20Order.java) | Easy | Insert each nums[i] at position index[i] of an ArrayList, then copy the list into an array. | O(n^2) | O(n) |
| [1861](https://leetcode.com/problems/rotating-the-box/) | [Rotating the Box](LeetCode_Problems/Java/medium/1861.%20Rotating%20the%20Box.java) | Medium | In each row let stones fall right toward the nearest obstacle, then write the rows into a rotated cols × rows grid. | O(m·n) | O(1) |
| [1914](https://leetcode.com/problems/cyclically-rotating-a-grid/) | [Cyclically Rotating a Grid](LeetCode_Problems/Java/medium/1914.%20Cyclically%20Rotating%20a%20Grid.java) | Medium | Peel each layer into a list, rotate the list by k mod its length, and write it back in the same order. | O(m·n) | O(m + n) |
| [2810](https://leetcode.com/problems/faulty-keyboard/) | [Faulty Keyboard](LeetCode_Problems/Java/easy/2810.%20Faulty%20Keyboard.java) | Easy | Append chars to a StringBuilder and reverse the whole builder on every 'i'. | O(n^2) | O(n) |
| [3248](https://leetcode.com/problems/snake-in-matrix/) | [Snake in Matrix](LeetCode_Problems/Java/easy/3248.%20Snake%20in%20Matrix.java) | Easy | Track the cell number directly: UP and DOWN move it by n, LEFT and RIGHT by 1. | O(m) | O(1) |

### Design

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [155](https://leetcode.com/problems/min-stack/) | [Min Stack](LeetCode_Problems/Java/medium/0155.%20Min%20Stack.java) | Medium | A hand-rolled linked stack whose every node stores its value and the minimum of everything beneath it. | O(1) per operation | O(n) |
| [225](https://leetcode.com/problems/implement-stack-using-queues/) | [Implement Stack using Queues](LeetCode_Problems/Java/easy/0225.%20Implement%20Stack%20using%20Queues.java) | Easy | Wraps java.util.Stack directly, delegating push, pop, top and empty to it instead of using queues. | O(1) per operation | O(n) |
| [232](https://leetcode.com/problems/implement-queue-using-stacks/) | [Implement Queue using Stacks](LeetCode_Problems/Java/easy/0232.%20Implement%20Queue%20using%20Stacks.java) | Easy | Push onto an in-stack; when the out-stack is empty, pour the in-stack into it so the oldest item is on top. | O(1) amortized | O(n) |
| [641](https://leetcode.com/problems/design-circular-deque/) | [Design Circular Deque](LeetCode_Problems/Java/medium/0641.%20Design%20Circular%20Deque.java) | Medium | Wraps an ArrayDeque and enforces capacity k by checking its size before each insert. | O(1) per operation | O(k) |
| [933](https://leetcode.com/problems/number-of-recent-calls/) | [Number of Recent Calls](LeetCode_Problems/Java/easy/0933.%20Number%20of%20Recent%20Calls.java) | Easy | Keep ping times in a queue and drop those older than t − 3000; the queue size is the answer. | O(1) amortized | O(n) |
| [1472](https://leetcode.com/problems/design-browser-history/) | [Design Browser History](LeetCode_Problems/Java/medium/1472.%20Design%20Browser%20History.java) | Medium | Doubly linked list of pages: visit cuts off the forward chain, and back or forward walk up to steps nodes. | O(steps) per move | O(n) |

### Union-Find

| # | Problem | Difficulty | Key idea | Time | Space |
|---|---|---|---|---|---|
| [990](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [Satisfiability of Equality Equations](LeetCode_Problems/Java/medium/0990.%20Satisfiability%20of%20Equality%20Equations.java) | Medium | Union the variables of every == equation; then any != equation whose variables share a root fails. | O(n) | O(1) |
| [1202](https://leetcode.com/problems/smallest-string-with-swaps/) | [Smallest String With Swaps](LeetCode_Problems/Java/medium/1202.%20Smallest%20String%20With%20Swaps.java) | Medium | Union swappable indices, give each component a min-heap of its chars, then rebuild by polling each index's component. | O((n + m) log n) | O(n) |
| [2316](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) | [Count Unreachable Pairs of Nodes in an Undirected Graph](LeetCode_Problems/Java/medium/2316.%20Count%20Unreachable%20Pairs%20of%20Nodes%20in%20an%20Undirected%20Graph.java) | Medium | Union by size over the edges; each component of size s pairs with every node not counted yet, adding s × remaining. | O(n + E) | O(n) |

## Codeforces

| # | Problem | Rating | Technique | Key idea | Time | Space |
|---|---|---|---|---|---|---|
| [1A](https://codeforces.com/problemset/problem/1/A) | [Theatre Square](Codeforces_Problems/ProblemSet/1A.cpp) | 1000 | Math | Cover each side with ceil(side / a) flagstones and multiply the two counts. | O(1) | O(1) |
| [4A](https://codeforces.com/problemset/problem/4/A) | [Watermelon](Codeforces_Problems/ProblemSet/4A.cpp) | 800 | Math | The melon splits into two positive even parts exactly when w is even and greater than 2. | O(1) | O(1) |
| [4C](https://codeforces.com/problemset/problem/4/C) | [Registration System](Codeforces_Problems/ProblemSet/4C.cpp) | 1300 | Arrays & Hashing | A hash map of name → times seen; print OK on first sight, otherwise the name plus its current count. | O(n·L) | O(n·L) |
| [25A](https://codeforces.com/problemset/problem/25/A) | [IQ test](Codeforces_Problems/ProblemSet/25A.cpp) | 1300 | Arrays & Hashing | Count odds and evens, remembering the last index of each; the parity seen only once marks the answer. | O(n) | O(n) |
| [58A](https://codeforces.com/problemset/problem/58/A) | [Chat room](Codeforces_Problems/ProblemSet/58A.cpp) | 1000 | Two Pointers | Scan the word, advancing through the letters of "hello" on each match; succeed once all five match. | O(n) | O(1) |
| [69A](https://codeforces.com/problemset/problem/69/A) | [Young Physicist](Codeforces_Problems/ProblemSet/69A.cpp) | 1000 | Math | Sum the force vectors coordinate by coordinate; the body is in equilibrium when all three sums are 0. | O(n) | O(1) |
| [71A](https://codeforces.com/problemset/problem/71/A) | [Way Too Long Words](Codeforces_Problems/ProblemSet/71A.cpp) | 800 | Strings | A word longer than 10 becomes its first letter, the number of letters between, and its last letter. | O(L) | O(L) |
| [118A](https://codeforces.com/problemset/problem/118/A) | [String Task](Codeforces_Problems/ProblemSet/118A.cpp) | 1000 | Strings | Lowercase each letter, drop vowels (y included), and put '.' before every consonant. | O(n) | O(n) |
| [122A](https://codeforces.com/problemset/problem/122/A) | [Lucky Division](Codeforces_Problems/ProblemSet/122A.cpp) | 1000 | Math | Hard-code the 14 lucky numbers up to 1000 and check whether any of them divides n. | O(1) | O(1) |
| [189A](https://codeforces.com/problemset/problem/189/A) | [Cut Ribbon](Codeforces_Problems/ProblemSet/189A.cpp) | 1300 | Dynamic Programming | dp[i] = most pieces summing to i; from each reachable length, push dp[i] + 1 to i + a, b and c. | O(n) | O(n) |
| [230B](https://codeforces.com/problemset/problem/230/B) | [T-primes](Codeforces_Problems/ProblemSet/230B.cpp) | 1300 | Math | A T-prime is the square of a prime: sieve primes up to 10^6 and test whether √x is a prime integer. | O(M log log M + n) | O(M) |
| [231A](https://codeforces.com/problemset/problem/231/A) | [Team](Codeforces_Problems/ProblemSet/231A.cpp) | 800 | Simulation | Count the problems where at least two of the three friends are sure of the solution. | O(n) | O(1) |
| [279B](https://codeforces.com/problemset/problem/279/B) | [Books](Codeforces_Problems/ProblemSet/279B.cpp) | 1400 | Sliding Window | Grow a window of consecutive books and shrink it from the left while its total time exceeds t; keep the longest. | O(n) | O(n) |
| [282A](https://codeforces.com/problemset/problem/282/A) | [Bit++](Codeforces_Problems/ProblemSet/282A.cpp) | 800 | Simulation | The middle character of each statement tells ++ from --; apply it to x. | O(n) | O(1) |
| [455A](https://codeforces.com/problemset/problem/455/A) | [Boredom](Codeforces_Problems/ProblemSet/455A.cpp) | 1500 | Dynamic Programming | Bucket points by value; dp[i] = max(dp[i − 1], dp[i − 2] + i × count[i]), like house robber. | O(n + M) | O(M) |
| [479A](https://codeforces.com/problemset/problem/479/A) | [Expression](Codeforces_Problems/ProblemSet/479A.cpp) | 1000 | Math | Evaluate the candidate ways to place + and × with brackets between a, b and c, and print the largest. | O(1) | O(1) |

<!-- index:end -->

## Practise with an AI coach

[`skills/leetcode-coach`](skills/leetcode-coach/SKILL.md) is an agent skill for Claude Code, Codex and other agents that read `SKILL.md` files. Tell it which problem you are on and it coaches instead of solving:

- **A hint ladder:** understand the limits and the brute force, name the pattern, the key insight, a pseudocode skeleton, and the full solution only when you ask for it. One rung per reply.
- **A review of your attempt:** traces your code on the edge cases that matter for the problem, finds the first failing input, and states the time and space of *your* code.
- **What to solve next:** an easier problem with the same pattern as a worked example, and two follow-ups, picked from [`data/problems.json`](data/problems.json).

**Claude Code**

```text
/plugin marketplace add elchibek5/leetcode-patterns-java
/plugin install leetcode-coach@elchibek5-leetcode
```

Then ask, for example: `/leetcode-coach:leetcode-coach I'm stuck on 424, I tried brute force`.

**Codex and other agents**

```sh
git clone https://github.com/elchibek5/leetcode-patterns-java
mkdir -p ~/.agents/skills && cp -r leetcode-patterns-java/skills/leetcode-coach ~/.agents/skills/
```

The skill reads the index from this repo when it is installed as a plugin, and from GitHub otherwise.

## How solutions are checked

On every push and pull request, CI compiles each Java solution against Java 21 with the imports LeetCode adds and stand-ins for LeetCode's helper classes (`ListNode`, `TreeNode`, and so on), and syntax-checks each C++ solution with g++. On pull requests and branches it also verifies that `data/problems.json`, this README and the stats card match the files in the repo. On `main`, a second workflow regenerates the index after every change to solutions, data or scripts and commits the update.

## Add a solution

1. Name the file `NNNN. Title.java`, for example `0070. Climbing Stairs.java`, and put it in `LeetCode_Problems/Java/easy`, `medium` or `hard`. Codeforces solutions go in `Codeforces_Problems/ProblemSet/` named by problem code, for example `4A.cpp`.
2. Push to `main`. The index updates itself: the new problem appears under **Unsorted** with its official title, difficulty and link. For a pull request, run `python3 scripts/build_index.py --write` yourself first, because the pull request check expects the index to be up to date.
3. Fill in `pattern`, `key_idea`, `time` and `space` for the new entry in [`data/problems.json`](data/problems.json), run `python3 scripts/build_index.py --write`, and push again.

To run the same checks as CI before pushing:

```sh
python3 -m unittest discover -s scripts
python3 scripts/build_index.py --check
python3 scripts/compile_check.py
```

## License

[MIT](LICENSE)
