#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <iostream>
#include <cmath>
using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, vector<string>> parking;
    map<string, int> store;
    for (string record : records){
        stringstream ss(record);
        string times = "", code = "", state = "";
        while (ss) {
            ss >> times >> code >> state;
        }
        parking[code].push_back(times);
        store[code] = 0;
    }

    for (const auto keys : parking){
        for (int i = 0 ; i < keys.second.size(); i+=2){
            if (i + 1 < keys.second.size()){
                int in_time = stoi(keys.second[i].substr(0, 2)), in_minute = stoi(keys.second[i].substr(3));
                int out_time = stoi(keys.second[i + 1].substr(0, 2)), out_minute = stoi(keys.second[i + 1].substr(3));
                int time = (out_time - in_time) * 60;
                int minute = out_minute - in_minute;
                int calculate = time + minute;
                store[keys.first] += calculate;
            } else {
                int in_time = stoi(keys.second[i].substr(0, 2)), in_minute = stoi(keys.second[i].substr(3));
                int time = (23 - in_time) * 60;
                int minute = 59 - in_minute;
                int calculate = time + minute;
                store[keys.first] += calculate;
            }
        }
    }
    for (const auto keys : store){
        int val = 0;
        int cal = keys.second;
        cal -= fees[0];
        val += fees[1];
        if (cal > 0 && cal % fees[2] == 0){
            val += (cal / fees[2]) * fees[3];
        } else if (cal > 0 && cal % fees[2] != 0) {
            val += (cal / fees[2]) * fees[3] + fees[3];
        }
        answer.push_back(val);
    }
    return answer;
}