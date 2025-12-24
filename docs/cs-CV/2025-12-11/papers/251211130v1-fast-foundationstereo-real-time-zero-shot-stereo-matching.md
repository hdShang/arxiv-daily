---
layout: default
title: "Fast-FoundationStereo: Real-Time Zero-Shot Stereo Matching"
---

# Fast-FoundationStereo: Real-Time Zero-Shot Stereo Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.11130" class="toolbar-btn" target="_blank">📄 arXiv: 2512.11130v1</a>
  <a href="https://arxiv.org/pdf/2512.11130.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.11130v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.11130v1', 'Fast-FoundationStereo: Real-Time Zero-Shot Stereo Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bowen Wen, Shaurya Dewan, Stan Birchfield

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-11

**🔗 代码/项目**: [PROJECT_PAGE](https://nvlabs.github.io/Fast-FoundationStereo/)

---

## 💡 一句话要点

**提出Fast-FoundationStereo，实现零样本立体匹配的实时性与高精度。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `立体匹配` `零样本学习` `知识蒸馏` `神经架构搜索` `结构化剪枝` `实时性` `深度估计`

## 📋 核心要点

1. 现有立体匹配基础模型虽然零样本泛化能力强，但计算复杂度高，难以满足实时应用的需求。
2. Fast-FoundationStereo通过知识蒸馏、神经架构搜索和结构化剪枝等技术，在保证精度的前提下大幅提升速度。
3. 该方法在零样本立体匹配任务上实现了超过10倍的加速，并在实时性方面达到了新的高度。

## 📝 摘要（中文）

本文提出Fast-FoundationStereo，旨在解决立体匹配基础模型在零样本泛化能力强但计算量大的问题，以及高效立体匹配架构鲁棒性不足且需要昂贵的领域微调的问题。该方法采用分而治之的加速策略，包括：知识蒸馏将混合骨干网络压缩为高效的学生网络；块状神经架构搜索自动发现延迟预算下的最优代价滤波设计；结构化剪枝消除迭代细化模块中的冗余。此外，引入自动伪标签生成流程，生成140万张真实场景立体图像对，以补充合成训练数据并促进知识蒸馏。最终模型比FoundationStereo快10倍以上，同时保持接近的零样本精度，在实时方法中建立了新的state-of-the-art。

## 🔬 方法详解

**问题定义**：论文旨在解决现有立体匹配方法在零样本泛化能力和实时性之间的trade-off问题。现有的立体匹配基础模型虽然具有强大的零样本泛化能力，但计算量巨大，难以满足实时应用的需求。而高效的立体匹配架构通常需要针对特定领域进行微调，泛化能力较弱。

**核心思路**：论文的核心思路是采用分而治之的加速策略，通过知识蒸馏、神经架构搜索和结构化剪枝等技术，在保证零样本泛化能力的前提下，大幅降低计算复杂度，实现实时立体匹配。

**技术框架**：Fast-FoundationStereo的整体框架包含三个主要模块：1) 混合骨干网络的知识蒸馏，将复杂的教师模型压缩为高效的学生模型；2) 基于块状神经架构搜索的代价滤波模块，自动搜索最优的滤波结构；3) 迭代细化模块的结构化剪枝，去除冗余连接。此外，还包含一个自动伪标签生成流程，用于生成大规模的真实场景立体图像对。

**关键创新**：该方法最重要的技术创新在于将知识蒸馏、神经架构搜索和结构化剪枝三种技术有机结合，并应用于零样本立体匹配任务。通过知识蒸馏，可以有效地将基础模型的知识迁移到轻量级的学生模型中。神经架构搜索可以自动发现最优的代价滤波结构，而结构化剪枝可以进一步降低模型的计算复杂度。

**关键设计**：在知识蒸馏方面，论文采用了混合骨干网络作为教师模型，并设计了专门的蒸馏损失函数。在神经架构搜索方面，论文采用了块状搜索空间，并引入了延迟预算约束。在结构化剪枝方面，论文采用了基于L1范数的剪枝方法，并对迭代细化模块进行了精细的剪枝。

## 📊 实验亮点

Fast-FoundationStereo在多个零样本立体匹配数据集上取得了显著的性能提升。实验结果表明，该方法比FoundationStereo快10倍以上，同时保持了接近的零样本精度。此外，该方法在实时性方面也优于其他现有的立体匹配方法，在KITTI数据集上达到了实时帧率。

## 🎯 应用场景

Fast-FoundationStereo具有广泛的应用前景，例如自动驾驶、机器人导航、增强现实等。该方法可以在资源受限的平台上实现高精度的实时立体匹配，为这些应用提供可靠的三维感知能力。未来，该方法可以进一步扩展到其他视觉任务，例如深度估计、三维重建等。

## 📄 摘要（原文）

> Stereo foundation models achieve strong zero-shot generalization but remain computationally prohibitive for real-time applications. Efficient stereo architectures, on the other hand, sacrifice robustness for speed and require costly per-domain fine-tuning. To bridge this gap, we present Fast-FoundationStereo, a family of architectures that achieve, for the first time, strong zero-shot generalization at real-time frame rate. We employ a divide-and-conquer acceleration strategy with three components: (1) knowledge distillation to compress the hybrid backbone into a single efficient student; (2) blockwise neural architecture search for automatically discovering optimal cost filtering designs under latency budgets, reducing search complexity exponentially; and (3) structured pruning for eliminating redundancy in the iterative refinement module. Furthermore, we introduce an automatic pseudo-labeling pipeline used to curate 1.4M in-the-wild stereo pairs to supplement synthetic training data and facilitate knowledge distillation. The resulting model can run over 10x faster than FoundationStereo while closely matching its zero-shot accuracy, thus establishing a new state-of-the-art among real-time methods. Project page: https://nvlabs.github.io/Fast-FoundationStereo/

