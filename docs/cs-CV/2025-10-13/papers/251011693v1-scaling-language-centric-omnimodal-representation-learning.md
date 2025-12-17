---
layout: default
title: Scaling Language-Centric Omnimodal Representation Learning
---

# Scaling Language-Centric Omnimodal Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11693" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11693v1</a>
  <a href="https://arxiv.org/pdf/2510.11693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11693v1" onclick="toggleFavorite(this, '2510.11693v1', 'Scaling Language-Centric Omnimodal Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenghao Xiao, Hou Pong Chan, Hao Zhang, Weiwen Xu, Mahani Aljunied, Yu Rong

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-10-13

**备注**: NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/LCO-Embedding/LCO-Embedding)

---

## 💡 一句话要点

**提出LCO-Emb框架，通过语言中心的多模态表征学习，提升跨模态检索性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `跨模态检索` `大型语言模型` `对比学习` `表征学习` `生成式预训练` `视觉-语言`

## 📋 核心要点

1. 现有基于MLLM的多模态嵌入方法缺乏对其优越性的深入理解，需要探究其内在机制。
2. 论文提出LCO-Emb框架，利用MLLM生成式预训练中的隐式跨模态对齐，并通过对比学习进行优化。
3. 实验表明，LCO-Emb在多种模态上取得了SOTA性能，并验证了生成能力与表示能力之间的缩放定律。

## 📝 摘要（中文）

本文旨在探索基于多模态大型语言模型（MLLM）并采用对比学习（CL）进行微调的多模态嵌入方法的优势。研究表明，MLLM方法的一个关键优势在于生成式预训练期间实现的隐式跨模态对齐，其中语言解码器学习利用共享表示空间内的多模态信号来生成单模态输出。通过对各向异性和核相似性结构的分析，证实了MLLM表示中潜在对齐的出现，使得CL能够作为轻量级的优化阶段。基于此，我们提出了一个以语言为中心的全模态嵌入框架，称为LCO-Emb。在不同的骨干网络和基准测试中进行的大量实验证明了其有效性，并在各种模态中实现了最先进的性能。此外，我们还发现了一个生成-表示缩放定律（GRSL），表明通过对比优化获得的表示能力与MLLM的生成能力呈正相关。这表明，提高生成能力是增强表示质量的有效范例。我们对GRSL进行了理论解释，将MLLM的生成质量与其表示性能的上限正式联系起来，并在具有挑战性的低资源视觉-文档检索任务中验证了它，表明在CL之前进行持续的生成式预训练可以进一步增强模型嵌入能力的潜力。代码、模型和资源可在https://github.com/LCO-Embedding/LCO-Embedding获取。

## 🔬 方法详解

**问题定义**：论文旨在解决如何有效学习多模态数据的统一表征，从而提升跨模态检索等任务的性能。现有方法，特别是基于对比学习的方法，虽然取得了一定的进展，但缺乏对MLLM在多模态表征学习中作用的深入理解，以及如何更好地利用MLLM的生成能力来提升表征质量。

**核心思路**：论文的核心思路是，MLLM在生成式预训练阶段已经学习到了隐式的跨模态对齐，这种对齐使得语言解码器能够利用多模态信号生成单模态输出。因此，可以通过对比学习对MLLM的表征进行微调，从而进一步提升表征的质量。此外，论文还提出了生成-表示缩放定律（GRSL），认为MLLM的生成能力越强，其表征能力也越强。

**技术框架**：LCO-Emb框架主要包含两个阶段：1) 利用MLLM进行生成式预训练，学习跨模态的隐式对齐；2) 使用对比学习对MLLM的表征进行微调，进一步提升表征的质量。框架可以采用不同的MLLM作为骨干网络，例如BLIP-2、InstructBLIP等。在对比学习阶段，可以使用不同的对比损失函数，例如InfoNCE。

**关键创新**：论文最重要的技术创新点在于提出了LCO-Emb框架，并揭示了MLLM在多模态表征学习中的作用。与现有方法相比，LCO-Emb更加注重利用MLLM的生成能力，并通过对比学习进行优化。此外，论文还提出了生成-表示缩放定律（GRSL），为多模态表征学习提供了一个新的视角。

**关键设计**：在生成式预训练阶段，可以使用不同的数据集和训练策略。在对比学习阶段，需要选择合适的对比损失函数和负样本采样策略。论文中使用了InfoNCE损失函数，并采用hard negative mining策略。此外，论文还对MLLM的结构进行了一些调整，例如添加了额外的线性层来映射不同模态的特征。

## 📊 实验亮点

LCO-Emb在多个跨模态检索任务上取得了SOTA性能。例如，在视觉-文档检索任务中，LCO-Emb相比于现有方法取得了显著的提升。此外，实验还验证了生成-表示缩放定律（GRSL），表明通过持续的生成式预训练可以进一步提升模型嵌入能力的潜力。

## 🎯 应用场景

该研究成果可广泛应用于跨模态信息检索、视觉问答、图像描述生成等领域。通过提升多模态表征的质量，可以改善用户在不同模态数据之间进行信息交互的体验，例如，用户可以通过文本查询检索相关的图像或视频，或者通过图像查询检索相关的文档。

## 📄 摘要（原文）

> Recent multimodal embedding approaches leveraging multimodal large language models (MLLMs) fine-tuned with contrastive learning (CL) have shown promising results, yet the underlying reasons behind their superiority remain underexplored. This work argues that a crucial advantage of MLLM-based approaches stems from implicit cross-modal alignment achieved during generative pretraining, where the language decoder learns to exploit multimodal signals within a shared representation space for generating unimodal outputs. Through analysis of anisotropy and kernel similarity structure, we empirically confirm that latent alignment emerges within MLLM representations, allowing CL to serve as a lightweight refinement stage. Leveraging this insight, we propose a Language-Centric Omnimodal Embedding framework, termed LCO-Emb. Extensive experiments across diverse backbones and benchmarks demonstrate its effectiveness, achieving state-of-the-art performance across modalities. Furthermore, we identify a Generation-Representation Scaling Law (GRSL), showing that the representational capabilities gained through contrastive refinement scales positively with the MLLM's generative capabilities. This suggests that improving generative abilities evolves as an effective paradigm for enhancing representation quality. We provide a theoretical explanation of GRSL, which formally links the MLLM's generative quality to the upper bound on its representation performance, and validate it on a challenging, low-resource visual-document retrieval task, showing that continual generative pretraining before CL can further enhance the potential of a model's embedding capabilities. Codes, models, and resources are available at https://github.com/LCO-Embedding/LCO-Embedding.

