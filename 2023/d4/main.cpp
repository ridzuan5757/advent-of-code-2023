#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>

int32_t main(int argc, char *argv[]) {
  std::ifstream input(argv[1]);

  if (!input.is_open()) {
    std::cerr << "Error. Cannot open file." << std::endl;
    return 1;
  }

  std::string line;
  while (std::getline(input, line)) {
    std::cout << line << std::endl;
  }

  input.close();
  return 0;
}
