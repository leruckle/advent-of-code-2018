package day03;

import java.util.List;

public class Grid {
    private int[][] grid;

    public Grid(int length, int width){
        this.grid = new int[length][width];
    }

    protected void markOutArea(Claim claim){
        for(int i=claim.getStartY(); i<claim.getEndY(); i++){
            for(int j=claim.getStartX(); j<claim.getEndX(); j++) {
                this.grid[i][j] = this.grid[i][j] + 1;
            }
        }
    }

    int getNumberOfOverlappingSquares(){
        int counter = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[i].length; j++){
                if(this.grid[i][j] > 1){
                    counter++;
                }
            }
        }
        return counter;
    }

    Claim findClaimWithNoOverlap(List<Claim> claims){
        claimLoop: for(Claim claim : claims){
            for(int i=claim.getStartY(); i<claim.getEndY(); i++){
                for(int j=claim.getStartX(); j<claim.getEndX(); j++) {
                    if(this.grid[i][j] != 1){
                        continue claimLoop;
                    }
                }
            }
            return claim;
        }
        throw new IllegalStateException("Sorry, I didn't find the claim you were looking for.");
    }

}
