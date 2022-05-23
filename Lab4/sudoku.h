/* This class lets you store, print and solve Sudoku problems. */
#include <vector>
#include <iostream>
#include <sstream>
using namespace std;

class Sudoku {


  public:
    void Clear();  
    string Read_From_Stdin();
    void Print_Screen() const; 
    void Print_Convert() const;
    bool Solve();
  protected:
    bool Is_Row_Valid(int r) const;
    bool Is_Col_Valid(int c) const;
    bool Is_Panel_Valid(int sr, int sc) const;
    bool Recursive_Solve(int r, int c);

    vector <string> Grid;
};
