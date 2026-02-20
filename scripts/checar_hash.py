import hashlib
import sys

def calculate_sha256(file_path):
    """Calcula o hash SHA-256 de um arquivo para fins forenses."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Lê o arquivo em blocos para não sobrecarregar a memória
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "Arquivo não encontrado."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python checar_hash.py <caminho_do_arquivo>")
    else:
        target_file = sys.argv[1]
        print(f"Analisando arquivo: {target_file}")
        print(f"Hash SHA-256: {calculate_sha256(target_file)}")
