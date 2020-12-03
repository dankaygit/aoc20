import com.dankay.ReadCSV;

import java.util.ArrayList;
import java.util.List;

public class day1 {

    public static void main(String[] args) {

        ReadCSV Reader = new ReadCSV();
        List<List<Integer>> input = Reader.readIntegers("../data/day1-input.csv", "\n\r");

        // Need to improve my ReadCSV class because in this instance it returned me a list of lists of one element each
        // The class needs to be a bit smarter about this
        List <Integer> actualInput = new ArrayList<>();
        for (List<Integer> l: input) {
            actualInput.add(l.get(0));
        }
        System.out.println(actualInput);


    }
}
