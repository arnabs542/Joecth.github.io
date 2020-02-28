---

layout: post
categories: Daily
tag: []
date: 2020-02-28

---



### Anagram in a string

```python
def find_anagrams(s, t):
  # Fill this in.

print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
```

```python
from collections import Counter
class Solution:
    def findAnagrams_Counter(self, s: str, p: str) -> List[int]:    # Took 7300 ms
        window = len(p)
        c_p = Counter(p)
        
        res = []
        for i in range(window-1, len(s)):   # 2
            pat = s[i-window+1:i+1]
            # print(pat)
            c_pat = Counter(pat)  
            
            if c_p == c_pat:
                res.append(i-window+1) 
        return res
            

    def findAnagrams(self, s: str, p: str) -> List[int]:    # 100 ms
        if not s or not p:
            return []
        
        enc_p = self.encoder(p)
        win = len(p)
        # enc_s = self.encoder(s[:win])
        
        offset = win-1
        res = []
        '''Dynamically update pattern in s'''
        # for i in range(offset, len(s)):
        enc_c = [0] * 26
        j = 0
        for i in range(len(s)):
            enc_c[ord(s[i]) - ord('a')] += 1
            if i - j >= win:
                enc_c[ord(s[j]) - ord('a')] -= 1
                j += 1
            if enc_c == enc_p:
                res.append(j)
        return res
        
    def findAnagrams_TLE(self, s: str, p: str) -> List[int]:    # TLE
        ''' TLE, SHOULD Dynamically  Update enc_tmp'''
        if not s or not p:
            return []
        
        enc_p = self.encoder(p)
        win = len(p)
        
        offset = win-1
        res = []
        for i in range(offset, len(s)):
            start = i - win + 1
            sub_s = s[start:i+1]
            # print(sub_s)
            enc_tmp = self.encoder(sub_s)  # 2 - (3-1) : 3  # No OOR
            
            if enc_tmp == enc_p:
                res.append(start)
        return res
```



### ~~Reverse Words~~

```python
def reverse_words(words):
  # Fill this in.

s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can
```

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        l = s.split()[::-1]
        res = ' '.join(l)
        
        return res
```

### ~~Reverse Words Ⅱ~~

Given an input string , reverse the string word by word. 

**Example:**

```
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
```

```python
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t = ' '.join(''.join(s).split()[::-1])
        
        for i in range(len(s)):
            s[i] = t[i]
```

### ~~Reverse Words Ⅲ~~

**Example 1:**

```
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        t  = s.split()
        res = []
        for w in t:
            w = w[::-1]
            res.append(w)
        
        return ' '.join(res)
```

