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
        bool flag = false;
        ListNode* ret = l1;
        ListNode* cur = l1;
        int tem;
        while(l1 && l2)
        {
            tem = l1->val + l2->val;
            if (flag) tem++;
            cur->val = tem%10;
            flag = tem/10;
            if (!l1->next)
            {
                cur->next = l2->next;
                cur = cur->next;
                l1 = l1->next;
                l2 = l2->next;
            }
            else
            {
                cur->next = l1->next;
                cur = cur->next;
                l1 = l1->next;
                l2 = l2->next;
            }
        }
        if (flag) cur->val++;
        return ret;
    }
};