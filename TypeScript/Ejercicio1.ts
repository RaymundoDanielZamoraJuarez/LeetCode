function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    
    function compareNumbers(a: number, b: number): number {
    return a - b;
    }

    const nums3: number[] = nums1.concat(nums2);
    const length: number = nums3.length;

    nums3.sort(compareNumbers);

    if(length % 2 === 0){
        const mid1: number = nums3[Math.floor(length/2 - 1)];
        const mid2: number = nums3[Math.floor(length/2)];
        return (mid1 + mid2)/2;
    } else {
        const mid: number = Math.floor(length/2);
        return nums3[mid];    
    }

};