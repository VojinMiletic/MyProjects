#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct human{
    int day;
    int month;
    int year;
    char Firstname[31];
    char Lastname[31];
    float weight;
    float high;
}human;

typedef struct humans{
    human h;
    struct humans *next;
}humans;

humans* createList(int firstYear, int secondYear){
    humans *head=NULL,*tmp, *tail=NULL;
    human debeli;
    FILE *file = fopen("patients.txt", "r");
    if(!file){
        printf("DAT_GRESKA");
        exit(0);
    }
    char *format = "%d-%d-%d %[^ ] %[^ ] %f %f\n";
    while(fscanf(file, format, &debeli.day,&debeli.month,&debeli.year,debeli.Firstname,debeli.Lastname,&debeli.weight,&debeli.high)==7){
        if(debeli.year < firstYear || debeli.year > secondYear) continue;
        else {
            tmp = malloc(sizeof(humans));
            tmp->next = NULL;
            tmp->h = debeli;

            if(!head) head = tmp;
            else tail -> next = tmp;
            tail = tmp;
        }
    }
    fclose(file);
    return head;
}

float BMI(human covek){
    float bmi = covek.weight / ((covek.high/100) * (covek.high/100));
    return bmi;
}
int criterium(human h1, human h2){
    if(BMI(h1) > BMI(h2)) return 1;
    else if(BMI(h1) < BMI(h2)) return -1;
    else{
        if(h1.year < h2.year) return 1;
        else if(h1.year > h2.year) return -1;
        else{
            if(h1.month < h2.month) return 1;
            else if(h1.month > h2.month) return -1;
            else{
                if(h1.day < h2.day) return 1;
                else if(h1.day > h2.day) return -1;
            }
        }
    }
    return 0;
}
void sortList(humans *head){
    human tmp;
    for(humans *p1 = head; p1; p1 = p1->next){
        for(humans *p2 = p1; p2; p2 = p2->next){
            if(criterium(p1->h,p2->h) == -1){
                tmp = p1->h;
                p1->h = p2->h;
                p2->h = tmp;
            }
            else continue;
        }
    }
}
void write(humans *head, int value){
    FILE *file = fopen("high_bmi.txt","w");
    while(value && head){
        human covek = head->h;
        float bmi = BMI(covek);
        fprintf(file,head->h.day < 10 ? "0%d-" : "%d-", head->h.day  );
        fprintf(file,head->h.month < 10 ? "0%d-" : "%d-", head->h.month  );
        fprintf(file,"%d %s %s %.2f\n",
                head->h.year, head->h.Firstname,head->h.Lastname,bmi);
        head = head->next;
        value--;
    }
    fclose(file);
}
void freeList(humans *head){
    humans *old;
    while(head){
        old = head;
        head = head->next;
        free(old);
    }
}

int main(){
    int startYear, stopYear,N;
    scanf("%d-%d", &startYear, &stopYear);
    scanf("%d", &N);
    humans *lista = createList(startYear, stopYear);
    sortList(lista);
    write(lista, N);
    freeList(lista);

    return 0;
}