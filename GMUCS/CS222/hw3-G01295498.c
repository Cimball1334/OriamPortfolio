/*
 * HW3-G01295498.c - Third Homework Assignment for CS222
 * 
 * Author: Craig Kimball
 * Date: 3/7/2022
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


//Method Prototypes
char *getDateAndTime();
int getInteger();
void saveToFile(char name[], int val, char buffer[]);
void decimalToBinary(int decValue, char binString[]);
void decimalToHex(int decValue, char hexString[]);
void decimalToOct(int decValue, char octString[]);

int main() {
   printf("Enter your name:");
   char name[21];
   char buffer[21];
   fgets(name,sizeof(name),stdin);
    // flag varaible to control the loop
   int flag = 1;
    //looping structure of the main method, allows for the user to continue entering integers until they chose not to
   while(flag == 1){

        
        int val = getInteger();

        if(val == -1){
            printf("Goodbye!");
            flag = -1;

        }
        else
        {
            printf("Decimal: %d \n", val);

            decimalToHex(val,buffer);  
            printf("Hexidecimal: %s \n",buffer);

            decimalToOct(val,buffer);
            printf("Octal: %s \n", buffer);

            decimalToBinary(val,buffer);
            printf("Binary: %s \n", buffer);

            // call to save method, allows for a cleaner loop structure of the saving process
            saveToFile(name,val,buffer);
            
        }
   } 
}

//unix method to get the current date and time of the system
///used in file saving
char *getDateAndTime(){
    
    time_t t;
    time(&t);
    return ctime(&t);
    
}

//method used to save the current scenario to a file using the file output stream
void saveToFile(char name[], int val, char buffer[]){   
    fflush(stdin);
    fflush(stdin);
    printf("Save to a file? (y/n):");
    char answer;
    scanf("%c",&answer);
    //picks up the new line character left over when the user hits enter
    getchar();
    
    if(answer == 'y'){
        fflush(stdin);

        printf("Enter file name:");
        char fileName[30];
        fgets(fileName,sizeof(fileName),stdin);

        FILE *f;
        //opens file with that filename the user entered with write privellages 
        f= fopen(fileName,"w");

        //writing information to the text file using fprintf
        fprintf(f,"%sToday's Date: %s\n",name,getDateAndTime());
        fprintf(f,"Decimal: %d \n", val);

        decimalToHex(val,buffer);  
        fprintf(f,"Hexidecimal: %s \n",buffer);

        decimalToOct(val,buffer);
        fprintf(f,"Octal: %s \n", buffer);

        decimalToBinary(val,buffer);
        fprintf(f,"Binary: %s \n", buffer);

        fclose(f);

        printf("File Saved.\n");

        }else if(answer != 'n' && answer != 'y'){
            //logic statement to see if the user entered and invalid character:
            printf("Error: Invalid Character\n");
            return saveToFile(name,val,buffer);
        }    
        //no logic is needed if the user enters "n" becuase no action is needed if they did. 

}

int getInteger(){
    fflush(stdin);
    printf("Enter an Integer[1-1,000,000] or type x to exit:");
    char input[21];
    fgets(input, sizeof(input),stdin);
    //this logic checks if the user entered a number at all
    if(atoi("x") == atoi(input)){
        return -1;
    }else{
        if(atoi(input) > 1000000 || atoi(input) < 1){
            printf("Error: %s is out of range \n",input);
            return getInteger();
        }
        return atoi(input);
    }
}
//converts a decimal number to a binary value
void decimalToBinary(int decValue, char binString[]){
    char placeHolder[21];
    int i;
    for(i=0; decValue>0;i++){
        //standard binary conversion using modulus 2 to find remainder and dividing by 2 to decrease the entered value
        // +'0' changes the integer to a character
        placeHolder[i] = decValue%2 +'0';
        decValue /= 2;
    }
    
    //flip string around to assign to binString
    int current = 0;
    for(i = i-1;i>=0; i--){
        binString[current] = placeHolder[i];
        current++;
    }
    binString[current] = '\0';

    // puts(binString);
}

void decimalToHex(int decValue, char hexString[]){
    char placeHolder[21];
    int i;
    for(i=0; decValue>0;i++){
        int temp = decValue %16;

        if(temp <10){
            temp += 48;
        }else{
            temp += 55;
        }

        placeHolder[i] = temp;
        decValue /= 16;
    }

    //flip string around to assign to binString
    int current = 0;
    for(i = i-1;i>=0; i--){
        hexString[current] = placeHolder[i];
        current++;
    }
    hexString[current] = '\0';
    // puts(hexString);
}

void decimalToOct(int decValue, char octString[]){
    char placeHolder[21];
    int i;
    //this oporates the same way the binary conversion works
    //modulus 8 allows to see if the value at that power has any factors of 8
    // dividing by 8 decreases the entered value to the next power of 8
    for(i=0; decValue>0;i++){
        placeHolder[i] = decValue%8 +'0';
        decValue /= 8;
    }

    //flip string around to assign to binString
    int current = 0;
    for(i = i-1;i>=0; i--){
        octString[current] = placeHolder[i];
        current++;
    }
    octString[current] = '\0';
    // puts(octString);

}
