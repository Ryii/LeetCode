class Solution
{
public:
    vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> ans;
        unordered_set<int> seen;
        for (int n : nums1)
        {
            if (seen.count(n))
                continue;
            int countA = min(count(nums1.begin(), nums1.end(), n), count(nums2.begin(), nums2.end(), n));
            for (int i = 0; i < countA; i++)
            {
                ans.push_back(n);
            }
            seen.insert(n);
        }

        return ans;
    }
};