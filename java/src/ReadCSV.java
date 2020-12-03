package com.dankay;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class ReadCSV {

    public List<List<Integer>> readIntegers(String filePath, String delimiter) {

        File inputFile = new File(filePath); // File opens the file
        Scanner inputStream; // open instance of a Scanner
        List<List<Integer>> output = new ArrayList<>(); //we'll put the read lines in here

        try {
            inputStream = new Scanner(inputFile); // tell

            while (inputStream.hasNext()) {
                String line = inputStream.next(); //feeds next line into a string
                List<String> values = Arrays.asList(line.split(delimiter)); //split the string into a string array,
                // then extracts the array into a list for conversion into list of Integers
                // Map list of strings to list of integers
                List<Integer> intValues = values.stream().map(Integer::parseInt).collect(Collectors.toList());
                output.add(intValues); //add the list of integers to the output
            }

            inputStream.close();
        } catch (
                FileNotFoundException e) {
            System.out.println("An error occurred: File Not Found");
            e.printStackTrace();
        }

        return output;

    }

    public List<List<Integer>> readIntegers(String filePath) {
        String delimiter = ",";
        return readIntegers(filePath, delimiter);
    }

    public List<List<String>> readStrings(String filePath, String delimiter) {

        File inputFile = new File(filePath); // File opens the file
        Scanner inputStream; // open instance of a Scanner
        List<List<String>> output = new ArrayList<>(); //we'll put the read lines in here

        try {
            inputStream = new Scanner(inputFile); // tell

            while (inputStream.hasNext()) {
                String line = inputStream.next(); //feeds next line into a string
                List<String> values = Arrays.asList(line.split(delimiter));
                output.add(values); //add the list of Strings to the output
            }

            inputStream.close();

        } catch (
                FileNotFoundException e) {
            System.out.println("An error occurred: File Not Found");
            e.printStackTrace();
        }

        return output;

    }

    public List<List<String>> readStrings(String filePath) {
        String delimiter = ",";
        return readStrings(filePath, delimiter);
    }

}