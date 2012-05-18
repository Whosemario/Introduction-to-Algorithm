#include<iostream>
using namespace std;

#define MAXN 1002
int stack[MAXN][3];
int arr[10005];

void Output(int * array , int size){
    for(int i=0;i<size;i++)
      cout<<array[i]<<" ";
    puts("");
}

void merge(int* array,int left,int mid,int right){
     int i=left,j=mid+1;
     int k=0;
     while(i<=mid&&j<=right){
         if(array[i]<=array[j])
            arr[k++]=array[i++];
         else
            arr[k++]=array[j++];
     }
     while(i<=mid){arr[k++]=array[i++];}
     while(j<=right){arr[k++]=array[j++];}
     for(i=0,j=left;i<k;i++,j++){
         array[j] = arr[i];
     }
}

void mergeSort(int* array, int left, int right){
     int size = 0;
     stack[size][0] = left;
     stack[size][1] = right;
     stack[size][2] = 0;
     size++;
     while(size){
         int l = stack[size-1][0];
         int r = stack[size-1][1];
         if(stack[size-1][2] == 0){
            stack[size-1][2] = 1;
            if(r-l==1){
                if(array[l]>array[r]){
                   int tmp = array[l];
                   array[l]=array[r];
                   array[r]=tmp;
                }
                size--;
            }
            else if(r-l==0){size--;}
            else{
                int m = (l+r)/2;
                stack[size][0]=l;
                stack[size][1]=m;
                stack[size][2]=0;
                size++;
                stack[size][0]=m+1;
                stack[size][1]=r;
                stack[size][2]=0;
                size++;
            }
         }
         else{
            merge(array,l,(l+r)/2,r);
            size--;
         }
     }
}

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    
    int n;
    cin>>n;
    int input[10005];
    int i;
    for(i=0;i<n;i++)
      cin>>input[i];
    mergeSort(input,0,n-1);
    Output(input,n);
}
