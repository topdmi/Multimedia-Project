// Script algoritmi di dithering

PImage img;

void setup() {
  size(500, 333);
  img = loadImage("im1.png"); 
  //filter(GRAY);
  //image(img,0,0); // Original image
  image(Floyd(img), 0, 0); // Floyd dithering
  //save("Floyd13.png");
  //image(Jarvis(img), 0, 0); // Jarvis dithering
  //save("Jarvis8.png");
}

int index(int x, int y) {
  return x + y * img.width;
}

PImage Floyd(PImage img) {

  PImage temp = img.copy();
  temp.loadPixels();

  for (int y = 0; y < temp.height-1; y++) {
    for (int x = 1; x < temp.width-1; x++) {

      color pix = temp.pixels[index(x, y)];

      // estrae i valori RGB dai pixel
      float oldR = red(pix);
      float oldG = green(pix);
      float oldB = blue(pix);

      int n = 8; // numero di colori disponibili nella palette

      // quantizza i valori in un range
      int newR = round(n * oldR / 255) * (255/n);
      int newG = round(n * oldG / 255) * (255/n);
      int newB = round(n * oldB / 255) * (255/n);

      // errore di ogni colore dopo la quantizzazione
      float errR = oldR - newR;
      float errG = oldG - newG;
      float errB = oldB - newB;

      // ripristina il valore del pixel      
      temp.pixels[index(x, y)] = color(newR, newG, newB);

      //applica algoritmo di Floyd

      //caso 1
      int index = index(x+1, y  );
      color c = temp.pixels[index];
      float r = red(c);
      float g = green(c);
      float b = blue(c);
      r = r + errR * 7/16.0;
      g = g + errG * 7/16.0;
      b = b + errB * 7/16.0;
      temp.pixels[index] = color(r, g, b);

      //caso 2
      index = index(x-1, y+1);
      c = temp.pixels[index];
      r = red(c);
      g = green(c);
      b = blue(c);
      r = r + errR * 3/16.0;
      g = g + errG * 3/16.0;
      b = b + errB * 3/16.0;
      temp.pixels[index] = color(r, g, b);

      //caso 3
      index = index(x, y+1);
      c = temp.pixels[index];
      r = red(c);
      g = green(c);
      b = blue(c);
      r = r + errR * 5/16.0;
      g = g + errG * 5/16.0;
      b = b + errB * 5/16.0;
      temp.pixels[index] = color(r, g, b);

      //caso 4
      index = index(x+1, y+1);
      c = temp.pixels[index];
      r = red(c);
      g = green(c);
      b = blue(c);
      r = r + errR * 1/16.0;
      g = g + errG * 1/16.0;
      b = b + errB * 1/16.0;
      temp.pixels[index] = color(r, g, b);
    }
  }

  temp.updatePixels();
  return temp;
}

PImage Jarvis(PImage image) {

  PImage temp = image.copy();
  temp.loadPixels();
  float[][] mask = { { 0, 0, 0, 7, 5}, { 3, 5, 7, 5, 3 }, { 1, 3, 5, 3, 1 } }; //kernel con 12 parametri

  for (int j=0; j<temp.height; j++) {
    for (int i=0; i<temp.width; i++) {

      color pix = temp.pixels[index(i, j)];

      // estrae i valori RGB dai pixel
      float oldR = red(pix);
      float oldG = green(pix);
      float oldB = blue(pix);

      int n = 8; // numero di colori disponibili nella palette

      // quantizza i valori in un range
      int newR = round(n * oldR / 255) * (255/n);
      int newG = round(n * oldG / 255) * (255/n);
      int newB = round(n * oldB / 255) * (255/n);

      // errore di ogni colore dopo la quantizzazione
      float errR = oldR - newR;
      float errG = oldG - newG;
      float errB = oldB - newB;

      // ripristina il valore del pixel      
      temp.pixels[index(i, j)] = color(newR, newG, newB);

      //applica algoritmo di jarvis
      for (int m=0; m<2; m++) {
        for (int k=-2; k<=2; k++) {
          if (m==0 && k<0) continue;
          else {
            float weight = mask[m][k+2];

            temp.set(i+k, j+m, color(
              red(temp.get(i+k, j+m)) + (weight / 48.0) * errR, 
              green(temp.get(i+k, j+m)) + (weight / 48.0) * errG, 
              blue(temp.get(i+k, j+m)) + (weight / 48.0) * errB));
          }
        }
      }
    }
  }

  temp.updatePixels();
  return temp;
}
