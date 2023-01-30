Container with most water
Problem Statement:  Given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Examples:

Input: nums = [1,4,2,3]
Output: 6
Explanation: At i = 1 and i=3 heights are 4 and 3, therefore the maximum amount of water can be stored there. To calculate any amount of water between 2 vertical lines it is the horizontal distance between them multiplied by the minimum of those 2 lines. So in the best case, the max distance between i=1 and i=3 is 2, and the minimum of 4 and 3 is 3, so total water is 2*3=6.


Example 2:
Input: nums = [1,8,6,2,5,4,8,3,7]
Output: 49
Here maximum water can be contained between i=1 and i=8
Solution
Disclaimer: Don’t jump directly to the solution, try it out yourself first.

Brute Force Approach:  
To get the maximum water, we can calculate using 2 loops. At each iteration, we require a distance between 2 lines and the minimum of those lines. So we start with i= 0 and j=i+1. Then calculate max at nums[i] for every other j. We keep a global max and when both loops are done, the value of the max is the answer.


In the above example , we start from i=0 , j starts from 1, for nums[i]=1 and nums[j] = 4, max is (1-0)*min(4,1) = 1, we the loop j till 3. Next iteration I starts at 1, for j = 2,3 and so on.
