class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        c2o = {")":"(","}":"{", "]":"["}
        
        for i in s:
            # print(s)
            if i in c2o:
                if st and st[-1]== c2o[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return len(st)==0