#include <stdio.h>
#include <stdlib.h>

int** unos( int igraci, int karte )
{
    int **podaci;
    podaci  = malloc(igraci * sizeof(int*));
    if(podaci==NULL)
    {
        exit(-1);
    }
    for(int i=0; i<igraci; i++ )
    {
        podaci[i] = malloc((karte*2)*sizeof(int));
        if(podaci[i]==NULL)
            exit(-1);
        for(int j=0; j<karte*2; j++){
            scanf("%d", &podaci[i][j]);
        }
    }
    return podaci;
}
int provera(int **matrica, int vrste, int kolone )
{
    for(int i=0; i<vrste; i++)
    {
        for(int j=0, k=1; j<kolone && k<kolone; j+=2 , k+=2)
        {
            if(matrica[i][j]<2 || matrica[i][j]>14) {
                return -1;
            }
            if(matrica[i][k]<1 || matrica[i][k]>4) {
                return -1;
            }
        }
    }
    return 0;
}
void ispis(int **matrica, int vrste, int kolone)
{
    for(int i=0; i<vrste; i++)
    {
        for(int j=0; j<kolone; j++)
        {
            printf(j!=kolone-1 ? "%d " : "%d", matrica[i][j]);
        }
        putchar('\n');
    }
}
void sortArr(int *niz, int duzina)
{
    int temp1, temp2;
    for(int i=0; i<duzina-1; i+=2)
    {
        for(int j=i+2; j<duzina; j+=2)
        {
            if(niz[i]*niz[i+1]<=niz[j]*niz[j+1])
            {
                temp1=niz[i]; temp2=niz[i+1]; niz[i]=niz[j]; niz[i+1]=niz[j+1]; niz[j]=temp1; niz[j+1]=temp2;
            }else
                continue;
        }
    }
}
void sortMat(int **matrica, int vrste, int kolone)
{
    for(int i=0; i<vrste; i++)
    {
        sortArr(matrica[i], kolone);
    }
}
void igra(int**matrica, int vrste, int kolone)
{
    int *rezultati= calloc(vrste, sizeof(int));
    if(rezultati==NULL)
    {
        exit(-1);
    }
    for(int j=0;j<kolone; j+=2)
    {
        int poeni=0, max=0,poeniIgraca , *krugIgre, brojac=0;
        krugIgre= malloc(vrste*sizeof(int));
        if(krugIgre==NULL)
            exit(-1);

        for(int i=0; i<vrste; i++)
        {
            if(matrica[i][j]*matrica[i][j+1] > max) {
                max = matrica[i][j] * matrica[i][j + 1];
            }
        }
        for(int i=0; i<vrste; i++)
        {
            poeni+=matrica[i][j]*matrica[i][j+1];
            if(matrica[i][j]*matrica[i][j+1] == max) {
                krugIgre[brojac++]=i;
            }
        }
        poeniIgraca=poeni/brojac;
        for(int k=0; k<brojac; k++)
        {
            rezultati[krugIgre[k]]+=poeniIgraca;
            printf("%d ", krugIgre[k]);
        }
        printf("%d %d", max, poeniIgraca);
        putchar('\n');
        free(krugIgre);
    }
    int pobednik=0, brojpoenaPobednika=0;
    for(int k=0; k<vrste; k++)
    {
        if(rezultati[k]>brojpoenaPobednika)
        {
            brojpoenaPobednika=rezultati[k];
            pobednik=k;
        }
    }
    for(int k=0; k<vrste; k++)
    {
        printf(k!=vrste-1 ? "%d " : "%d", rezultati[k]);
    }
    putchar('\n');
    printf("%d %d", pobednik, brojpoenaPobednika);
    free(rezultati);
}

void oslobodi(int **matrica, int vrste, int kolone)
{
    for(int i=0; i<vrste; i++)
    {
        free(matrica[i]);
    }
    free(matrica);

}

int main()
{
    int brojIgraca, brojKarata;
    int **matricaPodataka;

    scanf("%d %d", &brojIgraca, &brojKarata);
    if(brojIgraca<=0 || brojKarata<=0 || brojKarata>(52/brojIgraca) || brojIgraca>52)
        return 0;

    matricaPodataka = unos(brojIgraca, brojKarata);

    if(provera(matricaPodataka, brojIgraca, brojKarata*2)==-1)
    {
        printf("GRESKA");
        return 0;
    }
    ispis(matricaPodataka, brojIgraca, brojKarata*2);
    sortMat(matricaPodataka, brojIgraca, brojKarata*2);
    igra(matricaPodataka,brojIgraca, brojKarata*2);
    oslobodi(matricaPodataka, brojIgraca, brojKarata*2);

    return 0;
}
