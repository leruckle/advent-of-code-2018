package day03;

import utilities.InputFileReader;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day03 {
    static List<Claim> parseInputs(List<String> inputs){
        List<Claim> claims = new ArrayList<>();
        Pattern pattern = Pattern.compile("#([0-9]+)\\s@\\s([0-9]+),([0-9]+):\\s([0-9]+)x([0-9]+).*");
        for(String input : inputs){
            Matcher matcher = pattern.matcher(input);
            if(matcher.matches()){
                int id = Integer.parseInt(matcher.group(1));
                int startX = Integer.parseInt(matcher.group(2));
                int startY = Integer.parseInt(matcher.group(3));
                int width = Integer.parseInt(matcher.group(4));
                int height = Integer.parseInt(matcher.group(5));

                claims.add(new Claim(startX, startY, width, height, id));
            }
        }
        return claims;
    }

    static int part1(List<Claim> claims){
        Grid grid = new Grid(1000, 1000);
        for(Claim claim : claims){
            grid.markOutArea(claim);
        }
        int overlappingSquares = grid.getNumberOfOverlappingSquares();
        return overlappingSquares;
    }

    static int part2(List<Claim> claims){
        Grid grid = new Grid(1000, 1000);
        for(Claim claim : claims){
            grid.markOutArea(claim);
        }
        Claim goodClaim = grid.findClaimWithNoOverlap(claims);
        return goodClaim.getId();
    }

    public static void main(String[] args){
        List<String> inputs = new InputFileReader("day03.txt").readFile();
        List<Claim> claims = Day03.parseInputs(inputs);
        int id = Day03.part2(claims);
        System.out.println(id);
    }
}
