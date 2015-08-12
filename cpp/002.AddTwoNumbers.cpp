/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int flag = 0;
        ListNode* ret = l1;
        ListNode* cur = l1;
        int tem;
        while(l1 && l2)
        {
            tem = l1->val + l2->val;
            if (flag) tem++;
            cur->val = tem%10;
            flag = tem/10;
            l1 = l1->next;
            l2 = l2->next;
            if (!l1)
            {
                cur->next = l2;
                if (!cur->next && flag) {cur->next = new ListNode(1);flag = 0;}
                cur = cur->next;
            }
            else
            {
                cur->next = l1;
                cur = cur->next;
            }
        }
        while (flag) 
        {
            tem = cur->val+1;
            cur->val = tem%10;
            flag = tem/10;
            if (!cur->next && flag) {cur->next = new ListNode(1);flag = 0;}
            cur = cur->next;
        }
        return ret;
    }
};