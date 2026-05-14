def twoSum(nums,target):
    for key in range(len(nums)):
            for x in range(len(nums)):
                if key == x:
                    pass
                else:
                    if nums[key] + nums[x] == target:
                        return [key,x]