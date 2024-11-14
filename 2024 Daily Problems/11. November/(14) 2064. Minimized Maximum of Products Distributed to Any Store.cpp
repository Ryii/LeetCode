class Solution
{
public:
    int minimizedMaximum(int n, vector<int> &quantities)
    {
        int left = 0, right = *max_element(quantities.begin(), quantities.end());

        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (canDistribute(mid, quantities, n))
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }

        return left;
    }

    bool canDistribute(int m, vector<int> &quantities, int n)
    {
        int j = 0;
        int remaining = quantities[j];

        for (int i = 0; i < n; ++i)
        {
            if (remaining <= m)
            {
                j++;
                if (j == quantities.size())
                    return true;
                else
                    remaining = quantities[j];
            }
            else
            {
                remaining -= m;
            }
        }
        return false;
    }
};