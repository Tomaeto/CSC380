#include <iostream> 
#include <fstream>
#include <sstream> 
#include <map>
#include <stack>
#include <set> 
#include <algorithm>
#include <iomanip> 

struct ResponseBox {
  vector<string> responses; 
  void insert( string R ){responses.push_back( R );}
  string getResponse( ){return responses[rand()%responses.size()];} 
  void clear( ){responses.clear();}
  void view( ){for( string R : responses ) cout << "    " << R << endl;}
};

class Eliza { 
  
  public: 
    /* Constructor -- loads up the dialogue file */
    Eliza( string );
    /* Prints out the constructed multimap */
    void view( );
    /* Main chat function -- user input goes here and response is returned */
    string chat( string );

  private:
    /* Store the keys and value -- many-to-one  */
    multimap<string, ResponseBox> MM;
    /* Iterator for the multimap */ 
    multimap<string, ResponseBox>::iterator mm_it; 

    /* Check to see if user input contain a keyword */
    ResponseBox hasKeyWord( string );
    /* Check to see if user input matches with a key phrase */
    ResponseBox hasKeyPhrase( string );
    /* Preprocess word to remove alphanumerics characters and spaces */
    void cleanWord( string& );
    /* Takes user input and cleans every word and reconstruct to only include non-noise */
    void cleanPhrase( string& );
    /* return T if word is found in the noise set  */
    bool isNoise( const string );
    /* If response contains an asterisk, a deeper response will need to be constructed */
    bool needsDeepResponse( string );
    /* Construct a deeper response given the input and response */
    void getDeepResponse( string&, string& );
    /* remove initial and trailing whitespace */
    string trim( const string& );

    /* A set of words we consider noise to not be considered */
    set<string> noise = {
     "this",
     "that",
     "take",
     "want",
     "which",
     "then",
     "than",
     "will",
     "with",
     "have",
     "after",
     "such",
     "when",
     "some",
     "them",
     "could",
     "make",
     "through",
     "from",
     "were",
     "also",
     "into",
     "they",
     "their",
     "there",
     "because"
   };
};
