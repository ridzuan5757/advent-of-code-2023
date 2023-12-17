#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <ostream>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

std::vector<std::string> splitString(const std::string &input,
                                     const char delim) {
  std::istringstream stream(input);
  std::vector<std::string> tokens;
  std::string token;

  while (std::getline(stream >> std::ws, token, delim)) {
    tokens.push_back(token);
  }

  return tokens;
}

std::vector<int> stringToVector(const std::string &input) {

  std::istringstream stream(input);
  std::vector<int> result;
  std::string token;

  while (std::getline(stream >> std::ws, token, ' ')) {
    result.push_back(std::stoi(token));
  }

  return result;
}

template <typename T> void printVector(const std::vector<T> arr) {
  for (const auto &i : arr) {
    std::cout << i << " ";
  }
  std::cout << std::endl;
}

int32_t getDay(const std::string &input) {
  return std::stoi(input.substr(input.length() - 1));
}

int32_t main(int argc, char *argv[]) {
  int totalWin = 0;

  std::ifstream input(argv[1]);

  if (!input.is_open()) {
    std::cerr << "Error. Cannot open file." << std::endl;
    return 1;
  }

  std::string line;
  while (std::getline(input, line)) {
    std::vector<std::string> data = splitString(line, ':');
    int day = getDay(data[0]);
    std::vector<std::string> ticketData = splitString(data[1], '|');
    std::vector<int> winningTicket = stringToVector(ticketData[0]);
    std::vector<int> ticket = stringToVector(ticketData[1]);

    int winCount = 0;

    for (const auto &i : ticket) {
      auto it = std::find(winningTicket.begin(), winningTicket.end(), i);

      if (it != winningTicket.end()) {
        std::cout << "Found " << i << "in ";
        printVector(winningTicket);
        winCount += 1;
      }
    }

    totalWin += winCount;
  }

  input.close();
  std::cout << "Total win: " << totalWin << std::endl;
  return 0;
}
