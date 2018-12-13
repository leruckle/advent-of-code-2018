package day02;

import utilities.TallyMap;

public class IdentificationCode {
    final private String code;
    private TallyMap<Character> tally;

    public IdentificationCode(String code){
        this.code = code;
        this.tally = tallyLetters(code);
    }

    private TallyMap<Character> tallyLetters(String input){
        TallyMap<Character> tallyMap = new TallyMap<>();
        for(char letter : input.toCharArray()){
            tallyMap.tally(letter);
        }
        return tallyMap;
    }

    public boolean hasTriple(){
        return this.tally.containsTally(3);
    }

    public boolean hasDouble(){
        return this.tally.containsTally(2);
    }

    public String getCode(){
        return this.code;
    }
}
