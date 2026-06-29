class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []  # Stores final groups
        visited = [False] * len(strs)  # Tracks grouped words

        for i in range(len(strs)):
            if visited[i]:
                continue  # Skip if already grouped

            group = [strs[i]]  # Start a new group
            visited[i] = True  # Mark current word as grouped

            for j in range(i + 1, len(strs)):
                # Compare only words of same length
                if len(strs[i]) == len(strs[j]):

                    # Check if they are anagrams
                    if sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])  # Add to group
                        visited[j] = True  # Mark as grouped

            result.append(group)  # Save current group

        return result

