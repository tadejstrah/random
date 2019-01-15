#include <iostream>
#include <vector>
#include <cassert>
#include <fstream>
#include <algorithm>
using namespace std;

std::vector<std::string> split(const std::string& str, const std::string& delim) {
    assert(!delim.empty() && "Delimiter must not be empty.");
    std::vector<std::string> tokens;
    size_t prev = 0, pos = 0;
    do {
        pos = str.find(delim, prev);
        if (pos == std::string::npos) pos = str.length();
        tokens.emplace_back(str.substr(prev, pos-prev));
        prev = pos + delim.length();
    } while (pos < str.length() && prev < str.length());
    if (prev == str.length()) tokens.emplace_back("");
    return tokens;
}

std::vector<int> Vehicles;

struct Vehicle{
    int t1, t2 ;
    enum class VehicleType {CAR,BUS,MOTORCYCLE};
};



int main()
{

std::ifstream file("input.txt");
std::string str;
std::string file_contents;
while (std::getline(file, str))
{
  file_contents += str;
  file_contents.push_back('\n');
}  

string testString(file_contents);

vector<string> inputByLines = split(testString, "\n");

sort(inputByLines.begin(),inputByLines.end());


for (int i =  0; i < inputByLines.size()-1; i++) {
    cout << inputByLines[i] << "\n";
}

return 0;
}