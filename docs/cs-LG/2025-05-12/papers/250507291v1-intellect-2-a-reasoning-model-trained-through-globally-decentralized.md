---
layout: default
title: INTELLECT-2: A Reasoning Model Trained Through Globally Decentralized Reinforcement Learning
---

# INTELLECT-2: A Reasoning Model Trained Through Globally Decentralized Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07291" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07291v1</a>
  <a href="https://arxiv.org/pdf/2505.07291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07291v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07291v1', 'INTELLECT-2: A Reasoning Model Trained Through Globally Decentralized Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prime Intellect Team, Sami Jaghouar, Justus Mattern, Jack Min Ong, Jannik Straube, Manveer Basra, Aaron Pazdera, Kushal Thaman, Matthew Di Ferrante, Felix Gabriel, Fares Obeid, Kemal Erdem, Michael Keiblinger, Johannes Hagemann

**分类**: cs.LG, cs.DC

**发布日期**: 2025-05-12

**备注**: 26 pages, 12 figures

---

## 💡 一句话要点

**提出INTELLECT-2以实现全球去中心化的强化学习训练**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `去中心化训练` `强化学习` `分布式计算` `语言模型` `异步学习` `PRIME-RL` `TOPLOC` `SHARDCAST`

## 📋 核心要点

1. 现有的强化学习训练方法通常集中在单一地点，导致计算资源利用效率低下和训练速度缓慢。
2. INTELLECT-2通过全球分布式的异步强化学习框架，利用无权限计算贡献者的动态群体来进行训练，提升了训练效率。
3. 实验结果表明，INTELLECT-2在320亿参数范围内的推理能力超越了现有的QwQ-32B模型，显示出显著的性能提升。

## 📝 摘要（中文）

我们介绍了INTELLECT-2，这是首个通过全球分布式强化学习训练的320亿参数语言模型。与传统的集中式训练不同，INTELLECT-2在一个动态的、异构的无权限计算贡献者群体中，采用完全异步的强化学习进行训练。为了支持这一独特基础设施的训练，我们从头构建了多个组件：我们提出了PRIME-RL，这是一个专为分布式异步强化学习设计的训练框架，基于TOPLOC等新颖组件，后者验证来自不可信推理工作者的回滚。此外，我们对标准的GRPO训练配方和数据过滤技术进行了修改，这对实现训练稳定性和确保模型成功学习其训练目标至关重要，从而在32B参数范围内超越了QwQ-32B这一最先进的推理模型。我们开源了INTELLECT-2及其所有代码和数据，旨在鼓励和促进去中心化训练领域的开放研究。

## 🔬 方法详解

**问题定义**：论文旨在解决传统集中式强化学习训练的效率低下和资源利用不足的问题。现有方法在处理大规模模型训练时面临计算瓶颈和灵活性不足的挑战。

**核心思路**：INTELLECT-2的核心思路是通过全球分布式的异步强化学习框架，利用动态的、异构的计算资源来进行训练，从而提高训练的速度和效率。

**技术框架**：整体架构包括多个模块：PRIME-RL训练框架、TOPLOC验证组件和SHARDCAST广播机制。PRIME-RL负责协调训练过程，TOPLOC确保回滚的可信性，而SHARDCAST则高效地将策略权重从训练节点广播到推理工作者。

**关键创新**：最重要的技术创新在于构建了一个去中心化的训练框架，允许多个不可信的计算节点参与训练，这与传统的集中式训练方法本质上不同。

**关键设计**：在训练过程中，采用了改进的GRPO训练配方和数据过滤技术，以确保训练的稳定性和模型的有效学习。此外，模型的参数设置和损失函数设计也经过精心调整，以适应分布式训练的需求。

## 📊 实验亮点

实验结果显示，INTELLECT-2在320亿参数范围内的推理能力超越了QwQ-32B模型，具体性能提升幅度达到XX%（具体数据未知），证明了去中心化训练方法的有效性和可行性。

## 🎯 应用场景

该研究的潜在应用领域包括大规模语言模型的训练、分布式计算平台的优化以及去中心化人工智能系统的开发。通过提高训练效率，INTELLECT-2有望推动自然语言处理、智能助手等领域的进步，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce INTELLECT-2, the first globally distributed reinforcement learning (RL) training run of a 32 billion parameter language model. Unlike traditional centralized training efforts, INTELLECT-2 trains a reasoning model using fully asynchronous RL across a dynamic, heterogeneous swarm of permissionless compute contributors.
>   To enable a training run with this unique infrastructure, we built various components from scratch: we introduce PRIME-RL, our training framework purpose-built for distributed asynchronous reinforcement learning, based on top of novel components such as TOPLOC, which verifies rollouts from untrusted inference workers, and SHARDCAST, which efficiently broadcasts policy weights from training nodes to inference workers.
>   Beyond infrastructure components, we propose modifications to the standard GRPO training recipe and data filtering techniques that were crucial to achieve training stability and ensure that our model successfully learned its training objective, thus improving upon QwQ-32B, the state of the art reasoning model in the 32B parameter range.
>   We open-source INTELLECT-2 along with all of our code and data, hoping to encourage and enable more open research in the field of decentralized training.

