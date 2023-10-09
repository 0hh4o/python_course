def recover_secret(triplets):
    # 创建一个字典，用于存储每个字母的前一个字母
    prev_letters = {}

    # 构建字母关系
    for triplet in triplets:
        for i in range(2):
            if triplet[i] not in prev_letters:
                prev_letters[triplet[i]] = set()
            if triplet[i+1] not in prev_letters:
                prev_letters[triplet[i+1]] = set()
            prev_letters[triplet[i+1]].add(triplet[i])

    # 恢复原始字符串
    result = []
    while prev_letters:
        # 找到没有前一个字母的字母
        current_letter = next(letter for letter, prevs in prev_letters.items() if len(prevs) == 0)
        result.append(current_letter)
        del prev_letters[current_letter]

        # 更新其他字母的前一个字母集合
        for letter, prevs in prev_letters.items():
            if current_letter in prevs:
                prevs.remove(current_letter)
                
    result.reverse()
    return ''.join(result[::-1])

# 示例用法
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

secret_string = recover_secret(triplets)
print(secret_string)  # 输出：whatisup
