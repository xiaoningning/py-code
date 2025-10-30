MAPPING = {
    "2": "abc", "3": "def",
    "4": "ghi", "5": "jkl", "6": "mno",
    "7": "pqrs", "8": "tuv", "9": "wxyz",
}

def letter_combinations_dfs(digits: str) -> list:
    if not digits:
        return []
    
    res = []
    path = []

    def dfs(i: int) -> None:
        if i == len(digits):
            res.append("".join(path))
            return
        for c in MAPPING.get(digits[i], ""):
            path.append(c)
            dfs(i+1)
            path.pop()
    
    dfs(0)
    return res

def letter_combinations_bfs(digits: str) -> list:
    if not digits:
        return []
    
    level = [""]
    for d in digits:
        next_level = []
        for prefix in level:
            for c in MAPPING.get(d, ""):
                next_level.append(prefix + c)
        level = next_level
    return level

def main() -> None:
    digits = "23"
    print(f"dfs: {letter_combinations_dfs(digits)}")
    print(f"dfs: {letter_combinations_bfs(digits)}")
    
if __name__ == "__main__":
    main()
