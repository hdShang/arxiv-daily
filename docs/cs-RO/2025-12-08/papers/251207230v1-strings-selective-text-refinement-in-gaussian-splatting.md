---
layout: default
title: STRinGS: Selective Text Refinement in Gaussian Splatting
---

# STRinGS: Selective Text Refinement in Gaussian Splatting

**arXiv**: [2512.07230v1](https://arxiv.org/abs/2512.07230) | [PDF](https://arxiv.org/pdf/2512.07230.pdf)

**作者**: Abhinav Raundhal, Gaurav Behera, P J Narayanan, Ravi Kiran Sarvadevabhatla, Makarand Tapaswi

---

## 💡 一句话要点

**提出STRinGS框架，通过选择性文本细化解决3D高斯泼溅中文本细节重建问题**

**关键词**: `3D高斯泼溅` `文本重建` `选择性细化` `OCR评估` `场景理解` `数据集构建`

## 📋 核心要点

1. 核心问题：3D高斯泼溅在重建精细文本细节时易导致语义损失，影响场景理解。
2. 方法要点：分离处理文本与非文本区域，先细化文本区域再合并优化，提升文本可读性。
3. 实验或效果：在7K迭代下相对3DGS提升63.6%，引入OCR CER评估指标和STRinGS-360数据集。

## 📄 摘要（原文）

> Text as signs, labels, or instructions is a critical element of real-world scenes as they can convey important contextual information. 3D representations such as 3D Gaussian Splatting (3DGS) struggle to preserve fine-grained text details, while achieving high visual fidelity. Small errors in textual element reconstruction can lead to significant semantic loss. We propose STRinGS, a text-aware, selective refinement framework to address this issue for 3DGS reconstruction. Our method treats text and non-text regions separately, refining text regions first and merging them with non-text regions later for full-scene optimization. STRinGS produces sharp, readable text even in challenging configurations. We introduce a text readability measure OCR Character Error Rate (CER) to evaluate the efficacy on text regions. STRinGS results in a 63.6% relative improvement over 3DGS at just 7K iterations. We also introduce a curated dataset STRinGS-360 with diverse text scenarios to evaluate text readability in 3D reconstruction. Our method and dataset together push the boundaries of 3D scene understanding in text-rich environments, paving the way for more robust text-aware reconstruction methods.

