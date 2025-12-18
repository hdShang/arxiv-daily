---
layout: default
title: Non-Aligned Reference Image Quality Assessment for Novel View Synthesis
---

# Non-Aligned Reference Image Quality Assessment for Novel View Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08155" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08155v1</a>
  <a href="https://arxiv.org/pdf/2511.08155.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08155v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.08155v1', 'Non-Aligned Reference Image Quality Assessment for Novel View Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abhijay Ghildyal, Rajesh Sureddi, Nabajeet Barman, Saman Zadtootaghaj, Alan Bovik

**分类**: cs.CV

**发布日期**: 2025-11-11

**🔗 代码/项目**: [PROJECT_PAGE](https://stootaghaj.github.io/nova-project/)

---

## 💡 一句话要点

**提出NAR-IQA框架，用于解决新视角合成中非对齐参考图像的质量评估问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `新视角合成` `图像质量评估` `非对齐参考` `对比学习` `DINOv2` `LoRA` `时间感兴趣区域`

## 📋 核心要点

1. 现有全参考IQA方法在参考图像未对齐时失效，无参考IQA方法泛化性不足，难以评估新视角合成图像质量。
2. 提出NAR-IQA框架，利用对比学习和LoRA增强的DINOv2嵌入，并结合现有IQA方法的监督信息。
3. 实验表明，该模型在对齐和非对齐参考图像上均优于现有方法，且与人类主观评价高度相关。

## 📝 摘要（中文）

本文提出了一种非对齐参考图像质量评估(NAR-IQA)框架，专门用于新视角合成(NVS)图像的质量评估。该框架旨在解决在缺乏像素级对齐的ground truth参考图像时，传统全参考图像质量评估(FR-IQA)方法失效以及无参考图像质量评估(NR-IQA)方法泛化能力不足的问题。作者构建了一个大规模图像数据集，包含针对时间感兴趣区域(TROI)的合成失真，用于训练NAR-IQA模型。该模型基于对比学习框架，结合了LoRA增强的DINOv2嵌入，并利用现有IQA方法的监督信息进行指导。模型仅在合成失真数据上训练，避免过拟合特定的真实NVS样本，从而增强模型的泛化能力。实验结果表明，该模型优于当前最先进的FR-IQA、NR-IQA和NAR-IQA方法，在对齐和非对齐参考图像上均表现出强大的性能。此外，作者还进行了一项用户研究，收集了在NVS中观察非对齐参考图像时的人类偏好数据，发现所提出的质量预测模型与收集的主观评分之间存在很强的相关性。

## 🔬 方法详解

**问题定义**：论文旨在解决新视角合成(NVS)图像质量评估问题，尤其是在缺乏像素对齐的参考图像时。传统全参考IQA方法依赖于像素级别的对应关系，当参考图像与合成图像未对齐时，性能会显著下降。而无参考IQA方法虽然不需要参考图像，但在NVS场景下的泛化能力有限，难以准确评估合成图像的质量。

**核心思路**：论文的核心思路是利用非对齐的参考图像，通过对比学习的方式，学习图像的感知质量。核心在于提取参考图像和合成图像的特征，并学习一个能够容忍一定程度不对齐的质量评估模型。通过在合成数据上进行训练，增强模型的泛化能力，使其能够适应不同的NVS场景。

**技术框架**：整体框架包含以下几个主要模块：1) 数据集构建：构建包含合成失真的大规模数据集，模拟NVS中可能出现的各种质量问题。2) 特征提取：使用LoRA增强的DINOv2模型提取参考图像和合成图像的特征嵌入。3) 对比学习：利用对比学习框架，学习图像质量的表示，使得高质量的合成图像与参考图像的特征嵌入更加接近。4) 质量预测：基于学习到的特征表示，预测合成图像的质量得分。

**关键创新**：该论文的关键创新在于提出了一个专门针对NVS场景的NAR-IQA框架，该框架能够利用非对齐的参考图像进行质量评估。与传统的FR-IQA方法相比，该框架不需要像素级别的对齐，因此更加适用于实际的NVS应用场景。与NR-IQA方法相比，该框架利用了参考图像的信息，能够更准确地评估合成图像的质量。

**关键设计**：论文的关键设计包括：1) 使用LoRA对DINOv2模型进行增强，提高特征提取的效率和准确性。2) 构建包含时间感兴趣区域(TROI)失真的合成数据集，模拟NVS中可能出现的各种质量问题。3) 利用对比学习框架，学习图像质量的表示，并结合现有IQA方法的监督信息，提高模型的性能。4) 仅在合成数据上进行训练，避免过拟合特定的真实NVS样本，从而增强模型的泛化能力。

## 📊 实验亮点

该模型在合成数据集上训练，并在真实NVS数据集上进行了测试，结果表明该模型优于当前最先进的FR-IQA、NR-IQA和NAR-IQA方法。用户研究表明，该模型预测的质量得分与人类主观评价具有很强的相关性，验证了该模型的有效性。项目主页提供了数据集和代码。

## 🎯 应用场景

该研究成果可应用于各种新视角合成系统，例如虚拟现实、增强现实、自由视点视频等。通过自动评估合成图像的质量，可以优化NVS算法，提高用户体验。此外，该方法还可以用于评估不同NVS算法的性能，为算法选择提供依据。未来，该方法有望扩展到其他图像生成任务的质量评估中。

## 📄 摘要（原文）

> Evaluating the perceptual quality of Novel View Synthesis (NVS) images remains a key challenge, particularly in the absence of pixel-aligned ground truth references. Full-Reference Image Quality Assessment (FR-IQA) methods fail under misalignment, while No-Reference (NR-IQA) methods struggle with generalization. In this work, we introduce a Non-Aligned Reference (NAR-IQA) framework tailored for NVS, where it is assumed that the reference view shares partial scene content but lacks pixel-level alignment. We constructed a large-scale image dataset containing synthetic distortions targeting Temporal Regions of Interest (TROI) to train our NAR-IQA model. Our model is built on a contrastive learning framework that incorporates LoRA-enhanced DINOv2 embeddings and is guided by supervision from existing IQA methods. We train exclusively on synthetically generated distortions, deliberately avoiding overfitting to specific real NVS samples and thereby enhancing the model's generalization capability. Our model outperforms state-of-the-art FR-IQA, NR-IQA, and NAR-IQA methods, achieving robust performance on both aligned and non-aligned references. We also conducted a novel user study to gather data on human preferences when viewing non-aligned references in NVS. We find strong correlation between our proposed quality prediction model and the collected subjective ratings. For dataset and code, please visit our project page: https://stootaghaj.github.io/nova-project/

