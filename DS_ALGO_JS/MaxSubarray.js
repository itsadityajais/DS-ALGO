function maxSubArraySum(a,n) {
    let max_so_far=a[0],
    curr_max=0,
    start=0,end=0,s=0;

    for(i=0;i<n;i++){
        curr_max=curr_max+a[i];
        if(max_so_far<curr_max) {
           max_so_far=curr_max;

            start=s;
            end=i;
        }
        if(curr_max<0){
           curr_max=0;
            s=i+1;
        }
    }
    console.log("Maximum contiguous sum is "+max_so_far);
    console.log("From index "+start);
    console.log("To index "+end);
}
    let a=[-2,-3,4,-1,-2,1,5,-3,10,5,-2,-4,1];
    let n=a.length;
    maxSubArraySum(a, n);
   