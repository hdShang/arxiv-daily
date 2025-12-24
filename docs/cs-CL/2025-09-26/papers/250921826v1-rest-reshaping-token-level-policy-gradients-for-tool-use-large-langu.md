---
layout: default
title: "ResT: Reshaping Token-Level Policy Gradients for Tool-Use Large Language Models"
---

# ResT: Reshaping Token-Level Policy Gradients for Tool-Use Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21826" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21826v1</a>
  <a href="https://arxiv.org/pdf/2509.21826.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21826v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21826v1', 'ResT: Reshaping Token-Level Policy Gradients for Tool-Use Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Guojun Yin, Wei Lin, Ran He

**分类**: cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**ResT：重塑Token级策略梯度，提升LLM工具使用能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `工具使用` `强化学习` `策略梯度` `策略熵` `Token重加权` `智能体`

## 📋 核心要点

1. 现有工具使用LLM的强化学习训练依赖稀疏奖励，忽略了任务特性，导致策略梯度方差大，训练效率低。
2. ResT通过熵感知的token重加权来重塑策略梯度，逐步提升推理token的权重，从而稳定多轮工具使用任务的收敛。
3. ResT在BFCL和API-Bank上取得了SOTA结果，并在4B LLM微调后超越GPT-4o，证明了其有效性。

## 📝 摘要（中文）

大型语言模型(LLMs)通过调用外部工具，超越了被动生成，成为目标导向的智能体。强化学习(RL)为优化这些涌现的工具使用策略提供了一个原则性框架，但目前的主流范式仅依赖于稀疏的结果奖励，并且缺乏对工具使用任务特殊性的考虑，从而增加了策略梯度方差，导致训练效率低下。为了更好地理解和解决这些挑战，我们首先建立了策略熵与工具使用任务训练稳定性之间的理论联系，揭示了结构化的低熵token是奖励的主要决定因素。受此启发，我们提出了用于工具使用任务的重塑Token级策略梯度(ResT)。ResT通过熵感知的token重加权来重塑策略梯度，随着训练的进行，逐步提高推理token的权重。这种熵感知方案实现了从结构正确性到语义推理的平滑过渡，并稳定了多轮工具使用任务中的收敛。在BFCL和API-Bank上的评估表明，ResT取得了最先进的结果，优于现有方法高达8.76%。当在4B基础LLM上进行微调时，ResT在单轮任务上超过GPT-4o 4.11%，在多轮基础任务上超过GPT-4o 1.50%。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在工具使用任务中，由于强化学习训练依赖稀疏奖励和忽略任务特性，导致的策略梯度方差过大和训练效率低下的问题。现有方法难以有效区分结构性token和语义推理token的重要性，导致模型难以从结构正确性平滑过渡到语义推理。

**核心思路**：论文的核心思路是利用策略熵来指导token级别的策略梯度重塑。通过分析策略熵与训练稳定性的关系，发现低熵的结构化token是奖励的关键决定因素。因此，通过逐步提升推理token的权重，可以使模型更关注语义推理，从而提高训练效率和性能。

**技术框架**：ResT的整体框架包括以下几个主要步骤：1) 使用LLM生成工具使用序列；2) 计算每个token的策略熵；3) 根据策略熵对token的策略梯度进行重加权，逐步提升推理token的权重；4) 使用重加权后的策略梯度更新LLM的策略。该框架通过熵感知的token重加权，实现了从结构正确性到语义推理的平滑过渡。

**关键创新**：ResT最重要的技术创新点在于提出了熵感知的token重加权策略梯度方法。与现有方法不同，ResT不是简单地使用稀疏奖励来训练LLM，而是利用策略熵来区分不同token的重要性，并根据其重要性对策略梯度进行重加权。这种方法能够更有效地利用训练数据，提高训练效率和性能。

**关键设计**：ResT的关键设计包括：1) 策略熵的计算方式，论文可能采用了某种特定的熵计算公式，例如交叉熵或KL散度；2) token重加权的策略，论文可能设计了一个函数，根据token的策略熵来确定其权重，并随着训练的进行逐步提升推理token的权重；3) 强化学习算法的选择，论文可能采用了某种特定的强化学习算法，例如PPO或Actor-Critic。

## 📊 实验亮点

ResT在BFCL和API-Bank数据集上取得了显著的性能提升，优于现有方法高达8.76%。更重要的是，当在4B基础LLM上进行微调时，ResT在单轮任务上超过GPT-4o 4.11%，在多轮基础任务上超过GPT-4o 1.50%。这些实验结果充分证明了ResT在提升LLM工具使用能力方面的有效性。

## 🎯 应用场景

ResT的研究成果可以广泛应用于需要LLM进行工具使用的各种场景，例如智能助手、自动化客服、代码生成、科学研究等。通过提高LLM的工具使用能力，可以实现更高效、更智能的自动化任务处理，从而提升生产效率和用户体验。未来，该方法有望进一步扩展到更复杂的任务和更广泛的LLM应用领域。

## 📄 摘要（原文）

> Large language models (LLMs) transcend passive generation and act as goal-directed agents by invoking external tools. Reinforcement learning (RL) offers a principled framework for optimizing these emergent tool-use policies, yet the prevailing paradigm relies exclusively on sparse outcome rewards and lacks consideration of the particularity of tool-use tasks, inflating policy-gradient variance and resulting in inefficient training. To better understand and address these challenges, we first establish a theoretical link between policy entropy and training stability of tool-use tasks, which reveals that structured, low-entropy tokens are primary determinants of rewards. Motivated by this insight, we propose \textbf{Res}haped \textbf{T}oken-level policy gradients (\textbf{ResT}) for tool-use tasks. ResT reshapes the policy gradient through entropy-informed token reweighting, progressively upweighting reasoning tokens as training proceeds. This entropy-aware scheme enables a smooth shift from structural correctness to semantic reasoning and stabilizes convergence in multi-turn tool-use tasks. Evaluation on BFCL and API-Bank shows that ResT achieves state-of-the-art results, outperforming prior methods by up to $8.76\%$. When fine-tuned on a 4B base LLM, ResT further surpasses GPT-4o by $4.11\%$ on single-turn tasks and $1.50\%$ on multi-turn base tasks.

