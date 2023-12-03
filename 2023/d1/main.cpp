#include <fstream>
#include <iostream>
#include <string>
#include <vector>

template <typename T> void printVector(const std::vector<T> &vec) {
  std::cout << "[";
  for (size_t i = 0; i < vec.size(); i++) {
    std::cout << vec[i];

    if (i < vec.size() - 1) {
      std::cout << ",";
    }
  }
  std::cout << "]" << std::endl;
}

std::string extract(const std::string &line) {
  std::string result;

  for (char ch : line) {
    if (std::isdigit(ch)) {
      result += ch;
    }
  }

  return result;
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
    std::string numbers{extract(line)};
    std::string candidate =
        numbers.front().to_string() + numbers.back().to_string();
    std::cout << candidate << std::endl;
  }

  std::cout << result << std::endl;
  input_file.close();

  return 0;
}
