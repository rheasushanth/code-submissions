class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
                "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]

        def three(n):             
            words = []
            if n >= 100:
                words += [ones[n // 100], "Hundred"]
                n %= 100           
            if n >= 20:
                words.append(tens[n // 10])
                n %= 10            
            if n > 0:
                words.append(ones[n])   
            return words

        scales = ["", "Thousand", "Million", "Billion"]
        words = []
        i = 0
        while num > 0:
            chunk = num % 1000     
            if chunk:             
                part = three(chunk)
                if scales[i]:
                    part.append(scales[i])
                words = part + words   
            num //= 1000           
            i += 1

        return " ".join(words)