---
layout: default
title: DKDS: A Benchmark Dataset of Degraded Kuzushiji Documents with Seals for Detection and Binarization
---

# DKDS: A Benchmark Dataset of Degraded Kuzushiji Documents with Seals for Detection and Binarization

**arXiv**: [2511.09117v1](https://arxiv.org/abs/2511.09117) | [PDF](https://arxiv.org/pdf/2511.09117.pdf)

**作者**: Rui-Yang Ju, Kohei Yamashita, Hirotaka Kameko, Shinsuke Mori

---

## 💡 一句话要点

**提出DKDS数据集以解决古日文草书文档中噪声影响OCR准确性的问题**

**关键词**: `古日文草书识别` `文档二值化` `目标检测` `基准数据集` `印章检测` `OCR噪声处理`

## 📋 核心要点

1. 核心问题：现有OCR方法未考虑文档退化和印章噪声，影响古日文草书识别准确性
2. 方法要点：构建包含退化和印章的基准数据集，定义检测和二值化两个任务
3. 实验或效果：提供YOLO模型检测和多种二值化方法的基线结果，代码公开

## 📄 摘要（原文）

> Kuzushiji, a pre-modern Japanese cursive script, can currently be read and understood by only a few thousand trained experts in Japan. With the rapid development of deep learning, researchers have begun applying Optical Character Recognition (OCR) techniques to transcribe Kuzushiji into modern Japanese. Although existing OCR methods perform well on clean pre-modern Japanese documents written in Kuzushiji, they often fail to consider various types of noise, such as document degradation and seals, which significantly affect recognition accuracy. To the best of our knowledge, no existing dataset specifically addresses these challenges. To address this gap, we introduce the Degraded Kuzushiji Documents with Seals (DKDS) dataset as a new benchmark for related tasks. We describe the dataset construction process, which required the assistance of a trained Kuzushiji expert, and define two benchmark tracks: (1) text and seal detection and (2) document binarization. For the text and seal detection track, we provide baseline results using multiple versions of the You Only Look Once (YOLO) models for detecting Kuzushiji characters and seals. For the document binarization track, we present baseline results from traditional binarization algorithms, traditional algorithms combined with K-means clustering, and Generative Adversarial Network (GAN)-based methods. The DKDS dataset and the implementation code for baseline methods are available at https://ruiyangju.github.io/DKDS.

