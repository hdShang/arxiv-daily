---
layout: default
title: "TernaryCLIP: Efficiently Compressing Vision-Language Models with Ternary Weights and Distilled Knowledge"
---

# TernaryCLIP: Efficiently Compressing Vision-Language Models with Ternary Weights and Distilled Knowledge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21879" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21879v1</a>
  <a href="https://arxiv.org/pdf/2510.21879.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21879v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21879v1', 'TernaryCLIP: Efficiently Compressing Vision-Language Models with Ternary Weights and Distilled Knowledge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shu-Hao Zhang, Wei-Cheng Tang, Chen Wu, Peng Hu, Nan Li, Liang-Jie Zhang, Qi Zhang, Shao-Qun Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-23

---

## 💡 一句话要点

**TernaryCLIP：通过三元权重和知识蒸馏高效压缩视觉-语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CLIP模型压缩` `三元量化` `量化感知训练` `知识蒸馏` `视觉-语言模型` `模型加速` `资源受限设备`

## 📋 核心要点

1. 现有CLIP模型参数量大，计算成本高，难以在资源受限设备上部署。
2. TernaryCLIP通过将CLIP模型的权重三元化，并结合量化感知训练和知识蒸馏，实现模型压缩和加速。
3. 实验表明，TernaryCLIP在保持性能的同时，实现了显著的压缩率、推理加速和内存优化。

## 📝 摘要（中文）

本文提出TernaryCLIP，一个轻量级的计算框架，将CLIP模型的视觉和文本编码器的连接权重转换为三元格式，而非全精度或浮点格式。TernaryCLIP结合了量化感知训练和蒸馏模块，以防止精度下降，并实现低成本和高效的计算。综合实验表明，TernaryCLIP可以实现高达99%的三元化权重，使用1.58位的表示，16.98倍的压缩率，2.3倍的推理加速，16倍的存储减少，10倍的内存优化和60%的稀疏性，同时在41个常用数据集上的零样本图像分类和图像-文本检索任务中保持良好的性能。这项工作突出了对大型多模态模型进行极端量化的可行性，支持在资源受限的设备上进行有效和高效的部署。模型和代码可以在Hugging Face和GitHub上访问。

## 🔬 方法详解

**问题定义**：论文旨在解决CLIP模型计算开销大，难以在资源受限设备上部署的问题。现有方法通常采用模型剪枝或量化，但这些方法在极端量化（如二值化或三元化）时，性能下降明显。

**核心思路**：论文的核心思路是将CLIP模型的权重三元化，即权重取值为{-1, 0, 1}。为了弥补三元化带来的精度损失，论文采用了量化感知训练和知识蒸馏技术。量化感知训练在训练过程中模拟量化操作，使模型适应三元权重。知识蒸馏则利用原始CLIP模型作为教师模型，指导三元化后的学生模型学习。

**技术框架**：TernaryCLIP的整体框架包括三个主要阶段：1) 权重三元化：将CLIP模型的视觉和文本编码器的权重转换为三元格式。2) 量化感知训练：在训练过程中，模拟权重三元化操作，并使用量化后的权重进行前向传播和反向传播。3) 知识蒸馏：使用原始CLIP模型作为教师模型，利用其输出logits指导三元化后的学生模型进行训练。

**关键创新**：论文的关键创新在于将三元化权重、量化感知训练和知识蒸馏相结合，实现了CLIP模型的极端压缩和加速，同时保持了良好的性能。与传统的二值化或三元化方法相比，TernaryCLIP通过量化感知训练和知识蒸馏，有效地缓解了精度损失。

**关键设计**：论文的关键设计包括：1) 使用Straight-Through Estimator (STE)进行量化感知训练，解决梯度消失问题。2) 设计了基于logits的知识蒸馏损失函数，鼓励学生模型学习教师模型的输出分布。3) 对视觉和文本编码器分别进行三元化，并针对不同模态的特点进行优化。

## 📊 实验亮点

实验结果表明，TernaryCLIP在41个常用数据集上实现了显著的压缩和加速效果。具体来说，TernaryCLIP实现了高达99%的三元化权重，16.98倍的压缩率，2.3倍的推理加速，16倍的存储减少，10倍的内存优化和60%的稀疏性，同时在零样本图像分类和图像-文本检索任务中保持了与原始CLIP模型相近的性能。

## 🎯 应用场景

TernaryCLIP可应用于移动设备、嵌入式系统等资源受限的场景，实现高效的图像-文本理解和检索。例如，在智能手机上进行图像搜索、在机器人上进行视觉导航、在可穿戴设备上进行图像识别等。该研究为大型多模态模型在边缘设备上的部署提供了新的思路。

## 📄 摘要（原文）

> Recent years have witnessed an increasing interest in image-text contrastive modeling, exemplified by models such as Contrastive Language-Image Pretraining (CLIP). In this paper, we propose the TernaryCLIP, a lightweight computational framework that converts connection weights of both vision and text encoders of CLIP into the ternary format, instead of full-precision or floating ones. TernaryCLIP incorporates quantization-aware training and distillation modules, preventing precision degradation and enabling low-cost and high-efficiency computations. Comprehensive experiments demonstrate that TernaryCLIP can achieve up to 99\% ternarized weights with 1.58-bit representation, 16.98 $\times$ compression ratio, 2.3 $\times$ inference acceleration, 16 $\times$ storage reduction, 10 $\times$ memory optimization, and 60\% sparsity while maintaining promising performance on zero-shot image classification and image-text retrieval tasks across 41 commonly used datasets. Our work highlights the feasibility of extreme quantization for large multimodal models, supporting effective and efficient deployment on resource-constrained devices. The model and code can be accessed from Hugging Face and GitHub.

