# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rAcXhZQKTUfqLZUDPp-P2dHC5n0gQU9r
"""

# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16GenQkhkepnHy1VxYfLg_71X51hHm2Qh
"""

def kasallik_tashxisi(belgi):
     if belgi== "istima":
      return "Parasetamol iching"
     elif belgi == "bosh og'rig'i":
      return "Trimol iching"
     elif belgi == "tish og'rig'i":
      return "Quepen iching"
     else:
        return "Shifokorga murijat qiling"
belgi=input("Kasallik belgisini kiriting:   ")
natija=kasallik_tashxisi(belgi)
print(natija)