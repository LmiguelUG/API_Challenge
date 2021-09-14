A python script that applies 'inverted indices', as input interacts with the user using the console.

 - The first interaction indicates the type of file; either .zip or a folder.
 - The second interaction will ask for the address of the file indicated above.
 
 If it is a .zip, a decompression is carried out internally and the files / folders will be located in the path on which this script is being executed.
 
 - The inverted index algorithm is then carried out (For this the data is cleaned, in this case the lines read in each file).
 - The results will be written to an 'indexing.txt' file located in the directory where this script is run.
 - The third interaction with the user, once the indexing is completed, will be the request for the word that you want to know, location in the corresponding folders, subfolders
   and files.
