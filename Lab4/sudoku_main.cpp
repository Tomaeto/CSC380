/* This is a main() routine that lets you solve sudoku puzzles on standard input.
 *    It will read puzzles on standard input, and then let you:
 *
 *         - Either solve the puzzles or not.
 *              - Print the puzzle (solved or not).
*/

#include <iostream>
#include <cstdlib>
#include "sudoku.h"
using namespace std;

/* Sometimes it's convenient to have a helper procedure to handle errors
 *    on the command line.  We could, of course, have used try/catch, but
 *       the usage() command makes for cleaner code, in my opinion. */

  
int main(int argc, char **argv)
{

string solve = "yes";
string output = "screen";
 Sudoku sud; 
string r; 


  if (output == "screen") cout << "-------------------" << endl;

  while (true) {

    /* Read the puzzle and handle EOF/errors */

    r = sud.Read_From_Stdin();
    if (r != "") {
      if (r == "EOF") return 0;
      cout << r << endl;
      return 1;
    }

    /* Solve the puzzle if desired. **/

    if (solve == "yes") {
      if (!sud.Solve()) {
        cout << "Cannot solve puzzle" << endl;
      }
    }
  
    /* Print the puzzle. */

    if (output == "screen") {
      sud.Print_Screen();
      cout << "-------------------" << endl;
    } else {
      //sud.Print_Convert();
    }

    /* Clear the puzzle and try again. (Clearing is unnecessary, but may as well test it.) */

    //sud.Clear();
  }
}
