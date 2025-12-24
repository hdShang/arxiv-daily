---
layout: default
title: "ReST-RL: Achieving Accurate Code Reasoning of LLMs with Optimized Self-Training and Decoding"
---

# ReST-RL: Achieving Accurate Code Reasoning of LLMs with Optimized Self-Training and Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19576" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19576v2</a>
  <a href="https://arxiv.org/pdf/2508.19576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19576v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19576v2', 'ReST-RL: Achieving Accurate Code Reasoning of LLMs with Optimized Self-Training and Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sining Zhoubian, Dan Zhang, Jie Tang

**分类**: cs.AI, cs.LG

**发布日期**: 2025-08-27 (更新: 2025-09-08)

**备注**: 21 pages, 4 figures

**🔗 代码/项目**: [GITHUB](https://github.com/THUDM/ReST-RL)

---

## 💡 一句话要点

**提出ReST-RL以解决LLMs推理准确性不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `大型语言模型` `强化学习` `代码推理` `蒙特卡洛树搜索` `训练数据优化` `无注释学习` `推理准确性`

## 📋 核心要点

1. 现有的GRPO方法在推理准确性上存在奖励方差不足的问题，导致其效果不理想。
2. 本文提出的ReST-RL结合了改进的GRPO算法和测试时间解码方法，优化了训练数据的选择和使用。
3. 实验结果表明，ReST-RL在多个编码基准上显著超越了其他强化训练和解码验证基线，提升了推理能力。

## 📝 摘要（中文）

针对大型语言模型（LLMs）推理准确性提升的问题，现有的强化学习方法GRPO因奖励方差不足而失败，而基于过程奖励模型（PRMs）的验证方法在训练数据获取和验证有效性上存在困难。为了解决这些问题，本文提出了ReST-RL，一个统一的LLM强化学习范式，通过结合改进的GRPO算法与精心设计的测试时间解码方法，显著提升了LLMs的代码推理能力。ReST-GRPO采用优化的ReST算法来筛选和组装高价值训练数据，从而提高GRPO采样的奖励方差，增强训练的有效性和效率。通过蒙特卡洛树搜索（MCTS），我们在无注释的情况下收集准确的价值目标，进一步优化了测试时间解码方法VM-MCTS，最终在多个知名编码基准上验证了该方法的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）在代码推理中的准确性不足问题。现有的GRPO方法由于奖励方差小，导致推理效果不佳，而基于过程奖励模型的验证方法在数据获取和验证有效性上存在挑战。

**核心思路**：ReST-RL通过结合改进的GRPO算法与测试时间解码方法，优化了训练数据的选择，增强了奖励方差，从而提升了模型的推理能力。该方法的设计旨在通过高效的数据利用和无注释的价值目标收集来提高训练效果。

**技术框架**：ReST-RL的整体架构包括两个主要阶段：首先是ReST-GRPO阶段，通过优化的ReST算法筛选高价值训练数据；其次是VM-MCTS阶段，通过蒙特卡洛树搜索收集准确的价值目标并进行解码优化。

**关键创新**：ReST-RL的核心创新在于结合了优化的GRPO算法与无注释的价值模型训练，显著提高了奖励方差和推理准确性。这一方法与传统的强化学习和验证方法相比，具有更高的效率和有效性。

**关键设计**：在ReST-GRPO阶段，采用了优化的ReST算法进行数据筛选，确保训练数据的高价值；在VM-MCTS阶段，利用蒙特卡洛树搜索收集价值目标，设计了适应性MCTS算法以提供精确的过程信号和验证分数。

## 📊 实验亮点

实验结果显示，ReST-RL在多个知名编码基准（如APPS、BigCodeBench和HumanEval）上显著优于其他强化训练基线（如naive GRPO和ReST-DPO），以及解码和验证基线（如PRM-BoN和ORM-MCTS），提升幅度达到XX%，表明其在增强LLM推理能力方面的强大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动代码生成和智能编程助手等。通过提升LLMs的推理能力，ReST-RL能够在实际编程任务中提供更高的准确性和效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> With respect to improving the reasoning accuracy of LLMs, the representative reinforcement learning (RL) method GRPO faces failure due to insignificant reward variance, while verification methods based on process reward models (PRMs) suffer from difficulties with training data acquisition and verification effectiveness. To tackle these problems, this paper introduces ReST-RL, a unified LLM RL paradigm that significantly improves LLM's code reasoning ability by combining an improved GRPO algorithm with a meticulously designed test time decoding method assisted by a value model (VM). As the first stage of policy reinforcement, ReST-GRPO adopts an optimized ReST algorithm to filter and assemble high-value training data, increasing the reward variance of GRPO sampling, thus improving the effectiveness and efficiency of training. After the basic reasoning ability of LLM policy has been improved, we further propose a test time decoding optimization method called VM-MCTS. Through Monte-Carlo Tree Search (MCTS), we collect accurate value targets with no annotation required, on which VM training is based. When decoding, the VM is deployed by an adapted MCTS algorithm to provide precise process signals as well as verification scores, assisting the LLM policy to achieve high reasoning accuracy. We conduct extensive experiments on coding problems to verify the validity of the proposed RL paradigm. Upon comparison, our approach significantly outperforms other reinforcement training baselines (e.g., naive GRPO and ReST-DPO), as well as decoding and verification baselines (e.g., PRM-BoN and ORM-MCTS) on well-known coding benchmarks of various levels (e.g., APPS, BigCodeBench, and HumanEval), indicating its power to strengthen the reasoning ability of LLM policies. Codes for our project can be found at https://github.com/THUDM/ReST-RL.

