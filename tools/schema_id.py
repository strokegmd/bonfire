import zlib

def main() -> None:
    with open('raw.bf', 'r') as file:
        schema = file.read().splitlines()
        for line in schema:
            if '------' in line or '//' in line or not line:
                print(line)
                continue

            splitted = line.split()
            splitted[0] += f'#{hex(zlib.crc32(line.encode()))[2:]}'
            splitted[-1] += ';'
            
            print(' '.join(splitted))

if __name__ == '__main__':
    main()
