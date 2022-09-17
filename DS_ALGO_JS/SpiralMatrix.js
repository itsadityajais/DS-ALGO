let a=[
       [1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]
    ];
let i,j,count=0,r=0,c=0,row=3,col=3;
console.log(a);
while(count<=16){

    //take i-> which is changing 
    //when printing 1-4 row remains same and coulum changes from c1-c4
    for(i=c;i<=col;i++){
        console.log(a[r][i]);
    }
    r++;
    count++;

    for(i=r;i<=row;i++){
        console.log(a[i][col]);
    }
    col--;
    count++;

    for(i=col;i>=c;i--){
        console.log(a[row][i]);
    }
    row--;
    count++;

    for(i=row;i>=r;i--){
        console.log(a[i][c]);
    }
    c++;
    count++;

}
