#include <iostream>
#include <conio.h>

int main() {
  using namespace std;

  char key_control = 'a';

  cout << "Game started" << endl;

  while (key_control != '/r') {


    key_control = getche();

    switch(key_control){
      case key_control == 'w':
        cout << "↑ ";
      case key_control == 'a':
        cout << "";
      case key_control == 's':
        cout << "";
      case key_control == 'd':
        cout << "";
      case key_control == '/r':
        cout << "\n" << "Exiting game....." << endl; 
        break;
      default:
        cout << "\nPlease try another button" << endl;
    };
  };
  
  return 0;
};
