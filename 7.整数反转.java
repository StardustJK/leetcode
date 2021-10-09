/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 */

// @lc code=start
class Solution {
    public int reverse(int x) {
        String str2=x+"";
        char[] str=str2.toCharArray();
        int i=0,len=str.length-1;
        if(str[0]=='-'){
            i++;
            len=len+1;
        }
        for(;i<len/2;i++){
            char temp=str[i];
            str[i]=str[len-i];
            str[len-i]=temp;
        }
        int result=Integer.parseInt(String.valueOf(str));
        return result;
        
        
    }
}
// @lc code=end

