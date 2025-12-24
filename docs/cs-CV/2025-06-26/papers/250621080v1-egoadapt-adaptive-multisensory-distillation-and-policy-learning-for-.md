---
layout: default
title: "EgoAdapt: Adaptive Multisensory Distillation and Policy Learning for Efficient Egocentric Perception"
---

# EgoAdapt: Adaptive Multisensory Distillation and Policy Learning for Efficient Egocentric Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21080" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21080v1</a>
  <a href="https://arxiv.org/pdf/2506.21080.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21080v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21080v1', 'EgoAdapt: Adaptive Multisensory Distillation and Policy Learning for Efficient Egocentric Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sanjoy Chowdhury, Subrata Biswas, Sayan Nag, Tushar Nagarajan, Calvin Murdock, Ishwarya Ananthabhotla, Yijun Qian, Vamsi Krishna Ithapu, Dinesh Manocha, Ruohan Gao

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-06-26

**备注**: Accepted at ICCV 2025

---

## 💡 一句话要点

**提出EgoAdapt以解决多模态自我感知的高计算成本问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `自我中心感知` `多模态学习` `蒸馏训练` `策略学习` `高效推理`

## 📋 核心要点

1. 现有多模态自我中心感知模型在性能上虽有突破，但计算成本高，限制了其在实际应用中的部署。
2. EgoAdapt框架通过自适应跨模态蒸馏和策略学习，提升了不同自我中心感知任务的推理效率。
3. 在多个数据集上，EgoAdapt显著降低了计算资源消耗，同时保持或超越了现有模型的性能表现。

## 📝 摘要（中文）

现代感知模型，尤其是针对多感知自我中心任务的模型，虽然取得了显著的性能，但通常伴随高昂的计算成本。这些高需求在资源受限的环境中部署时面临挑战。本文提出EgoAdapt框架，能够自适应地进行跨模态蒸馏和策略学习，以实现不同自我中心感知任务的高效推理，包括自我中心动作识别、主动说话者定位和行为预测。我们提出的策略模块能够适应任务特定的动作空间，具有广泛的适用性。实验结果表明，在EPIC-Kitchens、EasyCom和Aria Everyday Activities等三个具有挑战性的自我中心数据集上，我们的方法显著提高了效率，GMACs减少了高达89.09%，参数减少了82.02%，能量减少了9.6倍，同时在许多情况下与对应的最先进模型的性能持平或超越。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态自我中心感知任务中的高计算成本问题。现有方法在性能上虽然表现优异，但在资源受限环境中的应用受到限制。

**核心思路**：EgoAdapt框架通过自适应的跨模态蒸馏和策略学习，优化了不同任务的推理过程，旨在提高效率并降低计算资源消耗。

**技术框架**：EgoAdapt的整体架构包括跨模态蒸馏模块和策略学习模块。跨模态蒸馏模块负责从不同感知模态中提取信息，而策略学习模块则根据任务特定的动作空间进行优化。

**关键创新**：EgoAdapt的主要创新在于其自适应性，能够根据不同任务的需求调整策略模块，显著提高了推理效率和资源利用率。与现有方法相比，其在多模态融合和策略优化方面具有本质的区别。

**关键设计**：在设计中，EgoAdapt采用了特定的损失函数来平衡不同模态的信息蒸馏，同时在网络结构上引入了可调节的参数设置，以适应不同任务的需求。

## 📊 实验亮点

实验结果显示，EgoAdapt在EPIC-Kitchens、EasyCom和Aria Everyday Activities数据集上，GMACs减少高达89.09%，参数减少82.02%，能量消耗降低9.6倍，同时在性能上与最先进模型持平或超越，展现出显著的效率提升。

## 🎯 应用场景

EgoAdapt框架在多个自我中心感知任务中展现出高效的推理能力，具有广泛的应用潜力。其可用于智能家居、机器人导航、虚拟现实等领域，能够在资源受限的环境中实现高效的感知与决策，推动相关技术的实际应用与发展。

## 📄 摘要（原文）

> Modern perception models, particularly those designed for multisensory egocentric tasks, have achieved remarkable performance but often come with substantial computational costs. These high demands pose challenges for real-world deployment, especially in resource-constrained environments. In this paper, we introduce EgoAdapt, a framework that adaptively performs cross-modal distillation and policy learning to enable efficient inference across different egocentric perception tasks, including egocentric action recognition, active speaker localization, and behavior anticipation. Our proposed policy module is adaptable to task-specific action spaces, making it broadly applicable. Experimental results on three challenging egocentric datasets EPIC-Kitchens, EasyCom, and Aria Everyday Activities demonstrate that our method significantly enhances efficiency, reducing GMACs by up to 89.09%, parameters up to 82.02%, and energy up to 9.6x, while still on-par and in many cases outperforming, the performance of corresponding state-of-the-art models.

