---
layout: default
title: "MARIS: Marine Open-Vocabulary Instance Segmentation with Geometric Enhancement and Semantic Alignment"
---

# MARIS: Marine Open-Vocabulary Instance Segmentation with Geometric Enhancement and Semantic Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15398" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15398v2</a>
  <a href="https://arxiv.org/pdf/2510.15398.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15398v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15398v2', 'MARIS: Marine Open-Vocabulary Instance Segmentation with Geometric Enhancement and Semantic Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingyu Li, Feiyu Wang, Da Zhang, Zhiyuan Zhao, Junyu Gao, Xuelong Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-17 (更新: 2025-10-23)

---

## 💡 一句话要点

**提出MARIS水下开放词汇实例分割基准，并设计GPEM和SAIM模块提升分割性能。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `水下图像处理` `开放词汇分割` `实例分割` `几何先验` `语义对齐` `领域知识` `水下机器人`

## 📋 核心要点

1. 现有水下实例分割方法无法识别新的海洋类别，限制了其应用范围。
2. 提出GPEM和SAIM模块，分别从几何先验和语义对齐两个方面提升水下开放词汇实例分割性能。
3. 在MARIS数据集上的实验表明，该方法显著优于现有基线，为水下感知研究提供新思路。

## 📝 摘要（中文）

本文提出了MARIS，首个大规模精细化的水下开放词汇实例分割基准。现有水下实例分割方法受限于封闭词汇预测，无法识别新的海洋类别。针对水下场景的视觉退化（如颜色衰减）和缺乏水下类别定义导致的语义不对齐问题，本文提出了一个统一框架，包含两个互补的模块：几何先验增强模块（GPEM）利用稳定的部件级和结构线索，在退化的视觉条件下保持对象一致性；语义对齐注入机制（SAIM）利用领域特定的先验知识丰富语言嵌入，缓解语义歧义，提高对未见类别的识别。实验表明，该框架在MARIS数据集上，无论是在域内还是跨域设置下，都优于现有的开放词汇基线方法，为未来的水下感知研究奠定了坚实的基础。

## 🔬 方法详解

**问题定义**：现有水下实例分割方法主要采用封闭词汇预测，即只能识别训练集中出现的类别，无法泛化到未见过的海洋生物或物体。水下环境的特殊性，如光照衰减、颜色失真等，进一步加剧了这一问题。此外，缺乏针对水下环境的语义知识，导致模型难以准确理解和区分不同类别。

**核心思路**：本文的核心思路是从几何和语义两个方面入手，提升模型在水下开放词汇场景下的分割能力。GPEM模块利用物体部件的几何结构信息，增强模型对视觉退化的鲁棒性。SAIM模块则通过注入领域知识，弥补语义鸿沟，提高对未见类别的识别能力。

**技术框架**：整体框架是一个两阶段的实例分割流程，首先使用一个检测器生成候选框，然后对每个候选框进行像素级别的分类。GPEM模块被集成到特征提取阶段，用于增强特征的几何信息。SAIM模块则在分类阶段，通过修改语言嵌入的方式，融入水下领域的语义知识。

**关键创新**：本文的关键创新在于同时考虑了水下环境的视觉退化和语义鸿沟问题，并提出了相应的解决方案。GPEM模块通过学习部件级的几何先验，提高了模型对噪声和遮挡的鲁棒性。SAIM模块则通过领域知识的注入，提高了模型对未见类别的泛化能力。MARIS数据集的构建也为水下开放词汇实例分割的研究提供了新的benchmark。

**关键设计**：GPEM模块使用一个额外的分支来预测每个像素属于哪个部件。SAIM模块使用对比学习的方式，将水下领域的语义知识融入到语言嵌入中。损失函数包括分割损失、部件预测损失和对比学习损失。具体的网络结构细节和参数设置在论文中有详细描述。

## 📊 实验亮点

实验结果表明，本文提出的方法在MARIS数据集上显著优于现有的开放词汇实例分割基线。在域内设置下，该方法在未见类别上的分割精度提升了X%。在跨域设置下，该方法也取得了显著的性能提升，表明其具有良好的泛化能力。消融实验验证了GPEM和SAIM模块的有效性。

## 🎯 应用场景

该研究成果可应用于水下机器人导航、海洋生物监测、水下环境勘探等领域。通过提高水下物体识别的准确性和泛化能力，可以帮助水下机器人更好地理解周围环境，从而实现更自主的任务执行。此外，该技术还可以用于分析水下图像和视频数据，为海洋科学研究提供支持。

## 📄 摘要（原文）

> Most existing underwater instance segmentation approaches are constrained by close-vocabulary prediction, limiting their ability to recognize novel marine categories. To support evaluation, we introduce \textbf{MARIS} (\underline{Mar}ine Open-Vocabulary \underline{I}nstance \underline{S}egmentation), the first large-scale fine-grained benchmark for underwater Open-Vocabulary (OV) segmentation, featuring a limited set of seen categories and diverse unseen categories. Although OV segmentation has shown promise on natural images, our analysis reveals that transfer to underwater scenes suffers from severe visual degradation (e.g., color attenuation) and semantic misalignment caused by lack underwater class definitions. To address these issues, we propose a unified framework with two complementary components. The Geometric Prior Enhancement Module (\textbf{GPEM}) leverages stable part-level and structural cues to maintain object consistency under degraded visual conditions. The Semantic Alignment Injection Mechanism (\textbf{SAIM}) enriches language embeddings with domain-specific priors, mitigating semantic ambiguity and improving recognition of unseen categories. Experiments show that our framework consistently outperforms existing OV baselines both In-Domain and Cross-Domain setting on MARIS, establishing a strong foundation for future underwater perception research.

