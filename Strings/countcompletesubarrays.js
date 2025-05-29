var countCompleteSubarrays = function(nums) {
    let hash_map = {};
    let distinct=new Set(nums).size
    let end=0,count=0;
    for(let left=0;left<nums.length;left++){
          if(left>0){
             let remove=nums[left-1];
             hash_map[remove]-=1
             if(hash_map[remove]===0){
                 delete hash_map[remove]
             }

          }
          
          while(end<nums.length && Object.keys(hash_map).length < distinct){

          
                     hash_map[nums[end]]+=hash_map.get(nums[end],0)+1
                    console.log(hash_map,"-",end)
                    end+=1;
          }

          if(Object.keys(hash_map).length === distinct){
              count+=nums.length-end+1
          }

    }

    return count
};

console.log(countCompleteSubarrays([1,3,1,2,2]))


let hash_map={}
