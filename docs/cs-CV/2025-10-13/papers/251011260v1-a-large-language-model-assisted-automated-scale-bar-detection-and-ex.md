---
layout: default
title: A Large-Language-Model Assisted Automated Scale Bar Detection and Extraction Framework for Scanning Electron Microscopic Images
---

# A Large-Language-Model Assisted Automated Scale Bar Detection and Extraction Framework for Scanning Electron Microscopic Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11260" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11260v1</a>
  <a href="https://arxiv.org/pdf/2510.11260.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11260v1" onclick="toggleFavorite(this, '2510.11260v1', 'A Large-Language-Model Assisted Automated Scale Bar Detection and Extraction Framework for Scanning Electron Microscopic Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Chen, Ruotong Yang, Zhengyang Zhang, Mehreen Ahmed, Yanming Wang

**分类**: cs.CV, cond-mat.mtrl-sci, cs.AI, physics.data-an

**发布日期**: 2025-10-13

**备注**: 14 pages, 6 figures

---

## 💡 一句话要点

**提出基于大语言模型的扫描电镜图像比例尺自动检测与提取框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扫描电镜图像` `比例尺检测` `大语言模型` `目标检测` `光学字符识别`

## 📋 核心要点

1. 目前扫描电镜图像比例尺的确定主要依赖手动操作，耗时且容易出错，限制了微观结构分析的效率和准确性。
2. 利用大语言模型（LLM）作为智能代理，结合目标检测和混合OCR系统，实现比例尺的自动检测、信息提取和结果验证。
3. 实验结果表明，该方法在比例尺检测和文本识别方面均优于现有方法，显著提升了扫描电镜图像分析的自动化水平。

## 📝 摘要（中文）

本文提出了一种多模态的扫描电镜（SEM）图像比例尺自动检测与提取框架，该框架结合了大语言模型（LLM）代理，能够同时进行目标检测、文本检测和文本识别。该框架包含四个阶段：1) 自动数据集生成（Auto-DG）模型，用于合成多样化的SEM图像数据集，确保模型的鲁棒性和泛化性；2) 比例尺目标检测；3) 使用混合光学字符识别（OCR）系统进行信息提取，该系统结合了基于DenseNet和卷积循环神经网络（CRNN）的算法；4) LLM代理，用于分析和验证结果的准确性。实验结果表明，该模型在目标检测方面表现出色，精度为100%，召回率为95.8%，在IoU=0.5时的平均精度均值（mAP）为99.2%，在IoU=0.5:0.95时为69.1%。混合OCR系统在Auto-DG数据集上实现了89%的精度、65%的召回率和75%的F1分数，显著优于几种主流的独立引擎。LLM被引入作为推理引擎和智能助手，可以建议后续步骤并验证结果。这种由LLM代理驱动的自动化方法显著提高了SEM图像中比例尺检测和提取的效率和准确性，为微观分析提供了一个有价值的工具，并推动了科学成像领域的发展。

## 🔬 方法详解

**问题定义**：论文旨在解决扫描电镜图像中比例尺手动检测和提取效率低、易出错的问题。现有方法主要依赖人工操作，耗时耗力，且容易受到人为因素的影响，导致分析结果的准确性降低。

**核心思路**：论文的核心思路是利用大语言模型（LLM）的推理能力，结合计算机视觉技术，构建一个自动化的比例尺检测和提取框架。通过自动生成数据集、目标检测、混合OCR和LLM验证等步骤，实现高效、准确的比例尺信息提取。

**技术框架**：该框架主要包含四个阶段：
1. **自动数据集生成（Auto-DG）**：合成多样化的SEM图像数据集，增强模型的泛化能力。
2. **比例尺目标检测**：使用目标检测算法定位图像中的比例尺区域。
3. **信息提取**：采用混合OCR系统，结合DenseNet和CRNN算法，识别比例尺上的文本信息。
4. **LLM验证**：利用LLM对提取的比例尺信息进行分析和验证，确保结果的准确性。

**关键创新**：该论文的关键创新在于将大语言模型（LLM）引入到扫描电镜图像分析流程中，作为推理引擎和智能助手。LLM不仅可以验证提取的比例尺信息，还可以根据图像内容和分析目标，提供后续分析步骤的建议。与传统方法相比，该方法实现了端到端的自动化，减少了人工干预，提高了分析效率和准确性。

**关键设计**：
* **Auto-DG模型**：用于生成多样化的SEM图像数据集，具体生成方式未知。
* **混合OCR系统**：结合DenseNet和CRNN算法，充分利用两种算法的优势，提高文本识别的准确率。
* **LLM代理**：使用LLM进行结果验证和后续步骤建议，具体LLM模型和prompt设计未知。

## 📊 实验亮点

该模型在比例尺目标检测方面表现出色，精度达到100%，召回率为95.8%，在IoU=0.5时的mAP为99.2%，在IoU=0.5:0.95时为69.1%。混合OCR系统在Auto-DG数据集上实现了89%的精度、65%的召回率和75%的F1分数，显著优于几种主流的独立引擎。

## 🎯 应用场景

该研究成果可广泛应用于材料科学、生物医学等领域，能够显著提高扫描电镜图像分析的效率和准确性，加速科研进程。该框架还可扩展到其他类型的显微图像分析，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> Microscopic characterizations, such as Scanning Electron Microscopy (SEM), are widely used in scientific research for visualizing and analyzing microstructures. Determining the scale bars is an important first step of accurate SEM analysis; however, currently, it mainly relies on manual operations, which is both time-consuming and prone to errors. To address this issue, we propose a multi-modal and automated scale bar detection and extraction framework that provides concurrent object detection, text detection and text recognition with a Large Language Model (LLM) agent. The proposed framework operates in four phases; i) Automatic Dataset Generation (Auto-DG) model to synthesize a diverse dataset of SEM images ensuring robust training and high generalizability of the model, ii) scale bar object detection, iii) information extraction using a hybrid Optical Character Recognition (OCR) system with DenseNet and Convolutional Recurrent Neural Network (CRNN) based algorithms, iv) an LLM agent to analyze and verify accuracy of the results. The proposed model demonstrates a strong performance in object detection and accurate localization with a precision of 100%, recall of 95.8%, and a mean Average Precision (mAP) of 99.2% at IoU=0.5 and 69.1% at IoU=0.5:0.95. The hybrid OCR system achieved 89% precision, 65% recall, and a 75% F1 score on the Auto-DG dataset, significantly outperforming several mainstream standalone engines, highlighting its reliability for scientific image analysis. The LLM is introduced as a reasoning engine as well as an intelligent assistant that suggests follow-up steps and verifies the results. This automated method powered by an LLM agent significantly enhances the efficiency and accuracy of scale bar detection and extraction in SEM images, providing a valuable tool for microscopic analysis and advancing the field of scientific imaging.

