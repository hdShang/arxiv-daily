---
layout: default
title: "RobIA: Robust Instance-aware Continual Test-time Adaptation for Deep Stereo"
---

# RobIA: Robust Instance-aware Continual Test-time Adaptation for Deep Stereo

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10107" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10107v1</a>
  <a href="https://arxiv.org/pdf/2511.10107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10107v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.10107v1', 'RobIA: Robust Instance-aware Continual Test-time Adaptation for Deep Stereo')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jueun Ko, Hyewon Park, Hyesong Choi, Dongbo Min

**分类**: cs.CV

**发布日期**: 2025-11-13

**备注**: Accepted by Neural Information Processing Systems (NeurIPS) 2025

---

## 💡 一句话要点

**提出RobIA框架，用于深度立体匹配中鲁棒的、实例感知的持续测试时自适应**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `深度立体匹配` `测试时自适应` `持续学习` `混合专家模型` `伪监督学习`

## 📋 核心要点

1. 现有测试时自适应方法依赖于静态目标域假设和输入不变的自适应策略，限制了其在持续域偏移下的有效性。
2. RobIA框架通过Attend-and-Excite混合专家模块和鲁棒的AdaptBN教师模型，实现输入特定的自适应和更广泛的监督。
3. 实验结果表明，RobIA在动态目标域中表现出优越的自适应性能，同时保持了计算效率。

## 📝 摘要（中文）

本文针对真实场景中深度立体匹配因动态域偏移、稀疏或不可靠监督以及获取密集真值标签的高成本而面临的挑战，提出了一种新颖的鲁棒、实例感知的持续测试时自适应（CTTA）框架RobIA。RobIA集成了两个关键组件：(1) Attend-and-Excite混合专家模块（AttEx-MoE），这是一个参数高效的模块，通过轻量级的自注意力机制动态地将输入路由到冻结的专家，该机制专为极线几何设计；(2) 鲁棒的AdaptBN教师模型，这是一个基于PEFT的教师模型，通过补充稀疏的手工标签来提供密集的伪监督。这种策略实现了输入特定的灵活性和广泛的监督覆盖，从而提高了域偏移下的泛化能力。大量实验表明，RobIA在动态目标域中实现了卓越的自适应性能，同时保持了计算效率。

## 🔬 方法详解

**问题定义**：深度立体匹配在真实世界中面临动态域偏移的问题，现有的测试时自适应方法难以应对持续变化的场景，并且依赖于静态假设，泛化能力不足。此外，获取密集的真值标签成本高昂，稀疏或不可靠的监督信息也限制了模型的性能。

**核心思路**：RobIA的核心思路是利用实例感知的自适应策略，针对每个输入样本动态地调整模型参数，从而更好地适应目标域的分布。通过混合专家模型和伪监督学习，提高模型的鲁棒性和泛化能力。

**技术框架**：RobIA框架主要包含两个核心模块：Attend-and-Excite混合专家模块（AttEx-MoE）和鲁棒的AdaptBN教师模型。AttEx-MoE负责动态地将输入路由到不同的专家，实现输入特定的自适应。AdaptBN教师模型则利用稀疏的手工标签生成密集的伪标签，为模型的训练提供更全面的监督信息。整个框架通过持续的测试时自适应，不断优化模型参数，以适应动态变化的目标域。

**关键创新**：RobIA的关键创新在于其实例感知的自适应策略和混合专家模型的设计。传统的测试时自适应方法通常采用输入不变的自适应策略，难以应对复杂的域偏移。RobIA通过AttEx-MoE模块，根据输入样本的特征动态地选择合适的专家，从而实现更精细的自适应。此外，AdaptBN教师模型利用伪标签学习，有效缓解了真值标签稀疏的问题。

**关键设计**：AttEx-MoE模块采用轻量级的自注意力机制，根据极线几何信息动态地选择专家。AdaptBN教师模型基于PEFT（Parameter-Efficient Fine-Tuning）方法，在保持计算效率的同时，实现模型的快速自适应。损失函数方面，结合了手工标签和伪标签的监督信息，以提高模型的训练效果。

## 📊 实验亮点

RobIA在动态目标域上实现了卓越的自适应性能，显著优于现有的测试时自适应方法。实验结果表明，RobIA在保持计算效率的同时，能够有效地应对复杂的域偏移，提高了深度估计的准确性和鲁棒性。具体性能数据和对比基线信息需要在论文中查找。

## 🎯 应用场景

RobIA框架可应用于自动驾驶、机器人导航、三维重建等领域，尤其适用于需要在动态变化环境中进行深度估计的场景。该研究的实际价值在于提高了深度估计的鲁棒性和泛化能力，降低了对大量标注数据的依赖，为相关应用提供了更可靠的技术支持。未来，该方法有望进一步扩展到其他视觉任务和领域。

## 📄 摘要（原文）

> Stereo Depth Estimation in real-world environments poses significant challenges due to dynamic domain shifts, sparse or unreliable supervision, and the high cost of acquiring dense ground-truth labels. While recent Test-Time Adaptation (TTA) methods offer promising solutions, most rely on static target domain assumptions and input-invariant adaptation strategies, limiting their effectiveness under continual shifts. In this paper, we propose RobIA, a novel Robust, Instance-Aware framework for Continual Test-Time Adaptation (CTTA) in stereo depth estimation. RobIA integrates two key components: (1) Attend-and-Excite Mixture-of-Experts (AttEx-MoE), a parameter-efficient module that dynamically routes input to frozen experts via lightweight self-attention mechanism tailored to epipolar geometry, and (2) Robust AdaptBN Teacher, a PEFT-based teacher model that provides dense pseudo-supervision by complementing sparse handcrafted labels. This strategy enables input-specific flexibility, broad supervision coverage, improving generalization under domain shift. Extensive experiments demonstrate that RobIA achieves superior adaptation performance across dynamic target domains while maintaining computational efficiency.

