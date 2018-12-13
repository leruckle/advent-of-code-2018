package utilities;

import java.util.HashMap;

public class TallyMap<T extends Object> {
    private HashMap<T, Integer> map = new HashMap<>();

    public void tally(T key){
        if(!this.map.containsKey(key)){
            this.map.put(key, 1);
        } else{
            int previousTally = this.map.get(key);
            int newTally = previousTally + 1;
            this.map.put(key, newTally);
        }
    }

    public int getTallyFor(T key){
        if(!this.map.containsKey(key)){
            return 0;
        } else{
            return this.map.get(key);
        }
    }

    public boolean containsTally(int tally){
        return this.map.containsValue(tally);
    }

}
