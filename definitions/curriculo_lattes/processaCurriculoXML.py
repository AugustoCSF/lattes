import zipfile
import io
import os
import sys
from curriculo_model import CurriculoVitae
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer

def processar_zip_lattes(caminho_zip, pasta_saida):
    # Cria a pasta de saída se não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    parser = XmlParser()
    serializer = JsonSerializer()

    with zipfile.ZipFile(caminho_zip, 'r') as z:
        # Lista todos os arquivos dentro do ZIP que terminam em .xml
        arquivos_xml = [f for f in z.namelist() if f.lower().endswith('.xml')]
        
        print(f"Encontrados {len(arquivos_xml)} currículos no arquivo ZIP.")

        for nome_arquivo in arquivos_xml:
            try:
                # 1. Abre o arquivo XML dentro do ZIP sem extrair para o disco
                with z.open(nome_arquivo) as xml_file:
                    # O xsdata aceita um file-like object (stream)
                    curriculo_obj = parser.from_bytes(xml_file.read(), CurriculoVitae)
                
                # 2. Define o nome do arquivo JSON de saída
                nome_json = nome_arquivo.rsplit('.', 1)[0] + ".json"
                caminho_json = os.path.join(pasta_saida, nome_json)

                # 3. Salva o JSON
                with open(caminho_json, "w", encoding="utf-8") as f:
                    f.write(serializer.render(curriculo_obj))

                print(f"Convertido: {nome_arquivo}")

            except Exception as e:
                print(f"Erro ao processar {nome_arquivo}: {e}")

# Uso do script

def __main()__:
    if not (len(sys.argv) in [3,4]):
        print("Uso arquivo xml:")
        print("\tpython {sys.argv[0]} <arquivo_xml> [pasta_saida]\n")
        print("Uso arquivo zip:")
        print("\tpython {sys.argv[0]} <arquivo_zip> [pasta_saida]\n")
        print("\tarquivo xml: XML do curriculo lattes")
        print("\tarquivo zip: ZIP com XMLs dos currículos lattes")
        print("\tpasta_saida: Pasta onde os arquivos JSON serão salvos (opcional, padrão: pasta atual)")
        
        sys.exit(1)

processar_zip_lattes("extracao_lattes.zip", "./output_json")
