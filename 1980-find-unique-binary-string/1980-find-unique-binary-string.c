char* findDifferentBinaryString(char** nums, int numsSize) {
    int n = numsSize;
    static char s[20];
    for(int i = 0; i < n; i++) {
        if(nums[i][i] == '0') {
            s[i] = '1';
        }
        else {
            s[i] = '0';
        }

    }
    s[n] = '\0';
    return s;
}

