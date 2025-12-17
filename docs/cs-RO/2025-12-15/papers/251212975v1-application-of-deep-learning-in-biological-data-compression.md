---
layout: default
title: Application of Deep Learning in Biological Data Compression
---

# Application of Deep Learning in Biological Data Compression

**arXiv**: [2512.12975v1](https://arxiv.org/abs/2512.12975) | [PDF](https://arxiv.org/pdf/2512.12975.pdf)

**作者**: Chunyu Zou

---

## 💡 一句话要点

**提出基于隐式神经表示的深度学习方法来压缩冷冻电镜生物数据**

**关键词**: `冷冻电镜数据压缩` `隐式神经表示` `深度学习压缩` `生物数据存储` `位置编码` `加权MSE损失`

## 📋 核心要点

1. 核心问题：冷冻电镜数据文件存储量大，对研究和教育构成挑战。
2. 方法要点：提取密度图后，用GZIP压缩，神经网络编码空间密度信息，结合位置编码和加权MSE损失提升重建精度。
3. 实验或效果：旨在提供实用高效的压缩方案，保持合理压缩比和文件间重建质量。

## 📄 摘要（原文）

> Cryogenic electron microscopy (Cryo-EM) has become an essential tool for capturing high-resolution biological structures. Despite its advantage in visualizations, the large storage size of Cryo-EM data file poses significant challenges for researchers and educators. This paper investigates the application of deep learning, specifically implicit neural representation (INR), to compress Cryo-EM biological data. The proposed approach first extracts the binary map of each file according to the density threshold. The density map is highly repetitive, ehich can be effectively compressed by GZIP. The neural network then trains to encode spatial density information, allowing the storage of network parameters and learnable latent vectors. To improve reconstruction accuracy, I further incorporate the positional encoding to enhance spatial representation and a weighted Mean Squared Error (MSE) loss function to balance density distribution variations. Using this approach, my aim is to provide a practical and efficient biological data compression solution that can be used for educational and research purpose, while maintaining a reasonable compression ratio and reconstruction quality from file to file.

