---
layout: default
title: "MMAR: A Challenging Benchmark for Deep Reasoning in Speech, Audio, Music, and Their Mix"
---

# MMAR: A Challenging Benchmark for Deep Reasoning in Speech, Audio, Music, and Their Mix

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13032" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13032v1</a>
  <a href="https://arxiv.org/pdf/2505.13032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13032v1', 'MMAR: A Challenging Benchmark for Deep Reasoning in Speech, Audio, Music, and Their Mix')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyang Ma, Yinghao Ma, Yanqiao Zhu, Chen Yang, Yi-Wen Chao, Ruiyang Xu, Wenxi Chen, Yuanzhe Chen, Zhuo Chen, Jian Cong, Kai Li, Keliang Li, Siyou Li, Xinfeng Li, Xiquan Li, Zheng Lian, Yuzhe Liang, Minghao Liu, Zhikang Niu, Tianrui Wang, Yuping Wang, Yuxuan Wang, Yihao Wu, Guanrou Yang, Jianwei Yu, Ruibin Yuan, Zhisheng Zheng, Ziya Zhou, Haina Zhu, Wei Xue, Emmanouil Benetos, Kai Yu, Eng-Siong Chng, Xie Chen

**分类**: cs.SD, cs.CL, cs.MM, eess.AS

**发布日期**: 2025-05-19

**备注**: Open-source at https://github.com/ddlBoJack/MMAR

---

## 💡 一句话要点

**提出MMAR基准以评估音频语言模型的深度推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频推理` `多模态学习` `深度学习` `音频语言模型` `基准评估` `链式思维` `复杂问题`

## 📋 核心要点

1. 现有基准通常局限于特定音频领域，缺乏对多模态音频推理的全面评估。
2. MMAR通过提供多达1000个音频-问题-答案三元组，涵盖多层次推理，促进音频语言模型的研究。
3. 在多种模型上评估MMAR，揭示了当前模型在理解和推理能力上的关键局限性。

## 📝 摘要（中文）

我们介绍了MMAR，这是一个新的基准，旨在评估音频语言模型（ALMs）在多学科任务中的深度推理能力。MMAR包含1000个精心策划的音频-问题-答案三元组，收集自真实互联网视频，并通过迭代错误修正和质量检查进行优化，以确保高质量。与现有的仅限于特定声音、音乐或语音领域的基准不同，MMAR扩展到广泛的现实音频场景，包括声音、音乐和语音的混合模态组合。每个问题在四个推理层次上进行分层分类：信号、感知、语义和文化，并在每个层次内增加子类别，以反映任务的多样性和复杂性。我们为每个问题注释了链式思维（CoT）推理，以促进未来音频推理的进展。每个基准项都要求多步骤的深度推理，超越表面理解，部分问题需要研究生级别的感知和领域特定知识，提升了基准的难度和深度。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有音频语言模型在多模态推理能力评估中的不足，尤其是缺乏对复杂音频场景的全面考量。现有方法往往局限于特定领域，无法有效评估模型的深度推理能力。

**核心思路**：论文提出MMAR基准，通过构建多层次的音频-问题-答案三元组，促进对音频语言模型的深度推理能力的评估。设计时考虑了多模态音频的复杂性，确保问题的多样性和挑战性。

**技术框架**：MMAR的整体架构包括四个推理层次：信号、感知、语义和文化。每个层次下又细分为多个子类别，以反映任务的多样性。每个问题都附有链式思维推理，促进模型的深度理解。

**关键创新**：MMAR的主要创新在于其多层次的推理结构和链式思维推理的引入，使得每个问题不仅要求表面理解，还需要深度的多步骤推理。这与现有方法的单一领域评估形成鲜明对比。

**关键设计**：在设计中，问题的选择经过严格的质量检查，确保其在多模态推理中的有效性。每个问题的难度和复杂性经过精心设计，部分问题需要研究生级别的知识，以提升基准的挑战性。

## 📊 实验亮点

在对多种大型模型的评估中，MMAR显示出其挑战性，揭示了当前模型在深度理解和推理能力上的关键局限性。具体实验结果表明，部分模型在复杂问题上的表现显著低于预期，强调了该基准的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能助手、音频内容分析等。MMAR基准的建立将推动音频语言模型在多模态推理方面的研究，促进相关技术在实际应用中的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce MMAR, a new benchmark designed to evaluate the deep reasoning capabilities of Audio-Language Models (ALMs) across massive multi-disciplinary tasks. MMAR comprises 1,000 meticulously curated audio-question-answer triplets, collected from real-world internet videos and refined through iterative error corrections and quality checks to ensure high quality. Unlike existing benchmarks that are limited to specific domains of sound, music, or speech, MMAR extends them to a broad spectrum of real-world audio scenarios, including mixed-modality combinations of sound, music, and speech. Each question in MMAR is hierarchically categorized across four reasoning layers: Signal, Perception, Semantic, and Cultural, with additional sub-categories within each layer to reflect task diversity and complexity. To further foster research in this area, we annotate every question with a Chain-of-Thought (CoT) rationale to promote future advancements in audio reasoning. Each item in the benchmark demands multi-step deep reasoning beyond surface-level understanding. Moreover, a part of the questions requires graduate-level perceptual and domain-specific knowledge, elevating the benchmark's difficulty and depth. We evaluate MMAR using a broad set of models, including Large Audio-Language Models (LALMs), Large Audio Reasoning Models (LARMs), Omni Language Models (OLMs), Large Language Models (LLMs), and Large Reasoning Models (LRMs), with audio caption inputs. The performance of these models on MMAR highlights the benchmark's challenging nature, and our analysis further reveals critical limitations of understanding and reasoning capabilities among current models. We hope MMAR will serve as a catalyst for future advances in this important but little-explored area.

