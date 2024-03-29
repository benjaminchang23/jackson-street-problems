#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <iostream>

void urldecode(char *dst, const char *src)
{
    char a, b;
    while (*src) {
        if ((*src == '%') && ((a = src[1]) && (b = src[2])) && (isxdigit(a) && isxdigit(b)))
        {
            if (a >= 'a')
                a -= 'a'-'A';
            if (a >= 'A')
                a -= ('A' - 10);
            else
                a -= '0';
            if (b >= 'a')
                b -= 'a'-'A';
            if (b >= 'A')
                b -= ('A' - 10);
            else
                b -= '0';
            *dst++ = 16*a+b;
            src+=3;
        }
        else if (*src == '+')
        {
            *dst++ = ' ';
            src++;
        }
        else
        {
            *dst++ = *src++;
        }
    }
    *dst++ = '\0';
}

int main()
{
    const auto input = "it%E2%80%99s";
    char output[256];
    std::cout << "input: " << input << std::endl;

    urldecode(output, input);

    std::cout << "output: " << output << std::endl;

    std::string input_str = std::string(output);
    const std::string remove_str = "’";

    std::cout << "input_str: " << input_str << std::endl;
    std::cout << "remove_str: " << remove_str << std::endl;

    const auto pos = input_str.find(remove_str);

    if (pos != std::string::npos)
        input_str.erase(pos, remove_str.length());

    std::cout << "input_str: " << input_str << std::endl;

    return 0;
}