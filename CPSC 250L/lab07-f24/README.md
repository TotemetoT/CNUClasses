# Lab 7 - **Taylor Swift Playlist Manager**

**Objective**: In this lab, you'll practice using Python classes, file handling, and sorting algorithms by creating a playlist manager for your friend's Taylor Swift song collection. You'll use a dataset from `taylor_album_songs.csv` (provided in the `data` folder).

> Note: This project uses data from
> https://www.kaggle.com/datasets/joebeachcapital/taylor-swift-all-songs-and-albums
> provided in our `data` folder.  
> We are only concerned with `taylor_album_songs.csv`.

Your main tasks:
1. Define two classes: one to represent songs and another to manage playlists.
2. Read song data from a file, store it in your classes, and allow for sorting and random access of songs.
3. Practice good coding habits by committing frequently and testing incrementally.

The solution must be demonstrated before the start of the next class
(Yes, I know fall break is coming up.  Focus on finishing during this lab period!)

---

### Instructions

Your friend is a huge Taylor Swift fan and needs a program to manage their playlists.
You will work with data provided in the file `taylor_album_songs.csv` (in the `data` folder).

### Key Tasks:

1. **Define the first class to hold song information**:
   - This class will hold details about each song: song name, album name, album release date, and duration (in seconds).
   - implement a method to return a nicely formatted string with these details.

   > Note: song name is `track_name` in file, use `release_date`

   > Note: the time duration is in the field `duration_ms` (milliseconds).
   > Can you use your program to figure out the relevant index instead of
   > manually counting the commas in header ?
   > Hint: look up the `index()` method for the list
   > https://docs.python.org/3/tutorial/datastructures.html

   > Note: I am calling these first class and second class. It is up to you to
   > define the class names and file names.


2. **Define a second class**:
   - This class should manage a collection of songs.
   - Include methods to:
     - **Add Song**: Add a song to your collection (that is, add an instance of first class).
     - **Get Album**: Retrieve all songs from a specific album
       * initially order by album, then title
        * later we will add parameter and set option to "shuffle" in random order.

        > NOTE: You friend may want to use this in online system that
        > gets called thousands of times, so you probably don't want
        > to have to search through a giant list of all songs to pick out each album.
        > How might you organize the data in second class to make this quicker ?


     - **Get Albums**: Return a list of all album names.

3. **File Input and main**:
   - Define a `read_song_data` function that reads the `taylor_album_songs.csv` file and populates your playlist class with song instances.

   > NOTE: I am making a distinction between a "method" that belongs in a class
   > and a "function" that is just part of script.
   > We often use interchangeably, but here I am being precise.
   >

   Define a script with a main function that will create an instance of your second class,
   read the data from file,  and store in the instance of your second class, and
   then demonstrate the functionality of the required methods.

   > Note: You may want to use the `next()` method to grab the first line (header)
   > out of your data file  after you open up the file and set up for reading.
   > This is easier than testing for header inside your loop.

    Using `readlines` or `csv.reader` creates an "iterator" that can use `next()`
    ```
    # Sample iterator of list where the first item is a header
    data = iter(["Header", "Row1", "Row2", "Row3", "Row4"])

    # Access the header using next()
    header = next(data)
    print(f"Header: {header}")

    # Process the remaining items in a loop
    for row in data:
        print(f"Processing: {row}")
    ```

    > Note: The basic list is *NOT* an iterator object that works with `next()`,
    but the `iter()` method creates an iterator from the list.

    > Warning: I strongly encourage you to practice incremental coding and
    > print out the header and relevant indices to make sure you are getting what
    > you need before you spend a lot of time debugging larger chunks.
    > Code and test incrementally.
    
----

   Part of your job is to convince your TA that the code is correct and complete.

   Think about how you will code incrementally *AND* test incrementally *AND* how you will demonstrate.


After the above is working,

4. **Shuffle and Random Selection**:
   - Modify the `Get Album` method to support a `shuffled=True` parameter, which returns the songs in a random order, make `shuffled=False` the default and sort by title
   - Add a `Get Random` method to second class that retrieves random songs from random albums (default: 5 songs, but the number can be specified).

   - Your code should not allow the same song to be chosen multiple times in shuffle.

   > Note: Look up `random.shuffle()` and `random.choice()` methods
   > https://docs.python.org/3/library/random.html#module-random

---

### Collaboration Guidelines

In this lab you may either:
 * **Work Independently**: Solve the entire lab on your own.
 * **Brainstorm with a Buddy**: Discuss the design, but write your code independently.
 * **Pair Programming**: Work with a partner where you take turns "driving"
   * See [Pair Programming](docs/pair_programming.md) for more information.
   * If you cannot complete everything before the end of lab, it is YOUR responsibility
     to meet with your partner outside of class and finish the Lab before the start of the next lab.
     * Pair programming requirements remain in force for work completed outside of class.
     * You are *NOT* allowed to work independently if using pair programming model.

---

### Grading Breakdown:

**In-Class Progress (30 points)**:
- 10 points: Design outline (in comments) committed during the first hour.
- 10 points: Demonstration of the Song class and basic functionality of `Add Song` by the end of lab.
- 10 points: Productive in-class use of time and showing incremental progress with at least three significant commits.

**Final Submission (70 points)**:
- 10 points: Proper Python style as per Pylint.
- 10 points: Song data is read from the file and stored in the playlist.
- 10 points: Basic functionality of "Get Album" with sorted songs demonstrated.
- 10 points: Correct implementation of sorted and shuffled options in "Get Album".
- 10 points: Random song functionality demonstrated with different song counts.
- 10 points: Proper use of Git with regular, meaningful commits.
- 10 points: Well-commented code with clear explanations.

---
 You are expected to show incremental progress throughout the lab.
 Accessing prior semester solutions of your own or anyone else's,
 including online tutoring sites such as
 (but not limited to) Chegg, Docsity, StackOverflow, ChatGPT or other is strictly
 forbidden and warrants a CHECS referral.

 Reference to StackOverflow for general questions (e.g. how to format a string) is allowed.

 You are only allowed to have general discussions (e.g. how to format a string)
 under empty hands rules.
 The design and implementation should be your own work, or in collaboration with "brainstorm buddy" or "pair programming" partner.

The use of ChatGPT for anything beyond "how do I format a string in Python" or
"show me an example of using the random.choice() method" is not allowed, but
use for basic questions (e.g. "show me random.choice() example") *is* allowed.

---
Copyright 2024 Christopher Newport University
All rights reserved.
Not for reposting to any public server
