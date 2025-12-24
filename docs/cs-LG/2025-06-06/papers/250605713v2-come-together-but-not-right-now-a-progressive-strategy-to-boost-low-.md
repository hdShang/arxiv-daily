---
layout: default
title: "Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation"
---

# Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05713" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05713v2</a>
  <a href="https://arxiv.org/pdf/2506.05713.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05713v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05713v2', 'Come Together, But Not Right Now: A Progressive Strategy to Boost Low-Rank Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhan Zhuang, Xiequn Wang, Wei Li, Yulong Zhang, Qiushi Huang, Shuhao Chen, Xuehao Wang, Yanbin Wei, Yuhe Nie, Kede Ma, Yu Zhang, Ying Wei

**分类**: cs.LG

**发布日期**: 2025-06-06 (更新: 2025-07-27)

**备注**: Accepted by ICML 2025. Code link: https://github.com/zwebzone/coto

**🔗 代码/项目**: [GITHUB](https://github.com/zwebzone/coto)

---

## 💡 一句话要点

**提出CoTo以解决低秩适应中的次优最小值问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩适应` `模型微调` `渐进式训练` `适配器合并` `剪枝鲁棒性` `损失空间探索` `合作博弈`

## 📋 核心要点

1. 现有的低秩适应方法常将适配器锁定在次优最小值，影响模型的泛化能力。
2. CoTo通过随机停用适配器，逐步增加其激活概率，促进更均衡的优化和损失空间的广泛探索。
3. 实验结果显示，CoTo在单任务性能和多任务合并准确性上均有显著提升，同时提高了剪枝的鲁棒性。

## 📝 摘要（中文）

低秩适应（LoRA）作为一种高效的参数微调技术，常常将适配器锁定在初始化附近的次优最小值，这限制了模型的泛化能力和后续操作如适配器合并与剪枝。本文提出了CoTo，一种渐进式训练策略，通过逐步增加适配器的激活概率，促进更平衡的优化和更广泛的损失空间探索。理论分析表明，CoTo增强了层级丢弃稳定性和线性模式连接性，并采用合作博弈方法量化每个适配器的边际贡献。大量实验表明，CoTo在单任务性能、多任务合并准确性、剪枝鲁棒性和训练开销方面均有显著提升，同时兼容多种LoRA变体。

## 🔬 方法详解

**问题定义**：本文旨在解决低秩适应（LoRA）中适配器锁定在次优最小值的问题，这限制了模型的泛化能力和后续操作的有效性。

**核心思路**：提出CoTo策略，通过逐步增加适配器的激活概率，并随机停用适配器，促进更均衡的优化和更广泛的损失空间探索。

**技术框架**：CoTo的整体架构包括适配器的激活概率调整、随机停用机制和合作博弈方法，分阶段进行训练以优化适配器的性能。

**关键创新**：CoTo的核心创新在于其渐进式训练策略，通过动态调整适配器的激活状态，增强了模型的优化能力，与传统方法相比，能够更有效地探索损失空间。

**关键设计**：在参数设置上，CoTo采用了动态调整的激活概率，并设计了适配器的随机停用机制，结合层级丢弃稳定性和线性模式连接性，优化了损失函数的设计。

## 📊 实验亮点

实验结果表明，CoTo在单任务性能上提升了X%，在多任务合并准确性上提高了Y%，并且在剪枝鲁棒性方面表现优异，相较于基线方法，训练开销降低了Z%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等大规模模型的微调，能够有效提升模型在特定任务上的性能，具有广泛的实际价值和未来影响。通过提高模型的泛化能力和适应性，CoTo为多任务学习和模型压缩提供了新的思路。

## 📄 摘要（原文）

> Low-rank adaptation (LoRA) has emerged as a leading parameter-efficient fine-tuning technique for adapting large foundation models, yet it often locks adapters into suboptimal minima near their initialization. This hampers model generalization and limits downstream operators such as adapter merging and pruning. Here, we propose CoTo, a progressive training strategy that gradually increases adapters' activation probability over the course of fine-tuning. By stochastically deactivating adapters, CoTo encourages more balanced optimization and broader exploration of the loss landscape. We provide a theoretical analysis showing that CoTo promotes layer-wise dropout stability and linear mode connectivity, and we adopt a cooperative-game approach to quantify each adapter's marginal contribution. Extensive experiments demonstrate that CoTo consistently boosts single-task performance, enhances multi-task merging accuracy, improves pruning robustness, and reduces training overhead, all while remaining compatible with diverse LoRA variants. Code is available at https://github.com/zwebzone/coto.

