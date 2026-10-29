# %%
import pandas as pd
from pathlib import Path
import requests

class DownloadTSE:

    def __init__(self) -> None:
        self.data_path = Path(__file__).parent / 'data'

    def _download_files(self, filename:str, year:int) -> bool:
        url = f"https://cdn.tse.jus.br/estatistica/sead/odsele/{filename}/{filename}_{year}.zip"
        response = requests.get(url)

        if response.status_code == 200:
            year_path = self.data_path / str(year)
            year_path.mkdir(parents=True, exist_ok=True)
            filename_path = year_path / f"{filename}_{year}.zip"

            with open(filename_path, "wb") as f:
                f.write(response.content)
            
            print(f"Arquivo {filename}_{year}.zip baixado com sucesso!")
            return True

        else:
            print(f"Falha ao baixar o {filename}_{year}.zip. Status code: {response.status_code}")
            return False

    def download_consulta_candidatura(self, year:int) -> bool:
        return self._download_files("consulta_cand", year)
    
    def download_bens_candidatos(self, year:int) -> bool:
        return self._download_files("bem_candidato", year)

    def download_coligacoes(self, year:int) -> bool:
        return self._download_files("consulta_coligacao", year)

    def download_motivo_cassacao(self, year:int) -> bool:
        return self._download_files("motivo_cassacao", year)

    def download_votacao_candidato_municipio_zona(self, year:int) -> bool:
        return self._download_files("votacao_candidato_munzona", year)

    def download_ano(self, year:int) -> None:

        self.download_consulta_candidatura(year)
        self.download_bens_candidatos(year)
        self.download_coligacoes(year)
        self.download_motivo_cassacao(year)
        self.download_votacao_candidato_municipio_zona(year)

# %%
downloader = DownloadTSE()
downloader.download_ano(2026)