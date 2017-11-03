// classes example
#include <iostream>

class Rectangle {
    int width, height;
  public:
    Rectangle (int,int);
    int area() {return width*height;}
};

Rectangle::Rectangle (int a, int b) {
  width = a;
  height = b;
}

int main () {
  Rectangle rect(3,4);
  std::cout << "area: " << rect.area();
  return 0;
}