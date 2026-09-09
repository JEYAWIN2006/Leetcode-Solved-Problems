INCLUSIVE_RNG_OFFSET = 1
COMMA_CNT_MULT = 1000
MIN_NUM_WITH_COMMAS = 1000
class Solution:
    def countCommas(self, num: int) -> int:
        comma_cnt = 0
        curr_num = MIN_NUM_WITH_COMMAS
        while curr_num <= num:
            comma_cnt += num - curr_num + INCLUSIVE_RNG_OFFSET
            curr_num *= COMMA_CNT_MULT

        return comma_cnt