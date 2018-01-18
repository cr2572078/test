class TEST:
    def __init__(self,s,n):
        self.s = s
        self.n = n
    # 去重
    def get_count_diff(self,s):
        return len(set(s))

    # 取到最长的字符串
    def get_longest_str(self):
        longest_str = ''
        length = len(self.s)
        if length <= self.n:
            return self.s
        for i in range(length-n):
            for j in range(i+4,length):
                temp_str = self.s[i:j+1]
                count = self.get_count_diff(temp_str)
                if count <= 4 and len(temp_str) > len(longest_str):
                    longest_str = temp_str
        return longest_str



s = "asdfsaaassssaaassssddddffffwwwwddddffffffff"
n = 4
string = TEST(s,n)
print(string.get_longest_str())
