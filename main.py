def removeInterrogation(sheet):
    for letter in sheet:
        if letter == "?":
            sheet = sheet.replace(letter, "")
    return sheet

if "__main__" == __name__:
    sheet = """
    [6u] p s 0 e r [tu] p
[8osf] w t y [uosf]
[4ips] 8 q w e t
i t e
[6u] p s 0 e [ru] [tp] s
[8osf] w t y [uosf]
[4isg] 8 q w e t
i [ts] [ea]
[0ep] s p
[9wp] a p a o p a
[70o] a o
[ep] [ua] s [up] s d
[ef] u j u j k
[wj] [yh] h [yf] h f
[0d] r a r p
[eus] a p
[6up] 0 [eus] r [tup]
[5p] [ya] [9p] [wa] [es] [ra] p
[3uo] 7 [0ua] [7uo]
[6up] [0a] [eus] p [0us] d
[6pf] 0 [esj] [0sj]
[5k] [dj] [9h] [wj] [ef] [rh] f
[3d] 7 [0a] [7d] s a
[6p] 0 e p
[9pdG] e [ypdG] u [Ipdh] u
[9pdG] e y [pdG] h
[6sfj] 0 [esfj] r [tsfk]
[6l] k j 0 e j h
[9pdG] e [ypdG] u [Ipdh] u
[9pdG] e y [pd]
[6psf] 0 [ep] r [tpsf] [rd]
[6psf] 0 e [psf]
[2pd?IG] 6 [9pdIG] 0 [Qpdh] 0
[2pdIG] 6 9 [pIG] h
[??sfj] 3 [6sfj] 7 [8sfk]
[?l] k j 3 6 j
[4sfj] 8 q w e t
i [ts] [ea]
[6up] 0 [eus] r [tup]
[5p] [ya] [9p] [wa] [eo] [rp] a
[3uo] 7 [0ua] [7uo]
[6up] [0a] [eus] p [0us] d
[6pf] 0 [esj] [0sj]
[5k] [dj] [9h] [wh] [ef] [rh] f
[3d] 7 [0a] 7 o 7
[6up] 0 e
[6ps] 0 [esf] 0 [ps] 0
[5ad] [9ps] [wad] [9sf] [ad] [9ps]
[3oa] 7 [0ad] 7 [oa] 7
[6ps] [0oa] [eps] [0ad] [sf] 0
[6sf] 0 [ejl] 0 [jl] 0
[5jl] [9hk] [whk] [9j] h 9
[3d] 7 [0a] 7 o 7
[6up] 0 e l k
[upj] l j
[yoj] k j k h j k
[ruh] k h
[pj] [fk] l [fj] l z
[px] f b f b
[on] b [dv] v [dx] v x
[uz] a k a j
[pfl] k j

Anexos
    """
    print(removeInterrogation(sheet))
