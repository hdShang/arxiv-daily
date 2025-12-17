---
layout: default
title: OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving
---

# OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14044" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14044</a>
  <a href="https://arxiv.org/pdf/2512.14044.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14044" onclick="toggleFavorite(this, '2512.14044', 'OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenguo Zhang, Haohan Zhen, Yishen Wang, Le Xu, Tianchen Deng, Xuefeng Chen, Qu Chen, Bo Zhang, Wuxiong Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**OmniDrive-R1：基于强化学习的多模态交错CoT，提升自动驾驶视觉语言模型的可靠性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉语言模型` `多模态学习` `思维链` `强化学习` `目标幻觉` `视觉 grounding`

## 📋 核心要点

1. 现有VLM在自动驾驶中面临目标幻觉问题，源于对未经验证文本CoT的依赖，且感知与推理解耦。
2. OmniDrive-R1提出交错多模态CoT，通过强化学习驱动视觉grounding，使模型自主关注关键区域。
3. 在DriveLMM-o1数据集上，OmniDrive-R1显著提升推理得分和答案准确率，优于Qwen2.5VL-7B基线。

## 📝 摘要（中文）

视觉语言模型(VLM)在自动驾驶等安全关键领域的部署受到可靠性问题的严重阻碍，特别是目标幻觉。这种失败源于它们对未经验证的、基于文本的思维链(CoT)的依赖。现有的多模态CoT方法试图缓解这个问题，但存在两个根本缺陷：(1)解耦的感知和推理阶段，阻碍了端到端联合优化；(2)依赖于昂贵的、密集的定位标注。我们提出了OmniDrive-R1，一个为自动驾驶设计的端到端VLM框架，它通过交错多模态思维链(iMCoT)机制统一了感知和推理。我们的核心创新是强化学习驱动的视觉 grounding 能力，使模型能够自主地引导其注意力并“放大”关键区域以进行细粒度分析。这种能力由我们的纯粹两阶段强化学习训练流程和Clip-GRPO算法实现。至关重要的是，Clip-GRPO引入了一种无标注的、基于过程的 grounding 奖励。这种奖励不仅消除了对密集标签的需求，还通过强制视觉焦点和文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在DriveLMM-o1上的大量实验证明了我们模型的显著改进。与基线Qwen2.5VL-7B相比，OmniDrive-R1将整体推理得分从51.77%提高到80.35%，最终答案准确率从37.81%提高到73.62%。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在自动驾驶场景中，由于依赖于纯文本的CoT推理，容易产生目标幻觉，导致决策错误。同时，现有的多模态CoT方法通常将感知和推理阶段解耦，无法进行端到端的联合优化，并且需要昂贵的密集标注。

**核心思路**：OmniDrive-R1的核心思路是通过交错的多模态CoT（iMCoT）机制，将感知和推理过程紧密结合，实现端到端的优化。同时，利用强化学习来驱动视觉 grounding，使模型能够自主地关注图像中的关键区域，从而减少目标幻觉。

**技术框架**：OmniDrive-R1是一个端到端的VLM框架，包含以下主要模块：1) 交错多模态CoT模块：将视觉信息和文本信息交替输入，进行感知和推理的融合。2) 强化学习模块：通过强化学习训练视觉 grounding 能力，使模型能够自主地选择关注的图像区域。3) Clip-GRPO算法：用于生成无标注的、基于过程的 grounding 奖励，鼓励模型关注与文本推理一致的视觉区域。

**关键创新**：OmniDrive-R1的关键创新在于：1) 提出了交错多模态CoT（iMCoT）机制，实现了感知和推理的端到端联合优化。2) 引入了强化学习来驱动视觉 grounding，使模型能够自主地关注图像中的关键区域。3) 提出了Clip-GRPO算法，生成无标注的、基于过程的 grounding 奖励，避免了对密集标注的依赖。

**关键设计**：OmniDrive-R1使用纯粹的两阶段强化学习训练流程。Clip-GRPO算法的关键在于设计了一个基于过程的 grounding 奖励，该奖励基于视觉焦点和文本推理之间的跨模态一致性。具体来说，模型会根据当前的文本推理状态，选择一个图像区域进行关注，然后根据该区域的视觉信息更新文本推理状态。如果更新后的文本推理状态与预期的一致，则给予模型正向奖励，否则给予负向奖励。这种奖励机制鼓励模型关注与文本推理相关的视觉区域。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14044/exam.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14044/overview.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14044/2_stage.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

OmniDrive-R1在DriveLMM-o1数据集上取得了显著的性能提升。与基线模型Qwen2.5VL-7B相比，OmniDrive-R1将整体推理得分从51.77%提高到80.35%，最终答案准确率从37.81%提高到73.62%。这些结果表明，OmniDrive-R1能够有效地减少目标幻觉，提高视觉语言模型在自动驾驶场景中的可靠性。

## 🎯 应用场景

OmniDrive-R1的研究成果可应用于自动驾驶、机器人导航、智能监控等领域。通过提高视觉语言模型的可靠性和准确性，可以提升自动驾驶系统的安全性，减少事故发生率。此外，该方法还可以应用于其他需要视觉和语言理解的场景，例如智能客服、图像描述等。

## 📄 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT)this http URLexisting multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localizationthis http URLwe introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

