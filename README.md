# Flash_Card_App
This program will help you learn French. 
How it works: The program shows the user the French word and its English translation after 3 seconds. If the user knows this word, he clicks the "yes" button, and the program will remove this word from the list of words to learn. "Pandas" is used in this project.

The program is made using Python.

Originally there is one data file in csv format - "french_words". It contains two rows of information - words in french and their translations. Later, the program creates a second csv file - "words_to_learn".
At the beginning, the program tries to read data from the file "words_to_learn", if it doesn't exist, it takes data from the original file "french_words" (try/except/else construction is used). "Pandas" library is used for reading and manipulating the data. 
Then the program creates an interface using "tkinter" library. "next_card" function gets triggered, it shows a french word (it is picked randomly from the data which was read at the beginning), then waits for 3 seconds and triggers the function "flip_the_card"
"flip_the_card" function changes the card color and shows the english translation of the french word. 

Then the program starts waiting for the user to click "yes" or "no" button. 
"Yes" button (meaning that the user already knows this word) triggeres "is_known" function. It deletes this word from the data and then writes already corrected data to the "words_to_learn" file. "next_card" function gets triggered afterwards.
"No" button just triggeres "next_card" function. 
