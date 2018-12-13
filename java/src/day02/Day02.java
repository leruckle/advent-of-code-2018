package day02;

import utilities.InputFileReader;

import java.util.ArrayList;
import java.util.List;

public class Day02 {

    static List<IdentificationCode> parseInputs(List<String> inputs){
        List<IdentificationCode> idCodes = new ArrayList<>(inputs.size());
        for(String input : inputs){
            idCodes.add(new IdentificationCode(input));
        }
        return idCodes;
    }

    static int part1(List<IdentificationCode> idCodes){
        int n_triples = 0;
        int n_doubles = 0;
        for(IdentificationCode code : idCodes){
            if(code.hasTriple()){
                n_triples++;
            }
            if(code.hasDouble()){
                n_doubles++;
            }
        }
        return n_doubles * n_triples;
    }

    static String part2(List<IdentificationCode> idCodes){
        String similarCodeStr1 = "";
        String similarCodeStr2 = "";
        iLoop: for(int i=0; i<idCodes.size(); i++){
            String codeStr1 = idCodes.get(i).getCode();
            jLoop: for(int j=i+1; j<idCodes.size(); j++){
                String codeStr2 = idCodes.get(j).getCode();
                int nDifferent = 0;
                for(int k=0; k<codeStr1.length(); k++) {
                    char letter1 = codeStr1.charAt(k);
                    char letter2 = codeStr2.charAt(k);
                    if (letter1 != letter2) {
                        nDifferent++;
                    }
                    if (nDifferent > 1) {
                        continue jLoop;
                    }
                }
                similarCodeStr1 = codeStr1;
                similarCodeStr2 = codeStr2;
                break iLoop;
            }
        }

        StringBuilder stringBuilder = new StringBuilder();
        for(int k=0; k<similarCodeStr1.length(); k++) {
            char letter1 = similarCodeStr1.charAt(k);
            char letter2 = similarCodeStr2.charAt(k);
            if (letter1 == letter2) {
                stringBuilder.append(letter1);
            }
        }
        String finalString = stringBuilder.toString();

        return finalString;
    }


    public static void main(String[] args){
        List<String> inputs = new InputFileReader("day02.txt").readFile();
        List<IdentificationCode> codes = Day02.parseInputs(inputs);
        int checksum = Day02.part1(codes);
        System.out.println(checksum);

        String finalString = Day02.part2(codes);
        System.out.println(finalString);
    }
}
