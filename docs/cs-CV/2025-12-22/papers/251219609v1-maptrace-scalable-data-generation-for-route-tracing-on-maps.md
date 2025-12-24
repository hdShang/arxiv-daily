---
layout: default
title: "MapTrace: Scalable Data Generation for Route Tracing on Maps"
---

# MapTrace: Scalable Data Generation for Route Tracing on Maps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19609" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19609v1</a>
  <a href="https://arxiv.org/pdf/2512.19609.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19609v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19609v1', 'MapTrace: Scalable Data Generation for Route Tracing on Maps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Artemis Panagopoulou, Aveek Purohit, Achin Kulshrestha, Soroosh Yazdani, Mohit Goyal

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**MapTrace：提出可扩展数据生成流程，提升MLLM地图路径追踪能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `地图路径追踪` `合成数据生成` `空间推理` `像素级标注`

## 📋 核心要点

1. 现有MLLM在地图路径追踪等精细空间理解任务中表现不足，无法有效解析和导航地图。
2. 论文提出一种可扩展的合成数据生成流程，利用合成地图和像素级解析自动生成精确标注。
3. 通过在合成数据集上微调MLLM，显著提升了模型在MapBench上的路径追踪成功率和鲁棒性。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）在许多视觉和文本推理任务上已达到类人性能，但在精细的空间理解方面，例如地图上的路径追踪，其能力仍然有限。与能够快速学习解析和导航地图的人类不同，当前的MLLM模型常常无法满足基本的路径约束，部分原因是收集大规模、像素精确的路径标注的成本过高且难度大。为了解决这个问题，我们引入了一个可扩展的合成数据生成流程，该流程利用合成地图图像和像素级解析来自动生成此项具有挑战性任务的精确标注。使用此流程，我们构建了一个包含4k张地图上23k个路径样本的微调数据集，使模型能够获得更像人类的空间能力。使用此数据集，我们对开源和专有的MLLM进行了微调。在MapBench上的结果表明，微调显著提高了鲁棒性，成功率提高了6.4个百分点，同时也降低了路径追踪误差（NDTW）。这些提升表明，预训练模型中缺乏的精细空间推理能力可以通过合成监督进行显式地教授。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在地图路径追踪任务中表现不佳的问题。现有方法依赖于人工标注的大规模数据集，成本高昂且难以获取像素级别的精确标注，导致模型无法有效学习地图的空间结构和路径约束。

**核心思路**：论文的核心思路是利用合成数据生成流程，自动创建包含精确路径标注的地图数据集。通过在合成数据上进行微调，使MLLM能够学习到精细的空间推理能力，从而提升其在真实地图上的路径追踪性能。这种方法避免了人工标注的成本和限制，具有良好的可扩展性。

**技术框架**：该方法主要包含以下几个阶段：1) 合成地图生成：生成具有多样化道路和地标的合成地图图像。2) 路径生成：在合成地图上随机生成起始点和目标点，并计算出连接它们的最佳路径。3) 像素级标注：利用地图生成过程中的信息，自动生成路径的像素级精确标注。4) 数据集构建：将合成地图图像和对应的路径标注组合成微调数据集。5) 模型微调：使用生成的数据集对MLLM进行微调，使其学习路径追踪任务。

**关键创新**：该方法最重要的技术创新点在于其可扩展的合成数据生成流程。该流程能够自动生成大规模、像素精确的路径标注，无需人工干预，从而降低了数据获取的成本和难度。此外，该方法还能够控制合成数据的多样性和复杂性，从而更好地训练模型。

**关键设计**：论文中没有详细描述具体的参数设置、损失函数和网络结构等技术细节。但是，可以推断，微调过程可能使用了标准的交叉熵损失函数来优化路径预测，并可能采用了数据增强等技术来提高模型的泛化能力。地图生成过程可能使用了程序化生成技术，以确保地图的多样性和真实性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19609v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19609v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19609v1/figures/data_dist.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，使用该方法生成的合成数据集对MLLM进行微调后，在MapBench上的路径追踪成功率提高了6.4个百分点，同时路径追踪误差（NDTW）也显著降低。这些结果表明，通过合成监督可以有效地提升MLLM在精细空间推理任务中的性能，使其更接近人类水平。

## 🎯 应用场景

该研究成果可应用于自动驾驶导航、机器人路径规划、地理信息系统等领域。通过提升模型在地图上的空间推理能力，可以实现更智能、更可靠的导航服务，并为相关应用提供更精确的地理信息支持。未来，该方法还可扩展到其他空间推理任务，例如室内导航、三维场景理解等。

## 📄 摘要（原文）

> While Multimodal Large Language Models have achieved human-like performance on many visual and textual reasoning tasks, their proficiency in fine-grained spatial understanding, such as route tracing on maps remains limited. Unlike humans, who can quickly learn to parse and navigate maps, current models often fail to respect fundamental path constraints, in part due to the prohibitive cost and difficulty of collecting large-scale, pixel-accurate path annotations. To address this, we introduce a scalable synthetic data generation pipeline that leverages synthetic map images and pixel-level parsing to automatically produce precise annotations for this challenging task. Using this pipeline, we construct a fine-tuning dataset of 23k path samples across 4k maps, enabling models to acquire more human-like spatial capabilities. Using this dataset, we fine-tune both open-source and proprietary MLLMs. Results on MapBench show that finetuning substantially improves robustness, raising success rates by up to 6.4 points, while also reducing path-tracing error (NDTW). These gains highlight that fine-grained spatial reasoning, absent in pretrained models, can be explicitly taught with synthetic supervision.

