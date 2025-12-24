---
layout: default
title: "FastVGGT: Training-Free Acceleration of Visual Geometry Transformer"
---

# FastVGGT: Training-Free Acceleration of Visual Geometry Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02560" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02560v2</a>
  <a href="https://arxiv.org/pdf/2509.02560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02560v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02560v2', 'FastVGGT: Training-Free Acceleration of Visual Geometry Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: You Shen, Zhipeng Zhang, Yansong Qu, Xiawu Zheng, Jiayi Ji, Shengchuan Zhang, Liujuan Cao

**分类**: cs.CV

**发布日期**: 2025-09-02 (更新: 2025-11-09)

**🔗 代码/项目**: [PROJECT_PAGE](https://mystorm16.github.io/fastvggt/)

---

## 💡 一句话要点

**FastVGGT：通过无训练Token合并加速视觉几何Transformer，提升3D视觉效率。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉` `Transformer` `Token合并` `模型加速` `无训练` `长序列` `三维重建`

## 📋 核心要点

1. 现有3D视觉Transformer模型在处理长序列图像时，推理效率低，难以扩展。
2. 提出FastVGGT，通过无训练的token合并策略，减少冗余计算，加速VGGT模型。
3. 实验表明，FastVGGT在保持重建能力的同时，实现了4倍的加速，并减轻了长序列误差累积。

## 📝 摘要（中文）

三维视觉基础模型最近在3D感知方面表现出卓越的能力。然而，由于推理时效率低下，将这些模型扩展到长序列图像输入仍然是一个重大挑战。本文对最先进的前馈视觉几何模型VGGT进行了详细分析，并确定了其主要瓶颈。可视化进一步揭示了注意力图中的token崩溃现象。受这些发现的启发，我们探索了token合并在前馈视觉几何模型中的潜力。由于3D模型的独特架构和特定于任务的属性，直接应用现有的合并技术具有挑战性。为此，我们提出了FastVGGT，它首次通过一种无训练机制在3D领域利用token合并来加速VGGT。我们设计了一种独特的token划分策略，专门为3D架构和任务量身定制，有效地消除了冗余计算，同时保留了VGGT强大的重建能力。在多个3D几何基准上的大量实验验证了我们方法的有效性。值得注意的是，对于1000个输入图像，FastVGGT实现了比VGGT快4倍的速度，同时减轻了长序列场景中的误差累积。这些发现强调了token合并作为可扩展3D视觉系统的原则性解决方案的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决3D视觉Transformer模型，特别是VGGT模型，在处理长序列图像输入时推理效率低下的问题。现有方法在扩展模型到长序列输入时面临计算量显著增加的挑战，导致实际应用受限。VGGT模型在注意力机制中存在token崩溃现象，进一步加剧了计算冗余。

**核心思路**：论文的核心思路是通过token合并来减少VGGT模型中的冗余计算，从而加速推理过程。通过合并相似或不重要的token，可以有效减少Transformer层的计算量，提高模型效率。论文特别强调了无训练的token合并策略，避免了额外的训练开销和对原始模型性能的潜在影响。

**技术框架**：FastVGGT的整体框架是在VGGT模型的基础上引入token合并模块。该模块在Transformer层之间进行token划分和合并操作。具体流程包括：1) 输入图像序列经过VGGT的初始处理；2) 在Transformer层中，应用token划分策略将token分成不同的组；3) 对每组token进行合并，减少token数量；4) 合并后的token继续通过后续的Transformer层；5) 最终输出3D重建结果。

**关键创新**：论文的关键创新在于提出了一种针对3D视觉Transformer的无训练token合并策略。与直接应用现有token合并技术不同，FastVGGT针对3D架构和任务特性，设计了独特的token划分策略，避免了性能下降。这种无训练的方式使得FastVGGT可以即插即用，无需重新训练模型，降低了使用成本。

**关键设计**：FastVGGT的关键设计包括：1) Token划分策略：根据3D场景的几何特性，将token划分为不同的组，例如基于空间位置或特征相似度。2) Token合并准则：采用无训练的方式，例如基于token的能量或重要性进行排序，合并低能量或不重要的token。3) 合并比例：根据计算资源和性能需求，动态调整合并比例，以达到最佳的加速效果。论文未明确提及损失函数和网络结构的修改，重点在于token合并模块的设计。

## 📊 实验亮点

实验结果表明，FastVGGT在1000个输入图像的情况下，实现了比VGGT快4倍的加速。同时，FastVGGT有效地减轻了长序列场景中的误差累积，保持了VGGT强大的重建能力。这些结果验证了token合并作为可扩展3D视觉系统有效解决方案的潜力。

## 🎯 应用场景

FastVGGT在机器人导航、自动驾驶、三维重建等领域具有广泛的应用前景。通过提高3D视觉模型的推理效率，可以支持更复杂的场景理解和更实时的决策。该研究有助于推动3D视觉技术在资源受限设备上的部署，例如移动机器人和嵌入式系统，并加速相关应用的落地。

## 📄 摘要（原文）

> Foundation models for 3D vision have recently demonstrated remarkable capabilities in 3D perception. However, scaling these models to long-sequence image inputs remains a significant challenge due to inference-time inefficiency. In this work, we present a detailed analysis of VGGT, a state-of-the-art feed-forward visual geometry model and identify its primary bottleneck. Visualization further reveals a token collapse phenomenon in the attention maps. Motivated by these findings, we explore the potential of token merging in the feed-forward visual geometry model. Owing to the unique architectural and task-specific properties of 3D models, directly applying existing merging techniques proves challenging. To this end, we propose FastVGGT, which, for the first time, leverages token merging in the 3D domain through a training-free mechanism for accelerating VGGT. we devise a unique token partitioning strategy tailored to 3D architectures and tasks, effectively eliminating redundant computation while preserving VGGT's powerful reconstruction capacity. Extensive experiments on multiple 3D geometry benchmarks validate the effectiveness of our approach. Notably, with 1000 input images, FastVGGT achieves a 4x speedup over VGGT while mitigating error accumulation in long-sequence scenarios. These findings underscore the potential of token merging as a principled solution for scalable 3D vision systems. Code is available at: https://mystorm16.github.io/fastvggt/.

