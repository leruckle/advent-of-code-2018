package day01;

import utilities.InputFileReader;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Day01 {

    public static int part1(List<String> inputs){
        int total = 0;
        for(String input : inputs){
            String operand = input.substring(0,1);
            int value = Integer.parseInt(input.substring(1));
            if(operand.equals("+")){
                total = total + value;
            }
            else if(operand.equals("-")){
                total = total - value;
            }
            else{
                throw new IllegalStateException("Unexpected operand: " + operand);
            }
        }
        return total;
    }

    public static int part2(List<String> inputs){
        Set<Integer> frequencies = new HashSet<>();
        frequencies.add(0);
        int counter = 0;
        int total = 0;
        while(true){
            int currentIndex = counter % inputs.size();
            String input = inputs.get(currentIndex);

            String operand = input.substring(0,1);
            int value = Integer.parseInt(input.substring(1));
            if(operand.equals("+")){
                total = total + value;
            }
            else if(operand.equals("-")){
                total = total - value;
            }
            else{
                throw new IllegalStateException("Unexpected operand: " + operand);
            }

            if(frequencies.contains(total)){
                break;
            } else{
                frequencies.add(total);
            }
            counter++;
        }
        return total;
    }

    public static void main(String[] args){
        List<String> inputs = new InputFileReader("day01.txt").readFile();

//        List<String> test_inputs = Arrays.asList("+3", "+3", "+4", "-2", "-4");
        int total = Day01.part2(inputs);
        System.out.println(total);
    }
}
