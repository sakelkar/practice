#include <string>
#include <stack>
using namespace std;

class Solution {
	bool isValid(string s) {
		stack<char> st;

		for (auto c: s) {
			if (c == '(' or c == '{' or c == '[') {
				st.push(c);
			} else {
				if (c == ']' and st.top() != '[') return(false);
				if (c == ')' and st.top() != '(') return(false);
				if (c == '}' and st.top() != '{') return(false);
			}
			st.pop();
		}
		return(st.empty());
	}
};
