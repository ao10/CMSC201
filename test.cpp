#include <iostream>
using namespace std;

int main(){
  const double RATE = 6.9;
  double deposit;
  
  cout<<"Enter the amount of the deposit $:";
  cin>>deposit;
  
  double newBalance;
  newBalance = deposit + deposit*(RATE/100);
  
  cout<<"Your new balance will be $" << newBalance << endl;


}
