---
layout: default
title: Predicting Polymer Solubility in Solvents Using SMILES Strings
---

# Predicting Polymer Solubility in Solvents Using SMILES Strings

**arXiv**: [2512.09784v1](https://arxiv.org/abs/2512.09784) | [PDF](https://arxiv.org/pdf/2512.09784.pdf)

**作者**: Andrew Reinhard

---

## 💡 一句话要点

**提出基于SMILES的深度学习框架，预测聚合物在溶剂中的溶解度，支持绿色化学与材料设计。**

**关键词**: `聚合物溶解度预测` `SMILES表示` `深度学习框架` `材料基因组项目` `溶剂筛选`

## 📋 核心要点

1. 核心问题：预测聚合物在溶剂中的溶解度对回收和制药等应用至关重要。
2. 方法要点：使用SMILES字符串构建特征，训练六层全连接神经网络进行预测。
3. 实验或效果：在模拟和实验数据上验证，模型在未见组合上保持高准确性。

## 📄 摘要（原文）

> Understanding and predicting polymer solubility in various solvents is critical for applications ranging from recycling to pharmaceutical formulation. This work presents a deep learning framework that predicts polymer solubility, expressed as weight percent (wt%), directly from SMILES representations of both polymers and solvents. A dataset of 8,049 polymer solvent pairs at 25 deg C was constructed from calibrated molecular dynamics simulations (Zhou et al., 2023), and molecular descriptors and fingerprints were combined into a 2,394 feature representation per sample. A fully connected neural network with six hidden layers was trained using the Adam optimizer and evaluated using mean squared error loss, achieving strong agreement between predicted and actual solubility values. Generalizability was demonstrated using experimentally measured data from the Materials Genome Project, where the model maintained high accuracy on 25 unseen polymer solvent combinations. These findings highlight the viability of SMILES based machine learning models for scalable solubility prediction and high-throughput solvent screening, supporting applications in green chemistry, polymer processing, and materials design.

