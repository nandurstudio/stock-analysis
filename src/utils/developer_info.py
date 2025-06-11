"""
Developer Info Parser

Modul ini menyediakan fungsi-fungsi untuk membaca dan menggunakan informasi dari file developer_info.txt
"""

import os
import configparser
from pathlib import Path


class DeveloperInfo:
    """
    Kelas yang menyediakan akses ke informasi pengembang dan proyek.
    """

    def __init__(self, info_file=None):
        """
        Inisialisasi dengan membaca file informasi pengembang.
        
        Args:
            info_file: Path ke file informasi pengembang. Jika None, akan mencari di lokasi default.
        """
        self.config = configparser.ConfigParser()
        
        if info_file is None:
            # Cari di beberapa lokasi yang mungkin
            base_dir = Path(__file__).parent.parent.parent.absolute()
            possible_locations = [
                os.path.join(base_dir, "developer_info.txt"),
                os.path.join(base_dir, "src", "developer_info.txt"),
                os.path.join(base_dir, "config", "developer_info.txt"),
                "developer_info.txt",
            ]
            
            for location in possible_locations:
                if os.path.exists(location):
                    info_file = location
                    break
        
        if info_file and os.path.exists(info_file):
            self.config.read(info_file, encoding="utf-8")
            self.available = True
        else:
            self.available = False
    
    def get(self, section, key, default=None):
        """
        Ambil nilai dari file konfigurasi.
        
        Args:
            section: Bagian dalam file konfigurasi.
            key: Kunci yang akan diambil.
            default: Nilai default jika kunci tidak ditemukan.
            
        Returns:
            Nilai dari kunci yang diminta atau nilai default.
        """
        if not self.available:
            return default
        
        try:
            return self.config[section][key]
        except (KeyError, configparser.NoSectionError):
            return default
    
    def get_developer_name(self):
        """Dapatkan nama pengembang."""
        return self.get("DEVELOPER_INFO", "DEVELOPER_NAME", "Stock Analysis Developer Team")
    
    def get_developer_email(self):
        """Dapatkan email pengembang."""
        return self.get("DEVELOPER_INFO", "DEVELOPER_EMAIL", "stock.analysis.dev@example.com")
    
    def get_project_info(self):
        """
        Dapatkan informasi proyek sebagai dictionary.
        
        Returns:
            Dictionary berisi informasi proyek.
        """
        if not self.available:
            return {
                "name": "Stock Analysis & Trading Recommendation Tool",
                "version": "1.1.0",
                "tagline": "Alat analisis saham dan rekomendasi trading komprehensif berbasis Python",
                "license": "MIT",
            }
        
        return {
            "name": self.get("PROJECT_INFO", "PROJECT_NAME", "Stock Analysis & Trading Recommendation Tool"),
            "version": self.get("PROJECT_INFO", "VERSION", "1.1.0"),
            "tagline": self.get("PROJECT_INFO", "PROJECT_TAGLINE", "Alat analisis saham dan rekomendasi trading"),
            "license": self.get("PROJECT_INFO", "LICENSE", "MIT"),
            "repository": self.get("PROJECT_INFO", "REPOSITORY", ""),
            "description": self.get("PROJECT_INFO", "PROJECT_DESCRIPTION", ""),
        }
    
    def get_social_media(self):
        """
        Dapatkan informasi media sosial sebagai dictionary.
        
        Returns:
            Dictionary berisi informasi media sosial.
        """
        if not self.available or "SOCIAL_MEDIA" not in self.config:
            return {}
        
        return {k: v for k, v in self.config["SOCIAL_MEDIA"].items()}
    
    def get_funding_links(self):
        """
        Dapatkan informasi pendanaan sebagai dictionary.
        
        Returns:
            Dictionary berisi informasi pendanaan.
        """
        if not self.available or "FUNDING" not in self.config:
            return {}
        
        return {k: v for k, v in self.config["FUNDING"].items()}
    
    def get_contributors(self):
        """
        Dapatkan daftar kontributor.
        
        Returns:
            List dictionary berisi informasi kontributor.
        """
        result = []
        
        if not self.available or "CONTRIBUTORS" not in self.config:
            return result
        
        for key, value in self.config["CONTRIBUTORS"].items():
            if key.startswith("CONTRIBUTOR_"):
                parts = value.split(",")
                if len(parts) >= 2:
                    name = parts[0].strip()
                    email = parts[1].strip()
                    role = parts[2].strip() if len(parts) > 2 else ""
                    result.append({
                        "name": name,
                        "email": email,
                        "role": role
                    })
        
        return result

    def generate_about_text(self):
        """
        Hasilkan teks 'Tentang' untuk aplikasi.
        
        Returns:
            String berisi informasi tentang aplikasi dan pengembang.
        """
        project_info = self.get_project_info()
        
        # Pastikan tidak double 'v' jika sudah ada 'v' di versi
        version = str(project_info['version'])
        if version.lower().startswith('v'):
            text = f"{project_info['name']} {version}\n"
        else:
            text = f"{project_info['name']} v{version}\n"
        text += f"{project_info['tagline']}\n\n"
        
        text += f"Dikembangkan oleh: {self.get_developer_name()}\n"
        text += f"Email: {self.get_developer_email()}\n"
        
        website = self.get("DEVELOPER_INFO", "DEVELOPER_WEBSITE", "")
        if website:
            text += f"Website: {website}\n"
        
        repository = project_info.get("repository", "")
        if repository:
            text += f"GitHub: {repository}\n"
        
        text += f"\nLisensi: {project_info['license']}\n"
        
        return text


# Contoh penggunaan
if __name__ == "__main__":
    info = DeveloperInfo()
    print(info.generate_about_text())
    
    print("\nSocial Media:")
    for platform, url in info.get_social_media().items():
        print(f"  {platform}: {url}")
    
    print("\nFunding Links:")
    for platform, url in info.get_funding_links().items():
        print(f"  {platform}: {url}")
