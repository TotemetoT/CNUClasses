#include <iostream>
#include <list>
#include <string.h>
#include <algorithm>
#include <cstring>
#include <format>
#include <ranges>
using namespace std;

/**
 * Reverses the inputted string
 * @param s String
 * @return Reversed input
 */
string reverse(string s) {
    string c;
    while (!s.empty()) {
        c += s.back();
        s.pop_back();
    }
    return c;
}

/**
 * Takes a string of numbers separated by spaces and
 * makes them a list for easier access
 * @param numString const char*
 * @return list of individual numbers
 */
list<string> split(const char* numString) {
    string temp;
    list<string> ret;
    while (*numString != '\0') {
        if (*numString == ' ') {
            if (!temp.empty()) {
                ret.push_back(temp);
                temp.clear();
            }
        } else {
            temp += *numString;
        }
        numString++;
    }
    if (!temp.empty()) {
        ret.push_back(temp);
    }
    return ret;
}

/**
 * Takes an inputted number as a string and adds its reverse until it's a palindrome
 * @param s String
 * @return list with cycle count & palindrome
 */
list<string> make_pall(string s) {
    int count = 1;
    long long intS = stoll(s);
    long long rev = stoll(reverse(s));
    intS += rev;
    rev = stoll(reverse(to_string(intS)));
    while (intS != rev) {
        count++;
        intS += rev;
        rev = stoll(reverse(to_string(intS)));
    }
    list<string> ret;
    ret.push_back(to_string(count));
    ret.push_back(to_string(intS));
    return ret;
}

/**
 * Takes a list with two values and appends them to the end of the string
 * @param l list<string>
 * @param s String
 * @return String
 */
string retString(list<string> l, string s) {
    string count = l.front();
    l.pop_front();
    string pall = l.back();
    if (s.empty()) {
        s = format("{} {}", count, pall);
    } else {
        s += format(" {} {}", count, pall);
    }
    return s;
}

char* process(const char* numbers);

/**
 * Takes given numbers and, using above methods, find the palindrome of the method and the
 * amount of cycles, finally ending with a list that contains the amount of cycles and the
 * palindromes of the given numbers
 * @param numbers const char*
 * @return char* of cycles and palindrome of given numbers
 */
char* process(const char* numbers) {
    // Check Null
    if (numbers == NULL) {
        return 0;
    } if (*numbers == '\0') {
        return strdup("");
    }
    list<string> nums = split(numbers);
    list<list<string>> ret;
    for (string s : nums) {
        ret.push_back(make_pall(s));
    }
    string final;
    for (list<string> l : ret) {
        final = retString(l, final);
    }
    return strdup(final.c_str());
}

int main() {
    const char* input    = NULL;
    const char* expected = 0;

    for (int i = 0; i <= 12; i++) {
        switch (i) {
        case 0:
            input    = "";
            expected = "";
            break;
        case 1:
            input    = "4 130031 9";
            expected = "1 8 1 260062 2 99";
            break;
        case 2:
            input    = "195 265 750";
            expected = "4 9339 5 45254 3 6666";
            break;
        case 3:
            input    = "2 99 4000000000 20 100 1";
            expected = "1 4 6 79497 1 4000000004 1 22 1 101 1 2";
            break;
        case 4:
            input    = "79 88 97 99";
            expected = "6 44044 6 44044 6 44044 6 79497";
            break;
        case 5:
            input    = "157 158 166 167 175 188 193 197";
            expected = "3 8888 3 11011 5 45254 11 88555588 4 9559 7 233332 8 233332 7 881188";
            break;
        case 6:
            input    = "266 273 274 292 365";
            expected = "11 88555588 4 5115 4 9559 8 233332 11 88555588";
            break;
        case 7:
            input    = "1089 1091 1099";
            expected = "4 79497 1 2992 2 11011";
            break;
        case 8:
            input    = "19991 2914560 12345678";
            expected = "8 16699661 5 47977974 1 99999999";
            break;
        case 9:
            input    = "777";
            expected = "4 23232";
            break;
        case 10:
            input    = "177 554";
            expected = "15 8836886388 3 11011";
            break;
        case 11:
            input    = "604 605 703 704 802 803 901 902";
            expected = "2 1111 1 1111 2 1111 1 1111 2 1111 1 1111 2 1111 1 1111";
            break;
        case 12:
            input    = "880";
            expected = "23 8813200023188";
            break;
        default:
            cout << "we should never get here" << endl;
            return -1;
        }
        char* actual = process( input );
	bool  equal  = false;
	if (actual != NULL) {
	    equal  = strcmp( expected, actual ) == 0;
	}
        cout << "test " << i << ": " << (equal ? "ok" : "failed");
        if (!equal) {
            cout << " expected [" << expected
                 << "] but was [" << (actual == NULL ? "NULL" : actual) << "]";
        }
        cout << endl;

        delete actual;
    }
    return EXIT_SUCCESS;
}
