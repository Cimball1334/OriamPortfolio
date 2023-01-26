/*
 * HW4-G01295498.c - Fourth Homework Assignment for CS222
 *
 * Author: Craig Kimball
 * Date: 3/29/2022
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
*Program should read from a text file up to 100 addresses and nicknames
*The program will output a list of addresses sorted by alias
*prompt for ascending or descending
*Save this list to the file named 222_Alias_list
*this list will contain name, current data and list
*Address will be read into an array of structs
* sorted using bubble sort
*/
/**
 * Address Sctruct
 * int val1, val2, val3, val4 store the 4 integer elements that make up an IP address
 * char alias stores the max 10 bit name associated with that address
 */
struct Address{
    int val1;
    int val2;
    int val3;
    int val4;
    char alias[10];
};

char *getDateAndTime();

int Read_Data_File(struct Address list[]);
void Bubble_sort(struct Address list[], int pos, int direction);
void swap(struct Address *x,struct Address *y);
void Generate_Alias_list(struct Address list[],char name[], int n);


int toupper(int ch);
int strcmp (const char* str1, const char* str2);

/**
 * Main method
 * Handles method calls
 */
int main(){
    char name[21];
    char direction;
    struct Address Addresses[100];

    printf("Enter Your name: \n");
    fgets(name,sizeof(name),stdin);

    printf("Do you want Ascending or Descending? (A/D)\n");
    scanf("%c",&direction);
    printf("Reading Data from CS222_Inet.txt");

    //gets direction as upper case ASCII
    int d = toupper(direction);

    //stores the final index position
    int rows = Read_Data_File(Addresses);

    Bubble_sort(Addresses,rows,d);
    Generate_Alias_list(Addresses,name,rows);
}

/**
 * Unix Method to get the current date and time of the system
 *
 */
char *getDateAndTime(){

    time_t t;
    time(&t);
    return ctime(&t);

}

/**
 * Bubble Sort
 *
 * A comparison sort that continually moves values in the correct direction based on order
 * to eventually get a sorted list
 *
 * Takes in a list of addresses, the final index of the initialized elements, and a direction to sort (A/D)
 */
void Bubble_sort(struct Address list[], int pos, int direction){
    //bubble sort works by incrementing through every element of the list over and over again, slowly increasing the starting position
    // it shoves all values left by swaping the position based on direction
    for(int i = 0; i < pos - 1; i++){
        for(int j = 0; j < pos-i-1; j++){

        //forwards
        //here we compare t he ascii of A and D to get ascending and descending order
            if(direction < 68){

                if( strcmp( list[j].alias,list[j+1].alias) > 0 ){
                    swap(&list[j],&list[j+1]);
                }
            //backwards
            }else{

                if( strcmp( list[j].alias,list[j+1].alias) < 0 ){
                    swap(&list[j],&list[j+1]);
                }
            }
        }
    }
}


/**
 * Swap function to be used in bubble sort
 * Creates temporary values to assign each others value at their indexes
 */
void swap(struct Address *x,struct Address *y){
    //stores value so it isnt lost
    struct Address temp = *x;
    //sets the values to be the same
    *x = *y;
    //sets the lost value to the temp value to swap their places
    *y = temp;
}

/**
 * File output Stream
 * Takes in a list of addresses, the users name, and the final position of the initialized elements
 */
void Generate_Alias_list(struct Address list[],char name[],int n){
    //write to file
    char fileName[] = "222_Alias_List";
    FILE *f;
    f = fopen(fileName,"w");
    
    fprintf(f,"%s%s\n",name,getDateAndTime());
    fprintf(f,"CS222 Network Alias Listing\n");
    
    //for each address in the list, up to the final index
    for(int i = 0; i<n;i++){
        fprintf(f,"%s\t%d.%d.%d.%d\n",list[i].alias,list[i].val1,list[i].val2,list[i].val3,list[i].val4);
    }

}

//return int that is the number of rows
/**
 * File input stream
 *
 * Takes input from a pre defined file
 * Assumes formatting is correct of type x.x.x.x "X"
 *
 * Return int, the final index of initialized elements
 */
int Read_Data_File(struct Address list[]){

    FILE *f;
    f = fopen("CS222_Inet.txt","r");
 
    int pos = 0;
    char buff[255];
    int b[4] = {0};

    int i = 1;

    while(fgets(buff,255,f)!=NULL && i > 0){
        char name[10] = "abcdefghjk";

        sscanf(buff,"%d.%d.%d.%d %s\n",b,b+1,b+2,b+3,name);
        struct Address addy = {b[0],b[1],b[2],b[3],*name};

        //sets each character of the name individually, was getting issues where it was only first character
        for(int i = 0; i < sizeof(name); i++){
            addy.alias[i] = name[i];
        }

        //checks for end case of 0.0.0.0 NONE
        if(addy.val1 == 0 || addy.val2 == 0 || addy.val3 == 0 || addy.val4 == 0){
            i = 0;
        }else{
            // adds the proper address to the list and increments position
            list[pos] = addy;
            pos++;
        }

    }
    return pos;

}