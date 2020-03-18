import numpy as np

if __name__ == '__main__':
    vector = np.array([0, 1, 2])
    print(vector, vector.shape, vector[:3])

    # numpy配列, スライス
    matrix = np.array([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])
    print(matrix, matrix.shape, matrix[:2, 1:])

    # numpy配列同士の演算
    a1 = np.array([
        [1, 2],
        [3, 4]
    ])
    b1 = np.array([
        [5, 6],
        [7, 8]
    ])
    print(a1 + b1)
    print(a1 * b1)

    # ブロードキャスト (スライスの異なるnumpy配列の演算)
    c1 = np.array([1, 2])
    print(a1 + c1)

    # ブロードキャスト (スカラー値の演算)
    print(a1 + 10)
    print(a1 * 2)

    # ベクトルの内積 (a1[0] * b[0] + a1[1] * b[1] + a1[2] * b[2] = 32)
    a2 = np.array([1, 2, 3])
    b2 = np.array([4, 5, 6])
    print(np.dot(a2, b2))

    # 行列の積とベクトルの内積
    A = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    B = np.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])
    print(np.dot(A, B))

    C = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    D = np.array([9, 8, 7])
    print(np.dot(C, D))

    # maxとargmax
    arr = np.array([100, 10, 1000])
    print(np.max(arr), np.argmax(arr))

    arr2 = np.array([
        [0.1, 0.4, 0.3],
        [0.9, 0.1, 0.5],
        [0.3, 0.6, 0.1]
    ])
    print(np.argmax(arr2, axis=0)) # axis=0: 縦方向に走査する
    print(np.argmax(arr2, axis=1)) # axis=1: 横方向に走査する

    # 統計関数(np.sum) : 配列の要素の合計値
    print(np.sum(arr2)) # => 3.3000000000000003 (3.3でないのは浮動少数点数の計算誤差)

    # 統計関数(np.mean) : 配列の要素の平均値
    print(np.mean(arr2)) # => 0.3666666666666667

    # 指数関数
    print(np.exp(arr2))

    # 乱数
    print(np.random.rand())
    print(np.random.rand(3, 3))

    # 乱数(シードを固定する)
    np.random.seed(42)
    print(np.random.rand()) # => 0.3745401188473625 (同じ値)

    # numpy配列の初期化
    print(np.zeros((3, 2))) # 引数にはshapeを渡す
    print(np.ones((3, 2)))

    # numpy配列の結合


