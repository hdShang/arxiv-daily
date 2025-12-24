---
layout: default
title: "Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in"
---

# Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14273" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14273v1</a>
  <a href="https://arxiv.org/pdf/2512.14273.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14273v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14273v1', 'Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoqian Shen, Min-Hung Chen, Yu-Chiang Frank Wang, Mohamed Elhoseiny, Ryo Hachiuma

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://xiaoqian-shen.github.io/Zoom-Zero/

---

## 💡 一句话要点

**Zoom-Zero：通过时间域缩放增强视频理解，解决GVQA中时序定位不准问题。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视频理解` `Grounded Video Question Answering` `时间域缩放` `强化学习` `多模态学习`

## 📋 核心要点

1. 现有GVQA模型时序感知能力有限，难以准确地将答案定位到视频片段，导致时序误判。
2. Zoom-Zero采用由粗到精的策略，先粗略定位相关片段，再精细缩放关键帧，进行视觉验证。
3. 实验表明，Zoom-Zero在时序定位和答案准确率上均有显著提升，尤其在长视频理解方面。

## 📝 摘要（中文）

本文提出Zoom-Zero，一个由粗到精的框架，旨在提升Grounded Video Question Answering (GVQA) 任务的性能。现有的大型视频语言模型(LVLMs)在时序感知方面存在局限性，而基于Group Relative Policy Optimization (GRPO)的方法难以准确地将答案定位到相关的视频片段，导致时序误判和幻觉。Zoom-Zero首先定位与查询相关的片段，然后进行时间域缩放，聚焦于最显著的帧，以进行更精细的视觉验证。该方法通过引入缩放精度奖励来验证时序定位的准确性，并促进对定位帧的细粒度视觉验证；同时采用token选择性信用分配，将奖励分配给负责时序定位或答案生成的token，从而缓解GRPO在处理多方面奖励信号时的问题。实验结果表明，该方法在NExT-GQA和ReXTime数据集上分别将时序定位精度提高了5.2%和4.6%，并将平均答案准确率提高了2.4%。此外，在推理过程中采用由粗到精的缩放方法，在不影响全局上下文的情况下保留了关键的视觉细节，从而进一步提升了长视频理解能力，在长视频基准测试中平均提高了6.4%。

## 🔬 方法详解

**问题定义**：论文旨在解决Grounded Video Question Answering (GVQA)任务中，现有大型视频语言模型(LVLMs)时序感知能力不足的问题。现有方法，如基于Group Relative Policy Optimization (GRPO)的方法，难以准确地将答案定位到相关的视频片段，导致时序误判和幻觉，影响答案的准确性。

**核心思路**：论文的核心思路是采用一种由粗到精的时间域缩放策略。首先，粗略地定位与问题相关的视频片段；然后，对这些片段进行时间域的“放大”，聚焦于最关键的帧，进行更细致的视觉验证。这种方法旨在提高模型对视频内容的时序感知能力，从而更准确地定位答案。

**技术框架**：Zoom-Zero框架包含两个主要阶段：粗略定位阶段和精细缩放阶段。在粗略定位阶段，模型首先根据问题定位到若干个候选的视频片段。在精细缩放阶段，模型对这些片段进行时间域的放大，提取关键帧，并进行更细致的视觉验证。整个框架利用强化学习进行训练，通过奖励机制来优化模型的时序定位能力和答案生成能力。

**关键创新**：论文的关键创新点在于两个方面：一是引入了“缩放精度奖励”，用于验证时序定位的准确性，并促进对定位帧的细粒度视觉验证；二是采用了“token选择性信用分配”，将奖励分配给负责时序定位或答案生成的token，从而缓解GRPO在处理多方面奖励信号时的问题。

**关键设计**：在缩放精度奖励方面，论文设计了一种基于IoU（Intersection over Union）的奖励函数，用于衡量模型预测的时序片段与真实答案片段之间的重叠程度。在token选择性信用分配方面，论文使用注意力机制来确定每个token对时序定位和答案生成的贡献程度，并根据贡献程度分配奖励。具体的网络结构和参数设置在论文中有详细描述，但未在此处详细展开。

## 📊 实验亮点

Zoom-Zero在NExT-GQA和ReXTime数据集上分别将时序定位精度提高了5.2%和4.6%，并将平均答案准确率提高了2.4%。此外，在长视频基准测试中，Zoom-Zero平均提高了6.4%，表明其在处理长视频理解任务方面的有效性。这些结果表明，Zoom-Zero在GVQA任务上取得了显著的性能提升。

## 🎯 应用场景

Zoom-Zero技术可应用于智能视频分析、视频搜索、智能客服等领域。例如，在视频搜索中，可以帮助用户快速定位到视频中包含特定信息的片段；在智能客服中，可以根据用户提出的问题，准确地从视频知识库中找到答案。该研究的未来影响在于提升视频理解的准确性和效率，推动视频智能化应用的发展。

## 📄 摘要（原文）

> Grounded video question answering (GVQA) aims to localize relevant temporal segments in videos and generate accurate answers to a given question; however, large video-language models (LVLMs) exhibit limited temporal awareness. Although existing approaches based on Group Relative Policy Optimization (GRPO) attempt to improve temporal grounding, they still struggle to faithfully ground their answers in the relevant video evidence, leading to temporal mislocalization and hallucinations. In this work, we present Zoom-Zero, a coarse-to-fine framework that first localizes query-relevant segments and then temporally zooms into the most salient frames for finer-grained visual verification. Our method addresses the limits of GRPO for the GVQA task with two key innovations: (i) a zoom-in accuracy reward that validates the fidelity of temporal grounding prediction and facilitates fine-grained visual verification on grounded frames; (ii) token-selective credit assignment, which attributes rewards to the tokens responsible for temporal localization or answer generation, mitigating GRPO's issue in handling multi-faceted reward signals. Our proposed method advances grounded video question answering, improving temporal grounding by 5.2\% on NExT-GQA and 4.6\% on ReXTime, while also enhancing average answer accuracy by 2.4\%. Additionally, the coarse-to-fine zoom-in during inference further benefits long-form video understanding by preserving critical visual details without compromising global context, yielding an average improvement of 6.4\% on long-video benchmarks.

