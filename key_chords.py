#半音階（＃基準）
CHROMATIC = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

#bを＃に変換
ENHARMONIC_FLAT_TO_SHARP = {"Db":"C#","Eb":"D#","Gb":"F#","Ab":"G#","Bb":"A#",}

MAJOR_INTERVALS = [2,2,1,2,2,2,1]

ROMAN_NUMERALS = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]

def normalize_key(key:str) -> str:
    """キー名をきれいにして、#表記に統一して返す"""
    key = key.strip().capitalize()
    if len(key) > 1:
        root = key[0].upper()
        accidental = key[1]
        key = root + accidental

        if key in ENHARMONIC_FLAT_TO_SHARP:
         key = ENHARMONIC_FLAT_TO_SHARP[key]
        if key not in CHROMATIC:
          raise ValueError(f"未知のキーです: {key}")

    return key 

def build_major_scale(root:str) -> list[str]:
        """ルートからメジャースケールを作る"""
        if root not in CHROMATIC:
            raise ValueError(f"未知のキーです: {root}")
        
        scale = [root]
        idx = CHROMATIC.index(root)

        for step in MAJOR_INTERVALS[:-1]:
            idx = (idx + step) % 12
            scale.append(CHROMATIC[idx])

        return scale
        
def build_triad(scale:list[str],degree:int) -> list[str]:
            """メジャースケールから度数に対応するトライアドを返す
    degree: 0〜6 (I〜vii°)"""
            #root + 3rd + 5th
            root = scale[degree]
            third = scale[(degree + 2) % 7]
            fifth = scale[(degree + 4) % 7]
            return[root,third,fifth]
        
        
def main():
    print("=== Key Helper ver0.1 ===")
    print("例: C, G, F#, Bb など\n")

    key_input = input("キーを入力してください: ")

    try:
        root = normalize_key(key_input)
        scale = build_major_scale(root)
    except ValueError as e:
        print(e)
        return

    print(f"\nKey: {root}")
    print("\nScale:")
    print("  " + " ".join(scale))

    print("\nDiatonic triads:")
    for i, roman in enumerate(ROMAN_NUMERALS):
        triad = build_triad(scale, i)
        print(f"  {roman:<4}: {'  '.join(triad)}")


if __name__ == "__main__":
  main()  