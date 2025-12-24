---
layout: default
title: "No Other Representation Component Is Needed: Diffusion Transformers Can Provide Representation Guidance by Themselves"
---

# No Other Representation Component Is Needed: Diffusion Transformers Can Provide Representation Guidance by Themselves

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02831" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02831v4</a>
  <a href="https://arxiv.org/pdf/2505.02831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02831v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02831v4', 'No Other Representation Component Is Needed: Diffusion Transformers Can Provide Representation Guidance by Themselves')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dengyang Jiang, Mengmeng Wang, Liuzhuozheng Li, Lei Zhang, Haoyu Wang, Wei Wei, Guang Dai, Yanning Zhang, Jingdong Wang

**分类**: cs.CV

**发布日期**: 2025-05-05 (更新: 2025-05-17)

**备注**: Self-Representation Alignment for Diffusion Transformers. Code: https://github.com/vvvvvjdy/SRA

---

## 💡 一句话要点

**提出自我表征对齐方法以优化扩散变换器的生成质量**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散变换器` `自我蒸馏` `表征学习` `生成模型` `深度学习`

## 📋 核心要点

1. 现有方法依赖复杂的外部表征训练框架或预训练模型，限制了扩散变换器的灵活性和效率。
2. 本文提出自我表征对齐（SRA）方法，通过自我蒸馏在生成训练中实现表征指导，简化了训练过程。
3. 实验表明，SRA在多种扩散变换器上均显著提升性能，超越传统方法并与依赖外部先验的方法相当。

## 📝 摘要（中文）

近期研究表明，学习有意义的内部表征可以加速生成训练并提升扩散变换器的生成质量。然而，现有方法需引入复杂的外部表征训练框架或依赖大规模预训练的表征基础模型。本文提出自我表征对齐（SRA）方法，利用扩散变换器的独特判别过程，在生成训练过程中自我蒸馏获取表征指导。SRA通过将早期层输出的高噪声潜在表征与后期层的低噪声表征对齐，逐步增强整体表征学习。实验结果显示，SRA在DiTs和SiTs上均显著提升性能，超越依赖复杂外部框架的方法，并与依赖强大外部表征先验的方法表现相当。

## 🔬 方法详解

**问题定义**：现有的扩散变换器在生成训练过程中需要依赖外部复杂的表征训练框架或预训练模型，导致训练效率低下和灵活性不足。

**核心思路**：本文提出的自我表征对齐（SRA）方法，利用扩散变换器的判别特性，通过自我蒸馏的方式在生成训练中实现表征指导，避免了外部依赖。

**技术框架**：SRA方法的整体流程包括：首先在生成训练过程中，获取早期层的高噪声潜在表征；然后将其与后期层的低噪声表征进行对齐，以增强表征学习。

**关键创新**：SRA的主要创新在于其自我蒸馏机制，使得扩散变换器能够在没有外部表征组件的情况下，独立提供表征指导，这与传统方法的依赖关系形成鲜明对比。

**关键设计**：在SRA中，关键设计包括对潜在表征的噪声水平进行控制，以及在对齐过程中使用的损失函数，这些设计确保了表征学习的有效性和稳定性。

## 📊 实验亮点

实验结果显示，SRA方法在DiTs和SiTs上均实现了显著的性能提升，超越了依赖复杂外部框架的传统方法，且在性能上与依赖强大外部表征先验的方法相当，展示了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、视频生成和其他需要高质量生成模型的任务。通过简化训练过程，SRA方法能够在资源有限的环境中实现高效的生成模型训练，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent studies have demonstrated that learning a meaningful internal representation can both accelerate generative training and enhance the generation quality of diffusion transformers. However, existing approaches necessitate to either introduce an external and complex representation training framework or rely on a large-scale, pre-trained representation foundation model to provide representation guidance during the original generative training process. In this study, we posit that the unique discriminative process inherent to diffusion transformers enables them to offer such guidance without requiring external representation components. We therefore propose Self-Representation Alignment (SRA), a simple yet straightforward method that obtains representation guidance through a self-distillation manner. Specifically, SRA aligns the output latent representation of the diffusion transformer in the earlier layer with higher noise to that in the later layer with lower noise to progressively enhance the overall representation learning during only the generative training process. Experimental results indicate that applying SRA to DiTs and SiTs yields consistent performance improvements. Moreover, SRA not only significantly outperforms approaches relying on auxiliary, complex representation training frameworks but also achieves performance comparable to methods that are heavily dependent on powerful external representation priors.

