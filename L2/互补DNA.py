def DNA_strand(dna):
    """
    获取DNA序列的互补序列
    :param dna: 输入的DNA序列
    :return: 互补的DNA序列
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in dna])

# 测试用例
print(DNA_strand("ATTGC"))  # 输出 "TAACG"
print(DNA_strand("AAAA"))   # 输出 "TTTT"
print(DNA_strand("ATCGT"))  # 输出 "TAGCA"
