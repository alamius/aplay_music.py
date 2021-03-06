
self_made_1 = [
    ("self_made_1", 4),
    [0, 1, 5],
    [0, 5, 8],
    [0, 5, 7],
    [0, 5, 9],
    #
    [-2, 1, 5, 10],
    # [-2, 1, 8],
    [-1, 5, 8, 11],
    [5, 8, 12],
    [5, 8, 12],
    #
    [4, 6, 9],
    [2, 6, 11],
    [3, 7, 10, 15],
    [7, 12, 15, 19],
    #
    [5, 9, 14, 17, 21],
    [4, 9, 13, 16, 21],
    [4, 11, 13, 16, 23],
    [1, 4, 11, 13, 19, 23],
    #
    [0, 3, 7, 12, 15, 19, 24],
    [0, 3, 7, 12, 15, 19, 24],
    [0, 3, 7, 12, 15, 19, 24],
    [0, 3, 7, 12, 15, 19, 24],
]
# ]+flatten([
#     #
#     [[5, 9, 14, 17, 21]]+
#     [[4, 9, 13, 16, 21]]+
#     [[4, 11, 13, 16, 23]]+
#     [[1, 4, 11, 13, 19, 23]]+
#     #
#     [[0+a, 3+a, 7+a, 12+a]]+[[0]]
#         for a in [
#             k for k in range(24, 11, -1)
#         ]
# ])

self_made_2_basis = [
    ("self_made_2_basis", 1),
    [0],
    [3, 0],
    [4, 0],
    [2],
    [8],
    [7],
    [5, 8],
    [1, 8],
    [11, 5],
    [9, 2],
    [6, 11],
    [10],
]

L = len(self_made_2_basis)-1
self_made_2 = (
    [("self_made_2", 1)]
    +self_made_2_basis[1:4]
    +[
        self_made_2_basis[1+(3+k)%L]
        +self_made_2_basis[1+k%L]
    for k in range(L)]
    +[
        self_made_2_basis[1+(3+k)%L]
        +self_made_2_basis[1+k%L]
        +[t+12 for t in self_made_2_basis[1+(3+k)%L]]
        +[t+12 for t in self_made_2_basis[1+k%L]]
    for k in range(L)]
)

self_made_3 = [
    ("self_made_3", 2),
    [-24, 0, 5, 12],
    [-12, 0, 5, 12],
    #
    [-3, 1, 6, 10],
    [-2, 1, 6, 10],
    #
    [-3, 2, 6, 9],
    [0, 3, 7, 7],
    #
    [2, 5, 5, 10],
    [3, 3, 7, 12],
    #
    [5, 1, 10, 13],
    [5, 1, 10, 17],
    #
    [7, 0, 12, 24],
    [7, 0, 12, 36],
]

clapping_1_base_1 = [3, 0, 3, 0, 0, 3, 0]
clapping_1_base_2 = [0, 7, 0, 0, 7, 0, 7]

clapping_1 = (
    [("clapping_1", 7)]
    +[[
        clapping_1_base_1[k%7], clapping_1_base_2[(k+d//2)%7]
        # [k%7, (k+d)%7]
    ] for d in range(0, -9, -1) for k in range(0, 8)]
)

clapping_2 = [ #just the pure combinations of [3, 7, 10, 12] can be precesssed be precessed by adding the arg "note_by_note"
    ("clapping_2", 1),
    [],
    [3],
    [7],
    [3, 7],
    [10],
    [3, 10],
    [7, 10],
    [3, 7, 10],
    [12],
    [3, 12],
    [7, 12],
    [3, 7, 12],
    [10, 12],
    [3, 10, 12],
    [7, 10, 12],
    [3, 7, 10, 12],
]

minimal_1_base_1 = [0, 4, 7, 8, 12, 7, 4]
minimal_1_base_2 = [-3, 0, 4, 7, 8, 4, 0]
minimal_1 = (
    [("minimal_1", 14)]
    +[[
        minimal_1_base_2[k//4%5]-12,
        minimal_1_base_2[(k+s)//2%5],
        minimal_1_base_1[k//2%5],
        minimal_1_base_1[(k+1)%5]+12,
    ] for s in range(0, 28) for k in range(0, 7)]
)

King_of_Thule = (
    [("König_von_Thule", 8)]
    +2*[[-5]]
    #
    +4*[[0]]
    +2*[[0]]
    +3*[[-5]]
    +1*[[-5]]
    +2*[[-5]]
    #
    +6*[[-4]]
    +4*[[-9]]
    +2*[[-9]]
    #
    +4*[[-7]]
    +2*[[-5]]
    +4*[[-4]]
    +2*[[-7]]
    #
    +8*[[-5]]
    +2*[[]]
    +2*[[-5]]
    #
    +4*[[0]]
    +2*[[0]]
    +4*[[-2]]
    +2*[[-2]]
    #
    +6*[[-9]]
    +4*[[-7]]
    +1*[[-7]]
    +1*[[-7]]
    #
    +4*[[-5]]
    +2*[[-4]]
    +4*[[-7]]
    +2*[[-5]]
    #
    +10*[[-12]]
)

# here: smallest unit of time: 1/8 note
# 1/2 note = 4*[[0, 3, 7]]
Scarborough_Fair = (
    [("Scarborough_Fair", 6)]
    +4*[[0, 0, 0]]
    +2*[[0, 0, 0]]
    #
    +4*[[7, 3, 0]]
    +2*[[7, 0, -5]]
    #
    +3*[[2, 2, -5]]
    +1*[[3, 0, -4]]
    +2*[[2, -2, -7]]
    #
    +6*[[0, -5, -9]]
    ##
    +2*[[0, -5, -9]]
    +2*[[7, 3, -2]]
    +2*[[10, 3, -5]]
    #
    +4*[[12, 8, -9]]
    +2*[[10, 7, -9]]
    #
    +2*[[7, 3, -11]]
    +2*[[9, 5, -12]]
    +2*[[5, 0, -12]]
    #
    +6*[[7, 0, -12]]
    ##
    +4*[[7, 0, -12]]
    +2*[[12, 3, -16]]
    #
    +4*[[12, 3, -16]]
    +2*[[12, 3, -16]]
    #
    +4*[[10, 3, -14]]
    +2*[[7, 3, -14]]
    #
    +3*[[7, -2, -9]]
    +1*[[5, -2, -7]]
    +2*[[3, -2, -5]]
    #
    +1*[[2, -3, -3]]
    +1*[[2, -7, -3]]
    +4*[[-2, -7, -2]]
    ##
    +4*[[-2, -7, -2]]
    +2*[[-2, -7, -14]]
    #
    +4*[[0, -5, -12]]
    +2*[[7, 0, -9]]
    #
    +4*[[5, 0, -7]]
    +2*[[3, -2, -5]]
    #
    +2*[[2, -3, -3]]
    +2*[[0, -7, 0]]
    +2*[[-2, -7, 2]]
    #
    +6*[[0, -5, 3]]
)
Scarborough_Fair = [Scarborough_Fair[0]]+[
    [chord[0]+12]+chord+[chord[2]-12]
    for chord in Scarborough_Fair[1:]
]
