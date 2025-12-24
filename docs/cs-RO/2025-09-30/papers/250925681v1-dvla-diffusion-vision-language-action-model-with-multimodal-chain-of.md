---
layout: default
title: "dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought"
---

# dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25681" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25681v1</a>
  <a href="https://arxiv.org/pdf/2509.25681.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25681v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25681v1', 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Wen, Minjie Zhu, Jiaming Liu, Zhiyuan Liu, Yicun Yang, Linfeng Zhang, Shanghang Zhang, Yichen Zhu, Yi Xu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-30

**备注**: technique report

---

## 💡 一句话要点

**提出dVLA：基于扩散模型和多模态CoT的视觉-语言-动作机器人控制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `扩散模型` `多模态学习` `机器人控制` `思维链` `跨模态推理` `强化学习`

## 📋 核心要点

1. 现有VLA模型在跨模态推理和泛化能力上存在不足，难以应对复杂任务和新环境。
2. dVLA采用扩散模型，结合多模态思维链，统一优化视觉、语言和动作，提升跨模态推理能力。
3. 实验表明，dVLA在LIBERO基准测试和真实机器人任务中均取得SOTA性能，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种基于扩散模型的视觉-语言-动作（VLA）模型dVLA，它利用多模态思维链在单个系统中统一视觉感知、语言推理和机器人控制。dVLA在单一扩散目标下联合优化感知、语言理解和动作，从而实现更强的跨模态推理和对新指令和对象的更好泛化。为了实际部署，我们通过结合前缀注意力掩码和KV缓存两种加速策略来缓解推理延迟，从而在测试时推理中实现高达数倍的加速。我们在模拟和真实世界中评估了dVLA：在LIBERO基准测试中，它实现了最先进的性能，平均成功率为96.4%，始终优于离散和连续动作策略；在真实的Franka机器人上，它成功地完成了一系列不同的任务，包括需要多步骤规划的具有挑战性的料箱拣选任务，展示了强大的真实世界性能。总之，这些结果强调了统一扩散框架在实用、高性能VLA机器人技术中的前景。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型在处理复杂机器人任务时，面临跨模态推理能力不足和泛化性差的问题。尤其是在需要多步骤规划和处理新颖对象的场景下，现有方法难以有效整合视觉信息、语言指令和动作控制，导致任务成功率较低。

**核心思路**：dVLA的核心思路是利用扩散模型强大的生成能力和多模态思维链（Chain-of-Thought, CoT）的推理能力，将视觉感知、语言理解和动作生成统一到一个框架中。通过联合优化这三个模态，dVLA能够更好地理解指令意图，并生成合理的动作序列。

**技术框架**：dVLA的整体架构包含视觉编码器、语言编码器、动作解码器以及一个基于扩散模型的生成模型。视觉编码器提取图像特征，语言编码器处理文本指令，然后将这些特征输入到扩散模型中。扩散模型通过逐步去噪的过程，生成最终的动作序列。多模态CoT模块则在扩散过程中引入中间推理步骤，帮助模型更好地理解任务需求。

**关键创新**：dVLA的关键创新在于将扩散模型和多模态CoT相结合，实现视觉、语言和动作的统一建模。与传统的VLA模型相比，dVLA能够更好地利用跨模态信息进行推理，从而提高任务成功率和泛化能力。此外，论文还提出了两种加速策略：前缀注意力掩码和KV缓存，以降低推理延迟。

**关键设计**：在扩散模型方面，论文采用了DDPM（Denoising Diffusion Probabilistic Models）作为基础框架，并针对VLA任务进行了改进。损失函数包括扩散损失和动作预测损失，用于优化模型的生成能力。为了加速推理，论文使用了前缀注意力掩码，减少了不必要的计算，并利用KV缓存存储中间结果，避免重复计算。

## 📊 实验亮点

dVLA在LIBERO基准测试中取得了96.4%的平均成功率，超越了现有的离散和连续动作策略，达到了SOTA水平。在真实的Franka机器人上，dVLA成功完成了包括料箱拣选在内的多种复杂任务，展示了其在真实环境中的鲁棒性和泛化能力。此外，通过引入前缀注意力掩码和KV缓存，dVLA的推理速度得到了显著提升。

## 🎯 应用场景

dVLA具有广泛的应用前景，可用于各种机器人任务，如家庭服务、工业自动化、医疗辅助等。通过理解人类指令和感知环境，dVLA能够执行复杂的任务，提高生产效率和服务质量。未来，dVLA有望成为通用机器人控制平台，赋能各行各业。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

