def has_33(nums):
    # Проходим по списку до предпоследнего элемента
    for i in range(len(nums) - 1):
        # Если текущий и следующий элементы равны 3
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Примеры вызова функции
print(has_33([1, 3, 3]))      # True
print(has_33([1, 3, 1, 3]))   # False
print(has_33([3, 1, 3]))      # False
