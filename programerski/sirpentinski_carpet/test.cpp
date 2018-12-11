 #include <png++/png.hpp>
#include <math.h>

int n =7;

int rowCount = std::pow(3,n);
int colCount = std::pow(3,n );

int** a = new int*[rowCount];

int randomCounter = 0;

void pobarvej(int x, int y, int size){
    randomCounter ++;
    if (randomCounter < 30){
       //  std::cout << size << "\n";  
      //   std::cout << x << "\n \n";
    }
    int tretjina = size /3;
    if(size <= 3){
        return;
    }
    for (int i= tretjina; i <= tretjina*2; i++){
        for(int j = tretjina; j <=tretjina*2; j++){
            a[x+i][y+j] = 1;
        }
    }
    for (int m=0; m<3;m++){
        for (int n=0; n<3; n++){
            pobarvej(tretjina*m+x, tretjina*n+y, tretjina);
        }

    }

}




int main(){




for(int i = 0; i < rowCount; ++i)
    a[i] = new int[colCount];

pobarvej(0,0,rowCount);


png::image< png::rgb_pixel > image(colCount,rowCount);

for (size_t y = 0; y < colCount; y++){
    for (size_t x = 0; x < rowCount; x++){
        int val = a[y][x] * 20;
        image[y][x] = png::rgb_pixel(val, val, val *10);
    }
}

 image.write("neki.png");

}