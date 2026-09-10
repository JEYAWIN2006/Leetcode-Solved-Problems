class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurences = {c: i for i, c in enumerate(s)}
        remaining_letters = set(s)
        solution_stack = []

        for i, c in enumerate(s):
            if c not in remaining_letters:
                continue

            while (
                solution_stack
                and c < solution_stack[-1]
                and last_occurences[solution_stack[-1]] > i
            ):
                remaining_letters.add(solution_stack.pop())

            solution_stack.append(c)
            remaining_letters.remove(c)

        return "".join(solution_stack)
        