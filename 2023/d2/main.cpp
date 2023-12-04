#include <cctype>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

std::map<std::string, int> gameLimit{{"red", 12}, {"green", 13}, {"blue", 14}};
bool checkGame(std::string);

int32_t extractGameNumber(std::string game) {
  std::string digit;
  for (const auto ch : game) {
    if (std::isdigit(ch)) {
      digit += ch;
    }
  }
  int test = std::stoi(digit);
  return std::stoi(digit);
}

bool extractGameSet(std::string gameData) {
  std::istringstream iss{gameData};
  std::string gameSet;
  while (std::getline(iss, gameSet, ';')) {
    if (!checkGame(gameSet)) {
      return false;
    }
  }
  return true;
}

bool checkGame(std::string gameSet) {
  std::istringstream iss{gameSet};
  std::string game;
  while (std::getline(iss >> std::ws, game, ',')) {
    std::istringstream issi{game};
    std::string gameProp;
    std::vector<std::string> gamePropBuf;
    while (std::getline(issi >> std::ws, gameProp, ' ')) {
      gamePropBuf.push_back(gameProp);
    }

    int32_t count = std::stoi(gamePropBuf.front());
    std::string colour = gamePropBuf.back();

    if (count > gameLimit[colour]) {
      return false;
    }
  }
  return true;
}

int32_t main(int arc, char *argv[]) {
  std::ifstream input_file(argv[1]);
  int result{0};

  if (!input_file.is_open()) {
    std::cerr << "Error opening the file" << std::endl;
    return 1;
  }

  std::string line;
  while (std::getline(input_file, line)) {

    std::vector<std::string> buf;
    std::istringstream iss{line};
    std::string gameset;
    while (std::getline(iss >> std::ws, gameset, ':')) {
      buf.push_back(gameset);
    }

    int32_t game = extractGameNumber(buf.front());
    std::string set = buf.back();
    if (extractGameSet(set)) {
      result += game;
    }
  }

  std::cout << result << std::endl;
  input_file.close();

  return 0;
}
