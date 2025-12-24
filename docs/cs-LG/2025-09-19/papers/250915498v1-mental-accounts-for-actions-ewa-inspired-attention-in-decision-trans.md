---
layout: default
title: "Mental Accounts for Actions: EWA-Inspired Attention in Decision Transformers"
---

# Mental Accounts for Actions: EWA-Inspired Attention in Decision Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15498" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15498v1</a>
  <a href="https://arxiv.org/pdf/2509.15498.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15498v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15498v1', 'Mental Accounts for Actions: EWA-Inspired Attention in Decision Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zahra Aref, Narayan B. Mandayam

**分类**: cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**EWA-VQ-ODT：利用经验加权吸引力改进在线决策Transformer的样本效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `在线决策Transformer` `经验加权吸引力` `向量量化` `连续控制` `强化学习`

## 📋 核心要点

1. 现有在线决策Transformer (ODT) 使用标准注意力，缺乏对动作结果的记忆，导致学习长期动作效果的效率低下。
2. 论文提出EWA-VQ-ODT，通过维护每个动作的心理账户，记录近期成功和失败，并用经验加权吸引力调节注意力。
3. 实验表明，EWA-VQ-ODT在连续控制任务中，相较于ODT，提高了样本效率和平均回报，尤其是在训练初期。

## 📝 摘要（中文）

Transformer已成为序列决策的强大架构，通过自注意力机制建模轨迹。在强化学习(RL)中，它们无需值函数近似即可实现回报条件控制。决策Transformer (DTs) 将RL视为监督序列建模，但仅限于离线数据且缺乏探索。在线决策Transformer (ODTs) 通过对on-policy rollouts进行熵正则化训练来解决此限制，为传统的RL方法（如Soft Actor-Critic）提供了一种稳定的替代方案，后者依赖于自举目标和奖励塑造。尽管如此，ODTs使用标准注意力，缺乏对特定动作结果的显式记忆，导致学习长期动作有效性的效率低下。受经验加权吸引力 (EWA) 等认知模型的启发，我们提出了EWA-VQ-ODT，它是一个轻量级模块，维护每个动作的心理账户，总结最近的成功和失败。连续动作通过直接网格查找路由到紧凑的向量量化码本，其中每个码存储一个标量吸引力，该吸引力通过衰减和基于奖励的强化在线更新。这些吸引力通过偏置与动作token相关的列来调节注意力，无需更改backbone或训练目标。在标准连续控制基准上，EWA-VQ-ODT提高了样本效率和平均回报，尤其是在早期训练中。该模块计算效率高，可通过每个代码的轨迹进行解释，并得到理论保证的支持，这些保证限制了吸引力动态及其对注意力漂移的影响。

## 🔬 方法详解

**问题定义**：现有在线决策Transformer (ODT) 在处理连续控制任务时，由于缺乏对动作历史的有效记忆机制，导致学习效率低下，尤其是在探索阶段，难以快速识别和利用有效的动作序列。标准注意力机制平等对待所有历史信息，无法区分不同动作带来的长期影响。

**核心思路**：借鉴认知模型中的经验加权吸引力 (EWA) 概念，为每个动作维护一个“心理账户”，记录其近期表现。通过量化动作空间，将连续动作映射到离散的码本，并为每个码维护一个吸引力值，该值根据动作的奖励进行更新。吸引力值用于调节注意力权重，从而使模型更加关注近期表现良好的动作。

**技术框架**：EWA-VQ-ODT在标准的在线决策Transformer (ODT) 框架上增加了一个轻量级的EWA模块。该模块包含一个向量量化 (VQ) 码本，用于将连续动作离散化。每个码对应一个吸引力值，该值通过衰减和基于奖励的强化进行在线更新。在计算注意力权重时，EWA模块会根据动作对应的吸引力值，对注意力矩阵的相应列进行偏置。整体训练流程与ODT相同，无需修改backbone或训练目标。

**关键创新**：核心创新在于将经验加权吸引力 (EWA) 的思想引入到Transformer的注意力机制中，通过维护动作的心理账户来增强模型对动作历史的记忆能力。与传统的注意力机制相比，EWA-VQ-ODT能够更加有效地利用历史信息，从而提高学习效率。此外，使用向量量化 (VQ) 码本将连续动作离散化，使得EWA模块能够处理连续动作空间。

**关键设计**：连续动作通过网格查找映射到VQ码本。每个码本条目维护一个标量吸引力值，该值根据以下公式更新：$A_{t+1}(a) = (1 - \beta) A_t(a) + \beta r_t$，其中 $A_t(a)$ 是动作 $a$ 在时间步 $t$ 的吸引力值，$eta$ 是学习率，$r_t$ 是时间步 $t$ 的奖励。吸引力值用于偏置注意力权重，具体而言，注意力矩阵的第 $i$ 行第 $j$ 列的权重 $w_{ij}$ 被修改为 $w_{ij} \cdot exp(A(a_j))$，其中 $a_j$ 是第 $j$ 个动作对应的码本条目。

## 📊 实验亮点

EWA-VQ-ODT在标准连续控制基准上进行了评估，结果表明，相较于ODT，EWA-VQ-ODT在样本效率和平均回报方面均有所提升，尤其是在训练初期。具体而言，EWA-VQ-ODT能够更快地学习到有效的策略，并在更少的训练样本下达到更高的性能。此外，论文还提供了理论保证，限制了吸引力动态及其对注意力漂移的影响。

## 🎯 应用场景

该研究成果可应用于各种需要高效探索和长期记忆的连续控制任务，例如机器人导航、自动驾驶、游戏AI等。通过增强模型对动作历史的记忆能力，可以提高智能体在复杂环境中的学习效率和决策能力，从而实现更智能、更自主的控制系统。此外，EWA-VQ-ODT的轻量级设计使其易于集成到现有的Transformer架构中，具有良好的应用前景。

## 📄 摘要（原文）

> Transformers have emerged as a compelling architecture for sequential decision-making by modeling trajectories via self-attention. In reinforcement learning (RL), they enable return-conditioned control without relying on value function approximation. Decision Transformers (DTs) exploit this by casting RL as supervised sequence modeling, but they are restricted to offline data and lack exploration. Online Decision Transformers (ODTs) address this limitation through entropy-regularized training on on-policy rollouts, offering a stable alternative to traditional RL methods like Soft Actor-Critic, which depend on bootstrapped targets and reward shaping. Despite these advantages, ODTs use standard attention, which lacks explicit memory of action-specific outcomes. This leads to inefficiencies in learning long-term action effectiveness. Inspired by cognitive models such as Experience-Weighted Attraction (EWA), we propose Experience-Weighted Attraction with Vector Quantization for Online Decision Transformers (EWA-VQ-ODT), a lightweight module that maintains per-action mental accounts summarizing recent successes and failures. Continuous actions are routed via direct grid lookup to a compact vector-quantized codebook, where each code stores a scalar attraction updated online through decay and reward-based reinforcement. These attractions modulate attention by biasing the columns associated with action tokens, requiring no change to the backbone or training objective. On standard continuous-control benchmarks, EWA-VQ-ODT improves sample efficiency and average return over ODT, particularly in early training. The module is computationally efficient, interpretable via per-code traces, and supported by theoretical guarantees that bound the attraction dynamics and its impact on attention drift.

