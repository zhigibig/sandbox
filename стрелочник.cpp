#include <iostream>
#include <conio.h>

int main() {
  using namespace std;

  char key_control = 'a';

  cout << "Game started" << endl;

  while (key_control != '/r') {


    key_control = getche();

    switch(key_control){
      case 'w':
        cout << " up ";
      case 'a':
        cout << " left ";
      case 's':
        cout << " down ";
      case 'd':
        cout << " right ";
      case '/r':
        cout << "\n" << "Exiting game....." << endl; 
        break;
      default:
        cout << "\n" << "Please try another button" << endl;
    };
  };
  
  return 0;
};
