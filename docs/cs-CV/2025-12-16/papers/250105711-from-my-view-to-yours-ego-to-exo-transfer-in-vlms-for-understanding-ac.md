---
layout: default
title: From My View to Yours: Ego-to-Exo Transfer in VLMs for Understanding Activities of Daily Living
---

# From My View to Yours: Ego-to-Exo Transfer in VLMs for Understanding Activities of Daily Living

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2501.05711" class="toolbar-btn" target="_blank">📄 arXiv: 2501.05711</a>
  <a href="https://arxiv.org/pdf/2501.05711.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2501.05711" onclick="toggleFavorite(this, '2501.05711', 'From My View to Yours: Ego-to-Exo Transfer in VLMs for Understanding Activities of Daily Living')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dominick Reilly, Manish Kumar Govind, Le Xue, Srijan Das

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Ego2ExoVLM，解决VLM在日常活动理解中视角转换的难题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `视觉语言模型` `视角转换` `知识蒸馏` `日常生活活动理解` `自我中心视角` `外视角` `序列蒸馏`

## 📋 核心要点

1. 现有VLM视角不变性训练使其难以理解外视角视频中的自我中心属性，限制了其在ADL等领域的应用。
2. Ego2ExoVLM通过序列蒸馏和自适应视觉tokens，将自我中心视角知识迁移到外视角VLM，提升理解能力。
3. Ego2ExoVLM在Ego-in-Exo和ADL基准测试中表现出色，尤其在ADL-X上达到SOTA，验证了其有效性。

## 📝 摘要（中文）

视觉语言模型(VLM)在各种视频理解任务中表现出色。然而，其视角不变性训练限制了它们从外视角视频观察中理解以自我为中心的属性（例如，人与物体的交互）的能力。这种限制对于许多应用至关重要，例如日常生活活动(ADL)监测，其中理解以自我为中心的属性至关重要，并且难以部署以自我为中心的相机。为了解决这个限制，我们提出了Ego2ExoVLM，一个VLM，它通过在训练期间利用时间同步的自我-外部视频来学习从外部视角视频推断以自我为中心的属性。Ego2ExoVLM通过使用两个组件来实现这一点：Ego2Exo序列蒸馏，它将知识从以自我为中心的教师转移到以外部为中心的学生，以及Ego自适应视觉tokens，旨在提高这种知识转移的有效性。为了衡量这种能力，我们引入了Ego-in-Exo Perception，一个包含3.9K个问题的基准，专门用于衡量从外部视角视频理解以自我为中心的属性。Ego2ExoVLM在Ego-in-Exo Perception和现有的ADL基准测试中的10个任务上进行了评估，在ADL-X基准测试套件上取得了最先进的结果，并在我们提出的基准测试中优于强大的基线。

## 🔬 方法详解

**问题定义**：现有视觉语言模型（VLM）在视频理解任务中表现良好，但其训练方式侧重于视角不变性，导致其难以从外视角（Exocentric）视频中理解以自我为中心（Egocentric）的属性，例如人与物体的交互方式。这限制了VLM在日常生活活动（ADL）监测等领域的应用，因为这些应用需要理解自我中心视角下的行为，而部署自我中心相机在实际中往往不可行。

**核心思路**：Ego2ExoVLM的核心思路是通过知识蒸馏，将以自我为中心的视角信息从一个“教师”模型（在自我中心视频上训练）迁移到一个“学生”模型（在外视角视频上训练）。通过这种方式，学生模型可以学习理解外视角视频中隐含的自我中心属性。这样设计的目的是为了让VLM能够更好地理解和推理外视角视频中的人类行为和活动。

**技术框架**：Ego2ExoVLM包含两个主要组件：Ego2Exo序列蒸馏和Ego自适应视觉tokens。Ego2Exo序列蒸馏负责将知识从自我中心视角的教师模型传递到外视角学生模型。Ego自适应视觉tokens则用于增强知识传递的有效性。整体流程是：首先，使用自我中心视频训练教师模型；然后，利用时间同步的自我中心和外视角视频，通过序列蒸馏的方式训练学生模型，使其能够模仿教师模型的行为；最后，使用Ego自适应视觉tokens进一步优化学生模型，使其更好地理解外视角视频中的自我中心属性。

**关键创新**：该论文的关键创新在于提出了Ego2Exo序列蒸馏和Ego自适应视觉tokens，用于解决VLM在外视角视频中理解自我中心属性的难题。与现有方法相比，Ego2ExoVLM能够更有效地利用自我中心视角的信息，提升VLM在外视角视频理解任务中的性能。

**关键设计**：Ego2Exo序列蒸馏的具体实现方式未知，但可以推测其使用了某种形式的序列到序列的损失函数，例如KL散度或交叉熵，来衡量学生模型和教师模型输出之间的差异。Ego自适应视觉tokens的具体结构和参数设置也未知，但可以推测其使用了某种形式的注意力机制，来选择性地关注与自我中心属性相关的视觉特征。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2501.05711/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2501.05711/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2501.05711/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Ego2ExoVLM在ADL-X基准测试套件上取得了state-of-the-art的结果，证明了其在ADL理解方面的优越性。此外，在作者提出的Ego-in-Exo Perception基准测试中，Ego2ExoVLM也优于强大的基线模型，验证了其在外视角视频中理解自我中心属性的能力。具体的性能数据和提升幅度在论文中未明确给出，但整体结果表明Ego2ExoVLM具有显著的优势。

## 🎯 应用场景

该研究成果可广泛应用于日常生活活动监测、智能家居、远程医疗、安全监控等领域。通过理解外视角视频中的自我中心属性，可以实现对老年人、残疾人等弱势群体的行为监测和辅助，提高生活质量和安全性。此外，该技术还可用于机器人导航和人机交互，使机器人能够更好地理解人类意图和行为。

## 📄 摘要（原文）

> Vision Language Models (VLMs) have achieved strong performance across diverse video understanding tasks. However, their viewpoint invariant training limits their ability to understand egocentric properties (e.g., human object interactions) from exocentric video observations. This limitation is critical for many applications, such as Activities of Daily Living (ADL) monitoring, where the understanding of egocentric properties is essential, and egocentric cameras are impractical to deploy. To address this limitation, we propose Ego2ExoVLM, a VLM that learns to infer egocentric properties from exocentric videos by leveraging time-synchronized ego-exo videos during training. Ego2ExoVLM accomplishes this through the use of two components: Ego2Exo Sequence Distillation, which transfers knowledge from an egocentric teacher to an exocentric student, and Ego Adaptive Visual Tokens, designed to enhance the effectiveness of this knowledge transfer. To measure this capability, we introduce Ego-in-Exo Perception, a benchmark of 3.9K questions curated to explicitly measure the understanding of egocentric properties from exocentric videos. Ego2ExoVLM is evaluated on 10 tasks across Ego-in-Exo Perception and existing ADL benchmarks, achieving state-of-the-art results on the ADL-X benchmark suite and outperforming strong baselines on our proposed benchmark. All code, models, and data will be released atthis https URL.

