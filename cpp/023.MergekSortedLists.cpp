/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <queue>
struct Q{
    ListNode *id;
    int val;
    bool operator < (const Q a)const
    {
        return val>a.val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue <Q> que;
        ListNode* rethead=NULL, *ret=NULL;
        int listnum = lists.size();
        Q tem;
        for (int i=0;i<listnum;++i)
        {
            tem.id = lists[i];
            if (tem.id)
            {
                tem.val = lists[i]->val;
                que.push(tem);
            }
        }
        if (que.empty()) return NULL;
        tem = que.top();
        que.pop();
        ret = tem.id;
        rethead = ret;
        if (tem.id->next)
        {
            tem.val = tem.id->next->val;
            tem.id = tem.id->next;
            que.push(tem);
        }
        
        while(!que.empty())
        {
            tem = que.top();
            que.pop();
            ret->next = tem.id;
            ret = ret->next;
            if (tem.id->next)
            {
                tem.val = tem.id->next->val;
                tem.id = tem.id->next;
                que.push(tem);
            }
        }
        ret->next = NULL;
        return rethead;
    }
};