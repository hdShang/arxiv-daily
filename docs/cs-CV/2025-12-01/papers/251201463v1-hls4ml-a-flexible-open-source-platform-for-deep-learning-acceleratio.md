---
layout: default
title: hls4ml: A Flexible, Open-Source Platform for Deep Learning Acceleration on Reconfigurable Hardware
---

# hls4ml: A Flexible, Open-Source Platform for Deep Learning Acceleration on Reconfigurable Hardware

**arXiv**: [2512.01463v1](https://arxiv.org/abs/2512.01463) | [PDF](https://arxiv.org/pdf/2512.01463.pdf)

**作者**: Jan-Frederik Schulte, Benjamin Ramhorst, Chang Sun, Jovan Mitrevski, Nicolò Ghielmetti, Enrico Lupi, Dimitrios Danopoulos, Vladimir Loncar, Javier Duarte, David Burnette, Lauri Laatu, Stylianos Tzelepis, Konstantinos Axiotis, Quentin Berthet, Haoyan Wang, Paul White, Suleyman Demirsoy, Marco Colombo, Thea Aarrestad, Sioni Summers, Maurizio Pierini, Giuseppe Di Guglielmo, Jennifer Ngadiuba, Javier Campos, Ben Hawks, Abhijith Gandrakota, Farah Fahim, Nhan Tran, George Constantinides, Zhiqiang Que, Wayne Luk, Alexander Tapper, Duc Hoang, Noah Paladino, Philip Harris, Bo-Cheng Lai, Manuel Valentin, Ryan Forelli, Seda Ogrenci, Lino Gerlach, Rian Flynn, Mia Liu, Daniel Diaz, Elham Khoda, Melissa Quinnan, Russell Solares, Santosh Parajuli, Mark Neubauer, Christian Herwig, Ho Fung Tsoi, Dylan Rankin, Shih-Chieh Hsu, Scott Hauck

---

## 💡 一句话要点

**提出hls4ml平台，将深度学习模型转换为HLS代码以加速FPGA/ASIC推理**

**关键词**: `深度学习加速` `硬件合成` `FPGA部署` `开源平台` `低延迟推理`

## 📋 核心要点

1. 核心问题：在低延迟、低资源消耗场景下加速深度学习推理
2. 方法要点：开源平台支持多框架模型转换，生成可集成到FPGA/ASIC的HLS代码
3. 实验或效果：应用于商业和科学领域，实现高效硬件加速

## 📄 摘要（原文）

> We present hls4ml, a free and open-source platform that translates machine learning (ML) models from modern deep learning frameworks into high-level synthesis (HLS) code that can be integrated into full designs for field-programmable gate arrays (FPGAs) or application-specific integrated circuits (ASICs). With its flexible and modular design, hls4ml supports a large number of deep learning frameworks and can target HLS compilers from several vendors, including Vitis HLS, Intel oneAPI and Catapult HLS. Together with a wider eco-system for software-hardware co-design, hls4ml has enabled the acceleration of ML inference in a wide range of commercial and scientific applications where low latency, resource usage, and power consumption are critical. In this paper, we describe the structure and functionality of the hls4ml platform. The overarching design considerations for the generated HLS code are discussed, together with selected performance results.

