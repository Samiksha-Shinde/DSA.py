class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        from collections import deque

        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            # Once valid strings are found at this level,
            # don't remove more parentheses.
            if found:
                continue

            for i in range(len(current)):
                if current[i] not in '()':
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result