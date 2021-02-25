void setup() {
  size (600, 600); 
}

void draw(){
  background(222);
  float x = 300;
  float y = 300;
  float radiusMin = 100;
  float radiusMax = 250;
  float radius1 = round(map(mouseY, 0, height, radiusMin-20, radiusMax));
  int n = 5;
  float angle = TWO_PI / n;
  float halfAngle = angle/2;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle)
  {
    float sx = x + cos(a) * radiusMin;
    float sy = y + sin(a) * radiusMin;
    vertex(sx, sy);
    sx = x + cos(a+halfAngle) * radius1;
    sy = y + sin(a+halfAngle) * radius1;
    vertex(sx, sy);  
  }
  endShape(CLOSE);
}
