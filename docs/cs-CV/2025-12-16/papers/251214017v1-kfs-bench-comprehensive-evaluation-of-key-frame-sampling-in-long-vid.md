---
layout: default
title: KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding
---

# KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14017" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14017v1</a>
  <a href="https://arxiv.org/pdf/2512.14017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14017v1" onclick="toggleFavorite(this, '2512.14017v1', 'KFS-Bench: Comprehensive Evaluation of Key Frame Sampling in Long Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zongyao Li, Kengo Ishida, Satoshi Yamazaki, Xiaotong Ji, Jianquan Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: WACV2026

**🔗 代码/项目**: [GITHUB](https://github.com/NEC-VID/KFS-Bench)

---

## 💡 一句话要点

**提出KFS-Bench基准，用于长视频问答中关键帧采样的全面评估。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `关键帧采样` `视频问答` `多模态学习` `基准数据集`

## 📋 核心要点

1. 现有长视频问答的关键帧采样方法缺乏直接评估手段，通常只能通过最终QA准确率间接评估采样质量。
2. 论文提出KFS-Bench基准，包含多场景标注，可以直接分析采样方法对关键内容的覆盖程度和采样质量。
3. 实验表明，采样精度、场景覆盖率和采样平衡是影响QA性能的关键因素，并提出了一种自适应平衡采样方法，提升了QA性能。

## 📝 摘要（中文）

本文提出了KFS-Bench，这是首个用于长视频问答（QA）中关键帧采样的基准，它具有多场景标注，能够直接且稳健地评估采样策略。关键帧采样对于高效的长视频理解至关重要。在长视频QA中，选择信息量大的帧能够使多模态大型语言模型（MLLM）提高准确性和效率。KFS-Bench解决了先前工作仅通过QA准确率间接评估帧选择质量的局限性。通过提供每个问题所需多个不相交场景的ground-truth标注，KFS-Bench允许我们直接分析不同的采样方法如何捕获整个长视频中的关键内容。使用KFS-Bench，我们对关键帧采样方法进行了全面研究，并确定不仅采样精度，而且场景覆盖率和采样平衡是影响QA性能的关键因素。考虑到所有因素，我们设计了一种新的采样质量指标，该指标与QA准确率相关。此外，我们开发了一种新的关键帧采样方法，该方法利用问题-视频相关性来平衡采样多样性与问题-帧相似性，从而提高相关场景的覆盖率。我们的自适应平衡采样方法在关键帧采样和QA性能方面均实现了卓越的性能。该基准可在https://github.com/NEC-VID/KFS-Bench上获得。

## 🔬 方法详解

**问题定义**：论文旨在解决长视频问答中关键帧采样策略的评估问题。现有方法主要依赖于最终的问答准确率来间接评估采样质量，无法直接衡量采样策略对关键信息的捕获能力，缺乏细粒度的评估标准。此外，如何平衡采样精度、场景覆盖率和采样平衡也是一个挑战。

**核心思路**：论文的核心思路是构建一个带有ground-truth多场景标注的基准数据集KFS-Bench，从而能够直接评估不同采样策略对关键场景的覆盖程度。同时，通过分析不同采样策略在KFS-Bench上的表现，揭示影响QA性能的关键因素，并设计一种自适应平衡采样方法，以平衡采样多样性与问题相关性。

**技术框架**：整体框架包括：1) 构建KFS-Bench基准数据集，包含长视频、问题以及对应的多个关键场景标注；2) 使用KFS-Bench评估现有关键帧采样方法，分析采样精度、场景覆盖率和采样平衡对QA性能的影响；3) 提出一种新的自适应平衡采样方法，该方法利用问题-视频相关性来指导关键帧的选择，平衡采样多样性与问题相关性；4) 在KFS-Bench上验证所提出方法的有效性。

**关键创新**：论文的关键创新在于：1) 提出了首个用于长视频问答关键帧采样的基准数据集KFS-Bench，该数据集包含多场景标注，能够直接评估采样策略的性能；2) 揭示了采样精度、场景覆盖率和采样平衡是影响QA性能的关键因素；3) 提出了一种自适应平衡采样方法，该方法能够根据问题-视频相关性动态调整采样策略，平衡采样多样性与问题相关性。

**关键设计**：自适应平衡采样方法的核心在于如何平衡采样多样性与问题相关性。具体来说，该方法首先计算问题与视频中每个帧的相关性得分，然后根据得分选择一部分帧作为候选帧。为了保证采样多样性，该方法采用了一种基于聚类的策略，将候选帧分成若干个簇，并在每个簇中选择最具代表性的帧。最终，该方法将选择的帧作为关键帧，用于后续的问答任务。

## 📊 实验亮点

实验结果表明，KFS-Bench能够有效评估关键帧采样策略的性能。提出的自适应平衡采样方法在KFS-Bench上取得了显著的性能提升，在关键帧采样和QA性能方面均优于现有方法。具体性能数据在论文中给出，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于智能视频分析、视频检索、智能监控等领域。通过高效的关键帧采样，可以降低计算成本，提高长视频理解的效率和准确性。未来，该研究可以进一步扩展到其他长视频理解任务，例如视频摘要、视频编辑等。

## 📄 摘要（原文）

> We propose KFS-Bench, the first benchmark for key frame sampling in long video question answering (QA), featuring multi-scene annotations to enable direct and robust evaluation of sampling strategies. Key frame sampling is crucial for efficient long-form video understanding. In long video QA, selecting informative frames enables multimodal large language models (MLLMs) to improve both accuracy and efficiency. KFS-Bench addresses the limitation of prior works that only indirectly assess frame selection quality via QA accuracy. By providing ground-truth annotations of multiple disjoint scenes required per question, KFS-Bench allows us to directly analyze how different sampling approaches capture essential content across an entire long video. Using KFS-Bench, we conduct a comprehensive study of key frame sampling methods and identify that not only sampling precision but also scene coverage and sampling balance are the key factors influencing QA performance. Regarding all the factors, we design a novel sampling quality metric that correlates with QA accuracy. Furthermore, we develop a novel key frame sampling method that leverages question-video relevance to balance sampling diversity against question-frame similarity, thereby improving coverage of relevant scenes. Our adaptively balanced sampling approach achieves superior performance in both key frame sampling and QA performance. The benchmark is available at https://github.com/NEC-VID/KFS-Bench.

