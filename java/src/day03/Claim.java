package day03;

public class Claim {
    final private int startX;
    final private int startY;
    final private int width;
    final private int height;
    final private int id;

    public Claim(int startX, int startY, int width, int height, int id){
        this.startX = startX;
        this.startY = startY;
        this.width = width;
        this.height = height;
        this.id = id;
    }

    int getStartX() {
        return startX;
    }

    int getStartY() {
        return startY;
    }

    int getWidth() {
        return width;
    }

    int getHeight() {
        return height;
    }

    int getEndX() {
        return this.startX + this.width;
    }

    int getEndY() {
        return this.startY + this.height;
    }

    int getId() {
        return id;
    }

    int[] getLowerRightDimension(){
        int[] toReturn = new int[2];
        toReturn[0] = this.startX + this.width;
        toReturn[1] = this.startY + this.height;
        return toReturn;
    }
}
