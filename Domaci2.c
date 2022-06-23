#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_EMAIL_ADRESS_LEN 321 //PO STANDARDU MAKSIMALNA DUZINA EMAIL ADRESE JE 320 KARAKTERA
#define MAX_DATE_LEN 11          
//PRAVIMO STRUKTURU PROGRAMER KOJA ČUVA PODATKE OD INTERESA O PROGRAMERU
typedef struct programer{
    char email[MAX_EMAIL_ADRESS_LEN];
    int lines;
}programer;
//PRAVIMO LISTU PROGRAMERI U KOJU ĆE BITI SMEŠTENI PODACI TIPA PROGRAMER
typedef struct prog{
    programer progr;
    struct prog* next;
}programeri;

//OVA FUNKCIJA ODREĐUJE DA LI SE PROGRAMER NALAZI LISTI
int inList(programeri *head, char* string){
    while(head){
        if(!strcmp(head->progr.email, string)) return 1;
        head = head->next;
    }
    return 0; //FUNKCIJA ĆE VRATITI 0 AKO PROGRAMER NIJE U LISTI
}
//KADA SE PROGRAMER NALAZI U LISTI(TO SMO ODREDILI POMOCU PREDHODNE FUNKCIJE) TREBA DA NADJEMO
//POZICIJU NA KOJOJ SE NALAZI I ONDA DA AŽURIRAMO LINIJE KODA
void find_and_increase(programeri *head, programeri *elem){
    while(head){
        if(!strcmp(head->progr.email, elem->progr.email)){
            head->progr.lines += elem->progr.lines;
        }
        head = head->next;
    }
}
//KRAJ BLOKA FUNKCIJA KOJE SU NAM REŠILE PROBLEM DUPLIKATA

//OVA FUNKCIJA PODATKE OD INTERESA IZ NAŠE DATOTEKE SMEŠTA U LISTU
programeri *create_list(){
    programeri *head=NULL ,*tail=NULL, *tmp;
    programer p;

    FILE *file = fopen("contribution.txt", "r");
    if(!file){
        printf("DAT_GRESKA");
        exit(0);
    }
    char garbage[MAX_DATE_LEN]; //DATUM NAM NIJE PODATAK OD INTERESA ZATO GA SMEŠTAMO U JEDNU PRIVREMENU PROMENLJIVU
    char *format = "%[^ ] %d %[^\n]\n"; //FORMAT KOJI ŽELIMO DA NAM "PROGUTA" FSCANF()
    while(fscanf(file, format, p.email, &p.lines,garbage)==3){
        tmp = malloc(sizeof(programeri)); 
        if(!tmp){
            printf("MEM_GRESKA");
            exit(-1);
        }
        tmp->progr = p;
        tmp->next = NULL;
        
        if(inList(head, tmp->progr.email)){
            find_and_increase(head, tmp);
        }
        else{
            if(!head){
                head = tmp;
            }
            else tail->next = tmp;
            tail = tmp;
        }
        free(tmp);
    }
    fclose(file);
    return head;
}
//OVAJ BLOK FUNKCIJA NAM SORTIRA LISTU PREMA ZADATIM KRITERIJUMIMA

int check(programer p1, programer p2){   //OVA FUNKCIJA ĆE PROVERITI DA LI JE PRVI ELEMENT PO ZADATIM KRITERIJUMIMA VEĆI ILI MANJI
    if(p1.lines > p2.lines) return 1;  //PRVI PRITERIJUM JE BROJ LINIJA KODA
    else if(p1.lines < p2.lines) return -1;
    else{//DRUGI KRITERIJUM JE EMAIL ADRESA(U LEKSIKOGRAFSKOM SMISLU)
        if(strcmp(p1.email, p2.email) > 0) return 1;
        else if(strcmp(p1.email, p2.email) < 0) return -1;
    }
}
//GLAVNA FUNKCIJA ZA SORTIRANJE, POSLE NJENOG POZIVA ĆEMO IMATI SORTIRANU LISTU 
void sortList(programeri *head){
    for(programeri *a1 = head; a1; a1 = a1->next){
        for(programeri *a2 = a1; a2; a2 = a2->next){
            if(check(a1->progr, a2->progr) == -1){
                programer tmp = a1->progr;
                a1->progr = a2->progr;
                a2->progr = tmp;
            }
        }
    }
}// KRAJ BLOKA FUNKCIJA KOJE SORTIRAJU LISTU 

//FUNKCIJA KOJA UPISUJE PODATKE IZ LISTE U DATOTEKU
void write(programeri *head){
    FILE *file= fopen("result.txt", "w");
    if(!file){
        printf("DAT_GRESKA");
        exit(0);
    }
    while(head){
        fprintf(file, head->next!=NULL ? "%s %d\n" : "%s %d", head->progr.email, head->progr.lines);
        head = head->next;
    }
    fclose(file);
}
//FUNKCIJA KOJA OSLOBADJA LISTU
void deallocateList ( programeri *head ) {
    programeri *old;
    while(head){
        old = head;
        head = head->next;
        free(old);
    }
}
//GLAVNA FUNKCIJA GDE ĆEMO POZVATI SVE PRETHOSNO REALIZOVANE FUNKCIJE(NEKE DIREKTNO A NEKE INDIREKTNO)
int main(){
    programeri *lista = create_list();
    sortList(lista);
    write(lista);
    deallocateList (lista);
    
    return 0;
}