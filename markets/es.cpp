#include <iostream>

using namespace std;

void print_profit(double price_move) {
  cout << "profit: $" << price_move * 50 << "\n";
}

int main() {

  double price_move;
  cout << "Enter price move: ";
  cin >> price_move;
  cout << "\n";

  print_profit(price_move);

  cout << endl;
  return 0;
}