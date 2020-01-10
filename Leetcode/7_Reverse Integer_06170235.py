class Solution:
    def reverse(self, x: int):
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x <= -2**31 or x > 2**31:
                return 0
            else:
                return x
        else:
            y = x - 2 * x
            y = str(y)
            y = y[::-1]
            y = int(y)
            if y <= -2**31 or y > 2**31:
                return 0
            else:
                return -y
            
#利用我在寫CodeSignal裡的題目checkPalindrome學到的使字串反轉，變數[::-1]。
#寫的過程發現整數不能反轉，所以要先將x轉成字串型態。
#後來又發現如果直接return字串型態的x，會發生例如120變012的問題（應該要是12），所以要再將x轉成整數型態。
#要注意如果反轉超過題目規定的範圍-2^31到2^31，就要return 0。
