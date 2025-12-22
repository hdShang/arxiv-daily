---
layout: default
title: GroundingME: Exposing the Visual Grounding Gap in MLLMs through Multi-Dimensional Evaluation
---

# GroundingME: Exposing the Visual Grounding Gap in MLLMs through Multi-Dimensional Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17495" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17495v1</a>
  <a href="https://arxiv.org/pdf/2512.17495.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17495v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17495v1', 'GroundingME: Exposing the Visual Grounding Gap in MLLMs through Multi-Dimensional Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rang Li, Lei Li, Shuhuai Ren, Hao Tian, Shuhao Gu, Shicheng Li, Zihao Yue, Yudong Wang, Wenhan Ma, Zhe Yang, Jingyuan Ma, Zhifang Sui, Fuli Luo

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**GroundingME：多维度评测揭示MLLM在视觉定位能力上的差距**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉定位` `多模态大语言模型` `基准测试` `视觉理解` `多维度评估`

## 📋 核心要点

1. 现有MLLM在视觉定位任务上表现看似出色，但现有评测benchmark难以反映真实场景的复杂性，无法有效评估模型真正的定位能力。
2. 提出GroundingME基准，从区分性、空间性、有限性和拒绝性四个维度系统性地评估MLLM的视觉定位能力，更贴近现实世界。
3. 实验表明现有MLLM在GroundingME上表现不佳，尤其在拒绝无法定位的查询时几乎完全失效，通过数据混合训练可显著提升拒绝准确率。

## 📝 摘要（中文）

视觉定位，即从自然语言描述中定位物体，是连接语言和视觉理解的关键桥梁。尽管多模态大型语言模型（MLLM）在现有基准测试中取得了令人印象深刻的分数，但一个根本问题仍然存在：MLLM是否真正像人类一样精细地将语言定位到视觉中，还是仅仅在简化的数据集上进行模式匹配？现有的基准测试未能捕捉到现实世界的复杂性，在现实世界中，人类可以轻松地处理模糊的引用，并识别何时无法进行定位。为了严格评估MLLM的真实能力，我们引入了GroundingME，这是一个基准测试，它在四个关键维度上系统地挑战模型：（1）区分性，区分高度相似的物体；（2）空间性，理解复杂的关系描述；（3）有限性，处理遮挡或微小物体；（4）拒绝性，识别无法定位的查询。通过结合自动生成和人工验证的精心策划，我们创建了1,005个具有挑战性的示例，反映了现实世界的复杂性。对25个最先进的MLLM的评估揭示了一个深刻的能力差距：最好的模型仅达到45.1%的准确率，而大多数模型在拒绝任务中的得分为0%，本能地幻觉出物体，而不是承认它们不存在，这引发了对部署的关键安全问题。我们探索了两种改进策略：（1）测试时缩放通过思考轨迹选择最佳响应，从而将复杂定位提高高达2.9%；（2）数据混合训练教会模型识别无法定位的查询，将拒绝准确率从0%提高到27.9%。因此，GroundingME既可以作为揭示MLLM当前局限性的诊断工具，也可以作为实现人类水平视觉定位的路线图。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在视觉定位任务中存在的真实能力评估问题。现有基准测试无法充分捕捉现实世界场景的复杂性，例如区分相似物体、理解空间关系、处理遮挡以及识别无法定位的查询。这导致模型在现有基准上表现良好，但实际应用中可能存在较大差距。

**核心思路**：论文的核心思路是构建一个更具挑战性和现实感的视觉定位基准测试集，即GroundingME。该基准从四个关键维度（区分性、空间性、有限性和拒绝性）系统性地评估MLLM的视觉定位能力，从而更准确地反映模型在真实场景中的表现。通过分析模型在这些维度上的表现，可以揭示模型在视觉定位方面的局限性，并为改进模型提供指导。

**技术框架**：GroundingME基准的构建流程主要包括以下几个阶段：1) 数据生成：结合自动生成和人工验证，创建包含1005个具有挑战性的示例。2) 维度设计：从区分性、空间性、有限性和拒绝性四个维度设计测试用例，覆盖现实世界场景中的常见挑战。3) 模型评估：使用GroundingME评估25个最先进的MLLM，分析模型在不同维度上的表现。4) 改进策略探索：探索测试时缩放和数据混合训练两种策略，以提升模型在复杂定位和拒绝任务上的性能。

**关键创新**：GroundingME的关键创新在于其多维度评估体系，能够更全面、更准确地评估MLLM的视觉定位能力。与现有基准测试相比，GroundingME更注重模拟现实世界场景的复杂性，例如引入相似物体、复杂空间关系、遮挡以及无法定位的查询。此外，论文还探索了两种有效的改进策略，为提升MLLM的视觉定位能力提供了新的思路。

**关键设计**：在数据生成方面，论文采用了自动生成和人工验证相结合的方法，以保证数据的质量和多样性。在维度设计方面，论文精心选择了区分性、空间性、有限性和拒绝性四个维度，这些维度涵盖了视觉定位任务中的关键挑战。在模型评估方面，论文使用了多种评估指标，例如准确率，以全面评估模型在不同维度上的表现。此外，论文还对测试时缩放和数据混合训练两种策略进行了详细的参数设置和实验分析。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17495v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17495v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17495v1/images/category.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有最先进的MLLM在GroundingME基准上的表现远低于人类水平，最佳模型仅达到45.1%的准确率，且在拒绝任务中几乎完全失效（0%准确率）。通过测试时缩放，复杂定位能力提升高达2.9%。通过数据混合训练，拒绝准确率从0%提升到27.9%，表明该方法能够有效提升模型识别无法定位查询的能力。

## 🎯 应用场景

该研究成果可应用于机器人导航、智能监控、图像搜索、辅助驾驶等领域。通过提高MLLM的视觉定位能力，可以使机器人在复杂环境中更好地理解人类指令，更准确地识别和定位目标物体，从而实现更智能、更安全的应用。此外，该研究提出的GroundingME基准可以作为评估和改进MLLM视觉定位能力的重要工具。

## 📄 摘要（原文）

> Visual grounding, localizing objects from natural language descriptions, represents a critical bridge between language and vision understanding. While multimodal large language models (MLLMs) achieve impressive scores on existing benchmarks, a fundamental question remains: can MLLMs truly ground language in vision with human-like sophistication, or are they merely pattern-matching on simplified datasets? Current benchmarks fail to capture real-world complexity where humans effortlessly navigate ambiguous references and recognize when grounding is impossible. To rigorously assess MLLMs' true capabilities, we introduce GroundingME, a benchmark that systematically challenges models across four critical dimensions: (1) Discriminative, distinguishing highly similar objects, (2) Spatial, understanding complex relational descriptions, (3) Limited, handling occlusions or tiny objects, and (4) Rejection, recognizing ungroundable queries. Through careful curation combining automated generation with human verification, we create 1,005 challenging examples mirroring real-world complexity. Evaluating 25 state-of-the-art MLLMs reveals a profound capability gap: the best model achieves only 45.1% accuracy, while most score 0% on rejection tasks, reflexively hallucinating objects rather than acknowledging their absence, raising critical safety concerns for deployment. We explore two strategies for improvements: (1) test-time scaling selects optimal response by thinking trajectory to improve complex grounding by up to 2.9%, and (2) data-mixture training teaches models to recognize ungroundable queries, boosting rejection accuracy from 0% to 27.9%. GroundingME thus serves as both a diagnostic tool revealing current limitations in MLLMs and a roadmap toward human-level visual grounding.

