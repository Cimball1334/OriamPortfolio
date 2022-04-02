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

struct Address{
    int val1;
    int val2;
    int val3;
    int val4;
    char *alias;
};

char *getDateAndTime();
void Bubble_sort();
void Generate_Alias_list();
void Read_Data_File(struct Address list[]);
void Save_File();

int main(){

    struct Address Addresses[100];

    Read_Data_File(Addresses);
    
    for(int i = 0; i<100; i++){
        // printf("Address %d: %d.%d.%d.%d Alias %s\n",i,Addresses[i].val1,Addresses[i].val2,Addresses[i].val3,Addresses[i].val4,Addresses[i].alias);
        printf("Alias: %s \n",Addresses[i].alias);
        // if(Addresses[i+1].alias == NULL){
        //     i = 101;
        // }
    }

}

//unix method to get the current date and time of the system
///used in file saving
char *getDateAndTime(){
    
    time_t t;
    time(&t);
    return ctime(&t);
    
}

void Bubble_sort(){

}

void Generate_Alias_list(char buff[]){

    
}

void Read_Data_File(struct Address list[]){
    
    FILE *f;
    f = fopen("CS222_Inet.txt","r");

    int pos = 0;
    char buff[255];
    int b[4] = {0};
    

    
    while(fgets(buff,255,f)!=NULL){
        char name[32] = "";
        sscanf(buff,"%d.%d.%d.%d %s\n",b,b+1,b+2,b+3,name);
    
        // printf("%d %d %d %d",b[0],b[1],b[2],b[3]);
        struct Address addy;
        // printf("%s\n",name);
        list[pos].alias = name;
        list[pos].val1 = b[0];
        list[pos].val2 = b[1];
        list[pos].val3 = b[2];
        list[pos].val4 = b[3];

        // printf("%d %d %d %d %s \n",addy.val1,addy.val2,addy.val3,addy.val4,addy.alias);

        //at this point I have a addy variable that contains the correct values
        //now just need to return it to the big list
        
        

    }

    
    
}