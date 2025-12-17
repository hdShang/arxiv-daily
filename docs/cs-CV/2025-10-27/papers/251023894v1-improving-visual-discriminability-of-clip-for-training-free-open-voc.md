---
layout: default
title: Improving Visual Discriminability of CLIP for Training-Free Open-Vocabulary Semantic Segmentation
---

# Improving Visual Discriminability of CLIP for Training-Free Open-Vocabulary Semantic Segmentation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23894" target="_blank" class="toolbar-btn">arXiv: 2510.23894v1</a>
    <a href="https://arxiv.org/pdf/2510.23894.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23894v1" 
            onclick="toggleFavorite(this, '2510.23894v1', 'Improving Visual Discriminability of CLIP for Training-Free Open-Vocabulary Semantic Segmentation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jinxin Zhou, Jiachen Jiang, Zhihui Zhu

**分类**: cs.CV

**发布日期**: 2025-10-27

**备注**: 23 pages, 10 figures, 14 tables

---

## 💡 一句话要点

**提出LHT-CLIP，无需训练即可提升CLIP在开放词汇语义分割中的视觉区分性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇语义分割` `CLIP模型` `视觉区分性` `无需训练` `注意力机制`

## 📋 核心要点

1. 现有方法在将CLIP应用于语义分割时，受限于CLIP图像级别预训练与像素级别理解的差异，导致分割性能不佳。
2. LHT-CLIP通过分析CLIP在层、头和token级别的视觉区分性，提出语义-空间重加权、选择性头增强和异常token替换等技术。
3. 实验表明，LHT-CLIP在多个语义分割基准上取得了最先进的性能，无需额外训练即可有效提升分割效果。

## 📝 摘要（中文）

将CLIP模型扩展到语义分割仍然具有挑战性，因为其图像级别的预训练目标与密集预测所需的像素级别视觉理解不一致。虽然之前的工作通过重组最后一层和特征取得了令人鼓舞的结果，但它们通常继承了前面层的全局对齐偏差，导致次优的分割性能。本文提出了LHT-CLIP，一种新颖的无需训练的框架，系统地利用CLIP在层、头和token级别的视觉区分性。通过全面的分析，揭示了三个关键见解：(i) 最后一层主要加强图像-文本对齐，牺牲了视觉区分性（例如，ViT-B/16中的最后3层和ViT-L/14中的8层），部分原因是异常token的出现；(ii) 一部分注意力头（例如，ViT-B/16中的144个头中的10个）在数据集上表现出一致的强视觉区分性；(iii) 与正常token相比，异常token显示出稀疏且一致的激活模式。基于这些发现，提出了三种互补技术：语义-空间重加权、选择性头增强和异常token替换，以有效地恢复视觉区分性并提高分割性能，而无需任何额外的训练、辅助预训练网络或广泛的超参数调整。在8个常见的语义分割基准上的大量实验表明，LHT-CLIP在各种场景中实现了最先进的性能，突出了其有效性和实际部署能力。

## 🔬 方法详解

**问题定义**：CLIP模型在图像级别的预训练目标与语义分割任务所需的像素级别视觉理解存在偏差。现有方法虽然尝试重组CLIP的最后一层和特征，但难以克服前面层的全局对齐偏差，导致分割性能受限。此外，异常token的出现进一步降低了视觉区分性。

**核心思路**：LHT-CLIP的核心思路是系统地挖掘和增强CLIP模型在不同层、不同注意力头以及不同token级别的视觉区分性。通过分析CLIP的内部表示，识别出具有强视觉区分性的层、头和token，并针对性地进行增强或替换，从而提高分割性能。

**技术框架**：LHT-CLIP框架主要包含三个模块：语义-空间重加权、选择性头增强和异常token替换。首先，语义-空间重加权模块旨在平衡语义信息和空间信息，以提高分割的准确性。其次，选择性头增强模块选择性地增强具有强视觉区分性的注意力头，抑制噪声头的干扰。最后，异常token替换模块检测并替换异常token，以减少其对分割结果的负面影响。

**关键创新**：LHT-CLIP的关键创新在于其对CLIP模型内部表示的深入分析，并基于分析结果提出了针对性的增强策略。与现有方法不同，LHT-CLIP不仅关注最后一层特征的重组，更注重挖掘和利用CLIP模型在不同层、头和token级别的视觉区分性。此外，LHT-CLIP无需额外的训练，降低了计算成本和部署难度。

**关键设计**：语义-空间重加权模块使用可学习的权重来平衡语义信息和空间信息。选择性头增强模块通过计算每个注意力头的视觉区分性得分，选择性地增强得分较高的头。异常token替换模块使用正常token的平均表示来替换异常token。具体实现细节包括视觉区分性得分的计算方法、异常token的检测阈值等。

## 📊 实验亮点

LHT-CLIP在8个常见的语义分割基准上取得了最先进的性能，显著优于现有方法。例如，在ADE20K数据集上，LHT-CLIP的mIoU指标超过了之前的最佳方法，无需任何额外的训练或数据增强。实验结果表明，LHT-CLIP能够有效地恢复CLIP的视觉区分性，并提高分割性能。

## 🎯 应用场景

LHT-CLIP可应用于各种需要开放词汇语义分割的场景，例如自动驾驶、机器人导航、医学图像分析等。该方法无需额外训练，具有很高的实用价值，可以快速部署到现有系统中，提升视觉理解能力，并为相关应用带来更精确的环境感知。

## 📄 摘要（原文）

> Extending CLIP models to semantic segmentation remains challenging due to the misalignment between their image-level pre-training objectives and the pixel-level visual understanding required for dense prediction. While prior efforts have achieved encouraging results by reorganizing the final layer and features, they often inherit the global alignment bias of preceding layers, leading to suboptimal segmentation performance. In this work, we propose LHT-CLIP, a novel training-free framework that systematically exploits the visual discriminability of CLIP across layer, head, and token levels. Through comprehensive analysis, we reveal three key insights: (i) the final layers primarily strengthen image-text alignment with sacrifice of visual discriminability (e.g., last 3 layers in ViT-B/16 and 8 layers in ViT-L/14), partly due to the emergence of anomalous tokens; (ii) a subset of attention heads (e.g., 10 out of 144 in ViT-B/16) display consistently strong visual discriminability across datasets; (iii) abnormal tokens display sparse and consistent activation pattern compared to normal tokens. Based on these findings, we propose three complementary techniques: semantic-spatial reweighting, selective head enhancement, and abnormal token replacement to effectively restore visual discriminability and improve segmentation performance without any additional training, auxiliary pre-trained networks, or extensive hyperparameter tuning. Extensive experiments on 8 common semantic segmentation benchmarks demonstrate that LHT-CLIP achieves state-of-the-art performance across diverse scenarios, highlighting its effectiveness and practicality for real-world deployment.

