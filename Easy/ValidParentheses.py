class Solution:
    def isValid(self, s: str) -> bool:
        # one thing to think about: we need to put every open bracket we 
        # encounter an open bracket and put it in the stack
        # if next is a closed bracket is it the same as the top of the stack
        # pop if found
        st = []
        if len(s) == 1:
            return False
        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            
            if (c == ')' or c == '}' or c == ']') and len(st) > 0:
                x = st.pop()
                if x == '(' and c != ')':
                    return False
                if x == '{' and c != '}':
                    return False
                if x == '[' and c != ']':
                    return False
            elif (c == ')' or c == '}' or c == ']') and len(st) == 0:
                return False
        
        return len(st) == 0

                