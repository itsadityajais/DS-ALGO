let a=[
       [1,2,3],
       [4,5,6],
       [7,8,9]
    ];
let i,j,k,temp;

// for(let x=0;x<3;x++){
//     console.log(a[x]);
// }

//SWAP
for(i=0;i<3;i++){
    for(j=i;j<3;j++){
        temp=a[i][j];
        a[i][j]=a[j][i];
        a[j][i]=temp;
    }
}
// console.log(a);

//REVERSE
for(i=0;i<3;i++){
    k=2;
    for(j=0;j<k;j++){
        temp=a[i][j];
        a[i][j]=a[i][k];
        a[i][k]=temp;
        k--;
    }
}
console.log("90 Degree Rotation of Matrix a is: ")
for(let x=0;x<3;x++){
    console.log(a[x]);
}
