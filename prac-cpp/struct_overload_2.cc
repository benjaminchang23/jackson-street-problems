#include <algorithm>
#include <iostream>
#include <vector>

struct container
{
    int a;
    int b;
    std::string c;
};

struct hash_fn
{
    std::size_t operator() (const container &con) const
    {
        std::size_t h1 = std::hash<int>()(con.a);
        std::size_t h2 = std::hash<int>()(con.b);
        std::size_t h3 = std::hash<std::string>()(con.c);

        return h1 ^ h2 ^ h3;
    }
};

inline bool operator == (const container &left, const container &right)
{
    return left.a == right.a && left.b == right.b && left.c == right.c;
}

inline bool operator < (const container &left, const container &right)
{
    if (left.a == right.a)
        return left.b < right.b;
    return left.a < right.a;
}

inline std::ostream& operator << (std::ostream &o, const container &con)
{
    o << "a: " << con.a << " ";
    o << "b: " << con.b << " ";
    o << "c: " << con.c << " ";
    return o;
}

struct compare_struct
{
    bool a_first = true;

    bool operator() (const container &left, const container &right)
    {

        if (a_first)
        {
            if (left.a == right.a)
                return left.b < right.b;
            return left.a < right.a;
        }

        if (left.b == right.b)
            return left.a < right.a;
        return left.b < right.b;
    }
};

int main()
{
    container con_0 {4, 1, "con_0"};
    container con_1 {1, 8, "con_1"};
    container con_2 {1, 3, "con_2"};
    container con_3 {5, 1, "con_3"};

    std::vector<container> vec;

    vec.emplace_back(con_0);
    vec.emplace_back(con_1);
    vec.emplace_back(con_2);
    vec.emplace_back(con_3);

    compare_struct compare;
    compare.a_first = false;

    std::sort(vec.begin(), vec.end(), compare);

    for (const auto & con : vec)
    {
        std::cout << con << std::endl;
    }

    return 0;
}