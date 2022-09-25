/*
 * HW5-G01295498.c - Fith Homework Assignment for CS222
 * 
 * Author: Craig Kimball
 * Date: 4/25/2022
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>

/**
 * open and read the input file
 * 
 * each ip vlaue must be within 0-255
 * invalid ip's go to 222_Error_report.txt
 * Valid ip's go to 222_Locality_Report.txt
 */

struct Address{
    int val1;
    int val2;
    int val3;
    int val4;
    char alias[10];
};

char *getDateAndTime();
int * readDataFile();
int checkAddress(int a);
int checkAlias(char a[]);
int generateLocalityRpt(int g, int b, char name[]);

struct Address *good/*[100]*/;
struct Address *bad/*[100]*/;


int main(){
    char name[21];
    
    printf("Enter Your name: \n");
    fgets(name,sizeof(name),stdin);
    
    int *posarr;
    posarr = readDataFile();

    generateLocalityRpt(posarr[0],posarr[1],name);
    
}

/**
 * @brief reads a list of addresses from a given set of data
 * 
 * @return int* the count of how many addresses do and do not fit the standards
 */
int* readDataFile(){
    FILE *f;
    f = fopen("CS222_Inet.txt","r");

    //number of good addresses
    int G = 0;
    int Gpos = 0;
    //number of bad addresses
    int B = 0;
    int Bpos = 0;

    //G and B are counters to how many addresses will be added
    //Gpos and Bpos are the current location of the recently added Address

    char buff[255];
    int b[4] = {0};
    
    //int flag represents a boolean
    int i = 1;
    while(fgets(buff,255,f) != NULL && i == 1){
            char name[15];
            sscanf(buff,"%d.%d.%d.%d %s\n",b,b+1,b+2,b+3,name);

            //checks to see if any values of the Address are 0
            if(b[0] == 0 || b[1] == 0 || b[2] == 0 || b[3] == 0){
                //sentinal flag - stop looping
                i = 0;
            }else{
                //checks if the current address is a good or bad address
                if( checkAlias(name) == 0 
                || checkAddress(b[0]) == 0 
                || checkAddress(b[1]) == 0 
                || checkAddress(b[2]) == 0 
                || checkAddress(b[3]) == 0){
                    //updates the number of bad addresses
                    B += 1;
                }else{
                    //updates the number of good addresses
                    G += 1;
                }
            }
    }
    
    //resets position to top of the document
    rewind(f);

    //reset flag for next loop
    i = 1;

    //dynamic memory allocation using the counter of Good and Bad Addresses
    good = (struct Address *)malloc(G*sizeof(struct Address));
    bad = (struct Address *)malloc(B*sizeof(struct Address));

    while(fgets(buff,255,f) != NULL && i == 1){
            char name[] = "abababababababababababa";
            sscanf(buff,"%d.%d.%d.%d %s\n",b,b+1,b+2,b+3,name);

            //creates a temporary struct storing the values that are read in
            struct Address addy = {b[0],b[1],b[2],b[3],*name};
        
            //sets each character of the name to the alias
            for(int i = 0; i < sizeof(name); i++){
                addy.alias[i] = ("%c",name[i]);
            }
            
            // stops at sentinal condition
            if(addy.val1 == 0 || addy.val2 == 0 || addy.val3 == 0 || addy.val4 == 0){
                i = 0;
            }else{

                //if address is bad
                if( checkAlias(addy.alias) == 0 
                || checkAddress(b[0]) == 0 
                || checkAddress(b[1]) == 0 
                || checkAddress(b[2]) == 0 
                || checkAddress(b[3]) == 0){
                    //adds the address to the list of bad addresses
                    bad[Bpos] = addy;
                    Bpos++;
                }else{
                    //adds the address to the list of good addresses
                    //sets the name of good addresses to upper-case
                    for(int i = 0; i < sizeof(addy.alias); i++){
                        addy.alias[i] = toupper(addy.alias[i]);
                    }
                    good[Gpos] = addy;
                    Gpos++;
                }
            }

        
    }
    
    //closes file
    fclose(f);

    //returns the count of Good and Bad Address locations
    static int a[2];
    a[0] = Gpos;
    a[1] = Bpos;
    return a;
    
}
/**
 * @brief creates 2 files returning the locality report and error report
 * 
 * @param g the number of Good addresses
 * @param b the number of Bad addresses
 * @param name the users name
 * @return int 
 */
int generateLocalityRpt(int g, int b, char name[]){
    char fileName[] = "222_Locality_Report";
    FILE *file;
    file = fopen(fileName,"w");

    //header for locality report
    fprintf(file,"%s%s",name,getDateAndTime());
    fprintf(file,"CS222 Network Locality Report\n");
    fprintf(file,"Addresses total: %d\n",g);

    //sets up 2d array to store unique ip pairs
    int pair[25][2];
    int pos = 0;

    //stores the first address into the list
    pair[0][0] = good[0].val1;
    pair[0][1] = good[0].val2;

    //for every address remaining in the Good Address list
    for(int i = 1; i < g; i++){
        //i represents each address location

        //bool flag
        int isIn = 0;

        //loops through the location within the 2d array of unique IP pairs
        for(int j = 0; j <= pos; j++){
            //j represents the stored locality

            //checks to see if the current IP Address is already inside the 2D array
            if(pair[j][0] == good[i].val1 && pair[j][1] == good[i].val2){

                //int flag represents a boolean
                isIn = 1;
                
            }
        }

        if(isIn == 0){
            //adds current IP Pair to Unique Pair list
            pair[pos][0] = good[i].val1;
            pair[pos][1] = good[i].val2;
            pos++;
        }  
    }

    fprintf(file,"Localities: %d\n",pos);

    //loops through the Unique IP pairs in the 2d int Array
    for(int i = 0; i < pos; i++){
        //header for each locality pair
        fprintf(file,"\n%d.%d\n",pair[i][0],pair[i][1]);

        //checks current pair against all Addresses in the Good List
        for(int j = 0; j < g; j++){
            if(pair[i][0] == good[j].val1 && pair[i][1] == good[j].val2){
                fprintf(file,"%s\n",good[j].alias);
            }
        }
    }

    //closes file
    fclose(file);

    strcpy(fileName,"CS222_Error_Report");
    FILE *f;
    f = fopen(fileName,"w");
    //header for error report
    fprintf(f,"%s%s",name,getDateAndTime());
    fprintf(f,"CS222 Error Report:\n\n");

    //prints each Address in the Bad List
    for(int i = 0; i < b; i++){
        fprintf(file,"%d.%d.%d.%d\t%s\n",bad[i].val1,bad[i].val2,bad[i].val3,bad[i].val4,bad[i].alias);
    }

    //closes the file
    fclose(f);
    return 1;
}

/**
 * @brief checls to see if a address element of a struct Address is within the bounds [0,255]
 * 
 * @param a - an integer address element
 * @return int 
 */
int checkAddress(int a){
    if(a<0 || a >255){
        return 0;
    }
    return 1;
}

/**
 * @brief Check if the Alias of a struct Address is less than 10 in length
 * 
 * @param a and character array - the alias of an adress
 * @return int 
 */
int checkAlias(char a[]){
    if(strlen(a)>10){
        return 0;
    }
    return 1;
}

/**
 * @brief Get the Date And Time object
 * 
 * @return char* 
 */
char *getDateAndTime(){
    
    time_t t;
    time(&t);
    return ctime(&t);
    
}