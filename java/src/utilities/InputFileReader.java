package utilities;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class InputFileReader {
    private Path filePath;

    public InputFileReader(String fileName){
        Path absPath = Paths.get("").toAbsolutePath();
        this.filePath = Paths.get(absPath.toString(), "input", fileName);
    }

    public List<String> readFile(){
        List<String> input = new ArrayList<>();
        try {
            input = Files.lines(this.filePath).collect(Collectors.toList());
            return input;
        } catch (IOException io){
            System.err.println(io.getMessage());
        }
        return input;
    }
}
