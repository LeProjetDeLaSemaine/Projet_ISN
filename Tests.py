#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Utilitaires import compressionFichier
import Huffman,Compression_Basique


#Test de compression de chaine
print(Compression_Basique.compresser("AAADDDDEEEEEDDDBBBBCDGKHEJGFDJFFFFFFFFFFFFFFFFFFFFF"))
input()

#Test de decompression de la chaine
print(Compression_Basique.decompresser("3A4D5E3D4B1C1D1G1K1H1E1J1G1F1D1J21F"))
input()

#Tests de compression de fichier
compressionFichier("Fichiers\\CompressionBasique\\TexteInitial.txt", "Fichiers\\CompressionBasique\\TexteCompressé.txt", Compression_Basique.compresser)
compressionFichier("Fichiers\\DécompressionBasique\\TexteCompressé.txt", "Fichiers\\DécompressionBasique\\TexteDecompressé.txt", Compression_Basique.decompresser)
input()

#Tests de Huffman:
#Construction du dictionnaire
print(Huffman.construireDict("lalalalalalalaburegeuskrbrej"))
