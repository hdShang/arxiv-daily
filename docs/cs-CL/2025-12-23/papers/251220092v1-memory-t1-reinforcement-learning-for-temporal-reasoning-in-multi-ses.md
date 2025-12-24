---
layout: default
title: Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents
---

# Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20092" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20092v1</a>
  <a href="https://arxiv.org/pdf/2512.20092.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20092v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20092v1', 'Memory-T1: Reinforcement Learning for Temporal Reasoning in Multi-session Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Du, Baojun Wang, Yifan Xiang, Zhaowei Wang, Wenyu Huang, Boyang Xue, Bin Liang, Xingshan Zeng, Fei Mi, Haoli Bai, Lifeng Shang, Jeff Z. Pan, Yuxin Jiang, Kam-Fai Wong

**分类**: cs.CL

**发布日期**: 2025-12-23

**🔗 代码/项目**: [GITHUB](https://github.com/Elvin-Yiming-Du/Memory-T1/)

---

## 💡 一句话要点

**提出Memory-T1框架，利用强化学习解决多轮对话Agent中的时序推理难题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `时序推理` `强化学习` `多轮对话` `长文本建模` `对话Agent`

## 📋 核心要点

1. 现有长文本模型在处理长程多轮对话时，难以准确识别时序信息，导致时序推理性能下降。
2. Memory-T1框架利用强化学习，学习时间感知的记忆选择策略，从对话历史中选择最相关的证据会话。
3. 实验表明，Memory-T1在Time-Dialog基准测试中显著提升了性能，并在长文本输入下保持了鲁棒性。

## 📝 摘要（中文）

本文提出Memory-T1框架，旨在解决会话Agent在长程多轮对话中进行时序推理时面临的挑战。现有方法在处理冗长且包含噪声的对话历史时，难以准确识别时序相关信息，严重影响推理性能。Memory-T1采用强化学习(RL)方法学习时间感知的记忆选择策略。该框架使用由粗到精的策略，首先通过时间和相关性过滤器将对话历史修剪为候选集，然后由RL Agent选择精确的证据会话。RL训练由多级奖励函数指导，优化(i)答案准确性，(ii)证据基础，以及(iii)时间一致性。特别是，时间一致性奖励通过评估会话级别（时间邻近度）和话语级别（时间保真度）与查询时间范围的对齐情况，提供密集信号，使Agent能够解决细微的时间歧义。在Time-Dialog基准测试中，Memory-T1将7B模型的整体得分提高到67.0%，为开源模型建立了新的最先进性能，并且优于14B基线模型10.2%。消融研究表明，时间一致性和证据基础奖励共同贡献了15.0%的性能提升。此外，Memory-T1在高达128k tokens的情况下保持了鲁棒性，而基线模型则崩溃，证明了其在处理大量对话历史中的噪声方面的有效性。

## 🔬 方法详解

**问题定义**：现有对话Agent在处理长程多轮对话时，由于对话历史冗长且包含噪声，难以准确识别与时间相关的关键信息，导致时序推理能力不足。现有方法无法有效区分不同时间段的信息，容易受到无关信息的干扰，从而影响最终的推理结果。

**核心思路**：Memory-T1的核心思路是利用强化学习，训练一个能够根据时间信息选择相关对话会话的Agent。通过学习时间感知的记忆选择策略，Agent可以从冗长的对话历史中提取出与当前问题最相关的证据，从而提高时序推理的准确性。这种方法模拟了人类在回忆信息时，会根据时间线索进行筛选的过程。

**技术框架**：Memory-T1框架采用由粗到精的策略。首先，利用时间和相关性过滤器对对话历史进行初步筛选，得到候选会话集合。然后，强化学习Agent从候选集中选择最终的证据会话。Agent的状态包括对话历史、当前问题和已选择的会话。Agent的动作是选择下一个会话。整个框架通过多级奖励函数进行训练，包括答案准确性奖励、证据基础奖励和时间一致性奖励。

**关键创新**：Memory-T1的关键创新在于引入了时间一致性奖励，该奖励从会话级别（时间邻近度）和话语级别（时间保真度）评估选择的会话与查询时间范围的对齐情况。这种时间一致性奖励能够提供密集的反馈信号，帮助Agent学习区分细微的时间差异，从而更准确地选择相关的证据会话。

**关键设计**：时间一致性奖励是关键设计之一，它包括会话级别的时间邻近度评估和话语级别的时间保真度评估。时间邻近度评估会话的时间戳与查询时间范围的接近程度。时间保真度评估会话中话语的时间顺序是否与查询时间范围一致。此外，框架还使用了注意力机制来融合选择的证据会话，并使用交叉熵损失函数来优化答案准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20092v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20092v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20092v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Memory-T1在Time-Dialog基准测试中取得了显著的性能提升，将7B模型的整体得分提高到67.0%，超越了14B基线模型10.2%。消融研究表明，时间一致性和证据基础奖励共同贡献了15.0%的性能提升。此外，Memory-T1在处理高达128k tokens的长文本输入时，仍然保持了鲁棒性，而基线模型则崩溃。

## 🎯 应用场景

Memory-T1框架可应用于各种需要时序推理的对话Agent，例如智能客服、虚拟助手、医疗诊断等。该框架能够提高Agent在处理复杂对话场景下的推理能力，从而提供更准确、更个性化的服务。未来，该研究可以扩展到其他需要处理长程依赖关系的自然语言处理任务中。

## 📄 摘要（原文）

> Temporal reasoning over long, multi-session dialogues is a critical capability for conversational agents. However, existing works and our pilot study have shown that as dialogue histories grow in length and accumulate noise, current long-context models struggle to accurately identify temporally pertinent information, significantly impairing reasoning performance. To address this, we introduce Memory-T1, a framework that learns a time-aware memory selection policy using reinforcement learning (RL). It employs a coarse-to-fine strategy, first pruning the dialogue history into a candidate set using temporal and relevance filters, followed by an RL agent that selects the precise evidence sessions. The RL training is guided by a multi-level reward function optimizing (i) answer accuracy, (ii) evidence grounding, and (iii) temporal consistency. In particular, the temporal consistency reward provides a dense signal by evaluating alignment with the query time scope at both the session-level (chronological proximity) and the utterance-level (chronological fidelity), enabling the agent to resolve subtle chronological ambiguities. On the Time-Dialog benchmark, Memory-T1 boosts a 7B model to an overall score of 67.0\%, establishing a new state-of-the-art performance for open-source models and outperforming a 14B baseline by 10.2\%. Ablation studies show temporal consistency and evidence grounding rewards jointly contribute to a 15.0\% performance gain. Moreover, Memory-T1 maintains robustness up to 128k tokens, where baseline models collapse, proving effectiveness against noise in extensive dialogue histories. The code and datasets are publicly available at https://github.com/Elvin-Yiming-Du/Memory-T1/

