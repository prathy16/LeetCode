// KEYBOARD
// a b c d e f g
// h i j k l m n
// o p q r s t u
// v w x y z

#include<iostream>
#include<vector>

using namespace std;

string moves(string word)
{
    pair<int, int> curPos(0,0);
    string output;
    int x, y, temp;

    for(char c: word)
    {
        x = (c - 'a')/7;
        y = (c - 'a')%7;

        temp = x - curPos.first;
        if(temp < 0){
          output.insert(output.end(), -temp, 'U');
        }
        else if(temp > 0){
          output.insert(output.end(), temp, 'D');
        }

        temp = y - curPos.second;
        if(temp < 0){
          output.insert(output.end(), -temp, 'L');
        }
        else if(temp > 0){
          output.insert(output.end(), temp, 'R');
        }

        curPos = pair<int, int>(x, y);
    }

    return output;
}

int main()
{
  string output = moves("prathy");
  cout << output << endl;
  return 0;
}
