#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Address{int val1; int val2; int val3; int val4; char alias[25];};

int Read_Data_File(struct Address lst[]);
void Bubble_sort(struct Address lst[], int stop, char d);
void Generare_Alias_List(char name[], int rows, struct Address lst[]);

char *getDateAndTime();
int toupper(int ch);
int strcmp (const char* str1, const char* str2);



int main(){

    printf("What is your name?\n");
    char name[30];
    fgets(name,sizeof(name),stdin);
    name[strlen(name)-1] = '\0';

    printf("Ascending or Descending order? A/D\n");
    char direction;
    scanf("%c",&direction);

    struct Address list[100];
    int rows = Read_Data_File(list);
    
    Bubble_sort(list,rows,direction);
    Generare_Alias_List(name,rows,list);

    // for(int i = 0; i < rows; i++){
    //     printf("%s\n",list[i].alias);
    // }

}

int Read_Data_File(struct Address lst[]){

    FILE *file;
    file = fopen("CS222_Inet.txt","r");

    char buffer[100];
    int rows = 0;
    //array for storing ip values
    int ip[4] = {0};

    while(fgets(buffer,100,file) != NULL){
        char name[30];
        
        sscanf(buffer,"%d.%d.%d.%d %s\n", ip, ip+1, ip+2, ip+3, name);
        struct Address address = {ip[0],ip[1],ip[2],ip[3],*name};
        strcpy(address.alias,name);
          
        if(address.val3 == 0){
            return rows;
        }else{
            lst[rows] = address;
            rows++;
        }

    }
    return rows;
}

void Bubble_sort(struct Address lst[], int stop, char dir){
    
    int i, j;
    int d = toupper(dir);
    for (i = 0; i < stop - 1; i++){
        for (j = 0; j < stop - i - 1; j++){
            if(d == 65){
                if(strcmp(lst[j].alias,lst[j+1].alias) > 0){
                    //swap j and j+1
                    struct Address temp = lst[j];
                    lst[j] = lst[j+1];
                    lst[j+1] = temp;
                }
            }else{
                
                if(strcmp(lst[j].alias,lst[j+1].alias) < 0){
                    //swap j and j+1
                    struct Address temp = lst[j];
                    lst[j] = lst[j+1];
                    lst[j+1] = temp;
                }
            }
        }  
    }
}

void Generare_Alias_List(char name[], int rows, struct Address lst[]){

    FILE *file;
    file = fopen("222_Alias_List","w");

    fprintf(file,"%s ",name);
    fprintf(file,"%s",getDateAndTime());
    fprintf(file, "CS222 Network Alias Listing\n");

    for(int i = 0; i < rows; i++){
         fprintf(file,"%s\t\t%d.%d.%d.%d\n",lst[i].alias,lst[i].val1,lst[i].val2,lst[i].val3,lst[i].val4);
    }

}

char *getDateAndTime(){
    time_t t;
    time(&t);
    return ctime(&t);
}
