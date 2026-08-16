import re
from pathlib import Path

def next_three_letters(ch: str) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    idx = letters.index(ch.lower())
    res = ''.join(letters[(idx + i + 1) % 26] for i in range(3))
    return res.upper() if ch.isupper() else res

def next_three_numbers(ch: str) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    idx = letters.index(ch.lower()) + 1  # 1-based
    nums = []
    for i in range(1, 4):
        n = (idx + i) % 26
        if n == 0:
            n = 26
        nums.append(str(n))
    return ''.join(nums)

def replace_targets(text: str, targets: str, mode: str = 'letters') -> str:
    """Replace any character in `targets` found in `text`.

    - If mode == 'letters': replace each target letter by the next 3 letters (preserve case).
    - If mode == 'numbers': replace each target letter by the next 3 numbers (based on alphabet index).
    """
    if not targets:
        return text
    pattern = '[' + re.escape(targets) + ']'

    def repl(m):
        ch = m.group()
        if not ch.isalpha():
            return ch
        if mode == 'letters':
            return next_three_letters(ch)
        if mode == 'numbers':
            return next_three_numbers(ch)
        raise ValueError("mode must be 'letters' or 'numbers'")

    return re.sub(pattern, repl, text, flags=re.IGNORECASE)


def main():
    data_dir = Path(__file__).parent.parent / 'data'
    dat_files = list(data_dir.glob('*.dat'))
    if not dat_files:
        print('No .dat found in', data_dir)
        return
    input_path = dat_files[0]
    with input_path.open('r', encoding='utf-8') as f:
        content = f.read()

    # Ejemplos de uso: ajustar según necesites
    content = replace_targets(content, 'MERCADO', mode='letters')
    content = replace_targets(content, 'Banco', mode='numbers')

    out_path = data_dir / 'anonimized_output.dat'
    with out_path.open('w', encoding='utf-8') as f:
        f.write(content)
    print('Wrote anonymized file to', out_path)


if __name__ == '__main__':
    main()