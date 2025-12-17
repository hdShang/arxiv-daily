---
layout: default
title: Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in
---

# Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in

**arXiv**: [2512.14273v1](https://arxiv.org/abs/2512.14273) | [PDF](https://arxiv.org/pdf/2512.14273.pdf)

**作者**: Xiaoqian Shen, Min-Hung Chen, Yu-Chiang Frank Wang, Mohamed Elhoseiny, Ryo Hachiuma

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://xiaoqian-shen.github.io/Zoom-Zero/

---

## 💡 一句话要点

**Zoom-Zero：通过时序缩放增强的视频理解框架，提升GVQA任务性能。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视频理解` `Grounded Video Question Answering` `时序定位` `强化学习` `粗到精方法` `视频语言模型` `长视频理解`

## 📋 核心要点

1. 现有GVQA方法在时序定位方面存在不足，难以准确地将答案定位到相关的视频片段，导致时序错位和幻觉。
2. Zoom-Zero采用由粗到精的策略，先粗略定位相关片段，再精细缩放至关键帧，进行视觉验证，提升时序定位的准确性。
3. 实验结果表明，Zoom-Zero在时序定位和答案准确率上均有显著提升，尤其在长视频理解方面表现突出。

## 📝 摘要（中文）

本文提出Zoom-Zero，一个由粗到精的框架，旨在解决大型视频语言模型（LVLMs）在Grounded Video Question Answering (GVQA) 任务中时序感知能力有限的问题。该框架首先定位与查询相关的视频片段，然后时序缩放到最显著的帧，进行更细粒度的视觉验证。Zoom-Zero通过两个关键创新改进了基于Group Relative Policy Optimization (GRPO) 的方法：(i) 缩放精度奖励，验证时序定位预测的准确性，并促进对定位帧的细粒度视觉验证；(ii) token选择性信用分配，将奖励归因于负责时序定位或答案生成的token，缓解GRPO在处理多方面奖励信号时的问题。实验表明，该方法在NExT-GQA和ReXTime数据集上分别提高了5.2%和4.6%的时序定位精度，同时平均答案准确率提高了2.4%。此外，推理期间的由粗到精的缩放进一步提升了长视频理解能力，在长视频基准测试中平均提高了6.4%，同时保留了关键视觉细节，且不影响全局上下文。

## 🔬 方法详解

**问题定义**：论文旨在解决Grounded Video Question Answering (GVQA) 任务中，现有大型视频语言模型（LVLMs）时序感知能力不足的问题。现有方法，如基于Group Relative Policy Optimization (GRPO) 的方法，在处理复杂的视频内容时，难以准确地将答案定位到相关的视频片段，导致时序定位错误和产生幻觉。

**核心思路**：Zoom-Zero的核心思路是采用一种由粗到精的时序缩放策略。首先，粗略地定位与问题相关的视频片段；然后，对这些片段进行更细致的分析，通过“缩放”到关键帧的方式，进行更精确的视觉验证。这种策略旨在弥补现有方法在细粒度时序理解上的不足。

**技术框架**：Zoom-Zero框架主要包含两个阶段：粗略定位阶段和精细缩放阶段。在粗略定位阶段，模型首先识别出与问题相关的视频片段。在精细缩放阶段，模型进一步聚焦于这些片段中的关键帧，进行更细致的视觉验证，从而生成更准确的答案。该框架利用强化学习进行训练，通过奖励机制来优化时序定位和答案生成。

**关键创新**：Zoom-Zero的关键创新在于两个方面：一是引入了“缩放精度奖励”，用于评估时序定位的准确性，并鼓励模型进行细粒度的视觉验证；二是采用了“token选择性信用分配”机制，将奖励分配给负责时序定位或答案生成的token，从而缓解了GRPO在处理多方面奖励信号时的问题。

**关键设计**：在奖励函数设计上，Zoom-Zero使用了缩放精度奖励，该奖励基于模型定位的关键帧与真实答案帧之间的重叠程度。此外，token选择性信用分配机制通过注意力权重来确定每个token对最终奖励的贡献，从而实现更有效的学习。具体的网络结构细节和超参数设置在论文中有详细描述（未知）。

## 📊 实验亮点

Zoom-Zero在NExT-GQA和ReXTime数据集上分别实现了5.2%和4.6%的时序定位精度提升，同时平均答案准确率提高了2.4%。尤其值得一提的是，该方法在长视频理解方面表现出色，在长视频基准测试中平均提高了6.4%，表明其在处理复杂视频内容时具有显著优势。

## 🎯 应用场景

Zoom-Zero技术可应用于智能视频分析、视频搜索、智能客服等领域。例如，在视频搜索中，可以更准确地定位到包含用户所需信息的视频片段；在智能客服中，可以根据用户提出的问题，快速定位到相关的视频内容，并给出准确的答案。该研究有助于提升视频理解的智能化水平，具有广阔的应用前景。

## 📄 摘要（原文）

> Grounded video question answering (GVQA) aims to localize relevant temporal segments in videos and generate accurate answers to a given question; however, large video-language models (LVLMs) exhibit limited temporal awareness. Although existing approaches based on Group Relative Policy Optimization (GRPO) attempt to improve temporal grounding, they still struggle to faithfully ground their answers in the relevant video evidence, leading to temporal mislocalization and hallucinations. In this work, we present Zoom-Zero, a coarse-to-fine framework that first localizes query-relevant segments and then temporally zooms into the most salient frames for finer-grained visual verification. Our method addresses the limits of GRPO for the GVQA task with two key innovations: (i) a zoom-in accuracy reward that validates the fidelity of temporal grounding prediction and facilitates fine-grained visual verification on grounded frames; (ii) token-selective credit assignment, which attributes rewards to the tokens responsible for temporal localization or answer generation, mitigating GRPO's issue in handling multi-faceted reward signals. Our proposed method advances grounded video question answering, improving temporal grounding by 5.2\% on NExT-GQA and 4.6\% on ReXTime, while also enhancing average answer accuracy by 2.4\%. Additionally, the coarse-to-fine zoom-in during inference further benefits long-form video understanding by preserving critical visual details without compromising global context, yielding an average improvement of 6.4\% on long-video benchmarks.

