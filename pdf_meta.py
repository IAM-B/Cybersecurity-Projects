#!/usr/bin/env python3
# coding:utf8
from PyPDF2 import PdfReader


with open("../../ANONOPS_The_Press_Release.pdf", "rb") as file:
    pdf_file = PdfReader(file)
    doc_info = pdf_file.metadata
    for info in doc_info:
        print("[*]" + info + ": " + doc_info[info])
