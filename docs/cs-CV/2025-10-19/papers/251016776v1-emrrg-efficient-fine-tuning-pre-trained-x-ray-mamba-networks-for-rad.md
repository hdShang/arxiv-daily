---
layout: default
title: "EMRRG: Efficient Fine-Tuning Pre-trained X-ray Mamba Networks for Radiology Report Generation"
---

# EMRRG: Efficient Fine-Tuning Pre-trained X-ray Mamba Networks for Radiology Report Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16776" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16776v1</a>
  <a href="https://arxiv.org/pdf/2510.16776.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16776v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16776v1', 'EMRRG: Efficient Fine-Tuning Pre-trained X-ray Mamba Networks for Radiology Report Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingzheng Zhang, Jinfeng Gao, Dan Xu, Jiangrui Yu, Yuhan Qiao, Lan Chen, Jin Tang, Xiao Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-19

**🔗 代码/项目**: [GITHUB](https://github.com/Event-AHU/Medical_Image_Analysis)

---

## 💡 一句话要点

**EMRRG：高效微调预训练Mamba X射线网络，用于放射报告生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学报告生成` `X射线图像` `Mamba网络` `参数高效微调` `Partial LoRA`

## 📋 核心要点

1. 现有医学报告生成模型过度依赖大型语言模型，忽略了预训练视觉模型和高效微调技术的潜力。
2. EMRRG框架通过参数高效的微调方法，利用预训练的Mamba网络作为视觉骨干，提取X射线图像特征。
3. 实验结果表明，EMRRG在多个基准数据集上表现出色，验证了所提出策略在X射线医学报告生成中的有效性。

## 📝 摘要（中文）

基于X射线图像的医学报告生成（MRG）是人工智能领域的一个关键方向，可以显著减轻临床医生的诊断负担并缩短患者的等待时间。现有的MRG模型主要依赖于大型语言模型（LLM）来改进报告生成，而对预训练视觉基础模型或高级微调技术的探索有限。主流框架要么避免微调，要么使用像LoRA这样简单的方法，常常忽略了增强交叉注意力机制的潜力。此外，虽然基于Transformer的模型在视觉-语言任务中占据主导地位，但像Mamba网络这样的非Transformer架构在医学报告生成方面的研究仍然不足，这为未来的研究提供了一个有希望的方向。在本文中，我们提出了EMRRG，一种新颖的X射线报告生成框架，该框架使用参数高效的方法微调预训练的Mamba网络。具体来说，X射线图像被分成patches，进行token化，并通过基于SSM的视觉骨干网络进行特征提取，其中Partial LoRA产生最佳性能。具有混合解码器的LLM生成医学报告，实现端到端训练，并在基准数据集上取得强大的结果。在三个广泛使用的基准数据集上的大量实验充分验证了我们提出的X射线MRG策略的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决X射线图像医学报告自动生成问题。现有方法主要依赖Transformer架构和大型语言模型，计算成本高昂，且对非Transformer架构（如Mamba）的探索不足。此外，现有微调方法（如LoRA）可能无法充分优化视觉特征提取过程，限制了报告生成的质量。

**核心思路**：论文的核心思路是利用Mamba架构作为视觉骨干网络，并采用参数高效的微调方法（Partial LoRA）来优化特征提取过程。Mamba架构具有线性复杂度，可以更高效地处理长序列数据，从而降低计算成本。Partial LoRA专注于微调部分网络参数，进一步提高微调效率。

**技术框架**：EMRRG框架包含以下主要模块：1) X射线图像预处理：将图像分割成patches并进行token化。2) 基于SSM的视觉骨干网络：使用Mamba架构提取图像特征。3) Partial LoRA微调：优化视觉骨干网络的参数。4) 混合解码器的LLM：生成医学报告。整个框架采用端到端训练方式。

**关键创新**：论文的关键创新在于：1) 将Mamba架构引入X射线医学报告生成任务，探索了非Transformer架构的潜力。2) 提出了Partial LoRA微调方法，更有效地优化视觉特征提取过程。3) 采用了混合解码器的LLM，提高了报告生成的质量。

**关键设计**：X射线图像被分割成固定大小的patches，然后通过线性投影层进行token化。Mamba架构的视觉骨干网络采用多层SSM模块堆叠而成。Partial LoRA选择性地微调部分SSM模块的参数。损失函数采用交叉熵损失，用于优化报告生成的准确性。混合解码器的LLM结合了自回归解码器和非自回归解码器，以提高生成效率和质量。

## 📊 实验亮点

论文在三个广泛使用的基准数据集上进行了实验，验证了EMRRG框架的有效性。实验结果表明，EMRRG在报告生成质量方面优于现有方法，并且具有更高的计算效率。Partial LoRA微调方法能够显著提高模型的性能，并且降低了微调成本。具体性能数据在论文中详细展示。

## 🎯 应用场景

该研究成果可应用于辅助放射科医生进行X射线图像诊断，自动生成初步的医学报告，从而减轻医生的工作负担，缩短患者的等待时间。此外，该技术还可以用于远程医疗和移动医疗应用，为缺乏医疗资源的地区提供支持。未来，该研究可以扩展到其他医学影像模态，如CT和MRI，实现更全面的医学报告自动生成。

## 📄 摘要（原文）

> X-ray image-based medical report generation (MRG) is a pivotal area in artificial intelligence that can significantly reduce diagnostic burdens for clinicians and patient wait times. Existing MRG models predominantly rely on Large Language Models (LLMs) to improve report generation, with limited exploration of pre-trained vision foundation models or advanced fine-tuning techniques. Mainstream frameworks either avoid fine-tuning or utilize simplistic methods like LoRA, often neglecting the potential of enhancing cross-attention mechanisms. Additionally, while Transformer-based models dominate vision-language tasks, non-Transformer architectures, such as the Mamba network, remain underexplored for medical report generation, presenting a promising avenue for future research. In this paper, we propose EMRRG, a novel X-ray report generation framework that fine-tunes pre-trained Mamba networks using parameter-efficient methods. Specifically, X-ray images are divided into patches, tokenized, and processed by an SSM-based vision backbone for feature extraction, with Partial LoRA yielding optimal performance. An LLM with a hybrid decoder generates the medical report, enabling end-to-end training and achieving strong results on benchmark datasets. Extensive experiments on three widely used benchmark datasets fully validated the effectiveness of our proposed strategies for the X-ray MRG. The source code of this paper will be released on https://github.com/Event-AHU/Medical_Image_Analysis.

