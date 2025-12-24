---
layout: default
title: "VideoTG-R1: Boosting Video Temporal Grounding via Curriculum Reinforcement Learning on Reflected Boundary Annotations"
---

# VideoTG-R1: Boosting Video Temporal Grounding via Curriculum Reinforcement Learning on Reflected Boundary Annotations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23397" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23397v1</a>
  <a href="https://arxiv.org/pdf/2510.23397.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23397v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.23397v1', 'VideoTG-R1: Boosting Video Temporal Grounding via Curriculum Reinforcement Learning on Reflected Boundary Annotations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lu Dong, Haiyu Zhang, Han Lin, Ziang Yan, Xiangyu Zeng, Hongjie Zhang, Yifei Huang, Yi Wang, Zhen-Hua Ling, Limin Wang, Yali Wang

**分类**: cs.CV

**发布日期**: 2025-10-27

**🔗 代码/项目**: [GITHUB](https://github.com/ldong1111/VideoTG-R1)

---

## 💡 一句话要点

**VideoTG-R1：通过反射边界标注的课程强化学习提升视频时序定位性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频时序定位` `多模态大语言模型` `强化学习` `课程学习` `边界反射` `难度估计` `视频理解`

## 📋 核心要点

1. 现有基于多模态大语言模型（MLLM）的视频时序定位方法忽略了训练样本质量和难度的挑战，导致性能瓶颈。
2. VideoTG-R1提出一种课程强化学习框架，利用边界反射代理过滤部分标注样本，并使用难度估计代理动态调整训练难度。
3. 实验表明，VideoTG-R1仅使用少量数据和计算资源，即可在视频时序定位和视频问答任务上超越全数据训练的模型。

## 📝 摘要（中文）

视频时序定位（VTG）旨在根据语言查询在视频中定位精确的片段，这是视频理解中的一个基本挑战。虽然最近的多模态大型语言模型（MLLM）已显示出通过强化学习（RL）解决VTG问题的潜力，但它们忽略了训练样本的质量和难度所带来的挑战。(1)部分标注的样本：许多样本包含超出标注间隔的相关片段，引入了模糊的监督。(2)难以定位的样本：零样本性能差的样本在RL训练期间产生持续较低且难以区分的奖励，在多个输出之间没有明确的偏好，从而阻碍了学习效率。为了应对这些挑战，我们提出了VideoTG-R1，一种新颖的具有反射边界标注的课程强化学习框架，能够实现数据高效的训练。具体来说，我们提出了一个边界反射代理，它利用MLLM来预测标注间隔之外的查询相关时间戳，从而使我们能够识别和过滤掉部分标注的样本，从而减少歧义。此外，我们引入了一个难度估计代理来评估每个样本的训练难度，并设计了一种课程强化学习策略，该策略根据训练步骤动态地屏蔽难以定位的视频样本，从而降低训练难度并提供更清晰的偏好。在VTG和基于视频的问答任务上的实验证明了我们方法的有效性。值得注意的是，仅使用10%的训练样本和21%的计算预算，VideoTG-R1在组相对策略优化（GRPO）和监督微调（SFT）下均优于全数据对应方法。

## 🔬 方法详解

**问题定义**：视频时序定位旨在根据给定的文本查询，在视频中找到对应的时间片段。现有的方法，特别是基于多模态大语言模型的方法，在训练时面临两个主要问题：一是训练数据中存在大量部分标注的样本，即相关片段超出标注范围，导致监督信号模糊；二是存在一些难以定位的样本，这些样本在强化学习训练中奖励信号稀疏，难以区分优劣。

**核心思路**：VideoTG-R1的核心思路是通过课程强化学习，逐步引入高质量且易于学习的样本，从而提高训练效率和模型性能。具体来说，它通过两个代理来解决上述两个问题：边界反射代理用于识别和过滤部分标注的样本，难度估计代理用于评估样本的训练难度，并根据难度动态调整训练过程。

**技术框架**：VideoTG-R1的整体框架包含以下几个主要模块：1) 边界反射代理：利用MLLM预测标注间隔之外的查询相关时间戳，用于识别部分标注样本。2) 难度估计代理：评估每个样本的训练难度。3) 课程强化学习策略：根据难度估计结果，动态屏蔽难以定位的视频样本。4) 训练过程：采用强化学习方法，优化模型的时序定位能力。

**关键创新**：VideoTG-R1的关键创新在于将课程学习的思想引入到基于MLLM的视频时序定位强化学习训练中，并设计了两个代理来分别解决数据质量和训练难度的问题。与现有方法相比，VideoTG-R1能够更有效地利用数据，并降低训练难度，从而提高模型性能。

**关键设计**：边界反射代理使用MLLM预测查询相关的时间戳，具体实现细节未知。难度估计代理的具体实现细节未知，但其输出用于指导课程学习策略。课程学习策略根据难度估计结果，动态调整训练样本的权重或屏蔽部分样本，具体调整策略未知。损失函数和网络结构细节未知。

## 📊 实验亮点

VideoTG-R1在视频时序定位和视频问答任务上取得了显著的性能提升。特别是在使用少量数据（10%的训练样本）和计算资源（21%的计算预算）的情况下，VideoTG-R1的性能优于使用全数据训练的基线模型，证明了该方法的有效性和数据效率。

## 🎯 应用场景

该研究成果可应用于智能视频分析、视频检索、智能客服等领域。例如，在视频检索中，可以根据用户输入的文本查询，快速准确地定位到视频中的相关片段。在智能客服中，可以根据用户的问题，在视频教程中找到对应的解决方案。该研究有助于提升视频理解和人机交互的效率和准确性。

## 📄 摘要（原文）

> Video temporal grounding (VTG) aims to locate precise segments in videos based on language queries, which is a fundamental challenge in video understanding. While recent Multimodal Large Language Models (MLLMs) have shown promise in tackling VTG through reinforcement learning (RL), they overlook the challenges arising from both the quality and difficulty of training samples. (1) Partially annotated samples. Many samples contain relevant segments beyond the annotated interval, introducing ambiguous supervision. (2) Hard-to-ground samples. Samples with poor zero-shot performance produce consistently low and indistinguishable rewards during RL training, exhibiting no clear preference among multiple outputs and thus hindering learning efficiency. To address these challenges, we propose VideoTG-R1, a novel curriculum RL framework with reflected boundary annotations, enabling data-efficient training. Specifically, we propose a Boundary Reflection Agent that utilizes MLLMs to predict query-relevant timestamps outside the annotated intervals, allowing us to identify and filter out partially annotated samples, thereby reducing ambiguity. Furthermore, we introduce a Difficulty Estimation Agent to assess the training difficulty of each sample and design a curriculum RL strategy that dynamically masks the videos of hard-to-ground samples according to the training steps, easing the training difficulty and providing clearer preference. Experiments on the VTG and grounded VideoQA tasks demonstrate the effectiveness of our method. Remarkably, with only 10% of the training samples and 21% of the computational budget, VideoTG-R1 outperforms full-data counterparts under both group relative policy optimization (GRPO) and supervised fine-tuning (SFT). The code is available at https://github.com/ldong1111/VideoTG-R1.

