---
layout: default
title: "OPPO: Accelerating PPO-based RLHF via Pipeline Overlap"
---

# OPPO: Accelerating PPO-based RLHF via Pipeline Overlap

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25762" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25762v1</a>
  <a href="https://arxiv.org/pdf/2509.25762.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25762v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25762v1', 'OPPO: Accelerating PPO-based RLHF via Pipeline Overlap')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaizhuo Yan, Yingjie Yu, Yifan Yu, Haizhong Zheng, Fan Lai

**分类**: cs.LG

**发布日期**: 2025-09-30

**备注**: Kaizhuo Yan and Yingjie Yu contributed equally to this work

---

## 💡 一句话要点

**OPPO：通过流水线重叠加速基于PPO的RLHF训练**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `人类反馈` `近端策略优化` `大型语言模型` `流水线并行`

## 📋 核心要点

1. 现有基于PPO的RLHF训练流程存在多模型依赖和长尾响应问题，导致训练效率低下。
2. OPPO通过步内和步间流水线重叠，使上下游模型并行计算，缓解长尾延迟，提升训练效率。
3. 实验表明，OPPO在不影响收敛性的前提下，将PPO-RLHF训练加速1.8-2.8倍，GPU利用率提升1.4-2.1倍。

## 📝 摘要（中文）

基于近端策略优化（PPO）的从人类反馈中强化学习（RLHF）是使大型语言模型（LLM）与人类偏好对齐的常用范例。然而，由于顺序多模型依赖（例如，奖励模型依赖于actor模型的输出）和长尾响应长度（其中少数长响应拖延了阶段完成），其训练流水线效率低下。我们提出了OPPO，一种新颖、轻量级且模型无关的基于PPO的RLHF框架，通过重叠流水线执行来提高训练效率。OPPO引入了两项新技术：（1）步内重叠，它以适当大小的块流式传输上游模型（例如，actor模型）的输出，使下游模型（例如，奖励模型）能够在上游模型继续解码时开始预填充；（2）步间重叠，它自适应地过度提交一些提示，并将长生成推迟到未来的步骤，从而在不丢弃部分工作的情况下减轻尾部延迟。OPPO可以轻松地与现有的PPO实现集成，只需更改几行代码。广泛的评估表明，OPPO将基于PPO的RLHF训练加速了1.8倍-2.8倍，并将GPU利用率提高了1.4倍-2.1倍，而不会影响训练收敛性。

## 🔬 方法详解

**问题定义**：论文旨在解决基于PPO的RLHF训练中存在的效率瓶颈问题。现有的RLHF训练流程通常是串行的，即奖励模型必须等待actor模型生成完整的响应后才能进行评估。此外，由于生成文本长度的不确定性，少数长文本生成会显著拖慢整个训练流程，形成长尾效应。这些因素导致GPU利用率低，训练时间长。

**核心思路**：OPPO的核心思路是通过流水线并行的方式，让actor模型和奖励模型能够同时工作，从而提高整体的训练效率。具体来说，OPPO采用了步内和步间两种重叠策略，尽可能地减少了模型之间的等待时间，并缓解了长尾效应带来的影响。

**技术框架**：OPPO框架主要包含以下两个核心模块：
1. **步内重叠（Intra-step overlap）**：将actor模型的输出进行分块，以流式传输的方式发送给奖励模型。奖励模型在接收到部分输出后即可开始预填充，无需等待actor模型生成完整的响应。
2. **步间重叠（Inter-step overlap）**：自适应地选择一部分提示进行过度提交，并将生成时间较长的响应推迟到后续步骤中处理。这样可以避免少数长响应拖慢整个训练批次的速度。

**关键创新**：OPPO的关键创新在于其流水线重叠策略，它打破了传统RLHF训练流程中的串行依赖关系，实现了actor模型和奖励模型的并行计算。这种方法能够有效地提高GPU利用率，并缩短训练时间。与现有方法相比，OPPO无需对模型结构进行修改，易于集成到现有的PPO实现中。

**关键设计**：OPPO的关键设计包括：
1. **分块大小**：步内重叠中，需要合理设置分块大小，以平衡预填充的效率和通信开销。
2. **过度提交策略**：步间重叠中，需要设计合理的过度提交策略，以避免过度增加计算量。
3. **延迟响应处理**：对于被推迟的响应，需要在后续步骤中进行处理，以保证训练的完整性。

## 📊 实验亮点

OPPO通过实验验证了其有效性。实验结果表明，OPPO可以将基于PPO的RLHF训练加速1.8倍-2.8倍，并将GPU利用率提高1.4倍-2.1倍，同时保持训练的收敛性。这些结果表明，OPPO是一种高效且实用的RLHF训练加速方法，具有重要的应用价值。

## 🎯 应用场景

OPPO框架可广泛应用于各种需要使用RLHF对大型语言模型进行对齐的场景，例如对话系统、文本生成、代码生成等。通过提高训练效率，OPPO可以帮助研究人员和开发者更快地训练出高质量的LLM，从而加速相关应用的落地和发展。该方法尤其适用于资源受限的场景，可以在有限的计算资源下实现更好的训练效果。

## 📄 摘要（原文）

> Proximal Policy Optimization (PPO)-based reinforcement learning from human feedback (RLHF) is a widely adopted paradigm for aligning large language models (LLMs) with human preferences. However, its training pipeline suffers from substantial inefficiencies due to sequential multi-model dependencies (e.g., reward model depends on actor outputs) and long-tail response lengths, where a few long responses straggle the stage completion. We present OPPO, a novel, lightweight, and model-agnostic PPO-based RLHF framework that improves training efficiency by overlapping pipeline execution. OPPO introduces two novel techniques: (1) Intra-step overlap, which streams upstream model outputs (e.g., actor model) in right-sized chunks, enabling the downstream model (e.g., reward) to begin prefill while the upstream continues decoding; and (2) Inter-step overlap, which adaptively overcommits a few prompts and defers long generations to future steps, mitigating tail latency without discarding partial work. OPPO integrates easily with existing PPO implementations with a few lines of code change. Extensive evaluations show that OPPO accelerates PPO-based RLHF training by $1.8 \times-2.8 \times$ and improves GPU utilization by $1.4 \times-2.1 \times$ without compromising training convergence.

