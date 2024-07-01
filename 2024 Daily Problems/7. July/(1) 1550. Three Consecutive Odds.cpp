#include <vector>

class Solution
{
public:
    bool threeConsecutiveOdds(vector<int> &arr)
    {
        if (arr.size() < 3)
            return false;
        bool a1 = (arr[0] % 2 == 1), a2 = (arr[1] % 2 == 1), a3 = (arr[2] % 2 == 1);

        for (int i = 3; i < arr.size(); i++)
        {
            if ((a1 == a2) && (a2 == a3) && (a3 == 1))
                return true;
            a1 = a2, a2 = a3, a3 = arr[i] % 2 == 1;
        }

        if ((a1 == a2) && (a2 == a3) && (a3 == 1))
            return true;

        return false;
    }
};