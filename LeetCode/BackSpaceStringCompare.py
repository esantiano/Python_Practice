class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sc = len(s)-1
        s_skip = 0
        tc = len(t)-1
        t_skip = 0

        while sc >= 0 or tc >= 0:
            while sc >= 0:
                if s_skip == 0 and s[sc] != '#':
                    break
                elif s[sc] == '#':
                    s_skip +=1
                else:
                    s_skip -=1
                sc-=1

            while tc >= 0:
                if t_skip == 0 and t[tc] != '#':
                    break
                elif t[tc] == '#':
                    t_skip +=1
                else:
                    t_skip -=1
                tc-=1
            
            char_s = s[sc] if sc >= 0 else ''
            char_t = t[tc] if tc >= 0 else ''

            if char_s != char_t:
                return False
            sc -=1
            tc -=1
        return True