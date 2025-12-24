---
layout: default
title: "Ring-lite: Scalable Reasoning via C3PO-Stabilized Reinforcement Learning for LLMs"
---

# Ring-lite: Scalable Reasoning via C3PO-Stabilized Reinforcement Learning for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14731" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14731v2</a>
  <a href="https://arxiv.org/pdf/2506.14731.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14731v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14731v2', 'Ring-lite: Scalable Reasoning via C3PO-Stabilized Reinforcement Learning for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ling Team, Bin Hu, Cai Chen, Deng Zhao, Ding Liu, Dingnan Jin, Feng Zhu, Hao Dai, Hongzhi Luan, Jia Guo, Jiaming Liu, Jiewei Wu, Jun Mei, Jun Zhou, Junbo Zhao, Junwu Xiong, Kaihong Zhang, Kuan Xu, Lei Liang, Liang Jiang, Liangcheng Fu, Longfei Zheng, Qiang Gao, Qing Cui, Quan Wan, Shaomian Zheng, Shuaicheng Li, Tongkai Yang, Wang Ren, Xiaodong Yan, Xiaopei Wan, Xiaoyun Feng, Xin Zhao, Xinxing Yang, Xinyu Kong, Xuemin Yang, Yang Li, Yingting Wu, Yongkang Liu, Zhankai Xu, Zhenduo Zhang, Zhenglei Zhou, Zhenyu Huang, Zhiqiang Zhang, Zihao Wang, Zujie Wen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-17 (更新: 2025-06-18)

**备注**: Technical Report

---

## 💡 一句话要点

**提出Ring-lite以解决大规模语言模型推理效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `专家混合模型` `强化学习` `蒸馏训练` `推理效率` `多领域数据集成` `模型优化` `计算稳定性`

## 📋 核心要点

1. 现有的语言模型在推理效率和稳定性方面存在不足，尤其是在大规模参数激活时。
2. 论文提出了一种结合蒸馏与强化学习的联合训练方法，并引入C3PO以提高训练稳定性。
3. 实验结果表明，Ring-lite在多个基准测试中表现优异，激活参数数量显著低于同类模型。

## 📝 摘要（中文）

我们提出了Ring-lite，一种基于专家混合模型（MoE）的语言模型，通过强化学习（RL）优化以实现高效且稳健的推理能力。该模型基于公开的Ling-lite模型，拥有168亿参数，其中275亿参数被激活。我们的方案在多个具有挑战性的基准测试（如AIME、LiveCodeBench、GPQA-Diamond）上，与最先进的小规模推理模型的性能相匹配，同时仅激活了可比模型所需参数的三分之一。为此，我们引入了一个结合蒸馏与RL的联合训练流程，揭示了MoE RL训练中的未记录挑战。我们提出了约束上下文计算策略优化（C3PO），增强了训练稳定性并提高了计算吞吐量。最后，我们开发了一个两阶段训练范式，以协调多领域数据集成，解决混合数据集训练中出现的领域冲突。

## 🔬 方法详解

**问题定义**：本论文旨在解决大规模语言模型在推理过程中的效率和稳定性问题。现有方法在处理复杂推理任务时，往往需要激活大量参数，导致计算资源浪费和训练不稳定。

**核心思路**：我们提出Ring-lite模型，通过结合蒸馏与强化学习的联合训练方法，优化模型的推理能力，同时减少激活参数的数量。C3PO策略的引入，旨在提升训练过程的稳定性和效率。

**技术框架**：整体架构包括三个主要模块：1) 蒸馏模块，通过选择基于熵损失的检查点进行训练；2) 强化学习模块，利用C3PO策略优化训练过程；3) 两阶段训练范式，协调多领域数据集成，解决领域冲突。

**关键创新**：最重要的技术创新在于C3PO策略的提出，它通过算法与系统的协同设计，显著提高了训练的稳定性和计算效率。这一方法在MoE RL训练中尚属首次。

**关键设计**：在训练过程中，我们采用了基于熵损失的检查点选择策略，优化了损失函数的设计，以确保在强化学习阶段获得更好的性能与效率平衡。

## 📊 实验亮点

实验结果显示，Ring-lite在多个基准测试中表现优异，能够与最先进的小规模推理模型相媲美，同时仅激活三分之一的参数。通过C3PO策略，训练稳定性显著提高，计算效率也得到了优化。

## 🎯 应用场景

Ring-lite模型的潜在应用领域包括自然语言处理、对话系统、智能问答等。其高效的推理能力和较低的参数激活需求，使其在资源受限的环境中具有实际价值，能够推动大规模语言模型的广泛应用与普及。

## 📄 摘要（原文）

> We present Ring-lite, a Mixture-of-Experts (MoE)-based large language model optimized via reinforcement learning (RL) to achieve efficient and robust reasoning capabilities. Built upon the publicly available Ling-lite model, a 16.8 billion parameter model with 2.75 billion activated parameters, our approach matches the performance of state-of-the-art (SOTA) small-scale reasoning models on challenging benchmarks (e.g., AIME, LiveCodeBench, GPQA-Diamond) while activating only one-third of the parameters required by comparable models. To accomplish this, we introduce a joint training pipeline integrating distillation with RL, revealing undocumented challenges in MoE RL training. First, we identify optimization instability during RL training, and we propose Constrained Contextual Computation Policy Optimization(C3PO), a novel approach that enhances training stability and improves computational throughput via algorithm-system co-design methodology. Second, we empirically demonstrate that selecting distillation checkpoints based on entropy loss for RL training, rather than validation metrics, yields superior performance-efficiency trade-offs in subsequent RL training. Finally, we develop a two-stage training paradigm to harmonize multi-domain data integration, addressing domain conflicts that arise in training with mixed dataset. We will release the model, dataset, and code.

