import unittest
import re


def sumstring(*strs):
    
    sum  = 0
    for s in strs:
        throw_negativenumex = False
        neg_numlist = []

        seplist = [",",r"\n"]
        if s == "": 
            continue
        if s[0:2] == "//":
            k = s.split("\n",1)
            s = k[1]
            if len(k[0][2:]) == 1:
                seplist += k[0][2:]
            else: 
                nsep = list(re.findall(r"\[([^\[\]]+)\]", k[0][2:]))
                for val in nsep:
                    if val != None:
                        val = re.escape(val)
                        seplist.append(val)
            
        matchlist = "|".join(seplist)
        for v in re.split(matchlist,s):
            num  = int(v,10)
            if num > 1000:
                continue
            if num < 0:
                throw_negativenumex = True
                neg_numlist.append(num)
                continue
            sum += num
    if throw_negativenumex:
        raise Exception("Liczby ujemne nie dozwolone",neg_numlist)
    return sum
class TestSumstring(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(sumstring(""),0,"")
    def test_one_argumetns(self):
        self.assertEqual(sumstring(""),0)
        self.assertEqual(sumstring("1"),1)
        self.assertEqual(sumstring("1,2"),3)

    def test_two_arguments(self):
        self.assertEqual(sumstring("",""),0)
        self.assertEqual(sumstring("1"),1)
        self.assertEqual(sumstring("1","2"),3)
        self.assertEqual(sumstring("1,2","2,4"),9)
        #2
    def test_any_argument_list(self):
        self.assertEqual(sumstring("1,2,3,4,5,6"),21)
        self.assertEqual(sumstring("1,2,3,4,6"),16)
        #3
    def test_delimiters(self):
        s = "1,2,3,4"
        s2 = "1\n2\n3\n4"
        s3 = "1\n2,3"
        self.assertEqual(sumstring(s),sumstring(s2))
        self.assertEqual(sumstring(s3),6)
        #4
    def test_seperator_list(self):
        s = "//;\n1;2;3;4"
        self.assertEqual(sumstring(s),10)
    def test_negative_num(self):
        s = "-1,-2,-3"
        with self.assertRaises(Exception):
            sumstring(s)
        
    def test_more_than_1k(self):
        s = "2000,2"
        self.assertEqual(sumstring(s),2)
    def test_multi_char_sep(self):
        s ="//[***]\n1***2"
        self.assertEqual(sumstring(s),3)
    def test_multiple(self):
        s ="//[***][;][/]\n1***2;3"
        self.assertEqual(sumstring(s),6)
    def test_multiple_multichar_sep(self):
        s ="//[***][;;;][/]\n1***2;;;3"
        self.assertEqual(sumstring(s),6)
unittest.main()
