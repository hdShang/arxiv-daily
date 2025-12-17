---
layout: default
title: SAGE: Training Smart Any-Horizon Agents for Long Video Reasoning with Reinforcement Learning
---

# SAGE: Training Smart Any-Horizon Agents for Long Video Reasoning with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13874" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13874</a>
  <a href="https://arxiv.org/pdf/2512.13874.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13874" onclick="toggleFavorite(this, '2512.13874', 'SAGE: Training Smart Any-Horizon Agents for Long Video Reasoning with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jitesh Jain, Jialuo Li, Zixian Ma, Jieyu Zhang, Chris Dongjoo Kim, Sangho Lee, Rohun Tripathi, Tanmay Gupta, Christopher Clark, Humphrey Shi

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出SAGE，利用强化学习训练智能任意时域Agent，用于长视频推理。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长视频推理` `任意时域推理` `强化学习` `多模态融合` `智能Agent` `视频理解`

## 📋 核心要点

1. 现有视频推理模型通常一次性处理大量帧并预测答案，类似于观看完整长视频，消耗大量资源，缺乏灵活性。
2. SAGE系统通过多轮推理处理长视频，并能单轮处理简单问题，模仿人类行为，实现任意时域的视频理解。
3. 通过Gemini-2.5-Flash生成合成数据训练SAGE-MM，并使用强化学习进行后训练，在SAGE-Bench上验证了有效性，取得了显著提升。

## 📝 摘要（中文）

本文提出SAGE，一个智能Agent系统，能够对长视频进行多轮推理，同时也能单轮处理简单问题，模拟人类在处理不同时长视频时的行为。为了训练SAGE的核心模块SAGE-MM，本文引入了一个简易的合成数据生成流程，该流程使用Gemini-2.5-Flash。此外，本文还提出了一种有效的强化学习后训练方法，对于在SAGE-MM中培养任意时域推理能力至关重要。为了评估真实娱乐场景下的视频推理能力，本文构建了SAGE-Bench，其平均视频时长超过700秒。实验结果表明，本文提出的系统、数据和强化学习方法是有效的，在开放式视频推理任务上取得了高达6.1%的显著提升，在超过10分钟的视频上取得了高达8.2%的提升。

## 🔬 方法详解

**问题定义**：现有视频推理模型在处理长视频时，通常需要一次性处理大量帧，计算成本高昂，并且缺乏像人类一样根据视频长度和任务复杂度调整推理策略的灵活性。这些模型无法有效利用视频中的关键信息，导致推理效率低下。

**核心思路**：SAGE的核心思路是模仿人类在观看视频时的行为，即根据视频的长度和任务的复杂程度，决定是快速浏览还是完整观看。通过引入一个智能Agent，SAGE能够进行多轮推理，逐步提取视频中的关键信息，从而实现高效的视频理解。

**技术框架**：SAGE系统主要包含两个核心模块：SAGE-MM（多模态模型）和强化学习训练模块。SAGE-MM负责从视频中提取特征并进行推理，而强化学习模块则用于优化SAGE-MM的推理策略。具体流程如下：1. 输入视频；2. SAGE-MM根据当前状态决定是观看更多帧还是输出答案；3. 如果选择观看更多帧，则更新状态并重复步骤2；4. 如果选择输出答案，则根据答案的正确性获得奖励，并使用强化学习算法更新SAGE-MM的策略。

**关键创新**：SAGE的关键创新在于其任意时域推理能力，即能够根据视频的长度和任务的复杂程度，动态调整推理策略。与传统的单轮推理模型相比，SAGE能够更有效地利用视频中的关键信息，从而提高推理效率和准确性。此外，使用Gemini-2.5-Flash生成合成数据，降低了训练成本。

**关键设计**：SAGE-MM采用多模态融合的方式，将视频帧和音频信息结合起来进行推理。强化学习算法采用Actor-Critic框架，其中Actor负责选择动作（观看更多帧或输出答案），Critic负责评估当前状态的价值。奖励函数的设计至关重要，需要平衡推理的准确性和效率。具体来说，如果输出的答案正确，则给予正向奖励；如果输出的答案错误，则给予负向奖励；如果观看的帧数过多，则给予负向奖励，以鼓励Agent尽快输出答案。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13874/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13874/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13874/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SAGE在开放式视频推理任务上取得了显著的性能提升，最高达到6.1%。尤其是在处理超过10分钟的长视频时，SAGE的性能提升高达8.2%。这些结果表明，SAGE的任意时域推理能力能够有效地利用视频中的关键信息，从而提高推理效率和准确性。与传统的单轮推理模型相比，SAGE具有明显的优势。

## 🎯 应用场景

SAGE具有广泛的应用前景，例如智能视频监控、智能客服、视频内容推荐等。通过模仿人类的推理方式，SAGE能够更有效地理解视频内容，从而为用户提供更智能、更个性化的服务。未来，SAGE有望成为视频理解领域的重要技术，推动相关产业的发展。

## 📄 摘要（原文）

> As humans, we are natural any-horizon reasoners, i.e., we can decide whether to iteratively skim long videos or watch short ones in full when necessary for a given task. With this in mind, one would expect video reasoning models to reason flexibly across different durations. However, SOTA models are still trained to predict answers in a single turn while processing a large number of frames, akin to watching an entire long video, requiring significant resources. This raises the question: Is it possible to develop performant any-horizon video reasoning systems? Inspired by human behavior, we first propose SAGE, an agent system that performs multi-turn reasoning on long videos while handling simpler problems in a single turn. Secondly, we introduce an easy synthetic data generation pipeline using Gemini-2.5-Flash to train the orchestrator, SAGE-MM, which lies at the core of SAGE. We further propose an effective RL post-training recipe essential for instilling any-horizon reasoning ability in SAGE-MM. Thirdly, we curate SAGE-Bench with an average duration of greater than 700 seconds for evaluating video reasoning ability in real-world entertainment use cases. Lastly, we empirically validate the effectiveness of our system, data, and RL recipe, observing notable improvements of up to 6.1% on open-ended video reasoning tasks, as well as an impressive 8.2% improvement on videos longer than 10 minutes.

